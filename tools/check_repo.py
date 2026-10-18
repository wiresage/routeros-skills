#!/usr/bin/env python3
"""Repository health checks that go beyond a single skill.

* the required root files exist
* README lists exactly the skills that exist
* shell scripts are committed executable
* hand-written prose follows the project style (no em dashes)

    python tools/check_repo.py
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = ["README.md", "AGENTS.md", "CONTRIBUTING.md", "LICENSE", "SECURITY.md"]
EM_DASH = "—"
README_ROW = re.compile(r"^\|\s*\[(routeros-[a-z0-9-]+)\]\(skills/([a-z0-9-]+)/SKILL\.md\)", re.MULTILINE)


def check_root_files(root: Path) -> list[str]:
    problems = []
    for name in REQUIRED_FILES:
        path = root / name
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            problems.append(f"{name}: required root file is missing or empty")
    license_file = root / "LICENSE"
    if license_file.is_file() and "MIT License" not in license_file.read_text(encoding="utf-8"):
        problems.append("LICENSE: expected the MIT License")
    return problems


def check_readme_inventory(root: Path) -> list[str]:
    readme = root / "README.md"
    skills_dir = root / "skills"
    if not readme.is_file() or not skills_dir.is_dir():
        return []
    on_disk = {p.name for p in skills_dir.iterdir() if p.is_dir()}
    listed = dict(README_ROW.findall(readme.read_text(encoding="utf-8")))
    problems = []
    for name in sorted(on_disk - set(listed)):
        problems.append(f"README.md: skill {name} exists but is not in the skills table")
    for name in sorted(set(listed) - on_disk):
        problems.append(f"README.md: skills table lists {name}, which does not exist")
    for name, folder in listed.items():
        if name != folder:
            problems.append(f"README.md: row {name} links to skills/{folder}")
    return problems


def check_executable_scripts(root: Path) -> list[str]:
    try:
        out = subprocess.run(
            ["git", "ls-files", "--stage", "--", "*.sh"],
            cwd=root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return []  # not a git checkout (for example an exported archive)
    problems = []
    for line in out.splitlines():
        mode, _, _, path = line.split(None, 3)
        if mode != "100755":
            problems.append(f"{path}: shell scripts must be committed executable (git update-index --chmod=+x)")
    return problems


def prose_files(root: Path) -> list[Path]:
    files = [root / name for name in REQUIRED_FILES if name != "LICENSE"]
    files += sorted((root / "skills").glob("*/SKILL.md"))
    return [p for p in files if p.is_file()]


def check_style(root: Path) -> list[str]:
    problems = []
    for path in prose_files(root):
        for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), start=1):
            if EM_DASH in line:
                problems.append(
                    f"{path.relative_to(root).as_posix()}:{number}: em dash in prose; use a comma, colon or full stop"
                )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    problems = (
        check_root_files(root) + check_readme_inventory(root) + check_executable_scripts(root) + check_style(root)
    )
    for problem in problems:
        print(f"error: {problem}")
    print(f"repository checks: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
