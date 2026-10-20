# Claude plugin

The repository is a Claude plugin and a one-plugin marketplace, so the skills can be installed and updated with Claude's
plugin commands instead of copying folders. It sits next to the other ways in (`npx skills add`, the install scripts, see the
[README](../README.md#install)) and does not replace them: all of them read the same `skills/` folder.

| File | Purpose |
| --- | --- |
| `.claude-plugin/plugin.json` | The plugin `routeros-skills`: name, version, description, author. No components are declared; the default `skills/` folder is loaded. |
| `.claude-plugin/marketplace.json` | The marketplace `wiresage` with one entry, `routeros-skills`, whose `source` is `./` (the repository root is the plugin). Other wiresage projects can join the same catalog later. |
| `tools/check_plugin.py` | Offline check of both files, the version rule, stray components at the root, the file and size limits and symlinks. |

## Install

In a terminal:

```bash
claude plugin marketplace add wiresage/routeros-skills
claude plugin install routeros-skills@wiresage
```

Or inside a Claude Code session: `/plugin marketplace add wiresage/routeros-skills`, then `/plugin install routeros-skills@wiresage`.
The skills appear namespaced by the plugin, for example `/routeros-skills:routeros-firewall`, and Claude also loads one on its own
when the task matches its description. `claude plugin details routeros-skills` lists the 34 skills.

To install for one project only, add `--scope project` to both commands (it writes `.claude/settings.json` in that project).

Claude desktop, claude.ai chat and Cowork: Anthropic's documentation says you add a GitHub repository as a marketplace under
**Customize > Plugins**, or use **Add > Upload plugin** with a zip of the repository. Those routes are **not tested here**.
Chat, Cowork and Claude Code all load skills. This plugin has nothing else (no hooks, agents, MCP servers or `bin/`).

## What it costs

Measured with `claude plugin details routeros-skills` on version 0.1.0:

- **About 5,700 tokens added to every session**, the names and descriptions of all 34 skills (140 to 210 each).
- **About 1,200 to 2,500 tokens each time a skill is used**, the `SKILL.md` that loads. Reference files cost more only when the
  agent opens them.

If that is too much for everyday sessions, install the plugin at project scope only where you work on MikroTik gear, or install
selected skills with `npx skills add wiresage/routeros-skills -s routeros-firewall routeros-vpn`.

## Updates and versions

`plugin.json` sets `version`. **A user keeps the copy they have until that version changes**, so a merge that should reach installed
users needs a version bump in the same pull request. The version is set only in `plugin.json` (the manifest wins over the
marketplace entry, so a second copy could only drift; `tools/check_plugin.py` rejects one).

Use plain `MAJOR.MINOR.PATCH`:

- patch: fixes to skill text, references refreshed from the manual, small script fixes;
- minor: a new skill or helper script, a changed skill name or behaviour users can notice;
- major: a skill removed or renamed so that existing prompts break.

To release, after the pull request with the bump is merged, from an up-to-date `master`:

```bash
claude plugin tag --dry-run          # shows routeros-skills--v0.1.0 and checks plugin.json against the marketplace entry
claude plugin tag --push             # creates and pushes the tag
```

Installed users update with `claude plugin marketplace update wiresage` and `claude plugin update routeros-skills@wiresage`
(a restart applies it). Without a bump, only people who install fresh get the new files.

## Test a change locally

- `claude plugin validate --strict .` (marketplace and plugin manifest), `claude plugin validate --strict skills` (the skills) and
  `python tools/check_plugin.py`. CI runs all of them.
- **Do not install from your working copy to measure size.** A marketplace added from a local path copies the whole working
  directory, including ignored files such as `.cache/`. A copy installed this way held 6,812 files and 119 MB, while the install
  from GitHub holds the 1,959 tracked files (17 MB). Add the pushed branch instead:
  `claude plugin marketplace add "https://github.com/wiresage/routeros-skills.git#<branch>"`.
- Use a separate config folder so tests do not touch your own setup: set `CLAUDE_CONFIG_DIR` to a short path (a long path breaks
  `git clone` on Windows).

## Limits and rules for the repository root

The root of the repository is the plugin root, so everything tracked in git is shipped and anything that matches a plugin
component location is loaded. `tools/check_plugin.py` therefore fails if the root gains `commands/`, `agents/`, `hooks/`, `bin/`,
`output-styles/`, `themes/`, `workflows/`, `monitors/`, `.mcp.json`, `.lsp.json`, `settings.json` or `CLAUDE.md`. claude.ai and
Cowork refuse a plugin with a top-level `bin/`, and allow 5,000 files and 200 MB per plugin (this one has 1,959 files and 17 MB).

## MikroTik's documentation

`references/` is MikroTik's documentation (see [NOTICE.md](../NOTICE.md)). This marketplace has the same exposure as the public
repository. `plugin.json` therefore has no `license` field: the MIT license covers the instructions, scripts and tools, not the
references. Submitting the plugin to Anthropic's public directory is a bigger step and needs a decision about those references
first (ask MikroTik, hold, or ship without `references/`).
