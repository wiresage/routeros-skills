#!/usr/bin/env python3
"""Check that docs-snapshot.json describes what is in the repository.

The snapshot is written by ``build_references.py``. This check catches a snapshot that was edited by hand, or references
that were changed without rebuilding it: for every skill in ``skills/`` the number of reference files must match.

    python tools/check_snapshot.py             # verify
    python tools/check_snapshot.py --summary   # print a Markdown summary (for the CI job summary)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("manual", "help", "not_included", "skills")


def reference_files(skill: Path) -> int:
    return sum(1 for _ in (skill / "references").rglob("*.md")) if (skill / "references").is_dir() else 0


def load(root: Path) -> dict:
    return json.loads((root / "docs-snapshot.json").read_text(encoding="utf-8"))


def check(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []
    try:
        snapshot = load(root)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"docs-snapshot.json: {exc}"], notes
    for key in REQUIRED:
        if key not in snapshot:
            errors.append(f"docs-snapshot.json: missing '{key}'")
    if errors:
        return errors, notes
    on_disk = {p.name: p for p in (root / "skills").iterdir() if p.is_dir()}
    described = snapshot["skills"]
    for name, folder in sorted(on_disk.items()):
        if name not in described:
            errors.append(f"docs-snapshot.json: skill {name} is not described")
            continue
        expected = described[name].get("files")
        actual = reference_files(folder)
        if expected != actual:
            errors.append(f"{name}: snapshot says {expected} reference files, found {actual}; rebuild the references")
    missing = sorted(set(described) - set(on_disk))
    if missing:
        notes.append(f"{len(missing)} skill(s) in the snapshot are not in the repository yet: {', '.join(missing)}")
    return errors, notes


def summary(root: Path) -> str:
    snapshot = load(root)
    manual, help_site = snapshot["manual"], snapshot["help"]
    lines = [
        "## Skills health check",
        "",
        f"- Documentation snapshot: {manual['crawled']} ({manual['guides']} guides, "
        f"{manual['cli_reference_pages']} CLI pages, {manual['hardware_manuals']} hardware manuals)",
        f"- help.mikrotik.com: {help_site['pages_crawled']} pages crawled, {help_site['imported']} imported, "
        f"{help_site['covered_by_manual']} covered by the manual, {help_site['excluded']} excluded",
        "",
        "| Skill | Reference files |",
        "| --- | ---: |",
    ]
    on_disk = sorted(p.name for p in (root / "skills").iterdir() if p.is_dir())
    lines += [f"| {name} | {reference_files(root / 'skills' / name)} |" for name in on_disk]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    parser.add_argument("--summary", action="store_true", help="print a Markdown summary instead of checking")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.summary:
        sys.stdout.write(summary(root))
        return 0
    errors, notes = check(root)
    for note in notes:
        print(f"note: {note}")
    for error in errors:
        print(f"error: {error}")
    print(f"snapshot check: {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
