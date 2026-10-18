#!/usr/bin/env python3
"""Check that the generated references contain everything that was crawled.

For every crawled page this looks up the generated file and compares the words
of the source with the words of the result, so a conversion bug that drops a
table, a list or a whole section shows up as a low match. It also checks for
leftover MDX and for broken relative links.

    python tools/verify_references.py --cache .cache
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

import build_references as br
import check_links
from bs4 import BeautifulSoup

REPO_ROOT = Path(__file__).resolve().parent.parent
WORD = re.compile(r"[A-Za-z][A-Za-z0-9_-]{3,}")
LEFTOVER = re.compile(r"<(ArgTable|ArgTableRow|Tabs|TabItem|WideTable|DocCardList|Columns?)\b|^:::", re.MULTILINE)
THRESHOLD = 0.97


def words(text: str) -> set[str]:
    return {w.lower() for w in WORD.findall(html.unescape(text))}


def strip_mdx(text: str) -> str:
    """Remove markup that is expected to disappear in conversion (links targets, image paths, tags)."""
    text = re.sub(r"\]\([^)]*\)", "]", text)
    text = re.sub(r"</?[A-Za-z][^>]*>", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\b(arg|typ|c1|c2|c3|mandatory|unset|syscap|deprecated)=", " ", text)
    text = re.sub(r"\{[^{}]*:\s*-?\d+[^{}]*\}", " ", text)  # internal numeric enum codes
    return text


def coverage(source: set[str], result: set[str]) -> float:
    return len(source & result) / len(source) if source else 1.0


def missing_words(source: set[str], result: set[str], limit: int = 8) -> str:
    return ", ".join(sorted(source - result)[:limit])


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_output(skills: Path, scope_for: dict[str, str], out: str) -> Path:
    return skills / scope_for[out] / "references" / out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cache", type=Path, default=REPO_ROOT / ".cache")
    parser.add_argument("--skills", type=Path, default=REPO_ROOT / "skills")
    args = parser.parse_args()
    cache, skills = args.cache, args.skills

    scopes = br.load_scopes(REPO_ROOT / "tools" / "scopes.json")
    rules = br.build_prefix_rules(scopes)
    manifest = json.loads(read(cache / "manual" / "manifest.json"))
    problems: list[str] = []
    checked = {"guides": 0, "cli": 0, "products": 0, "help": 0}
    weakest: list[tuple[float, str]] = []

    all_outputs = {p.relative_to(skills).as_posix(): p for p in skills.rglob("*.md")}

    def locate(scope: str, out: str) -> Path | None:
        return all_outputs.get(f"{scope}/references/{out}")

    # --- narrative guides and CLI pages
    cli_text: dict[str, str] = {}
    for record in manifest["pages"]:
        path = record["path"]
        source = read(cache / "manual" / "pages" / path)
        relative = path[len("docs/") :].removesuffix(".md")
        if relative.startswith("cli-reference/"):
            cli_path = relative[len("cli-reference/") :]
            scope = br.match_scope("cli", cli_path, rules)
            candidates = [cli_path]
            parent = cli_path.rpartition("/")[0]
            if parent:
                candidates.append(parent)
            output = next((p for c in candidates if (p := locate(scope or "", f"cli/{c}.md"))), None)
            if output is None:
                problems.append(f"{path}: no generated file")
                continue
            text = read(output)
            names = re.findall(r'<ArgTableRow\s+arg="([^"]*)"', source)
            missing = [n for n in names if f"`{n}`" not in text]
            if missing:
                problems.append(f"{path}: arguments missing from {output.name}: {missing[:5]}")
            if "/" + cli_path not in text:
                problems.append(f"{path}: heading /{cli_path} not found in {output.name}")
            checked["cli"] += 1
            cli_text[cli_path] = source
            continue
        scope = br.match_scope("manual", relative, rules)
        output = locate(scope or "", f"guides/{relative}.md")
        if output is None:
            problems.append(f"{path}: no generated file")
            continue
        ratio = coverage(words(strip_mdx(source)), words(read(output)))
        checked["guides"] += 1
        weakest.append((ratio, path))
        if ratio < THRESHOLD:
            problems.append(f"{path}: only {ratio:.1%} of the source words are in {output.name}")

    # --- hardware manuals
    for file in sorted((cache / "manual" / "hardware").glob("*.json")):
        page = json.loads(read(file))
        text_source = BeautifulSoup(page["html"], "lxml").get_text(" ")
        main = locate("routeros-hardware", f"products/{file.stem}.md")
        if main is None:
            problems.append(f"hardware/{file.stem}: no generated file")
            continue
        combined = read(main)
        regulatory = locate("routeros-hardware", f"regulatory/{file.stem}.md")
        if regulatory:
            combined += read(regulatory)
        ratio = coverage(words(text_source), words(combined))
        checked["products"] += 1
        weakest.append((ratio, f"hardware/{file.stem}"))
        if ratio < THRESHOLD:
            problems.append(f"hardware/{file.stem}: only {ratio:.1%} of the source words are in the output")

    # --- help pages that were imported
    help_dir = cache / "help"
    imported = {pid for s in scopes.values() for pid in s.get("help", [])}
    for pid in sorted(imported):
        page = json.loads(read(next(help_dir.glob(f"*-{pid}.json"))))
        scope = next(n for n, s in scopes.items() if pid in s.get("help", []))
        folder = skills / scope / "references" / "help"
        marker = f"> Source: {page['url']}\n"
        slug_match = [p for p in folder.glob("*.md") if marker in read(p)]
        if not slug_match:
            problems.append(f"help/{pid} {page['title']}: no generated file")
            continue
        source_words = words(BeautifulSoup(page["html"], "lxml").get_text(" "))
        output_words = words(read(slug_match[0]))
        ratio = coverage(source_words, output_words)
        checked["help"] += 1
        weakest.append((ratio, f"help/{pid} {page['title']}"))
        if ratio < THRESHOLD:
            lost = missing_words(source_words, output_words)
            problems.append(
                f"help/{pid} {page['title']}: only {ratio:.1%} of the source words are in the output ({lost})"
            )

    # --- leftovers and links
    leftovers = 0
    for relative, path in all_outputs.items():
        if relative.endswith("INDEX.md"):
            continue
        in_fence = False
        for number, line in enumerate(read(path).split("\n"), start=1):
            if line.lstrip().startswith(("```", "~~~")):
                in_fence = not in_fence
            if not in_fence and (LEFTOVER.search(line) or "&gt;" in line or "&lt;" in line):
                problems.append(f"{relative}:{number}: leftover markup: {line.strip()[:80]}")
                leftovers += 1
                break
    link_problems = check_links.check(skills.parent)
    problems.extend(link_problems)

    weakest.sort()
    print("weakest matches:", ", ".join(f"{r:.1%} {p}" for r, p in weakest[:5]))
    print("checked:", ", ".join(f"{v} {k}" for k, v in checked.items()))
    for problem in problems[:60]:
        print(f"problem: {problem}")
    print(f"{len(problems)} problem(s) ({leftovers} leftover-markup, {len(link_problems)} broken link(s))")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
