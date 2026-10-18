# /cmr/upgrade

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/upgrade

Package: cmr; Type: Directory

An upgrade rule describes when and to which channel to upgrade selected devices (by labels).

**Flags**

- `X` (disabled): Rule is disabled.
- `D` (dynamic): Rule is dynamic.

**Arguments**

- `name` (string; unset): Name of the upgrade rule.
- `labels` (object; unset): Select the devices the rule covers using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used. If omitted, the rule covers all connected devices. Default: `all`.
- `order` (object): Execution order (by labels). Required when `fail-policy=continue-order`.
- `channel` (alt; mandatory): Upgrade channel: `long-term`, `stable`, `testing`, or `development`. Alternatively, pin a specific version by giving the version directly as the value, for example `channel=7.24.4`.
- `schedule-time` (multi { array-id, array-id, time: super { time: date , [day] [ @enum (sun | mon | tue | wed | thu | fri | sat)] } }; unset): When upgrades start: a time with an optional weekday given after `@`. For example `14:00:00` starts every day at 14:00 and `00:00:00@sat` starts every Saturday at midnight. Multiple entries are comma-separated, for example `00:00:00@sat,00:00:00@sun`.
- `strategy` (enum; unset): How devices are upgraded: `parallel` upgrades all covered devices at the same time; `sequential` upgrades them one after another and waits for each to finish. With `continue-order` the devices are processed per label group in the order given by `order`: in `parallel` the devices of each group are upgraded together, in `sequential` one at a time. Default: `parallel`.
- `fail-policy` (enum; unset): Behaviour if a device fails: `continue` skips the failed device and continues with the rest; `stop` stops the whole upgrade on the first failure and does not continue with the remaining devices or with the next label group; `continue-order` skips the failed device and continues with the next label group, processing the labels one group after another in the order given by `order`. With `sequential` the rest of the failed device's group is skipped; with `parallel` only the failed device is abandoned and devices already in progress in the group finish. Default: `stop`.

## Commands

### /cmr/upgrade/show-devices

Package: cmr; Type: Command

Lists the devices the selected upgrade rule covers. A device is claimed by the first rule in the list that covers it, so a rule can list no devices when an earlier rule covers them all.

**Flags**

- `p` (remote-pending): Controller requests pairing.
- `I` (inactive): Device is inactive.
- `S` (stale): No connection (stale).
- `L` (controller): The CMR server itself (self-client).
- `C` (connected): Device is connected.
- `U` (upgrade-available): A newer update is available.

**Arguments**

- `only-upgradable` (bool): Show only the devices that can actually be upgraded.

### /cmr/upgrade/trigger

Package: cmr; Type: Command

Starts the job of a chosen rule right away, without waiting for the schedule-time. Only one upgrade job runs at a time; triggering another rule while a job is in progress places the new job in a [queued state](upgrade/job.md#cmr-upgrade-job) until the current job finishes.

Triggering forces an early upgrade of the rule's covered devices: the job runs immediately and upgrades each covered device that has a newer version available, without waiting for the schedule-time. Covered devices that are already up to date are skipped, so the run's counter counts only the upgraded ones. To upgrade a single device regardless of its rule, see [`/cmr/device/upgrade`](device.md).

### /cmr/upgrade/version-check

Package: cmr; Type: Command

Lists the newest version available for each upgrade channel that is configured in an upgrade rule. Channels that no rule uses are not checked.

**Read-only arguments**

- `channel` (alt): Channel checked.
- `version` (string): Available versions.
