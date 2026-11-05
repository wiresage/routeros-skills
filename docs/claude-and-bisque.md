# Claude Code reviews and Bisque video explainers

`.github/workflows/claude.yml` lets a maintainer ask `@claude` for help on an issue or pull request. When Claude is asked to
review or explain a pull request, it can also make a short narrated video of it. The video is published to this
repository's channel on Bisque Cloud, <https://bisque.today/p/wiresage/routeros-skills>, and the link is commented on the
pull request. The design follows [wiresage/mikrotik-mcp#197](https://github.com/wiresage/mikrotik-mcp/pull/197); the
background is in [issue #9](https://github.com/wiresage/routeros-skills/issues/9).

## How to use it

Write a comment that contains `@claude` on a pull request or issue, for example:

```text
@claude review this pull request
```

Only users with write access to the repository can trigger it. Claude replies as the Claude GitHub app. A reply about a
pull request ends with one line, `Video: yes` or `Video: no`, and the reason. For yes, a second job publishes the video and
comments the watch link a few minutes later.

The prompt asks for a video when the reasoning matters more than the diff: a new skill or script, a change to `tools/` or to
a workflow, a design decision. It asks for no video for a refresh that only regenerates files under `skills/*/references/`,
a dependency bump, formatting, a typo or a small fix.

## One-time setup (what only a maintainer can do)

A pull request cannot create secrets or install apps, so these steps come after the merge. Until the secret exists, an
`@claude` comment starts a run that fails at the Claude step and publishes nothing.

1. **Install the Claude GitHub app** on `wiresage/routeros-skills`: <https://github.com/apps/claude>, then choose the
   repository. If it is already installed for the organisation, check that this repository is included.
2. **Create a Claude Code OAuth token.** In a terminal where Claude Code is signed in with the subscription that should pay
   for the runs, run `claude setup-token` and copy the token it prints. Runs use that subscription's quota.
3. **Add it as a repository secret.** Repository, Settings, Secrets and variables, Actions, New repository secret. Name:
   `CLAUDE_CODE_OAUTH_TOKEN`. Or from a terminal with the GitHub CLI:

   ```bash
   gh secret set CLAUDE_CODE_OAUTH_TOKEN -R wiresage/routeros-skills
   ```

   The command asks for the value; paste the token there so it does not land in your shell history.
4. **Try it.** Comment `@claude review this pull request` on an open pull request and watch the *Claude Code* workflow in the
   Actions tab.
5. **Claim the channel (optional).** After the first video, sign in at <https://bisque.today> with GitHub as an admin of the
   repository. There you can claim the channel, choose another voice, or delete a video.

No Bisque account, key or token is needed: the `publish` job proves its identity to Bisque with the workflow's own GitHub
OIDC token.

## What runs, and what each part can do

| Part | Permissions | Can do | Cannot do |
| --- | --- | --- | --- |
| `claude` job | `contents`, `pull-requests` and `issues` write; `id-token` write; `actions` read | Read the repository, comment, push a branch when asked, write `.explainer/`, run four subcommands of `present.mjs` | Run `login` or `publish`, fetch from the web, edit the presenter script (it is outside the workspace) |
| `publish` job | `contents` read; `pull-requests` write; `id-token` write | Publish the artifact `explainer` as this repository and comment the link | Run a model, see the secret `CLAUDE_CODE_OAUTH_TOKEN`, change the repository |

Details that matter:

- The only folder that is published is `.explainer/`, written by Claude in the `claude` job. If a pull request commits its
  own `.explainer/`, the check `git ls-files .explainer` finds it and nothing is published.
- The `publish` job runs `bisque-cloud/presenter`, third-party code, with `id-token: write`. That is why it is pinned to a full
  commit and runs on its own runner without the secret.
- A video of a pull request in a public repository is public on bisque.today. The action's default `visibility` is public for a
  public repository and private for a private one.
- `publish` is `continue-on-error`, so a failed publish never turns the run red; look at the job log when no link appears.

## Pins and how to update them

Every `uses:` line is a full commit SHA with the version in a comment. Nothing floats.

| Pin | Where | Rule |
| --- | --- | --- |
| `bisque-cloud/presenter` | `PRESENTER_COMMIT` in the workflow `env`, and the `uses:` line of the `publish` step | The two must be the same commit: the plugin Claude writes with and the action that publishes must match. |
| `anthropics/claude-code-action` | the `uses:` line of the Claude step | Resolve the release tag to its commit with `gh api repos/anthropics/claude-code-action/git/ref/tags/<tag>` (an annotated tag needs one more call to `git/tags/<sha>`). |
| `actions/*` | the other `uses:` lines | The same SHAs as the other workflows where the action is shared. |

To update one, change it in a pull request, run `actionlint` on the workflow, and read the release notes of the action first.
Because GitHub runs comment-triggered workflows from `master`, the change is only exercised after it is merged.

## Turning it off

- **Only the videos:** delete the `publish` job and the steps from *Check out the presenter plugin* to *Keep the presentation
  out of commits*, and remove `plugin_marketplaces`, `plugins` and the `--allowedTools` argument. Plain `@claude` replies
  keep working.
- **Everything:** delete the workflow file, or disable *Claude Code* in the Actions tab.
