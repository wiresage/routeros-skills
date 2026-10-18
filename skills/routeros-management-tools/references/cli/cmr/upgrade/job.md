# /cmr/upgrade/job

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/upgrade/job

Package: cmr; Type: Directory

One upgrade job is one upgrade run. Jobs are created from upgrade rules, and their parameters are copied from the rule at creation and are read-only. A scheduled job resolves its device list only when it starts, so `show-devices` for a scheduled job can be empty. Remove a queued or processing job to cancel it. The job state becomes `cancelled`.

**Flags**

- `X` (disabled): Job is disabled.
- `R` (rule): Job created from an upgrade rule.

**Read-only arguments**

- `labels` (object; unset): Devices the job covers, selected by labels. Empty for a job that `/cmr/device/upgrade` started for devices selected by number.
- `order` (object): Execution order of the label groups, used with `continue-order`.
- `channel` (alt): Upgrade channel or the pinned version the job installs. Empty when each device upgrades on its own upgrade channel.
- `strategy` (enum; unset): How the job upgrades devices: `parallel` all at the same time, `sequential` one after another. With `continue-order` the devices are processed per label group in the order given by `order`.
- `fail-policy` (enum; unset): Behaviour of the job if a device fails: `continue`, `stop`, or `continue-order`. `stop` halts the whole job on the first failure; `continue-order` continues with the next label group in `order`.
- `schedule-time` (date; unset): When the job is scheduled to run, in the same format as the rule's `schedule-time`.
- `starts-in` (time; unset): Time remaining until the job starts. Shown for scheduled jobs.
- `start-time` (date; unset): When the job started running.
- `end-time` (date; unset): When the job finished.
- `state` (enum (scheduled | queued | waiting devices | queued (busy) | version check | processing | done | cancelled)): Current job state: `scheduled` (waiting to run), `queued` (created while another job runs, starts when it finishes), `waiting devices`, `version check` (looking up the available version), `processing` (upgrading), `done` (finished), or `cancelled` (removed).
- `success` (composite { success: num , total: num }; unset): Upgraded/total, for example `3/10`. A `0/total` occurs when the devices are already on the target version or a covered device is unreachable when the job starts.
- `run-time` (time; unset): How long the job took to run.
- `packages` (multi { package: string }; unset): Packages the job upgrades.

## Commands

### /cmr/upgrade/job/run-next

Package: cmr; Type: Command

Runs the next scheduled upgrade job right away. For a job of an upgrade rule, the job starts as a new run, and the originally scheduled job remains scheduled. A job scheduled with `/cmr/device/upgrade` has no schedule to keep, so that job itself starts. Only one upgrade job runs at a time, so a job started while another job is already in progress is queued, not interrupted.

### /cmr/upgrade/job/show-devices

Package: cmr; Type: Command

Shows the devices the selected job covers. A scheduled job resolves its device list only when the job starts, so the output for a job that has not started yet can be empty.

**Flags**

- `L` (controller): Include the CMR server itself (self-client).
