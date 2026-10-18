#!/usr/bin/env python3
"""Build every skill's ``references/`` folder from the crawled documentation.

Input (made by ``crawl_manual.py`` and ``crawl_help.py``): the ``.cache`` folder.
Output: ``skills/<scope>/references/`` with

    INDEX.md        what is inside, with one-line summaries (start here)
    guides/         narrative pages of the manual, same path as on the site
    cli/            CLI reference; a menu page includes its commands
    products/       hardware manuals (routeros-hardware only)
    help/           pages that only exist on help.mikrotik.com
    regulatory/     safety and regulatory texts shared by many products

Hand-written notes can sit next to INDEX.md (``references/*.md``); the build
never touches them. Everything in the generated folders is rewritten on each run.

    python tools/build_references.py --cache .cache
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

import htmlmd
import mdx

REPO_ROOT = Path(__file__).resolve().parent.parent
MANUAL = "https://manual.mikrotik.com"
GENERATED = ("guides", "cli", "products", "help", "regulatory")
BOILERPLATE_DESCRIPTION = re.compile(r"^RouterOS (directory|command|settings) reference for ")
# Hardware manual sections that are legal or safety text shared by many products.
SHARED_SECTIONS = {
    "safety warnings",
    "eurasian conformity mark",
    "norma oficial mexicana",
    "ce declaration of conformity",
    "federal communication commission interference statement",
    "innovation, science and economic development canada",
    "ukca marking",
    "the national commission for the state regulation of communications and informatization by ukraine",
}
META_LINE = re.compile(r"^\*\*([A-Za-z ]+):\*\*\s*(.*)$")
# Quick guides repeat the same text in about 25 languages, each under a heading such as "DE - Deutsche. Kurzanleitung".
TRANSLATION_HEADING = re.compile(r"^(?!EN\b)[A-Z]{2,3}\s*[-–—]\s*\S|^Informaci[oó]n M[eé]xico", re.IGNORECASE)


def slugify(text: str) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return text.strip("-") or "page"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


@dataclass
class Entry:
    """One generated reference file."""

    scope: str
    kind: str  # guides | cli | products | help | quick-guides
    out: str  # path inside references/, POSIX style
    title: str
    summary: str = ""
    source: str = ""
    group: str = ""


@dataclass
class Context:
    scopes: dict[str, dict]
    manual_pages: dict[str, dict]
    prefix_rules: list[tuple[str, str, str]]
    placement: dict[str, Entry] = field(default_factory=dict)  # manual page path -> entry
    children: set[str] = field(default_factory=set)  # manual paths that have child pages


# ------------------------------------------------------------------ scopes


def load_scopes(path: Path) -> dict[str, dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {s["name"]: s for s in data["scopes"]}


def build_prefix_rules(scopes: dict[str, dict]) -> list[tuple[str, str, str]]:
    rules = []
    for name, scope in scopes.items():
        rules.extend(("manual", prefix, name) for prefix in scope.get("manual", []))
        rules.extend(("cli", prefix, name) for prefix in scope.get("cli", []))
    return rules


def match_scope(kind: str, path: str, rules: list[tuple[str, str, str]]) -> str | None:
    best: tuple[int, str] | None = None
    for rule_kind, prefix, name in rules:
        if rule_kind != kind:
            continue
        exact = prefix.endswith("$")
        stem = prefix.removesuffix("$")
        matches = path == stem or (not exact and path.startswith(stem + "/"))
        if matches and (best is None or len(stem) > best[0]):
            best = (len(stem), name)
    return best[1] if best else None


# ------------------------------------------------------------------ links


def page_url(path: str) -> str:
    """Public URL of a manual page given its ``docs/...md`` path."""
    return f"{MANUAL}/{path.removesuffix('.md')}"


def make_rewriter(ctx: Context, page_path: str, entry: Entry):
    """Return a function that rewrites links of one page.

    Links to pages of the same skill become relative file links; everything
    else points at the public manual so that no link depends on another skill
    being installed.
    """
    stem = page_path.removesuffix(".md")
    bases = [posixpath.dirname(page_path)]
    if stem in ctx.children:
        bases.insert(0, stem)

    def rewrite(target: str) -> str:
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith(("//", "#")):
            return target
        path_part, _, fragment = target.partition("#")
        path_part = path_part.partition("?")[0]
        suffix = f"#{fragment}" if fragment else ""
        if not path_part:
            return target
        found = None
        candidates = (
            [path_part.lstrip("/")]
            if path_part.startswith("/")
            else [posixpath.normpath(posixpath.join(base, path_part)) for base in bases]
        )
        for candidate in candidates:
            base = candidate.removesuffix(".md").rstrip("/")
            variants = [candidate, base, base + ".md"]
            if posixpath.basename(base) == posixpath.basename(posixpath.dirname(base)):
                variants.append(posixpath.dirname(base) + ".md")  # section pages are written as name/name.md
            found = next((v for v in variants if v in ctx.placement), None)
            if found:
                break
        if found:
            target_entry = ctx.placement[found]
            if target_entry.scope == entry.scope:
                relative = posixpath.relpath(target_entry.out, posixpath.dirname(entry.out))
                return relative + suffix
            return page_url(found) + suffix
        site_path = candidates[0].removesuffix(".md").lstrip("/")
        if site_path.startswith(".."):
            return target
        return f"{MANUAL}/{site_path}{suffix}"

    return rewrite


# ------------------------------------------------------------------ narrative pages


def split_header(text: str) -> tuple[str, str, str]:
    """Split a manual page into ``(title, description, body)``.

    The source repeats the title (``# Title``, ``> summary``, ``# Title``).
    """
    lines = text.replace("\r\n", "\n").split("\n")
    title = ""
    description = ""
    index = 0
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines) and lines[index].startswith("> "):
        description = lines[index][2:].strip()
        index += 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines) and lines[index].strip() == f"# {title}":
        index += 1
    return title, description, "\n".join(lines[index:])


def convert_guide(ctx: Context, page_path: str, text: str, entry: Entry) -> str:
    title, description, body = split_header(text)
    converted = mdx.convert(body, make_rewriter(ctx, page_path, entry))
    note = f"> Source: {page_url(page_path)}"
    if description and not BOILERPLATE_DESCRIPTION.match(description):
        note += f"\n>\n> {description}"
    return f"# {title or entry.title}\n\n{note}\n\n{converted}"


# ------------------------------------------------------------------ CLI pages


@dataclass
class CliSection:
    path: str
    meta: list[tuple[str, str]]
    body: str


SECTION_HEAD = re.compile(r"^## (\S+)\s*$")


def is_section_start(lines: list[str], index: int) -> bool:
    """A CLI section starts with ``## menu/path`` followed by ``**Key:** value`` lines that include the type."""
    if not SECTION_HEAD.match(lines[index]):
        return False
    following = [line for line in lines[index + 1 : index + 6] if line.strip()]
    return any(line.startswith("**Type:**") for line in following)


def parse_cli(text: str) -> tuple[str, list[CliSection]]:
    """Parse a CLI reference page into its sections."""
    _, description, rest = split_header(text.replace("\r\n", "\n"))
    lines = re.sub(r"^\s*-{5,}\s*\n", "", rest.lstrip("\n")).split("\n")
    starts = [i for i in range(len(lines)) if is_section_start(lines, i)]
    sections: list[CliSection] = []
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        match = SECTION_HEAD.match(lines[start])
        assert match is not None
        block = lines[start + 1 : end]
        meta = []
        while block and (not block[0].strip() or META_LINE.match(block[0])):
            line = block.pop(0)
            found = META_LINE.match(line)
            if found:
                meta.append((found.group(1), found.group(2).strip()))
        sections.append(CliSection(path=match.group(1), meta=meta, body="\n".join(block)))
    if not sections:
        sections.append(CliSection(path="", meta=[], body="\n".join(lines)))
    return description, sections


def meta_line(meta: list[tuple[str, str]]) -> str:
    return "; ".join(f"{key}: {value}" for key, value in meta)


def cli_section_text(ctx: Context, page_path: str, section: CliSection, entry: Entry, heading: str | None) -> str:
    """Render one CLI section; ``heading`` is the full heading line, or None when the page title already names it."""
    body = mdx.convert(section.body, make_rewriter(ctx, page_path, entry)).strip("\n")
    parts = [heading] if heading else []
    if section.meta:
        parts.append(meta_line(section.meta))
    if body:
        parts.append(body)
    return "\n\n".join(parts)


def cli_kind(sections: list[CliSection]) -> str:
    for section in sections:
        for key, value in section.meta:
            if key == "Type":
                return value
    return "Directory"


# ------------------------------------------------------------------ hardware and help HTML


def split_sections(markdown: str) -> list[tuple[str, str]]:
    """Split Markdown at level-2 headings: ``[(heading, text-including-heading)]``; the lead has heading ''."""
    parts = re.split(r"(?m)^(?=## )", markdown)
    result = []
    for part in parts:
        match = re.match(r"## (.+)", part)
        heading = re.sub(r"[*_`]", "", match.group(1)).strip() if match else ""
        result.append((heading, part))
    return result


def drop_translations(markdown: str) -> str:
    """Keep the English quick guide and drop its translations."""
    kept = [text for heading, text in split_sections(markdown) if not TRANSLATION_HEADING.match(heading)]
    return "".join(kept)


def split_regulatory(markdown: str) -> tuple[str, str]:
    """Separate safety and regulatory sections (identical boilerplate for every product) from the rest.

    Returns ``(main, regulatory)``; ``regulatory`` is empty when the page has no such section.
    """
    main = []
    regulatory = []
    for heading, text in split_sections(markdown):
        target = regulatory if heading.lower() in SHARED_SECTIONS else main
        target.append(text.rstrip("\n") + "\n\n")
    return "".join(main).rstrip("\n") + "\n", "".join(regulatory).rstrip("\n") + "\n" if regulatory else ""


def product_pages(markdown: str, slug: str, title: str, source: str, up: str) -> tuple[str, str]:
    """Return the product page body and, when there is regulatory text, the text of its companion file.

    ``up`` is the relative path from the product page to ``references/``.
    """
    main, regulatory = split_regulatory(markdown)
    if not regulatory:
        return main, ""
    link = f"[regulatory/{slug}.md]({up}regulatory/{slug}.md)"
    pointer = f"## Safety and regulatory information\n\nSafety warnings and regulatory statements are in {link}.\n"
    companion = f"# {title}: safety and regulatory information\n\n> Source: {source}\n\n{regulatory}"
    return main.rstrip("\n") + "\n\n" + pointer, companion


# ------------------------------------------------------------------ build


def short(text: str, limit: int = 160) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "..."


def md_link(label: str, target: str) -> str:
    return f"[{label}]({target})"


def build(cache: Path, scopes_file: Path, skills_dir: Path, only: set[str] | None) -> int:
    scopes = load_scopes(scopes_file)
    rules = build_prefix_rules(scopes)
    manifest = json.loads((cache / "manual" / "manifest.json").read_text(encoding="utf-8"))
    crawled = manifest["crawled"]
    manual_pages = {r["path"]: r for r in manifest["pages"]}
    ctx = Context(scopes=scopes, manual_pages=manual_pages, prefix_rules=rules)
    stems = {p.removesuffix(".md") for p in manual_pages}
    ctx.children = {s for s in stems if any(o.startswith(s + "/") for o in stems)}

    unassigned: list[str] = []
    entries: dict[str, list[Entry]] = {name: [] for name in scopes}
    cli_pages: dict[str, dict] = {}

    # 1. assign every manual page to a skill
    for path, record in sorted(manual_pages.items()):
        relative = path[len("docs/") :].removesuffix(".md")
        if relative.startswith("cli-reference/"):
            cli_pages[relative[len("cli-reference/") :]] = record
            continue
        scope = match_scope("manual", relative, rules)
        if scope is None:
            unassigned.append(path)
            continue
        entry = Entry(scope, "guides", f"guides/{relative}.md", record["title"], record["description"], page_url(path))
        ctx.placement[path] = entry
        entries[scope].append(entry)

    # 2. CLI pages: directories get a file, commands are merged into their menu when it is in the same skill
    cli_scope: dict[str, str] = {}
    for cli_path in sorted(cli_pages):
        scope = match_scope("cli", cli_path, rules)
        if scope is None:
            unassigned.append(f"docs/cli-reference/{cli_path}.md")
            continue
        cli_scope[cli_path] = scope
    cli_text = {p: (cache / "manual" / "pages" / r["path"]).read_text(encoding="utf-8") for p, r in cli_pages.items()}
    parsed = {p: parse_cli(t) for p, t in cli_text.items() if p in cli_scope}
    kinds = {p: cli_kind(sections) for p, (_, sections) in parsed.items()}
    merged_into: dict[str, str] = {}
    for cli_path, kind in kinds.items():
        parent = cli_path.rpartition("/")[0]
        if (
            kind == "Command"
            and parent in kinds
            and kinds[parent] != "Command"
            and cli_scope[parent] == cli_scope[cli_path]
        ):
            merged_into[cli_path] = parent
    root_page = "docs/cli-reference.md"
    if root_page in manual_pages and root_page not in ctx.placement:
        unassigned.append(root_page)
    for cli_path in sorted(parsed):
        record = cli_pages[cli_path]
        path = record["path"]
        target = merged_into.get(cli_path, cli_path)
        scope = cli_scope[target]
        entry = Entry(scope, "cli", f"cli/{target}.md", "/" + target, record["description"], page_url(path))
        ctx.placement[path] = entry
        if cli_path not in merged_into:
            entry.group = kinds[cli_path]
            entries[scope].append(entry)
    ctx.children |= {f"docs/cli-reference/{p}" for p in cli_pages if any(o.startswith(p + "/") for o in cli_pages)}

    if unassigned:
        print("pages without a skill (add them to tools/scopes.json):")
        for path in unassigned:
            print("  ", path)
        return 1

    # 3. help pages
    help_pages = {}
    for file in sorted((cache / "help").glob("*.json")):
        page = json.loads(file.read_text(encoding="utf-8"))
        help_pages[page["id"]] = page
    help_assigned: dict[str, str] = {}
    for name, scope in scopes.items():
        for page_id in scope.get("help", []):
            if page_id not in help_pages:
                print(f"help page {page_id} listed for {name} was not crawled")
                return 1
            help_assigned[page_id] = name
    quick_guides = [p for p in help_pages.values() if p["space"] == "QG" and p["id"] not in help_assigned]

    # 4. write everything
    written: dict[str, int] = {}
    for name in scopes:
        if only and name not in only:
            continue
        references = skills_dir / name / "references"
        for folder in GENERATED:
            shutil.rmtree(references / folder, ignore_errors=True)
        references.mkdir(parents=True, exist_ok=True)

    def wanted(scope: str) -> bool:
        return not only or scope in only

    for path, entry in sorted(ctx.placement.items()):
        if not wanted(entry.scope) or entry.kind != "guides":
            continue
        text = (cache / "manual" / "pages" / path).read_text(encoding="utf-8")
        write(skills_dir / entry.scope / "references" / entry.out, convert_guide(ctx, path, text, entry))

    for cli_path in sorted(parsed):
        if cli_path in merged_into:
            continue
        description, sections = parsed[cli_path]
        record = cli_pages[cli_path]
        entry = ctx.placement[record["path"]]
        if not wanted(entry.scope):
            continue
        out = [f"# /{cli_path}\n\n> Source: {entry.source}"]
        for section in sections:
            heading = f"## /{section.path}" if len(sections) > 1 else None
            out.append(cli_section_text(ctx, record["path"], section, entry, heading))
        commands = sorted(c for c, parent in merged_into.items() if parent == cli_path)
        if commands:
            out.append("## Commands")
            for command in commands:
                command_record = cli_pages[command]
                command_entry = ctx.placement[command_record["path"]]
                for section in parsed[command][1]:
                    heading = f"### /{section.path or command}"
                    out.append(cli_section_text(ctx, command_record["path"], section, command_entry, heading))
        write(skills_dir / entry.scope / "references" / entry.out, "\n\n".join(out).rstrip("\n") + "\n")

    hardware_dir = cache / "manual" / "hardware"
    product_entries: list[Entry] = []
    for file in sorted(hardware_dir.glob("*.json")):
        page = json.loads(file.read_text(encoding="utf-8"))
        slug = file.stem
        category = " > ".join(page["breadcrumbs"][:-1]) if page["breadcrumbs"] else ""
        entry = Entry("routeros-hardware", "products", f"products/{slug}.md", page["title"], "", page["url"], category)
        product_entries.append(entry)
        if not wanted(entry.scope):
            continue
        markdown = htmlmd.docusaurus_to_markdown(page["html"], page["url"])
        body, regulatory = product_pages(markdown, slug, page["title"], page["url"], "../")
        head = f"# {page['title']}\n\n> Source: {page['url']}\n"
        if category:
            head += f">\n> Category: {category}\n"
        references = skills_dir / entry.scope / "references"
        write(references / entry.out, head + "\n" + body)
        if regulatory:
            write(references / "regulatory" / f"{slug}.md", regulatory)
    entries["routeros-hardware"].extend(product_entries)

    used_slugs: dict[str, set[str]] = {}

    def help_entry(page: dict, scope: str, folder: str) -> Entry:
        taken = used_slugs.setdefault(f"{scope}/{folder}", set())
        slug = slugify(page["title"])
        if slug in taken:
            slug = f"{slug}-{page['id']}"
        taken.add(slug)
        kind = "help" if folder == "help" else "quick-guides"
        return Entry(scope, kind, f"{folder}/{slug}.md", page["title"], "", page["url"], page["space"])

    for page_id in sorted(help_assigned, key=lambda i: (help_pages[i]["space"], help_pages[i]["title"])):
        page = help_pages[page_id]
        scope = help_assigned[page_id]
        entry = help_entry(page, scope, "help")
        entries[scope].append(entry)
        if not wanted(scope):
            continue
        markdown = htmlmd.confluence_to_markdown(page["html"])
        note = (
            f"> Source: {page['url']}\n>\n> Only on help.mikrotik.com: the manual has no equivalent page. "
            f"The help site is frozen; this page was last edited {page['modified'][:10]}."
        )
        write(skills_dir / scope / "references" / entry.out, f"# {page['title']}\n\n{note}\n\n{markdown}")

    for page in sorted(quick_guides, key=lambda p: (p["title"], p["id"])):
        entry = help_entry(page, "routeros-hardware", "help/quick-guides")
        entries["routeros-hardware"].append(entry)
        if not wanted(entry.scope):
            continue
        slug = Path(entry.out).stem
        markdown = drop_translations(htmlmd.confluence_to_markdown(page["html"]))
        body, regulatory = product_pages(markdown, slug, page["title"], page["url"], "../../")
        note = (
            f"> Source: {page['url']}\n>\n> Only on help.mikrotik.com: the manual has no quick guides. "
            f"The help site is frozen; this page was last edited {page['modified'][:10]}. "
            "The translations into other languages are omitted; the English guide is complete."
        )
        references = skills_dir / entry.scope / "references"
        write(references / entry.out, f"# {page['title']}\n\n{note}\n\n{body}")
        if regulatory:
            write(references / "regulatory" / f"{slug}.md", regulatory)

    # 5. indexes
    for name, scope in scopes.items():
        if not wanted(name):
            continue
        written[name] = write_index(skills_dir / name, scope, entries[name], crawled)
    print(f"built {sum(written.values())} reference files in {len(written)} skills (documentation crawled {crawled})")
    return 0


def write_index(skill_dir: Path, scope: dict, entries: list[Entry], crawled: str) -> int:
    references = skill_dir / "references"
    lines = [
        f"# {scope['title']}: reference index",
        "",
        f"Generated by `tools/build_references.py` from manual.mikrotik.com (crawled {crawled}) and, for the",
        "help-only pages, from help.mikrotik.com. Do not edit generated files by hand; change the generator instead.",
        "Each file starts with a `Source:` line. Figures are not included; open the source page to see them.",
        "",
    ]
    notes = sorted(p for p in references.glob("*.md") if p.name != "INDEX.md")
    if notes:
        lines += ["## Curated notes", ""]
        for note in notes:
            first = note.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ").strip()
            lines.append(f"- {md_link(first or note.stem, note.name)}")
        lines.append("")

    def section(title: str, kind: str, label_is_path: bool = False) -> None:
        items = sorted((e for e in entries if e.kind == kind), key=lambda e: e.out)
        if not items:
            return
        lines.extend([f"## {title}", ""])
        for item in items:
            summary = "" if BOILERPLATE_DESCRIPTION.match(item.summary) else short(item.summary)
            extra = f" ({item.group})" if item.group and kind == "cli" else ""
            tail = f": {summary}" if summary else ""
            lines.append(f"- {md_link(item.title, item.out)}{extra}{tail}")
        lines.append("")

    section("Guides (manual)", "guides")
    section("CLI reference", "cli")
    section("Help-only pages", "help")
    products = sorted((e for e in entries if e.kind == "products"), key=lambda e: (e.group, e.title.lower()))
    if products:
        lines.extend(["## Product manuals (manual.mikrotik.com/hardware)", ""])
        current = None
        for item in products:
            if item.group != current:
                current = item.group
                lines.extend(["", f"### {current or 'Other'}", ""])
            lines.append(f"- {md_link(item.title, item.out)}")
        lines.append("")
    section("Quick guides (help-only)", "quick-guides")
    write(references / "INDEX.md", "\n".join(lines).rstrip("\n") + "\n")
    return sum(1 for _ in references.rglob("*.md"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cache", type=Path, default=REPO_ROOT / ".cache")
    parser.add_argument("--scopes", type=Path, default=REPO_ROOT / "tools" / "scopes.json")
    parser.add_argument("--skills", type=Path, default=REPO_ROOT / "skills")
    parser.add_argument("--only", nargs="*", help="rebuild only these skills")
    args = parser.parse_args()
    return build(args.cache, args.scopes, args.skills, set(args.only) if args.only else None)


if __name__ == "__main__":
    sys.exit(main())
