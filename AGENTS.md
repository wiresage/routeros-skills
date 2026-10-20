# AGENTS.md

Instructions for AI agents (and people) who work **on this repository**. To *use* the skills, read [README.md](README.md).

## What this repository is

A collection of agent skills for MikroTik RouterOS. Each skill is a folder under `skills/` with a `SKILL.md` and a
`references/` folder. The references are generated from the official documentation; the `SKILL.md` files are written by
hand. Everything must stay agent-agnostic: Claude Code, Codex, Copilot and other agents read the same files.

## Layout

```text
skills/<name>/SKILL.md          hand-written instructions (front matter: name, description)
skills/<name>/scripts/          optional helpers, only when they add value
skills/<name>/references/       generated documentation; INDEX.md lists it
scripts/                        installers for users (shell and PowerShell)
tools/                          maintenance tools: validators, crawlers, the reference builder
docs-snapshot.json              generated: what the references were built from
.github/workflows/ci.yml        validation, lint and the post-merge health check
```

## Commands

| Task | Command |
| --- | --- |
| Validate every skill | `python tools/validate_skills.py` |
| Check relative links | `python tools/check_links.py` |
| Check root files, README table, style | `python tools/check_repo.py` |
| Check that property names in `SKILL.md` exist in the references | `python tools/check_properties.py` |
| Check `skills.sh.json` (groups on the skills.sh page) against the skills and the README | `python tools/check_skills_sh.py` |
| Check the Claude plugin manifests, the version rule, root components and file limits | `python tools/check_plugin.py` and `claude plugin validate --strict .` |
| See whether skills.sh lists every skill | `python tools/skills_sh_status.py` |
| Lint and format Python | `ruff check . && ruff format --check .` |
| Lint shell scripts | `shellcheck $(git ls-files '*.sh')` |
| Lint PowerShell | `Invoke-ScriptAnalyzer -Path . -Recurse -Severity Warning,Error` |
| Refresh the documentation | `pip install -r tools/requirements.txt`, then `python tools/crawl_manual.py crawl`, `python tools/crawl_help.py crawl`, `python tools/build_references.py`, `python tools/verify_references.py` |

Run the validators, the links check and the repository check before every commit. CI runs the same commands.

## Git workflow

- **Never push to `master`.** Every change goes through a pull request: create a branch from an up-to-date `master`
  (`feat/<topic>`, `fix/<topic>`, `docs/<topic>`), push the branch, open a PR against `master`, and wait for CI to pass.
  A maintainer merges; do not merge your own PR unless the maintainer asked you to. Do not rewrite pushed history on `master`.
- One commit per step of work, using [Conventional Commits](https://www.conventionalcommits.org): `feat(skills): add
  routeros-firewall`, `fix(tools): ...`, `docs: ...`, `ci: ...`, `chore: ...`. Scopes in use: `skills`, `tools`, `scripts`, `ci`.
- A commit that adds or changes a skill also updates the README skills table so that `check_repo.py` stays green.
- The PR description says what changed, why, and how it was checked (commands run, scripts tested against a stub or a
  lab router).

## Rules for skills

1. **Front matter** has `name` and `description` and nothing agent-specific (no `allowed-tools`, `model`, hooks and so on).
   `name` equals the folder name, starts with `routeros-`, uses lowercase letters, digits and single hyphens.
   `description` is one line, at most 1024 characters, says what the skill covers and ends with when to use it
   (`Use when ...`). It must not contain angle brackets. The validator enforces this.
2. **Size.** Keep `SKILL.md` under 500 lines. Put detail in `references/` and tell the agent when to open it.
3. **Reachability.** Everything an agent needs must be reachable from `SKILL.md` through relative links or paths. Do not
   link to other skills by path; name them (`routeros-firewall`) because a user may have installed only some skills.
4. **Truth.** State only what the references support or what you ran against a router. When you cite behaviour, name the
   reference file. Do not paper over gaps with memory: if the documentation is silent, say so in the skill.
5. **RouterOS 7 syntax.** Examples use full slash paths (`/ip/firewall/filter/add ...`), named items or `find` instead of
   item numbers, and documentation addresses (`192.0.2.0/24`, `2001:db8::/32`) or obvious placeholders.
6. **Safe by default.** Show read-only commands first. Mark destructive or lock-out-prone commands and say that they need
   the user's confirmation. Never put real credentials, keys or serial numbers in examples.
7. **Prose style.** Plain, direct sentences. No em dashes (use commas, colons or parentheses). `check_repo.py` enforces it
   for `SKILL.md` and the root documents.

## Rules for scripts

- Only `.sh`, `.ps1` and `.py` files. Mention each script in the `SKILL.md` that ships it, with an example call.
- Python: 3.10 or newer, standard library only, `#!/usr/bin/env python3`, passes `ruff`.
- Shell: bash, `#!/usr/bin/env bash`, `set -euo pipefail`, passes `shellcheck`, committed executable.
- PowerShell: runs on Windows PowerShell 5.1 and PowerShell 7, passes PSScriptAnalyzer.
- Read secrets from environment variables, never from arguments (arguments show up in process lists and shell history).
  Default to read-only operations. Verify TLS certificates unless the user passes an explicit flag.

## skills.sh

skills.sh lists a public repository after someone installs it with `npx skills add`; there is no publish step and no
token. `skills.sh.json` groups the skills on the repository page and must stay equal to the README topic groups (add a new
skill to both; `tools/check_skills_sh.py` fails otherwise). `.github/workflows/skills-sh.yml` checks that the real CLI
installs every skill and, after a merge that changes a `SKILL.md`, runs the install that lists or refreshes the repository.
Read [docs/skills-sh.md](docs/skills-sh.md) before changing either.

## Claude plugin

The repository root is a Claude plugin (`.claude-plugin/plugin.json`) and the marketplace `wiresage` (`marketplace.json`, source
`./`). Everything tracked in git is shipped, and a file or folder at the root that matches a plugin component location is
loaded, so never add `commands/`, `agents/`, `hooks/`, `bin/`, `.mcp.json`, `settings.json` or `CLAUDE.md` at the root
(`tools/check_plugin.py` fails if you do). Set the version only in `plugin.json` and bump it when a change should reach
installed users; keep SKILL.md free of plugin-only variables such as `${CLAUDE_PLUGIN_ROOT}`, so the skills stay portable.
Read [docs/claude-plugin.md](docs/claude-plugin.md) first.

## Generated files

`skills/*/references/` (everything except hand-written notes that sit directly in `references/`) and `docs-snapshot.json`
are generated. Never edit them by hand: change `tools/` (or `tools/scopes.json`, which assigns pages to skills) and
rebuild. `python tools/verify_references.py` compares every generated file with its crawled source.

## Adding a skill

1. Decide the scope. One skill covers one area an agent would reason about as a unit; do not duplicate another skill.
2. Add the skill to `tools/scopes.json` (manual page prefixes, CLI menu prefixes, help-only pages), rebuild and verify.
3. Read the guides that matter, then write `SKILL.md`: when to use it, the workflow, recipes with commands, pitfalls,
   a table of which reference to open for which need.
4. Add scripts only if they remove real friction, and test them.
5. Add the README table row, run all checks, commit with `feat(skills): add <name>`.

## Companion projects

The skills are designed to be combined with [routeros-lsp](https://github.com/wiresage/routeros-lsp) (checks `.rsc`
scripts) and [mikrotik-mcp](https://github.com/wiresage/mikrotik-mcp) (talks to devices). Skills must still be useful when
neither is present.
