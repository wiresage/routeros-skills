"""Convert rendered documentation HTML to plain Markdown.

Two sources are handled:

* Docusaurus articles from manual.mikrotik.com (the hardware manuals exist only
  as rendered HTML).
* Confluence export views from help.mikrotik.com/docs.

Both are cleaned of site chrome first, then converted with ``markdownify``.
Pictures cannot be used offline, so they become a short ``*[Figure: alt]*`` note.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

HELP_BASE = "https://help.mikrotik.com"
JUNK_SELECTORS = [
    "script",
    "style",
    "svg",
    "button",
    "nav",
    "a.hash-link",
    ".theme-doc-breadcrumbs",
    ".theme-doc-footer",
    ".theme-edit-this-page",
    ".pagination-nav",
    ".tocCollapsible",
    ".toc-macro",
    ".aui-icon",
    ".confluence-information-macro-icon",
    "span.emoticon",
]
CONFLUENCE_PANELS = {
    "confluence-information-macro-warning": "Warning",
    "confluence-information-macro-note": "Note",
    "confluence-information-macro-tip": "Tip",
    "confluence-information-macro-information": "Info",
}
INVISIBLE = re.compile("[​‌‍﻿]")


class Converter(MarkdownConverter):
    """markdownify with table cells kept on one line and figures reduced to a note."""

    def convert_img(self, el: Tag, text: str, parent_tags: set[str]) -> str:  # noqa: ARG002
        alt = (el.get("alt") or "").strip()
        return f"*[Figure: {alt}]*" if alt else "*[Figure]*"

    def _cell(self, text: str) -> str:
        text = re.sub(r"\n{2,}", "\n", text.strip())
        text = text.replace("|", "\\|")
        return re.sub(r"\s*\n\s*", "<br>", text)

    def convert_td(self, el: Tag, text: str, parent_tags: set[str]) -> str:
        return super().convert_td(el, self._cell(text), parent_tags)

    def convert_th(self, el: Tag, text: str, parent_tags: set[str]) -> str:
        return super().convert_th(el, self._cell(text), parent_tags)


def _replace_with_html(tag: Tag, markup: str) -> None:
    fragment = BeautifulSoup(markup, "lxml")
    body = fragment.body or fragment
    new_children = list(body.children)
    for child in new_children:
        tag.insert_before(child.extract())
    tag.decompose()


def _code_language(pre: Tag) -> str:
    """Language of a code block: a Confluence brush parameter or a ``language-xxx`` class."""
    match = re.search(r"brush:\s*([A-Za-z0-9_+-]+)", str(pre.get("data-syntaxhighlighter-params", "")))
    if match:
        brush = match.group(1).lower()
        return "" if brush in ("text", "plain") else brush
    holders = [pre, pre.find("code"), *pre.find_parents("div", limit=3)]
    for holder in holders:
        for name in (holder.get("class") or []) if isinstance(holder, Tag) else []:
            if name.startswith("language-"):
                return name.removeprefix("language-")
    return ""


def _code_container(pre: Tag) -> Tag:
    """The outermost wrapper that belongs to this code block (copy button, header and so on)."""
    for parent in pre.find_parents("div", limit=4):
        classes = set(parent.get("class") or [])
        if "theme-code-block" in classes or {"code", "panel"} <= classes:
            return parent
    return pre


def _normalise_code_blocks(soup: BeautifulSoup) -> None:
    for pre in soup.find_all("pre"):
        if pre.parent is None:
            continue
        lines = pre.select("span.token-line")
        text = "\n".join(line.get_text("") for line in lines) if lines else pre.get_text("")
        language = _code_language(pre)
        replacement = soup.new_tag("pre")
        code = soup.new_tag("code")
        if language:
            code["class"] = [f"language-{language}"]
        code.string = text.replace("\xa0", " ").strip("\n")
        replacement.append(code)
        _code_container(pre).replace_with(replacement)


def _normalise_admonitions(soup: BeautifulSoup) -> None:
    for box in soup.select("div.theme-admonition"):
        heading = box.select_one("[class*=admonitionHeading]")
        label = heading.get_text(" ", strip=True).capitalize() if heading else "Note"
        content = box.select_one("[class*=admonitionContent]")
        inner = content.decode_contents() if content else ""
        _replace_with_html(box, f"<blockquote><p><strong>{label}</strong></p>{inner}</blockquote>")
    for panel in soup.select("div.confluence-information-macro"):
        kind = next((CONFLUENCE_PANELS[c] for c in panel.get("class", []) if c in CONFLUENCE_PANELS), "Note")
        body = panel.select_one(".confluence-information-macro-body")
        inner = body.decode_contents() if body else panel.decode_contents()
        _replace_with_html(panel, f"<blockquote><p><strong>{kind}</strong></p>{inner}</blockquote>")


def _normalise_tabs(soup: BeautifulSoup) -> None:
    for container in soup.select("div.tabs-container"):
        labels = [li.get_text(" ", strip=True) for li in container.select("ul[role=tablist] > li")]
        panels = container.select("div[role=tabpanel]")
        parts = []
        for index, panel in enumerate(panels):
            label = labels[index] if index < len(labels) else f"Tab {index + 1}"
            parts.append(f"<p><strong>{label}</strong></p>{panel.decode_contents()}")
        _replace_with_html(container, "".join(parts))
    for expand in soup.select("div.expand-container"):
        title = expand.select_one(".expand-control-text")
        content = expand.select_one(".expand-content")
        label = title.get_text(" ", strip=True) if title else "Details"
        _replace_with_html(expand, f"<p><strong>{label}</strong></p>{content.decode_contents() if content else ''}")


def _absolute_links(soup: BeautifulSoup, base: str) -> None:
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if not href.startswith(("#", "mailto:", "tel:")):
            link["href"] = urljoin(base, href)


def _clean(soup: BeautifulSoup) -> None:
    for selector in JUNK_SELECTORS:
        for tag in soup.select(selector):
            tag.decompose()
    for status in soup.select("span.status-macro"):
        status.replace_with(NavigableString(f"[{status.get_text(' ', strip=True)}]"))
    _normalise_tabs(soup)
    _normalise_admonitions(soup)
    _normalise_code_blocks(soup)


def _fence_language(pre: Tag) -> str | None:
    code = pre.find("code")
    for name in (code.get("class") or []) if isinstance(code, Tag) else []:
        if name.startswith("language-"):
            return name.removeprefix("language-")
    return None


def _convert(soup: BeautifulSoup) -> str:
    converter = Converter(
        heading_style="ATX",
        bullets="-",
        escape_underscores=False,
        escape_asterisks=False,
        code_language_callback=_fence_language,
    )
    text = converter.convert_soup(soup)
    text = INVISIBLE.sub("", text).replace("\xa0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip("\n") + "\n"


def docusaurus_to_markdown(article_html: str, base_url: str) -> str:
    """Convert a Docusaurus ``<article>``; the page title heading is removed (callers add their own)."""
    soup = BeautifulSoup(article_html, "lxml")
    for heading in soup.find_all("h1"):
        heading.decompose()
    _clean(soup)
    _absolute_links(soup, base_url)
    return _convert(soup)


def confluence_to_markdown(export_html: str, base_url: str = HELP_BASE + "/docs/") -> str:
    """Convert a Confluence ``export_view`` body."""
    soup = BeautifulSoup(export_html, "lxml")
    _clean(soup)
    _absolute_links(soup, base_url)
    return _convert(soup)
