"""Convert the manual's MDX source pages into plain Markdown.

The manual is written in MDX: Markdown plus a few React components
(``ArgTable``, ``Tabs``, ``WideTable`` ...) and Docusaurus admonitions. Agents
and GitHub both read plain Markdown better, so the components are rewritten and
everything else is passed through untouched.

All transformations skip fenced code blocks and inline code.
"""

from __future__ import annotations

import html
import re
from collections.abc import Callable

FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"(`+)(?:(?!\1).)+?\1")
IMAGE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)((?:\s+\"[^\"]*\")?)\)")
ADMONITION_OPEN = re.compile(r"^:::(\w+)(?:\[(.*)\]|\s+(.*))?$")
TAB_ITEM = re.compile(r"""^<TabItem\b[^>]*\blabel=(?:"([^"]*)"|'([^']*)')[^>]*>\s*$""")
DROPPED_TAGS = re.compile(
    r"^\s*</?(Tabs|WideTable|Columns|Column|center)>\s*$|^\s*<DocCardList\s*/>\s*$|^\s*</TabItem>\s*$"
)
ADMONITION_LABELS = {
    "note": "Note",
    "info": "Info",
    "tip": "Tip",
    "warning": "Warning",
    "danger": "Danger",
    "caution": "Caution",
}

LinkRewriter = Callable[[str], str]


def _prose_line(line: str, rewrite: LinkRewriter) -> str:
    """Rewrite figures, links and entities in one line, leaving inline code exactly as written.

    Code spans are set aside first because link text often contains code: ``[`ip/address`](path)``.
    """
    spans: list[str] = []

    def stash(match: re.Match[str]) -> str:
        spans.append(match.group(0))
        return f"\x00{len(spans) - 1}\x00"

    text = INLINE_CODE.sub(stash, line)
    text = IMAGE.sub(lambda m: f"*[Figure: {m.group(1).strip()}]*" if m.group(1).strip() else "*[Figure]*", text)
    text = LINK.sub(lambda m: f"[{m.group(1)}]({rewrite(m.group(2))}{m.group(3)})", text)
    text = html.unescape(text)
    return re.sub(r"\x00(\d+)\x00", lambda m: spans[int(m.group(1))], text)


def convert_blocks(text: str, rewrite: LinkRewriter) -> str:
    """Rewrite admonitions, tabs, dropped wrappers, images, links and entities."""
    out: list[str] = []
    fence_marker: str | None = None
    quote_depth = 0
    for raw in text.split("\n"):
        line = raw.rstrip()
        prefix = "> " * quote_depth
        fence = FENCE.match(line)
        if fence_marker is None:
            if fence:
                fence_marker = fence.group(1)
                out.append(prefix + line)
                continue
            if line.strip() == ":::" and quote_depth:
                quote_depth -= 1
                continue
            opened = ADMONITION_OPEN.match(line.strip())
            if opened:
                label = ADMONITION_LABELS.get(opened.group(1).lower(), opened.group(1).capitalize())
                title = (opened.group(2) or opened.group(3) or "").strip()
                heading = f"**{label}: {title}**" if title else f"**{label}**"
                out.append(prefix + "> " + heading)
                quote_depth += 1
                out.append(prefix + ">")
                continue
            tab = TAB_ITEM.match(line.strip())
            if tab:
                out.append(f"**{tab.group(1) or tab.group(2)}**")
                continue
            if DROPPED_TAGS.match(line):
                continue
            line = _prose_line(line, rewrite)
            out.append((prefix + line) if line.strip() else prefix.rstrip())
        else:
            if fence and fence.group(1) == fence_marker and line.strip() == fence_marker:
                fence_marker = None
            out.append((prefix + line) if line.strip() else prefix.rstrip())
    return "\n".join(out)


# ---------------------------------------------------------------- ArgTable

ARG_TABLE = re.compile(r"<ArgTable\b(?P<attrs>[^>]*)>(?P<body>.*?)</ArgTable>", re.DOTALL)
ATTR = re.compile(r"""\s*([A-Za-z0-9_-]+)="([^"]*)\"""", re.DOTALL)
NUMERIC_MAP = re.compile(r"\s*\{\s*(?:[^{}:,]+:\s*-?\d+\s*,?\s*)+\}")
TABLE_TITLES = {
    "Argument": "Arguments",
    "Read-only Argument": "Read-only arguments",
    "Flag": "Flags",
}


def parse_rows(body: str) -> list[tuple[dict[str, str], str]]:
    """Parse ``<ArgTableRow ...>text</ArgTableRow>`` elements; attributes may span lines."""
    rows = []
    position = 0
    while True:
        start = body.find("<ArgTableRow", position)
        if start < 0:
            return rows
        cursor = start + len("<ArgTableRow")
        attrs: dict[str, str] = {}
        while True:
            match = ATTR.match(body, cursor)
            if not match:
                break
            attrs[match.group(1)] = match.group(2)
            cursor = match.end()
        close = re.compile(r"\s*(/?)>").match(body, cursor)
        if not close:
            raise ValueError(f"malformed ArgTableRow near {body[start : start + 80]!r}")
        cursor = close.end()
        if close.group(1):
            rows.append((attrs, ""))
            position = cursor
            continue
        end = body.index("</ArgTableRow>", cursor)
        rows.append((attrs, body[cursor:end]))
        position = end + len("</ArgTableRow>")


def clean_type(raw: str) -> str:
    """Collapse whitespace and drop the internal numeric enum codes (``{ accept:0, drop:10 }``)."""
    text = html.unescape(raw)
    text = NUMERIC_MAP.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    enum = re.fullmatch(r"enum \(([^()]*)\)", text)
    if enum:
        return f"enum: {enum.group(1).strip()}" if enum.group(1).strip() else "enum"
    return text


def render_row(attrs: dict[str, str], body: str, rewrite: LinkRewriter, flag_table: bool) -> list[str]:
    name = attrs.get("arg", "")
    kind = clean_type(attrs.get("typ", ""))
    description = convert_blocks(body.strip("\n"), rewrite).strip("\n")
    if flag_table:
        if not description or description == kind:
            return [f"- `{name}`: {kind}"]
        head = f"- `{name}` ({kind})"
    else:
        notes = [kind] if kind else []
        if attrs.get("mandatory") == "1":
            notes.append("mandatory")
        if attrs.get("unset") == "1":
            notes.append("unset")
        if attrs.get("deprecated") == "1":
            notes.append("deprecated")
        if attrs.get("syscap"):
            notes.append(f"syscap={attrs['syscap']}")
        head = f"- `{name}`" + (f" ({'; '.join(notes)})" if notes else "")
    lines = description.split("\n") if description else []
    if not lines:
        return [head]
    first, rest = lines[0], lines[1:]
    result = [f"{head}: {first}" if first.strip() else head]
    result.extend(("  " + line) if line.strip() else "" for line in rest)
    return result


def render_arg_table(match: re.Match[str], rewrite: LinkRewriter) -> str:
    """Render one ``ArgTable`` element as a titled bullet list."""
    attrs = {m.group(1): m.group(2) for m in ATTR.finditer(match.group("attrs"))}
    title = attrs.get("c1", "Arguments")
    flag_table = title == "Flag"
    lines = [f"**{TABLE_TITLES.get(title, title)}**", ""]
    for row_attrs, row_body in parse_rows(match.group("body")):
        lines.extend(render_row(row_attrs, row_body, rewrite, flag_table))
    return "\n".join(lines)


def convert(text: str, rewrite: LinkRewriter) -> str:
    """Full conversion of one MDX page body."""
    text = text.replace("\r\n", "\n")
    parts = []
    position = 0
    for match in ARG_TABLE.finditer(text):
        parts.append(convert_blocks(text[position : match.start()], rewrite))
        parts.append(render_arg_table(match, rewrite))
        position = match.end()
    parts.append(convert_blocks(text[position:], rewrite))
    text = re.sub(r"\n{3,}", "\n\n", "".join(parts))
    return text.strip("\n") + "\n"
