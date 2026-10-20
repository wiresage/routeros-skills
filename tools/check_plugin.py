#!/usr/bin/env python3
"""Check the Claude plugin manifests of this repository, offline.

The repository root is a Claude plugin (``.claude-plugin/plugin.json``) and a one-plugin marketplace
(``.claude-plugin/marketplace.json``, source ``./``). Everything tracked in git is shipped to a user's plugin cache, and
anything at the root that matches a plugin component location is loaded. This check keeps that safe:

* both manifests are valid JSON with the fields the plugin and marketplace need, and the names agree;
* the version is a plain ``MAJOR.MINOR.PATCH`` set in ``plugin.json`` only (the manifest wins over the marketplace
  entry, so a second copy would only drift);
* the manifest declares no components of its own: the skills come from the default ``skills/`` folder;
* no folder or file at the repository root would be picked up as a plugin component (``commands/``, ``agents/``,
  ``hooks/``, ``bin/``, ``.mcp.json`` and so on), and ``claude.ai`` refuses a plugin with a top-level ``bin/``;
* the tracked files stay inside the claude.ai and Cowork limits (5,000 files, 200 MB per plugin) and contain no
  symlinks.

``claude plugin validate --strict .`` (run in CI) is the authority on the schema; this check covers what it does not.

    python tools/check_plugin.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_FILES, MAX_BYTES = 5000, 200 * 1024 * 1024
WARN_FILES, WARN_BYTES = 4000, 150 * 1024 * 1024
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
VERSION = re.compile(r"^\d+\.\d+\.\d+$")
RESERVED_PREFIXES = ("claude-", "anthropic-", "anthropics-", "cc-plugin-")
RESERVED_NAMES = {"claude", "anthropic", "anthropics", "claude-code", "claude-mods"}
MANIFEST_COMPONENT_KEYS = {
    "skills",
    "commands",
    "agents",
    "hooks",
    "mcpServers",
    "lspServers",
    "outputStyles",
    "workflows",
    "channels",
    "settings",
    "experimental",
}
ROOT_COMPONENTS = [
    "commands",
    "agents",
    "hooks",
    "bin",
    "output-styles",
    "themes",
    "workflows",
    "monitors",
    ".mcp.json",
    ".lsp.json",
    "settings.json",
    "CLAUDE.md",
]


def load(path: Path) -> tuple[dict | None, list[str]]:
    if not path.is_file():
        return None, [f"{path.relative_to(ROOT).as_posix()} not found"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [f"{path.relative_to(ROOT).as_posix()} is not valid JSON: {exc}"]
    if not isinstance(data, dict):
        return None, [f"{path.relative_to(ROOT).as_posix()}: the top level must be an object"]
    return data, []


def check_name(name: object, what: str) -> list[str]:
    if not isinstance(name, str) or not NAME.match(name):
        return [f"{what}: name must be kebab-case (lowercase letters, digits, hyphens), got {name!r}"]
    if name in RESERVED_NAMES or name.startswith(RESERVED_PREFIXES):
        return [f"{what}: name {name!r} passes as one of Anthropic's own and is reserved"]
    return []


def check_plugin(plugin: dict) -> list[str]:
    problems = check_name(plugin.get("name"), "plugin.json")
    version = plugin.get("version")
    if not isinstance(version, str) or not VERSION.match(version):
        problems.append(f"plugin.json: version must look like 1.2.3, got {version!r}")
    if not isinstance(plugin.get("description"), str) or not plugin["description"].strip():
        problems.append("plugin.json: description is missing")
    author = plugin.get("author")
    if not isinstance(author, dict) or not isinstance(author.get("name"), str) or not author["name"].strip():
        problems.append("plugin.json: author.name is missing")
    declared = sorted(MANIFEST_COMPONENT_KEYS & plugin.keys())
    if declared:
        problems.append(f"plugin.json: declares components ({', '.join(declared)}); the skills must come from skills/")
    return problems


def check_marketplace(marketplace: dict, plugin: dict) -> list[str]:
    problems = check_name(marketplace.get("name"), "marketplace.json")
    owner = marketplace.get("owner")
    if not isinstance(owner, dict) or not isinstance(owner.get("name"), str) or not owner["name"].strip():
        problems.append("marketplace.json: owner.name is missing")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1 or not isinstance(plugins[0], dict):
        return [*problems, "marketplace.json: plugins must hold exactly one entry (this repository's plugin)"]
    entry = plugins[0]
    if entry.get("name") != plugin.get("name"):
        problems.append(
            f"marketplace.json: entry name {entry.get('name')!r} differs from plugin.json {plugin.get('name')!r}"
        )
    if entry.get("source") != "./":
        problems.append(f"marketplace.json: source must be './' (the repository root), got {entry.get('source')!r}")
    if "version" in entry:
        problems.append("marketplace.json: do not set version on the entry; plugin.json is the only place for it")
    return problems


def check_root(root: Path) -> list[str]:
    return [
        f"{name} at the repository root would be loaded as a plugin component"
        for name in ROOT_COMPONENTS
        if (root / name).exists()
    ]


def check_skills(root: Path) -> list[str]:
    skills = root / "skills"
    if not skills.is_dir():
        return ["skills/ not found"]
    return [
        f"skills/{p.name} has no SKILL.md"
        for p in sorted(skills.iterdir())
        if p.is_dir() and not (p / "SKILL.md").is_file()
    ]


def tracked_files(root: Path) -> list[tuple[str, str, int]] | None:
    """(mode, path, size) of every file git tracks, or None outside a git checkout."""
    try:
        listing = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-s", "-z"], capture_output=True, check=True
        ).stdout.decode("utf-8", errors="replace")
    except (OSError, subprocess.CalledProcessError):
        return None
    files = []
    for record in filter(None, listing.split("\0")):
        meta, _, path = record.partition("\t")
        mode = meta.split()[0]
        target = root / path
        files.append((mode, path, target.stat().st_size if target.is_file() else 0))
    return files


def check_files(files: list[tuple[str, str, int]]) -> tuple[list[str], list[str]]:
    """Return (problems, warnings) for the tracked files."""
    problems, warnings = [], []
    problems += [
        f"{path} is a symlink; plugins must not contain symlinks" for mode, path, _ in files if mode == "120000"
    ]
    count, total = len(files), sum(size for _, _, size in files)
    if count > MAX_FILES:
        problems.append(f"{count} tracked files exceed the {MAX_FILES} files a claude.ai plugin may hold")
    elif count > WARN_FILES:
        warnings.append(f"{count} tracked files, close to the {MAX_FILES} file limit of claude.ai")
    if total > MAX_BYTES:
        problems.append(f"{total / 1024 / 1024:.0f} MB tracked exceed the {MAX_BYTES // 1024 // 1024} MB plugin limit")
    elif total > WARN_BYTES:
        warnings.append(f"{total / 1024 / 1024:.0f} MB tracked, close to the {MAX_BYTES // 1024 // 1024} MB limit")
    return problems, warnings


def main(root: Path = ROOT) -> int:
    plugin, problems = load(root / ".claude-plugin" / "plugin.json")
    marketplace, more = load(root / ".claude-plugin" / "marketplace.json")
    problems += more
    warnings: list[str] = []
    if plugin is not None:
        problems += check_plugin(plugin)
        if marketplace is not None:
            problems += check_marketplace(marketplace, plugin)
    problems += check_root(root) + check_skills(root)
    files = tracked_files(root)
    if files is None:
        warnings.append("not a git checkout: file count, size and symlink checks skipped")
    else:
        file_problems, file_warnings = check_files(files)
        problems += file_problems
        warnings += file_warnings
    for warning in warnings:
        print(f"warning: {warning}")
    for problem in problems:
        print(problem)
    print(f"plugin check: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
