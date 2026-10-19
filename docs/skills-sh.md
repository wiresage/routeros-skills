# Publishing to skills.sh

[skills.sh](https://skills.sh) is the agent skills directory run by Vercel Labs. This page explains how a repository gets
listed there, what this repository does about it, and what you have to do by hand. The short version: **no API key, token or
Vercel project is needed**, because skills.sh has no publish API.

## How listing works

Facts taken from the [skills.sh docs](https://www.skills.sh/docs), the [FAQ](https://www.skills.sh/docs/faq),
[Customize](https://www.skills.sh/docs/customize), the [API reference](https://www.skills.sh/docs/api) and the source of the
[skills CLI](https://github.com/vercel-labs/skills) (version 1.7.2 when this was written):

- A repository is listed when someone runs `npx skills add owner/repo`. The CLI sends an anonymous install event to
  skills.sh (skill names, file paths, agents, a timestamp) **only for public GitHub repositories**, and the leaderboard is
  ranked by those events. skills.sh documents no crawling of GitHub, and a community answer based on the CLI source says GitHub topics do not trigger discovery.
- There is no submission form, no publish command in the CLI, and no write endpoint in the skills.sh API (the API is
  read-only). Packs (unlisted bundles) can be created only in the web UI after signing in with Vercel.
- Skills are discovered by the CLI in `skills/<name>/SKILL.md`, which needs `name` and `description` in its front matter. All 34
  skills of this repository are found.
- `skills.sh.json` at the repository root controls only how the repository page groups the skills. skills.sh reads it in the
  background after an install with telemetry on, so a change shows up after the next install and a cache refresh.
- Removing a skill from the repository does not remove it from the skills.sh index. Ask in an issue at
  [vercel-labs/skills](https://github.com/vercel-labs/skills/issues) if a stale entry must go.
- Audits of listed skills are produced automatically by Vercel's partners after the first install; see
  [skills.sh/audits](https://skills.sh/audits).

## What this repository ships

| File | Purpose |
| --- | --- |
| `skills.sh.json` | Seven topic groups, the same as the README skills tables |
| `tools/check_skills_sh.py` | Offline check: valid against the published schema, every skill in exactly one group, groups equal to the README |
| `tools/skills_sh_status.py` | Reads the public page `https://www.skills.sh/wiresage/routeros-skills` and reports whether every skill is on it |
| `.github/workflows/skills-sh.yml` | `compatibility` on pull requests and pushes, `publish` after a merge that changes a `SKILL.md` or `skills.sh.json` |

The `compatibility` job installs the repository with the real CLI (version pinned in the workflow, telemetry **off**) and fails
if the CLI finds a different number of skills than there are folders, or if an installed copy differs from the source. The
`publish` job installs `wiresage/routeros-skills` from GitHub with telemetry **on**, then polls the public page for up to ten
minutes and writes the result to the job summary. It never runs for forks or pull requests, uses no secrets, and only has
`contents: read`.

What was observed: on 2026-10-18 one install from a local shell (telemetry on, scratch folder, the command in step 3 below) made
<https://www.skills.sh/wiresage/routeros-skills> show all 34 skills within a minute. The page then reported 0 installs and the
badge still answered "resource not found", so counts and badge lag behind the listing. Whether an install reported from CI does
the same is what the first `publish` run after a merge shows.

Two honest limits:

- The CLI marks installs from CI (`ci=1`). skills.sh does not document whether such an install lists a new repository or
  refreshes its page, and a community answer in the Vercel forum suggests it may not. The `publish` job therefore reports what the
  page shows instead of assuming success, and it only warns by default.
- Every `publish` run is one more install event for this repository. That is why it runs only when a `SKILL.md` or
  `skills.sh.json` changes (or when you start it), not on every merge. The workflow does not hide that it runs in CI.

## Tokens and keys: what you need

Nothing. Check against the list of things people usually expect:

| You may think you need | Reality |
| --- | --- |
| A skills.sh or Vercel API key or token to publish | There is no publish API. Not needed. |
| A Vercel account or project to host anything | Not needed. skills.sh reads the public GitHub repository. |
| A personal access token for GitHub Actions | Not needed. The built-in `GITHUB_TOKEN` is enough, and the repository is public. |
| A Vercel OIDC token | Only for reading the skills.sh REST API (`/api/v1/...`) from an app deployed on Vercel. Publishing does not use it. |
| A Vercel sign-in | Only to create a pack in the browser at <https://skills.sh/packs/create>. Packs are optional and cannot be created from CI. |

## Step by step after the pull request is merged

1. **Merge the pull request.** The merge changes `skills.sh.json` and a workflow file, so the `skills.sh` workflow runs on
   `master` (Actions tab, workflow *skills.sh*). The `compatibility` job must be green; then `publish` installs the repository
   with telemetry on and checks the page.
2. **Read the job summary** of the `publish` job. If it says the skills are listed, you are done (go to step 5).
3. **If the page does not list the skills**, run the install once from your own shell, where telemetry is not flagged as CI. Use a
   scratch folder so no skills land in a real project. You need Node 22.20 or newer (`node --version`; the CLI prints a
   warning on older versions).

   ```bash
   cd "$(mktemp -d)"
   npx skills add wiresage/routeros-skills -a claude-code -s '*' --copy -y
   ```

   ```powershell
   $dir = Join-Path $env:TEMP "skills-sh-check"; New-Item -ItemType Directory -Force $dir | Out-Null; Set-Location $dir
   npx skills add wiresage/routeros-skills -a claude-code -s '*' --copy -y
   ```

   Do not set `DISABLE_TELEMETRY` or `DO_NOT_TRACK`, or nothing is reported. This is one ordinary install, the same as any user's.
4. **Check the page.** Allow some minutes, then:

   ```bash
   python tools/skills_sh_status.py --timeout 600 --interval 30
   ```

   Exit status 0 means every skill is on <https://www.skills.sh/wiresage/routeros-skills>; 3 means the repository is not listed yet;
   4 means it is listed but some skills are missing (the grouping and listing can lag behind; run the install again later).
5. **The README badge** links to the page and shows the number of skills it lists:

   ```markdown
   [![skills.sh](https://skills.sh/b/wiresage/routeros-skills)](https://skills.sh/wiresage/routeros-skills)
   ```

6. **Later changes** follow the normal pull request flow. When a merge changes a `SKILL.md` or `skills.sh.json`, `publish` runs
   again. To run it by hand: Actions, *skills.sh*, *Run workflow* (options: install or only verify, fail if not listed, minutes to wait),
   or `gh workflow run skills-sh.yml -f publish=true -f require_listing=true`.

## When you add or rename a skill

Add the skill to its group in **both** the README table and `skills.sh.json` (same group, same order). `python tools/check_skills_sh.py`
and CI fail if they differ. Skill names are the slugs skills.sh shows, so renaming a skill creates a new entry and leaves the old
one in the index.

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `404` from the status tool | Nobody has installed it with telemetry on yet. Do step 3. |
| Listed, but the groups are not shown | skills.sh reads `skills.sh.json` on the next install with telemetry and caches repo pages. Install again and wait. |
| Listed, but a new skill is missing | The page updates on installs; install again from your shell. Check `npx skills add wiresage/routeros-skills --list` shows it. |
| Old skill still listed | The index keeps removed skills. Open an issue at vercel-labs/skills with the repository and skill names. |
| `compatibility` fails with "CLI found N, repository has M" | A folder has no valid `SKILL.md` (needs `name` and `description`), or a `SKILL.md` has YAML the CLI cannot read. Run `npx skills add . --list` locally. |
| `compatibility` fails with "Installed copy differs" | The CLI skipped or changed a file. On Windows, very long paths can be skipped; the CI runner is Linux. |
| Node warning `EBADENGINE` | The CLI wants Node 22.20 or newer. |

## Changing the CLI version

The workflow pins `skills@1.7.2`. To move to a newer release, read its changelog (discovery rules, telemetry, new commands),
change `SKILLS_CLI` in `.github/workflows/skills-sh.yml` in a pull request, and let the `compatibility` job prove it still finds all
skills.
