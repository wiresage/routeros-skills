#!/usr/bin/env python3
"""Check that the RouterOS property names used in SKILL.md files exist in the documentation.

Every ``name=value`` pair in a skill (code blocks and inline code) is a claim that ``name`` is a property of some
command. This script looks for the name in the generated references of all skills; a name that appears nowhere is
probably invented, misspelled or from memory, and needs a look.

    python tools/check_properties.py                 # check every skill
    python tools/check_properties.py skills/routeros-dhcp
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAIR = re.compile(r"(?<![\w./:-])([a-z][a-z0-9]*(?:[-.][a-z0-9]+)*)=(?=[\"'\w!$\[.:@/-]|$)")
WORD = re.compile(r"[a-z][a-z0-9]*(?:[-.][a-z0-9]+)*")
FENCE = re.compile(r"^\s*(```|~~~)")
BARE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)+$")
# Names that are not RouterOS properties: shell variables, script and tool options, URL query keys, and the like.
IGNORED = {"user", "pass", "key", "dir"}


def vocabulary(skills_dir: Path) -> set[str]:
    words: set[str] = set()
    for path in skills_dir.glob("*/references/**/*.md"):
        words.update(WORD.findall(path.read_text(encoding="utf-8").lower()))
    return words


def pairs_in(path: Path) -> list[tuple[int, str]]:
    found = []
    in_fence = False
    lines = path.read_text(encoding="utf-8").split("\n")
    # Skip the front matter.
    start = lines[1:].index("---") + 2 if lines and lines[0] == "---" else 0
    for number, line in enumerate(lines[start:], start=start + 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            found.extend((number, m.group(1)) for m in PAIR.finditer(line.lower()))
            continue
        for span in re.findall(r"`([^`]+)`", line):
            found.extend((number, m.group(1)) for m in PAIR.finditer(span.lower()))
            if BARE.match(span.lower()):
                found.append((number, span.lower()))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("skills", nargs="*", type=Path)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    args = parser.parse_args()
    skills_dir = args.root / "skills"
    known = vocabulary(skills_dir)
    folders = [p.resolve() for p in args.skills] or sorted(p for p in skills_dir.iterdir() if p.is_dir())
    problems = 0
    root = args.root.resolve()
    for folder in folders:
        skill_md = folder / "SKILL.md"
        if not skill_md.is_file():
            continue
        where = skill_md.relative_to(root).as_posix()
        for number, name in pairs_in(skill_md):
            if name not in known and name not in IGNORED:
                print(f"error: {where}:{number}: '{name}' appears nowhere in the references")
                problems += 1
    print(f"property check: {problems} unknown name(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
