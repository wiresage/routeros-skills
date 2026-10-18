# Contributing

Thanks for helping. The goal of this project is that an AI agent gets RouterOS right: the right command, the right
property, no lock-out. Every change should move toward that.

[AGENTS.md](AGENTS.md) holds the full rules; this page is the short version for people.

## Set up

You need Python 3.10 or newer and [ruff](https://docs.astral.sh/ruff/). Shellcheck and PowerShell with PSScriptAnalyzer are
optional locally because CI runs them.

```bash
git clone https://github.com/wiresage/routeros-skills.git
cd routeros-skills
pip install ruff
python tools/validate_skills.py && python tools/check_links.py && python tools/check_repo.py
ruff check . && ruff format --check .
```

Refreshing the documentation needs three more packages (`pip install -r tools/requirements.txt`).

## What to change where

| You want to | Change |
| --- | --- |
| Fix or improve the instructions of a skill | `skills/<name>/SKILL.md` |
| Fix a wrong or missing page in a `references/` folder | Not the file itself: the file is generated. Fix `tools/` or report the error to MikroTik if the source is wrong |
| Move a documentation page to another skill | `tools/scopes.json`, then rebuild |
| Add a helper script | `skills/<name>/scripts/`, and mention it in that skill's `SKILL.md` |
| Add a skill to the skills.sh page | `skills.sh.json` and the README table, in the same group (see [docs/skills-sh.md](docs/skills-sh.md)) |
| Add a skill | See "Adding a skill" in [AGENTS.md](AGENTS.md) |
| Refresh the documentation snapshot | `crawl_manual.py`, `crawl_help.py`, `build_references.py`, `verify_references.py` in `tools/` |

## Quality bar

- **Evidence.** A claim in a `SKILL.md` must be backed by the references or by a command you ran on a router. Say which.
  If RouterOS and the documentation disagree, add a note to the skill; the router decides what works.
- **Safety.** Examples are read-only unless the point is to change something. Lock-out and data-loss risks are stated next
  to the command that causes them.
- **Brevity.** An agent pays for every line it loads. Put the common path in `SKILL.md`, the rare one in `references/`.
- **Portability.** No agent-specific front matter or tool names. A skill must read the same in Claude Code, Codex and
  Copilot.
- **Tests for scripts.** Run them against a stub or a lab router and say how in the commit message.

## Commits

One logical step per commit, in [Conventional Commits](https://www.conventionalcommits.org) form. Examples:

```text
feat(skills): add routeros-wireguard
fix(skills): correct the input chain order in routeros-firewall
feat(tools): keep tables inside table cells when converting help pages
docs: explain how to install the skills for Copilot
```

## Pull requests

Nobody pushes to `master`, maintainers included. Work on a branch (or a fork), open a pull request against `master`,
describe what changed, why, and how you checked it, and let CI pass. A maintainer merges it. Keep one logical change per
pull request, with one commit per step.

## CI

[.github/workflows/ci.yml](.github/workflows/ci.yml) runs on every pull request and on every push to `master` (a merge is
a push): skill validation, link and repository checks, ruff, shellcheck and PSScriptAnalyzer. A failing run on `master`
is the health check telling you something broke; fix it before anything else.

## Reporting problems

Wrong or dangerous advice in a skill is a bug; open an issue with the skill name, the line and what a router actually does.
Security problems go through [SECURITY.md](SECURITY.md).
