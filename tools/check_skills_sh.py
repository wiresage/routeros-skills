#!/usr/bin/env python3
"""Check ``skills.sh.json``, the display configuration that skills.sh reads from the repository root.

The file groups the skills on the repository page at https://skills.sh. This check keeps it correct and in step with
the repository:

* the file follows the published schema (https://skills.sh/schemas/skills.sh.schema.json): only the known keys, 1 to 50
  groups, a title of at most 120 characters, a description of at most 500, 1 to 500 skill names per group;
* every name in a group is a skill folder under ``skills/``, and every skill is in exactly one group;
* the groups are the same as the topic groups of the README skills tables (same titles, same skills, same order).

    python tools/check_skills_sh.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_URL = "https://skills.sh/schemas/skills.sh.schema.json"
TOP_LEVEL_KEYS = {"$schema", "schema", "notGrouped", "groupings"}
GROUP_KEYS = {"title", "description", "skills"}
README_HEADING = re.compile(r"^###\s+(.+?)\s*$")
README_ROW = re.compile(r"^\|\s*\[(routeros-[a-z0-9-]+)\]\(skills/[a-z0-9-]+/SKILL\.md\)")


def check_schema(config: object) -> list[str]:
    """Return the ways in which ``config`` breaks the published schema (the subset that can break)."""
    if not isinstance(config, dict):
        return ["skills.sh.json: the top level must be an object"]
    problems = [f"skills.sh.json: unknown key {key!r}" for key in config if key not in TOP_LEVEL_KEYS]
    if config.get("$schema") not in (None, SCHEMA_URL):
        problems.append(f"skills.sh.json: $schema should be {SCHEMA_URL}")
    if config.get("notGrouped", "bottom") not in ("top", "bottom"):
        problems.append("skills.sh.json: notGrouped must be 'top' or 'bottom'")
    groups = config.get("groupings")
    if not isinstance(groups, list) or not 1 <= len(groups) <= 50:
        return [*problems, "skills.sh.json: groupings must be a list of 1 to 50 groups"]
    for number, group in enumerate(groups, start=1):
        where = f"skills.sh.json: group {number}"
        if not isinstance(group, dict):
            problems.append(f"{where} must be an object")
            continue
        problems += [f"{where}: unknown key {key!r}" for key in group if key not in GROUP_KEYS]
        title = group.get("title")
        if not isinstance(title, str) or not 1 <= len(title) <= 120:
            problems.append(f"{where}: title must be a string of 1 to 120 characters")
        description = group.get("description", "")
        if not isinstance(description, str) or len(description) > 500:
            problems.append(f"{where}: description must be a string of at most 500 characters")
        skills = group.get("skills")
        if not isinstance(skills, list) or not 1 <= len(skills) <= 500:
            problems.append(f"{where}: skills must be a list of 1 to 500 names")
        elif not all(isinstance(name, str) and 1 <= len(name) <= 120 for name in skills):
            problems.append(f"{where}: every skill name must be a string of 1 to 120 characters")
    return problems


def check_inventory(config: dict, skill_names: set[str]) -> list[str]:
    """Every skill is in exactly one group and every grouped name is a skill of this repository."""
    problems = []
    seen: dict[str, str] = {}
    for group in config.get("groupings", []):
        for name in group.get("skills", []):
            if name not in skill_names:
                problems.append(f"skills.sh.json: group {group.get('title')!r} lists {name}, which is not a skill")
            elif name in seen:
                problems.append(f"skills.sh.json: {name} is in both {seen[name]!r} and {group.get('title')!r}")
            else:
                seen[name] = group.get("title", "")
    problems += [f"skills.sh.json: skill {name} is not in any group" for name in sorted(skill_names - set(seen))]
    return problems


def readme_groups(readme: str) -> list[tuple[str, list[str]]]:
    """The ``### Title`` sections of the README that contain a skills table, as (title, skill names)."""
    groups: list[tuple[str, list[str]]] = []
    title = None
    for line in readme.splitlines():
        heading = README_HEADING.match(line)
        if heading:
            title = heading.group(1)
            continue
        row = README_ROW.match(line)
        if row and title:
            if not groups or groups[-1][0] != title:
                groups.append((title, []))
            groups[-1][1].append(row.group(1))
    return groups


def check_readme(config: dict, readme: str) -> list[str]:
    """The groups of ``skills.sh.json`` equal the README groups, in the same order."""
    expected = readme_groups(readme)
    actual = [(g.get("title"), list(g.get("skills", []))) for g in config.get("groupings", [])]
    if actual == expected:
        return []
    problems = []
    if [t for t, _ in actual] != [t for t, _ in expected]:
        problems.append(
            "skills.sh.json: group titles differ from the README: "
            f"{[t for t, _ in actual]} against {[t for t, _ in expected]}"
        )
    for (title, skills), (_, wanted) in zip(actual, expected, strict=False):
        if skills != wanted:
            problems.append(f"skills.sh.json: group {title!r} differs from the README table: {skills} against {wanted}")
    return problems


def main(root: Path = ROOT) -> int:
    path = root / "skills.sh.json"
    if not path.is_file():
        print("error: skills.sh.json not found", file=sys.stderr)
        return 1
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"error: skills.sh.json is not valid JSON: {exc}", file=sys.stderr)
        return 1
    problems = check_schema(config)
    if not problems:
        skill_names = {p.name for p in (root / "skills").iterdir() if (p / "SKILL.md").is_file()}
        problems = check_inventory(config, skill_names)
        problems += check_readme(config, (root / "README.md").read_text(encoding="utf-8"))
    for problem in problems:
        print(problem)
    print(f"skills.sh.json check: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
