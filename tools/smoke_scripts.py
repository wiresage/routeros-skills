#!/usr/bin/env python3
"""Smoke-test every script shipped in this repository: each must start and print its help.

Checks the installers in ``scripts/`` and the helpers in ``skills/*/scripts/``. A Python or shell script must exit
with 0 when called with ``--help``; a PowerShell script must have help that PowerShell can read (skipped without
``pwsh``).

    python tools/smoke_scripts.py
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TIMEOUT = 60
GIT_BASH = Path(os.environ.get("PROGRAMFILES", r"C:\Program Files")) / "Git" / "bin" / "bash.exe"


def scripts() -> list[Path]:
    found = [*sorted((REPO_ROOT / "scripts").glob("*")), *sorted((REPO_ROOT / "skills").glob("*/scripts/*"))]
    return [p for p in found if p.suffix in {".py", ".sh", ".ps1"}]


def find_bash() -> str | None:
    """On Windows prefer Git Bash: a bare ``bash`` may be the WSL launcher, which cannot see drive paths."""
    if sys.platform == "win32" and GIT_BASH.is_file():
        return str(GIT_BASH)
    return shutil.which("bash")


def command_for(script: Path) -> list[str] | None:
    if script.suffix == ".py":
        return [sys.executable, str(script), "--help"]
    if script.suffix == ".sh":
        bash = find_bash()
        return [bash, script.as_posix(), "--help"] if bash else None
    pwsh = shutil.which("pwsh")
    if pwsh is None:
        return None
    escaped = str(script).replace("'", "''")
    return [pwsh, "-NoProfile", "-NonInteractive", "-Command", f"if (-not (Get-Help -Full '{escaped}')) {{ exit 1 }}"]


def main() -> int:
    failures = 0
    checked = 0
    for script in scripts():
        command = command_for(script)
        relative = script.relative_to(REPO_ROOT).as_posix()
        if command is None:
            print(f"skip: {relative} (interpreter not installed)")
            continue
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=TIMEOUT, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            print(f"error: {relative}: {exc}")
            failures += 1
            continue
        checked += 1
        if result.returncode != 0:
            print(f"error: {relative} exited with {result.returncode}: {result.stderr.strip()[:200]}")
            failures += 1
    print(f"smoke-tested {checked} script(s): {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
