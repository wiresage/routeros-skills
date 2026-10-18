#!/usr/bin/env python3
"""Check that every relative link in the repository's Markdown files resolves.

Absolute URLs and pure ``#anchor`` links are not followed; the job of this
script is to catch moved or deleted files inside the repository.

    python tools/check_links.py
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".cache", ".venv", "venv", "node_modules", "__pycache__"}
LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
EXTERNAL = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if not SKIP_DIRS.intersection(p.relative_to(root).parts))


def links_in(path: Path) -> list[tuple[int, str]]:
    found = []
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), start=1):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK.finditer(INLINE_CODE.sub("", line)):
            found.append((number, match.group(1)))
    return found


def check(root: Path) -> list[str]:
    problems = []
    for path in markdown_files(root):
        for number, target in links_in(path):
            if EXTERNAL.match(target) or target.startswith(("#", "//")):
                continue
            file_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not file_part:
                continue
            resolved = (root / file_part.lstrip("/")) if file_part.startswith("/") else (path.parent / file_part)
            if not resolved.exists():
                problems.append(f"{path.relative_to(root).as_posix()}:{number}: broken link to {target}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    files = markdown_files(root)
    problems = check(root)
    for problem in problems:
        print(f"error: {problem}")
    print(f"checked {len(files)} Markdown file(s): {len(problems)} broken link(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
