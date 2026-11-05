#!/usr/bin/env python3
r"""Measure how much of the RouterOS manual each skill leads an agent to, and compare the snapshot with the live manual.

Every page of the manual is in some skill's ``references/`` folder: ``tools/scopes.json`` assigns it and the build fails
for a page without a skill. That alone does not help an agent, because it opens a reference only when ``SKILL.md`` (or
``INDEX.md``) leads it there. This tool measures the first half of that chain, from the files in the repository only:

* a **guide** or a **help-only page** is *named* when the skill's ``SKILL.md`` links its file or its folder;
* a **CLI menu** is *named* when the skill's ``SKILL.md`` writes the menu path (``/ip firewall filter`` or
  ``/ip/firewall/filter``) or links its reference file or folder, and *named elsewhere* when only another skill does;
* what ``tools/coverage_policy.json`` excludes, with a reason, is left out of the counts.

The numbers are written to ``docs/skill-coverage.md``, which CI keeps current. With a copy of the manual's index
(``llms.txt``) the tool also reports drift: pages the manual has and the snapshot lacks, pages the snapshot has and the
manual dropped, and new pages that no skill in ``tools/scopes.json`` would take (the next build would fail on those).
``docs/manual.lock.json`` records which manual version and corpus hashes the snapshot was last compared with.

    python tools/skill_coverage.py                       # print the report
    python tools/skill_coverage.py --write               # write docs/skill-coverage.md
    python tools/skill_coverage.py --check               # CI: inputs valid, report current (offline)
    python tools/skill_coverage.py --list routeros-dns   # everything this skill's SKILL.md does not name
    python tools/skill_coverage.py --fetch --check --report drift.md --json drift.json
    python tools/skill_coverage.py --manual-index .cache/manual/llms.txt \
        --manual-corpus .cache/manual/llms-full.txt --write-lock

Exit status: 0 success, 1 problems found (invalid inputs, stale report, new pages without a skill, or any drift with
``--strict``), 2 usage or I/O error.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT = Path("docs/skill-coverage.md")
POLICY = Path("tools/coverage_policy.json")
LOCK = Path("docs/manual.lock.json")
SCOPES = Path("tools/scopes.json")
SNAPSHOT = Path("docs-snapshot.json")
MANUAL = "https://manual.mikrotik.com"
INDEX_URL = f"{MANUAL}/llms.txt"
CORPUS_URL = f"{MANUAL}/llms-full.txt"
MAX_DOWNLOAD = 32 * 1024 * 1024
USER_AGENT = "routeros-skills-coverage (+https://github.com/wiresage/routeros-skills)"
# Reference folders that are looked up with a script or the index, not routed one by one.
LOOKUP_FOLDERS = ("products", "regulatory")
POLICY_FOLDERS = ("guides", "help", "cli")
BACKLOG_ROWS = 25
LARGEST_GUIDES = 15

TYPE_LINE = re.compile(r"^Type: (.+)$", re.MULTILINE)
SOURCE_LINE = re.compile(r"^> Source: (\S+)", re.MULTILINE)
COMMAND_HEADING = re.compile(r"^### (/\S+)", re.MULTILINE)
ARGUMENT = re.compile(r"^- `([a-z0-9][a-z0-9.-]*)` \(", re.MULTILINE)
REFERENCE_PATH = re.compile(r"(?<![\w.-])((?:guides|help|cli)(?:/[\w.-]+)+)/?(?![\w.-])")
FILE_NAME = re.compile(r"(?<![\w.-])([\w-]+\.md)(?![\w])")
PATH_START = re.compile(r"(?<![\w./:-])/(?=[a-z0-9])")
TOKEN = re.compile(r"[a-z0-9][a-z0-9-]*")
SEPARATOR = re.compile(r"[/ \t]+")
INDEX_VERSION = re.compile(r"Index of the RouterOS (\S+) manual")
INDEX_ENTRY = re.compile(r"\]\(" + re.escape(MANUAL) + r"/docs/([^)\s#?]+?)\.md\)")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


class CoverageError(Exception):
    """An input is missing or malformed."""


# ------------------------------------------------------------------ inventory


@dataclass
class Page:
    """A guide or a help-only page below ``references/``."""

    skill: str
    folder: str
    rel: str
    size: int
    source: str | None
    status: str = "unnamed"


@dataclass
class Menu:
    """A CLI menu page below ``references/cli/``; the commands of the menu are inside it."""

    skill: str
    path: str
    rel: str
    args: int
    status: str = "unnamed"


@dataclass
class Skill:
    name: str
    lines: int
    text: str
    pages: list[Page] = field(default_factory=list)
    menus: list[Menu] = field(default_factory=list)
    commands: set[str] = field(default_factory=set)
    lookup: dict[str, int] = field(default_factory=dict)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def load_inventory(root: Path) -> dict[str, Skill]:
    """Read every skill: its SKILL.md and the pages below its references folder."""
    skills: dict[str, Skill] = {}
    for skill_md in sorted((root / "skills").glob("*/SKILL.md")):
        text = read(skill_md)
        skill = Skill(skill_md.parent.name, len(text.splitlines()), text)
        refs = skill_md.parent / "references"
        for file in sorted(refs.rglob("*.md"), key=lambda p: p.relative_to(refs).as_posix()):
            rel = file.relative_to(refs).as_posix()
            folder = rel.split("/", 1)[0]
            if "/" not in rel:
                continue
            body = read(file)
            if folder in ("guides", "help"):
                source = SOURCE_LINE.search(body)
                skill.pages.append(Page(skill.name, folder, rel, len(body.encode("utf-8")), source and source[1]))
            elif folder == "cli":
                add_cli_page(skill, rel, body)
            elif folder in LOOKUP_FOLDERS:
                skill.lookup[folder] = skill.lookup.get(folder, 0) + 1
        skills[skill.name] = skill
    return skills


def add_cli_page(skill: Skill, rel: str, body: str) -> None:
    title = body.split("\n", 1)[0]
    if not title.startswith("# /"):
        raise CoverageError(f"{skill.name}/references/{rel}: the first line is not '# /menu/path'")
    path = title[2:].strip()
    kind = TYPE_LINE.search(body)
    skill.commands.update(COMMAND_HEADING.findall(body))
    if kind and kind[1].strip() == "Command":
        skill.commands.add(path)
    else:
        skill.menus.append(Menu(skill.name, path, rel, len(ARGUMENT.findall(body))))


# ------------------------------------------------------------------ policy


def load_policy(root: Path) -> list[dict[str, str]]:
    path = root / POLICY
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CoverageError(f"{POLICY.as_posix()}: {exc}") from exc
    entries = data.get("excluded") if isinstance(data, dict) else None
    if not isinstance(entries, list):
        raise CoverageError(f"{POLICY.as_posix()}: 'excluded' must be a list")
    return entries


def check_policy(entries: list[dict[str, str]], skills: dict[str, Skill]) -> list[str]:
    """Problems with the exclusions: a wrong shape, an unknown skill, or an entry that matches nothing."""
    problems: list[str] = []
    for number, entry in enumerate(entries, 1):
        label = f"{POLICY.as_posix()}: excluded[{number}]"
        if not isinstance(entry, dict) or set(entry) != {"skill", "folder", "prefix", "reason"}:
            problems.append(f"{label}: needs exactly skill, folder, prefix and reason")
            continue
        if entry["skill"] not in skills:
            problems.append(f"{label}: unknown skill {entry['skill']!r}")
        elif entry["folder"] not in POLICY_FOLDERS:
            problems.append(f"{label}: folder must be one of {', '.join(POLICY_FOLDERS)}")
        elif not str(entry["reason"]).strip():
            problems.append(f"{label}: a reason is required")
        elif not any(excluded_by(entry, item) for item in items_of(skills[entry["skill"]])):
            problems.append(f"{label}: matches nothing in {entry['skill']} (remove it)")
    return problems


def item_key(item: Page | Menu) -> tuple[str, str]:
    """(folder, path below the folder without .md) of a page or menu."""
    if isinstance(item, Menu):
        return "cli", item.path.lstrip("/")
    return item.folder, item.rel[len(item.folder) + 1 :].removesuffix(".md")


def items_of(skill: Skill) -> list[Page | Menu]:
    return [*skill.pages, *skill.menus]


def excluded_by(entry: dict[str, str], item: Page | Menu) -> bool:
    folder, key = item_key(item)
    prefix = entry["prefix"].strip("/")
    return entry["folder"] == folder and (prefix == "" or key == prefix or key.startswith(prefix + "/"))


# ------------------------------------------------------------------ naming


class Trie:
    """The CLI paths of the manual as a tree, so a written command can be resolved to the menu it names."""

    def __init__(self) -> None:
        self.children: dict[str, Trie] = {}
        self.kind: str | None = None
        self.path = ""

    def add(self, path: str, kind: str) -> None:
        node = self
        walked = ""
        for part in path.strip("/").split("/"):
            walked += "/" + part
            node = node.children.setdefault(part, Trie())
            node.path = walked
        if node.kind != "menu":
            node.kind = kind


def build_trie(skills: dict[str, Skill]) -> Trie:
    trie = Trie()
    for skill in skills.values():
        for command in skill.commands:
            trie.add(command, "command")
    for skill in skills.values():
        for menu in skill.menus:
            trie.add(menu.path, "menu")
    return trie


def nearest_menu(trie: Trie, path: str) -> str | None:
    parts = path.strip("/").split("/")
    for depth in range(len(parts) - 1, 0, -1):
        node = trie
        for part in parts[:depth]:
            node = node.children[part]
        if node.kind == "menu":
            return node.path
    return None


def mentioned_paths(text: str, trie: Trie) -> set[str]:
    """CLI menus (and the menus of commands) that ``text`` writes as a path, in either spelling.

    ``/ip firewall filter add chain=input`` and ``/ip/firewall/filter`` both name ``/ip/firewall/filter``. The walk
    follows the manual's own menu tree and stops at the first word that is not a child, so prose after a menu does not
    count and a parent is not credited for a child that is written out.
    """
    found: set[str] = set()
    for line in text.splitlines():
        for start in PATH_START.finditer(line):
            node, pos, deepest = trie, start.end(), None
            while True:
                token = TOKEN.match(line, pos)
                # A letter or underscore right after the token makes it a different word (a name, a variable).
                glued = token and line[token.end() : token.end() + 1].replace("_", "A").isalpha()
                child = node.children.get(token[0]) if token and not glued else None
                if child is None:
                    break
                node, pos = child, token.end()
                if child.kind:
                    deepest = child
                separator = SEPARATOR.match(line, pos)
                if not separator:
                    break
                pos = separator.end()
            if deepest is None:
                continue
            if deepest.kind == "menu":
                found.add(deepest.path)
            else:
                menu = nearest_menu(trie, deepest.path)
                if menu:
                    found.add(menu)
    return found


@dataclass
class Mentions:
    """The reference files, folders and bare file names that one SKILL.md writes."""

    files: set[str]
    folders: set[str]
    names: set[str]


def file_mentions(text: str) -> Mentions:
    """Reference files and folders that ``text`` writes, as paths below ``references/``.

    ``references/cli/ip/dns.md`` is the file ``cli/ip/dns.md``; ``references/cli/ip/dns/`` (or the same without the
    trailing slash) is the folder ``cli/ip/dns``. A folder one level below its top folder (``cli/ip``) counts as well,
    so a skill can route a whole area with one folder. The bare top folders (``cli``, ``guides``) name nothing.
    """
    files: set[str] = set()
    folders: set[str] = set()
    for match in REFERENCE_PATH.finditer(text):
        path = match[1].rstrip(".-")
        (files if path.endswith(".md") else folders).add(path)
    return Mentions(files, folders, set(FILE_NAME.findall(text)))


def names_file(mentions: Mentions, rel: str, unique_names: set[str]) -> bool:
    """True when the mentions include the file ``rel``, a folder above it, or its file name when that is unique."""
    parts = rel.split("/")
    in_folder = any("/".join(parts[:depth]) in mentions.folders for depth in range(2, len(parts)))
    return rel in mentions.files or in_folder or (parts[-1] in unique_names and parts[-1] in mentions.names)


def unique_file_names(skill: Skill) -> set[str]:
    """File names that only one page of the skill has, so the bare name leads to exactly one page."""
    names = [p.rel.rsplit("/", 1)[-1] for p in skill.pages]
    return {name for name in names if names.count(name) == 1}


def classify(skills: dict[str, Skill], policy: list[dict[str, str]]) -> None:
    """Set the status of every page and menu."""
    trie = build_trie(skills)
    credits = {name: mentioned_paths(skill.text, trie) for name, skill in skills.items()}
    for skill in skills.values():
        mentions = file_mentions(skill.text)
        unique_names = unique_file_names(skill)
        for item in items_of(skill):
            if any(entry["skill"] == skill.name and excluded_by(entry, item) for entry in policy):
                item.status = "excluded"
            elif isinstance(item, Menu):
                if item.path in credits[skill.name] or names_file(mentions, item.rel, set()):
                    item.status = "named"
                elif any(item.path in found for other, found in credits.items() if other != skill.name):
                    item.status = "elsewhere"
            elif names_file(mentions, item.rel, unique_names):
                item.status = "named"


# ------------------------------------------------------------------ the report


def percent(part: int, whole: int) -> str:
    return "n/a" if whole == 0 else f"{int(100 * part / whole + 0.5)}%"


def counted(items: list[Page | Menu]) -> list[Page | Menu]:
    return [item for item in items if item.status != "excluded"]


def cluster(path: str) -> str:
    return "/" + "/".join(path.strip("/").split("/")[:3])


def load_json(root: Path, name: Path) -> dict:
    try:
        data = json.loads((root / name).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CoverageError(f"{name.as_posix()}: {exc}") from exc
    if not isinstance(data, dict):
        raise CoverageError(f"{name.as_posix()}: the top level must be an object")
    return data


def render_report(skills: dict[str, Skill], policy: list[dict[str, str]], snapshot: dict, lock: dict | None) -> str:
    pages = [p for s in skills.values() for p in s.pages]
    menus = [m for s in skills.values() for m in s.menus]
    guides = [p for p in pages if p.folder == "guides"]
    helps = [p for p in pages if p.folder == "help"]
    manual = snapshot.get("manual", {})
    out = [
        "# Skill coverage",
        "",
        "Generated by `python tools/skill_coverage.py --write`. Do not edit by hand: change a `SKILL.md`, "
        "`tools/scopes.json` or `tools/coverage_policy.json` and run the command again. CI fails when this file "
        "is stale.",
        "",
        "Every page of the manual is in some skill's `references/` folder. An agent opens a reference only when the "
        "skill leads it there, so this page measures how much of each skill's references its `SKILL.md` **names**:",
        "",
        "- A guide or help-only page is *named* when `SKILL.md` links its file or its folder.",
        "- A CLI menu is *named* when `SKILL.md` writes the menu path (`/ip firewall filter` or `/ip/firewall/filter`) "
        "or links its file or folder. It is *named elsewhere* when only another skill's `SKILL.md` does.",
        "- A page that is not named is still in `references/` and in the skill's `INDEX.md`, so an agent can find it "
        "by browsing. Nothing tells it to look. That is a gap in the routing, not in the documentation.",
        "- Product manuals and regulatory texts are looked up with a script or the index and are not counted.",
        "- The counts leave out what `tools/coverage_policy.json` excludes, with a reason.",
        "",
        f"Snapshot: manual.mikrotik.com crawled {manual.get('crawled', 'unknown')}. " + manual_line(lock),
        "",
        "## Summary",
        "",
        "| | Named | Named elsewhere | Not named | Excluded | Total |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        summary_row("Guides", guides),
        summary_row("Help-only pages", helps),
        summary_row("CLI menus", menus),
        "",
        f"The skills hold {sum(len(s.commands) for s in skills.values())} CLI commands inside those menu pages and "
        f"{sum(sum(s.lookup.values()) for s in skills.values())} product manual and regulatory pages that are "
        "looked up rather than routed.",
        "",
        "## By skill",
        "",
        "| Skill | SKILL.md lines | Guides named | Size named | Menus named | Named elsewhere | Not named |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for skill in skills.values():
        out.append(skill_row(skill))
    out += ["", *render_backlog(skills), *render_largest_guides(guides), *render_policy(policy, skills)]
    out += [
        "## Improving a number",
        "",
        "1. `python tools/skill_coverage.py --list <skill>` prints everything that skill does not name.",
        "2. Teach it in `SKILL.md` (a recipe with the menu path, or a row in the routing table that links the file or "
        "its folder), or move the page to the skill that should own it in `tools/scopes.json`.",
        "3. A page that should not be routed goes into `tools/coverage_policy.json` with a reason.",
        "4. Run `python tools/skill_coverage.py --write` and commit the new report with the change.",
        "",
    ]
    return "\n".join(out)


def manual_line(lock: dict | None) -> str:
    if not lock:
        return "No manual lock is recorded."
    manual = lock.get("manual", {})
    return (
        f"Last compared with the live manual {manual.get('version', 'unknown')} on {lock.get('reviewed', 'unknown')} "
        "(see `docs/manual.lock.json`)."
    )


def summary_row(label: str, items: list[Page] | list[Menu]) -> str:
    counts = {status: sum(1 for i in items if i.status == status) for status in ("named", "elsewhere", "unnamed")}
    excluded = sum(1 for i in items if i.status == "excluded")
    scored = len(items) - excluded
    return (
        f"| {label} | {counts['named']} ({percent(counts['named'], scored)}) | {counts['elsewhere']} | "
        f"{counts['unnamed']} | {excluded} | {len(items)} |"
    )


def skill_row(skill: Skill) -> str:
    link = f"[{skill.name}](../skills/{skill.name}/SKILL.md)"
    scored_pages = [p for p in skill.pages if p.status != "excluded"]
    named_pages = [p for p in scored_pages if p.status == "named"]
    total_size = sum(p.size for p in scored_pages)
    named_size = sum(p.size for p in named_pages)
    scored_menus = [m for m in skill.menus if m.status != "excluded"]
    named = sum(1 for m in scored_menus if m.status == "named")
    elsewhere = sum(1 for m in scored_menus if m.status == "elsewhere")
    return (
        f"| {link} | {skill.lines} | {len(named_pages)}/{len(scored_pages)} | {percent(named_size, total_size)} | "
        f"{named}/{len(scored_menus)} ({percent(named, len(scored_menus))}) | {elsewhere} | "
        f"{len(scored_menus) - named - elsewhere} |"
    )


def render_backlog(skills: dict[str, Skill]) -> list[str]:
    groups: dict[tuple[str, str], list[int]] = {}
    for skill in skills.values():
        for menu in skill.menus:
            if menu.status == "unnamed":
                entry = groups.setdefault((skill.name, cluster(menu.path)), [0, 0])
                entry[0] += 1
                entry[1] += menu.args
    ranked = sorted(groups.items(), key=lambda kv: (-kv[1][1], -kv[1][0], kv[0]))[:BACKLOG_ROWS]
    out = [
        "## Largest gaps among CLI menus",
        "",
        f"The {len(ranked)} areas with the most arguments in menus that no `SKILL.md` names (for the skill that holds "
        "them), grouped by the first three path levels. Arguments are what an agent would otherwise have to guess.",
        "",
        "| Skill | Area | Menus not named | Arguments |",
        "| --- | --- | ---: | ---: |",
    ]
    out += [f"| {skill} | `{area}` | {count} | {args} |" for (skill, area), (count, args) in ranked]
    return out + [""]


def render_largest_guides(guides: list[Page]) -> list[str]:
    unnamed = sorted((g for g in guides if g.status == "unnamed"), key=lambda g: (-g.size, g.skill, g.rel))
    out = [
        "## Largest guides not named",
        "",
        f"The {min(LARGEST_GUIDES, len(unnamed))} biggest guide pages that their skill's `SKILL.md` does not link.",
        "",
        "| Skill | Guide | Size |",
        "| --- | --- | ---: |",
    ]
    for guide in unnamed[:LARGEST_GUIDES]:
        label = "/".join(guide.rel.removeprefix("guides/").split("/")[-3:])
        link = f"[{label}](../skills/{guide.skill}/references/{guide.rel})"
        out.append(f"| {guide.skill} | {link} | {guide.size / 1024:.1f} KiB |")
    return out + [""]


def render_policy(policy: list[dict[str, str]], skills: dict[str, Skill]) -> list[str]:
    out = ["## Exclusions", ""]
    if not policy:
        return [*out, "None. Add an entry to `tools/coverage_policy.json` for a page that should not be routed.", ""]
    out += ["| Skill | Folder | Prefix | Pages | Reason |", "| --- | --- | --- | ---: | --- |"]
    for entry in policy:
        count = sum(1 for item in items_of(skills[entry["skill"]]) if excluded_by(entry, item))
        prefix = entry["prefix"].strip("/") or "(all)"
        out.append(f"| {entry['skill']} | {entry['folder']} | `{prefix}` | {count} | {entry['reason']} |")
    return out + [""]


def render_list(skill: Skill) -> str:
    """Everything one skill's SKILL.md does not name, for the person who wants to improve it."""
    out = [f"{skill.name}: {skill.lines} lines in SKILL.md", ""]
    unnamed = sorted((p for p in skill.pages if p.status == "unnamed"), key=lambda p: (-p.size, p.rel))
    out.append(f"Guides and help pages not named ({len(unnamed)}), largest first:")
    out += [f"  {p.size / 1024:6.1f} KiB  references/{p.rel}" for p in unnamed] or ["  none"]
    groups: dict[str, list[Menu]] = {}
    for menu in skill.menus:
        if menu.status in ("unnamed", "elsewhere"):
            groups.setdefault(cluster(menu.path), []).append(menu)
    out += ["", f"CLI menus not named ({sum(len(v) for v in groups.values())}), by area:"]
    for area, members in sorted(groups.items(), key=lambda kv: (-sum(m.args for m in kv[1]), kv[0])):
        out.append(f"  {area}: {len(members)} menus, {sum(m.args for m in members)} arguments")
        out += [f"      {m.path}{' (named elsewhere)' if m.status == 'elsewhere' else ''}" for m in members]
    return "\n".join(out) + "\n"


# ------------------------------------------------------------------ the manual: index, lock, drift


@dataclass
class Index:
    version: str | None
    guides: set[str]
    cli: set[str]
    entries: int


def parse_index(text: str) -> Index:
    """Read the manual's ``llms.txt``: its version and the documentation page paths (without ``.md``)."""
    version = INDEX_VERSION.search(text)
    paths = set(INDEX_ENTRY.findall(text))
    cli = {"/" + p.removeprefix("cli-reference/") for p in paths if p.startswith("cli-reference/")}
    return Index(version and version[1], {p for p in paths if not p.startswith("cli-reference/")}, cli, len(paths))


def snapshot_pages(skills: dict[str, Skill]) -> tuple[set[str], set[str]]:
    """Guide paths (below docs/) and CLI paths of the manual that the references were built from."""
    prefix = MANUAL + "/docs/"
    guides = {
        p.source.removeprefix(prefix).rstrip("/")
        for s in skills.values()
        for p in s.pages
        if p.folder == "guides" and p.source and p.source.startswith(prefix)
    }
    cli = {m.path for s in skills.values() for m in s.menus} | {c for s in skills.values() for c in s.commands}
    return guides, cli


def scope_rules(root: Path) -> list[tuple[str, str, str]]:
    """The longest-prefix rules of tools/scopes.json (the same rule as ``build_references.match_scope``)."""
    scopes = load_json(root, SCOPES).get("scopes")
    if not isinstance(scopes, list):
        raise CoverageError(f"{SCOPES.as_posix()}: 'scopes' must be a list")
    rules = []
    for scope in scopes:
        rules += [("manual", prefix, scope["name"]) for prefix in scope.get("manual", [])]
        rules += [("cli", prefix, scope["name"]) for prefix in scope.get("cli", [])]
    return rules


def match_scope(kind: str, path: str, rules: list[tuple[str, str, str]]) -> str | None:
    best: tuple[int, str] | None = None
    for rule_kind, prefix, name in rules:
        if rule_kind != kind:
            continue
        stem = prefix.removesuffix("$")
        if (path == stem or (not prefix.endswith("$") and path.startswith(stem + "/"))) and (
            best is None or len(stem) > best[0]
        ):
            best = (len(stem), name)
    return best[1] if best else None


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def check_lock(lock: dict) -> list[str]:
    problems = []
    version = lock.get("manual", {}).get("version") if isinstance(lock.get("manual"), dict) else None
    if not isinstance(version, str) or not version:
        problems.append(f"{LOCK.as_posix()}: manual.version is required")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(lock.get("reviewed", ""))):
        problems.append(f"{LOCK.as_posix()}: reviewed must be a date (YYYY-MM-DD)")
    for key in ("index", "corpus"):
        entry = lock.get(key)
        if not isinstance(entry, dict) or not SHA256.match(str(entry.get("sha256", ""))):
            problems.append(f"{LOCK.as_posix()}: {key}.sha256 must be a SHA-256 in lower-case hex")
        elif not isinstance(entry.get("bytes"), int) or entry["bytes"] <= 0:
            problems.append(f"{LOCK.as_posix()}: {key}.bytes must be a positive integer")
    return problems


def make_lock(index: bytes, corpus: bytes, meta: dict[str, dict], snapshot: dict, reviewed: str) -> dict:
    parsed = parse_index(index.decode("utf-8"))
    if not parsed.version:
        raise CoverageError("the index has no 'Index of the RouterOS <version> manual' line")
    lock: dict = {
        "_comment": (
            "Written by 'python tools/skill_coverage.py --write-lock' after a drift review. It records the manual "
            "the references were last compared with; the report in docs/skill-coverage.md does not depend on it."
        ),
        "manual": {"url": MANUAL, "version": parsed.version},
        "reviewed": reviewed,
        "snapshot_crawled": snapshot.get("manual", {}).get("crawled"),
    }
    for key, data, url in (("index", index, INDEX_URL), ("corpus", corpus, CORPUS_URL)):
        entry = {"url": url, "sha256": sha256(data), "bytes": len(data)}
        if key == "index":
            entry["entries"] = parsed.entries
        entry.update({k: v for k, v in meta.get(key, {}).items() if v})
        lock[key] = entry
    return lock


def compute_drift(
    skills: dict[str, Skill],
    rules: list[tuple[str, str, str]],
    live: Index,
    lock: dict | None,
    live_hashes: dict[str, str],
) -> dict:
    snap_guides, snap_cli = snapshot_pages(skills)

    def side(live_set: set[str], snap_set: set[str], kind: str) -> dict[str, list[dict[str, str | None]]]:
        def owner(path: str) -> str | None:
            return match_scope(kind, path.lstrip("/"), rules)

        return {
            "added": [{"path": p, "skill": owner(p)} for p in sorted(live_set - snap_set)],
            "removed": [{"path": p, "skill": owner(p)} for p in sorted(snap_set - live_set)],
        }

    guides = side(live.guides, snap_guides, "manual")
    cli = side(live.cli, snap_cli, "cli")
    unassigned = [p["path"] for group in (guides, cli) for p in group["added"] if p["skill"] is None]
    changes: list[str] = []
    if lock:
        locked = lock.get("manual", {}).get("version")
        if live.version and locked and live.version != locked:
            changes.append(f"manual version {locked} -> {live.version}")
        for key in ("index", "corpus"):
            seen = live_hashes.get(key)
            if seen and seen != lock.get(key, {}).get("sha256"):
                changes.append(f"{key} content changed since {lock.get('reviewed', 'the last review')}")
    return {
        "live_version": live.version,
        "live_entries": live.entries,
        "guides": guides,
        "cli": cli,
        "unassigned": unassigned,
        "lock_changes": changes,
        "lock_present": lock is not None,
    }


def drift_counts(drift: dict) -> tuple[int, int]:
    """(errors, warnings): a new page without a skill is an error; any other difference is a warning."""
    pages = sum(len(drift[kind][side]) for kind in ("guides", "cli") for side in ("added", "removed"))
    return len(drift["unassigned"]), pages - len(drift["unassigned"]) + len(drift["lock_changes"])


def render_drift(drift: dict) -> str:
    errors, warnings = drift_counts(drift)
    out = [
        "# Manual drift",
        "",
        f"The live manual is version {drift['live_version'] or 'unknown'} "
        f"with {drift['live_entries']} pages in its index.",
        "",
    ]
    if not drift["lock_present"]:
        out.append("- There is no `docs/manual.lock.json` to compare the manual with.")
    else:
        out += [f"- {change}" for change in drift["lock_changes"]] or ["- Nothing changed against the manual lock."]
    out += ["", f"{errors} page(s) without a skill (errors), {warnings} other difference(s) (warnings).", ""]
    for title, kind in (("Guides", "guides"), ("CLI paths", "cli")):
        for side, heading in (
            ("added", "in the manual, not in the snapshot"),
            ("removed", "in the snapshot, not in the manual"),
        ):
            rows = drift[kind][side]
            if not rows:
                continue
            out += [f"## {title} {heading} ({len(rows)})", "", "| Path | Skill |", "| --- | --- |"]
            out += [f"| `{r['path']}` | {r['skill'] or '**none: add it to tools/scopes.json**'} |" for r in rows]
            out.append("")
    if errors == warnings == 0:
        out += ["The snapshot has every page of the manual and nothing the manual dropped.", ""]
        return "\n".join(out)
    if errors:
        out += [
            "A page without a skill makes `build_references.py` stop. Give it a skill in `tools/scopes.json` (or make "
            "the build skip it if it is not documentation) before the next crawl.",
            "",
        ]
    out += [
        "To refresh the snapshot run `crawl_manual.py`, `build_references.py` and `verify_references.py`, then "
        "`python tools/skill_coverage.py --manual-index .cache/manual/llms.txt "
        "--manual-corpus .cache/manual/llms-full.txt --write-lock` on the files the crawl downloaded, and `--write` "
        "for the coverage report.",
        "",
    ]
    return "\n".join(out)


def download(url: str) -> tuple[bytes, dict[str, str | None]]:
    """Fetch one of the two fixed manual URLs; nothing else can be requested."""
    if url not in (INDEX_URL, CORPUS_URL):
        raise CoverageError(f"refusing to fetch {url}")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            if not response.geturl().startswith(MANUAL + "/"):
                raise CoverageError(f"{url} redirected outside {MANUAL}")
            body = response.read(MAX_DOWNLOAD + 1)
            meta = {"etag": response.headers.get("ETag"), "last_modified": response.headers.get("Last-Modified")}
    except (urllib.error.URLError, TimeoutError) as exc:
        raise CoverageError(f"{url}: {exc}") from exc
    if len(body) > MAX_DOWNLOAD:
        raise CoverageError(f"{url} is larger than {MAX_DOWNLOAD} bytes")
    return body, meta


# ------------------------------------------------------------------ command line


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this repository)")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help=f"write {REPORT.as_posix()}")
    mode.add_argument("--check", action="store_true", help="verify the inputs and that the report is current")
    mode.add_argument("--list", metavar="SKILL", help="print everything one skill's SKILL.md does not name")
    parser.add_argument("--fetch", action="store_true", help="download llms.txt and llms-full.txt from the manual")
    parser.add_argument("--manual-index", type=Path, metavar="FILE", help="a copy of the manual's llms.txt")
    parser.add_argument("--manual-corpus", type=Path, metavar="FILE", help="a copy of the manual's llms-full.txt")
    parser.add_argument("--report", type=Path, metavar="FILE", help="write the drift report as Markdown")
    parser.add_argument("--json", type=Path, metavar="FILE", help="write the drift report as JSON")
    parser.add_argument("--strict", action="store_true", help="treat drift as a failure too")
    parser.add_argument("--write-lock", action="store_true", help=f"write {LOCK.as_posix()} from the manual files")
    args = parser.parse_args(argv)
    has_input = args.fetch or args.manual_index
    if args.fetch and (args.manual_index or args.manual_corpus):
        parser.error("--fetch cannot be combined with --manual-index or --manual-corpus")
    for flag in ("report", "json", "strict", "write_lock", "manual_corpus"):
        if getattr(args, flag) and not has_input:
            parser.error(f"--{flag.replace('_', '-')} needs --fetch or --manual-index")
    if args.write_lock and not (args.fetch or args.manual_corpus):
        parser.error("--write-lock needs the corpus: use --fetch or --manual-corpus")
    return args


def manual_files(args: argparse.Namespace) -> tuple[bytes, bytes | None, dict[str, dict]]:
    if args.fetch:
        index, index_meta = download(INDEX_URL)
        corpus, corpus_meta = download(CORPUS_URL)
        return index, corpus, {"index": index_meta, "corpus": corpus_meta}
    corpus = args.manual_corpus.read_bytes() if args.manual_corpus else None
    return args.manual_index.read_bytes(), corpus, {}


def run_drift(args: argparse.Namespace, skills: dict[str, Skill], snapshot: dict, lock: dict | None) -> int:
    index, corpus, meta = manual_files(args)
    live = parse_index(index.decode("utf-8"))
    hashes = {"index": sha256(index)}
    if corpus is not None:
        hashes["corpus"] = sha256(corpus)
    drift = compute_drift(skills, scope_rules(args.root), live, lock, hashes)
    text = render_drift(drift)
    print(text)
    if args.report:
        args.report.write_text(text, encoding="utf-8", newline="\n")
    if args.json:
        args.json.write_text(json.dumps(drift, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    if args.write_lock:
        new_lock = make_lock(index, corpus or b"", meta, snapshot, datetime.now(timezone.utc).date().isoformat())
        (args.root / LOCK).parent.mkdir(parents=True, exist_ok=True)
        (args.root / LOCK).write_text(json.dumps(new_lock, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {LOCK.as_posix()}")
    errors, warnings = drift_counts(drift)
    return 1 if errors or (args.strict and warnings) else 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    root: Path = args.root
    try:
        skills = load_inventory(root)
        policy = load_policy(root)
        snapshot = load_json(root, SNAPSHOT)
        lock = load_json(root, LOCK) if (root / LOCK).exists() else None
        problems = check_policy(policy, skills) + (check_lock(lock) if lock else [])
        if problems:
            print("\n".join(problems), file=sys.stderr)
            return 1
        classify(skills, policy)
        report = render_report(skills, policy, snapshot, lock)
        status = 0
        if args.list:
            if args.list not in skills:
                print(f"unknown skill {args.list!r}", file=sys.stderr)
                return 2
            print(render_list(skills[args.list]), end="")
        elif args.write:
            (root / REPORT).parent.mkdir(parents=True, exist_ok=True)
            (root / REPORT).write_text(report, encoding="utf-8", newline="\n")
            print(f"wrote {REPORT.as_posix()}")
        elif args.check:
            current = read(root / REPORT) if (root / REPORT).exists() else ""
            if current != report:
                diff = difflib.unified_diff(
                    current.splitlines(), report.splitlines(), "committed", "generated", lineterm="", n=1
                )
                print("\n".join(list(diff)[:60]), file=sys.stderr)
                print(f"{REPORT.as_posix()} is stale: run 'python tools/skill_coverage.py --write'", file=sys.stderr)
                status = 1
            else:
                print(f"{REPORT.as_posix()} is current")
        elif not (args.fetch or args.manual_index):
            print(report, end="")
        if args.fetch or args.manual_index:
            status = max(status, run_drift(args, skills, snapshot, lock))
        return status
    except (CoverageError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
