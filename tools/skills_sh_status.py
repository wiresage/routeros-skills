#!/usr/bin/env python3
"""Report whether the skills of this repository are listed on https://skills.sh.

skills.sh has no publish API: a repository appears after someone installs it with the ``skills`` CLI (the CLI reports
the install anonymously), so this tool only reads the public repository page and checks that every skill of this
repository is named on it. No account, token or API key is needed.

    python tools/skills_sh_status.py                      # repository from GITHUB_REPOSITORY or the git origin
    python tools/skills_sh_status.py --repo owner/repo --timeout 600 --interval 30
    python tools/skills_sh_status.py --skill pdf --skill docx --repo anthropics/skills

Exit status: 0 every skill is listed, 2 the page could not be read, 3 the repository is not listed, 4 the repository is
listed but some skills are missing, 1 bad usage.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = "https://www.skills.sh/{repo}"
USER_AGENT = "routeros-skills-status-check (+https://github.com/wiresage/routeros-skills)"
REPO_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def detect_repo() -> str | None:
    """The repository from GITHUB_REPOSITORY (GitHub Actions) or from the git origin remote."""
    from_env = os.environ.get("GITHUB_REPOSITORY")
    if from_env:
        return from_env
    try:
        url = subprocess.run(
            ["git", "-C", str(ROOT), "remote", "get-url", "origin"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    match = re.search(r"github\.com[:/]([^/]+/[^/]+?)(?:\.git)?$", url)
    return match.group(1) if match else None


def local_skills(root: Path = ROOT) -> list[str]:
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(p.name for p in skills_dir.iterdir() if (p / "SKILL.md").is_file())


def fetch_page(repo: str, timeout: float = 30.0) -> tuple[int, str]:
    """Return (HTTP status, body) of the repository page; a 404 is a normal answer, other failures raise OSError."""
    request = urllib.request.Request(PAGE.format(repo=repo), headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return 404, ""
        raise OSError(f"HTTP {exc.code} from {request.full_url}") from exc
    except urllib.error.URLError as exc:
        raise OSError(f"could not reach {request.full_url}: {exc.reason}") from exc


def missing_skills(html: str, skills: list[str]) -> list[str]:
    """Skills whose names do not appear on the page (whole-name match, so ``a`` does not match ``a-b``)."""
    return [s for s in skills if not re.search(rf"(?<![\w-]){re.escape(s)}(?![\w-])", html)]


def evaluate(status: int, html: str, skills: list[str]) -> tuple[int, str]:
    """Map a page answer to an exit status and a one-line message."""
    if status == 404:
        return 3, "the repository is not listed on skills.sh yet"
    missing = missing_skills(html, skills)
    if missing:
        return 4, f"listed, but {len(missing)} of {len(skills)} skills are missing: {', '.join(missing)}"
    return 0, f"listed, all {len(skills)} skills are on the page"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", help="owner/repo on GitHub (default: GITHUB_REPOSITORY or the git origin)")
    parser.add_argument("--skill", action="append", default=[], help="skill name to look for (default: skills/*)")
    parser.add_argument("--timeout", type=float, default=0, help="keep checking for this many seconds (default: once)")
    parser.add_argument("--interval", type=float, default=30, help="seconds between checks (default: 30)")
    args = parser.parse_args()

    repo = args.repo or detect_repo()
    if not repo or not REPO_PATTERN.match(repo):
        print("error: give --repo owner/repo", file=sys.stderr)
        return 1
    skills = args.skill or local_skills()
    if not skills:
        print("error: no skills to look for (run from the repository root or pass --skill)", file=sys.stderr)
        return 1

    deadline = time.monotonic() + args.timeout
    while True:
        try:
            code, message = evaluate(*fetch_page(repo), skills)
        except OSError as exc:
            code, message = 2, str(exc)
        print(f"{repo}: {message}")
        if code == 0 or code == 1 or time.monotonic() + args.interval > deadline:
            break
        time.sleep(args.interval)
    return code


if __name__ == "__main__":
    sys.exit(main())
