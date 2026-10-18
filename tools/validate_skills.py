#!/usr/bin/env python3
"""Validate the format and folder structure of every skill in ``skills/``.

A skill is one folder with a ``SKILL.md`` file and, optionally, ``scripts/``,
``references/`` and ``assets/``. This repository keeps skills agent-agnostic, so
the front matter is limited to the fields every agent understands.

    python tools/validate_skills.py              # validate all skills
    python tools/validate_skills.py skills/routeros-firewall
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_PREFIX = "routeros-"
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_COMPATIBILITY = 500
MAX_BODY_LINES = 500
# Fields defined by the shared Agent Skills format. Anything else is vendor-specific.
ALLOWED_FIELDS = {"name", "description", "license", "compatibility"}
ALLOWED_ENTRIES = {"SKILL.md", "scripts", "references", "assets"}
SCRIPT_SUFFIXES = {".sh", ".ps1", ".py"}
SHEBANGS = {
    ".sh": ("#!/usr/bin/env bash", "#!/bin/sh", "#!/bin/bash"),
    ".py": ("#!/usr/bin/env python3",),
}
REFERENCE_SUFFIXES = {".md", ".rsc", ".txt", ".json"}
USE_WHEN = re.compile(r"\buse (this skill )?(when|for|to)\b", re.IGNORECASE)


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, where: Path | str, message: str) -> None:
        self.errors.append(f"{_rel(where)}: {message}")

    def warn(self, where: Path | str, message: str) -> None:
        self.warnings.append(f"{_rel(where)}: {message}")


def _rel(where: Path | str) -> str:
    path = Path(where)
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(where)


def parse_front_matter(text: str) -> tuple[dict[str, str], str, str | None]:
    """Split ``text`` into ``(fields, body, problem)``.

    Only single-line ``key: value`` pairs are accepted. Block scalars and nested
    maps are not portable across agents, so they are reported as problems.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text, "the file must start with a '---' front matter block"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, text, "the front matter block is not closed with '---'"
    fields: dict[str, str] = {}
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            return {}, "", f"line {number}: expected a single-line 'key: value' pair, got {line!r}"
        key, raw = match.group(1), match.group(2).strip()
        if raw in (">", "|", ">-", "|-", ">+", "|+"):
            return {}, "", f"line {number}: block scalars are not portable; write '{key}' on one line"
        if raw[:1] == '"':
            try:
                value = json.loads(raw)
            except json.JSONDecodeError:
                return {}, "", f"line {number}: invalid double-quoted string"
        elif raw[:1] == "'":
            if len(raw) < 2 or raw[-1] != "'":
                return {}, "", f"line {number}: invalid single-quoted string"
            value = raw[1:-1].replace("''", "'")
        else:
            value = raw
        if key in fields:
            return {}, "", f"line {number}: duplicate key '{key}'"
        fields[key] = value
    return fields, "\n".join(lines[end + 1 :]), None


def validate_front_matter(skill: Path, fields: dict[str, str], report: Report) -> None:
    skill_md = skill / "SKILL.md"
    for key in sorted(set(fields) - ALLOWED_FIELDS):
        report.error(
            skill_md, f"front matter field '{key}' is not portable (allowed: {', '.join(sorted(ALLOWED_FIELDS))})"
        )
    name = fields.get("name", "")
    if not name:
        report.error(skill_md, "front matter is missing 'name'")
    else:
        if len(name) > MAX_NAME or not NAME_PATTERN.match(name):
            report.error(
                skill_md,
                f"name {name!r} must be lowercase letters, digits and single hyphens, at most {MAX_NAME} characters",
            )
        if name != skill.name:
            report.error(skill_md, f"name {name!r} must match the folder name {skill.name!r}")
        if not name.startswith(NAME_PREFIX):
            report.error(skill_md, f"name {name!r} must start with '{NAME_PREFIX}'")
    description = fields.get("description", "")
    if not description:
        report.error(skill_md, "front matter is missing 'description'")
    else:
        if len(description) > MAX_DESCRIPTION:
            report.error(skill_md, f"description is {len(description)} characters; the limit is {MAX_DESCRIPTION}")
        if len(description) < 80:
            report.error(
                skill_md, "description is too short to route a request; say what the skill covers and when to use it"
            )
        if "<" in description or ">" in description:
            report.error(skill_md, "description must not contain angle brackets")
        if not USE_WHEN.search(description):
            report.error(skill_md, "description must say when to use the skill ('Use when ...')")
    compatibility = fields.get("compatibility")
    if compatibility is not None and len(compatibility) > MAX_COMPATIBILITY:
        report.error(skill_md, f"compatibility is longer than {MAX_COMPATIBILITY} characters")


def validate_body(skill: Path, body: str, report: Report) -> None:
    skill_md = skill / "SKILL.md"
    if not body.strip():
        report.error(skill_md, "the skill has no instructions after the front matter")
        return
    lines = body.strip("\n").split("\n")
    if len(lines) > MAX_BODY_LINES:
        report.error(
            skill_md, f"the body is {len(lines)} lines; keep it under {MAX_BODY_LINES} and move detail into references/"
        )
    in_fence = False
    headings = []
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and re.match(r"^#{1,6} \S", line):
            headings.append(line)
    if not headings or not headings[0].startswith("# "):
        report.error(skill_md, "the body must start with a level-1 heading")
    if "\r" in body:
        report.error(skill_md, "use LF line endings")


def validate_layout(skill: Path, body: str, report: Report) -> None:
    for entry in sorted(skill.iterdir()):
        if entry.name not in ALLOWED_ENTRIES:
            report.error(
                entry, f"unexpected entry; a skill folder may only contain {', '.join(sorted(ALLOWED_ENTRIES))}"
            )
    scripts = skill / "scripts"
    if scripts.is_dir():
        for path in sorted(scripts.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix not in SCRIPT_SUFFIXES:
                report.error(path, f"scripts must be {', '.join(sorted(SCRIPT_SUFFIXES))} files")
                continue
            first = path.read_text(encoding="utf-8").split("\n", 1)[0]
            expected = SHEBANGS.get(path.suffix)
            if expected and first not in expected:
                report.error(path, f"first line must be one of: {', '.join(expected)}")
            relative = path.relative_to(skill).as_posix()
            if relative not in body:
                report.error(path, f"{relative} is not mentioned in SKILL.md, so an agent cannot discover it")
    references = skill / "references"
    if references.is_dir():
        if "references/" not in body:
            report.error(skill / "SKILL.md", "references/ exists but SKILL.md never points to it")
        for path in sorted(references.rglob("*")):
            if path.is_file() and path.suffix not in REFERENCE_SUFFIXES:
                report.error(path, f"references may only be {', '.join(sorted(REFERENCE_SUFFIXES))} files")
        if not (references / "INDEX.md").is_file():
            report.error(references, "references/ needs an INDEX.md that lists what is inside")


def validate_skill(skill: Path, report: Report) -> None:
    skill_md = skill / "SKILL.md"
    if not skill_md.is_file():
        report.error(skill, "folder has no SKILL.md")
        return
    text = skill_md.read_text(encoding="utf-8")
    fields, body, problem = parse_front_matter(text)
    if problem:
        report.error(skill_md, problem)
        return
    validate_front_matter(skill, fields, report)
    validate_body(skill, body, report)
    validate_layout(skill, body, report)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "skills", nargs="*", type=Path, help="skill folders to check (default: every folder in skills/)"
    )
    args = parser.parse_args()

    report = Report()
    if args.skills:
        folders = [p.resolve() for p in args.skills]
    elif SKILLS_DIR.is_dir():
        folders = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    else:
        report.error(SKILLS_DIR, "skills/ directory does not exist")
        folders = []
    for folder in folders:
        validate_skill(folder, report)

    for message in report.warnings:
        print(f"warning: {message}")
    for message in report.errors:
        print(f"error: {message}")
    print(f"checked {len(folders)} skill(s): {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
