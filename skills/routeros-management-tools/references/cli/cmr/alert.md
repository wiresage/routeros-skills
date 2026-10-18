# /cmr/alert

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/alert

Package: cmr; Type: Directory

An alert rule defines conditions and runs its actions on the CMR controller. Device rules select devices with `labels`. State alerts remain active while all configured state conditions match and run actions once when they become active. They fire again only after their conditions stop matching and then match again. Event alerts run actions for each matching occurrence and never remain active or contribute to active-alert counters. A rule can contain multiple state conditions but at most one event condition. Most alerts apply per device; `upgrade-job-done` is a system event for a whole upgrade job. See [CMR - Alert rules](../../guides/management-tools/cmr.md#alert-rules) for conditions, actions, and alert scope.

**Flags**

- `X` (disabled): Alert rule is disabled.

**Arguments**

- `name` (string; unset): Name of the alert rule.
- `labels` (object; unset): Select the devices, by labels, that the alert rule applies to. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.

  When `labels` is not set, the rule applies to all connected devices (`labels=all`).
- `connected` (bool; unset): State condition that matches whether the device is connected (`yes`) or disconnected (`no`).

  Default: no.
- `cpu-above` (num; unset): Alert when CPU load is above the given percent value (0..100); a value equal to the threshold also fires the rule.

  Default: unset.
- `cpu-below` (num; unset): Alert when CPU load is below the given percent value (0..100); it fires only for values strictly below the threshold.

  Default: unset.
- `hdd-above` (num; unset): Alert when disk (HDD) load is above the given percent value (0..100); a value equal to the threshold also fires the rule.

  Default: unset.
- `hdd-below` (num; unset): Alert when disk (HDD) load is below the given percent value (0..100); it fires only for values strictly below the threshold.

  Default: unset.
- `mem-above` (num; unset): Alert when RAM load is above the given percent value (0..100); a value equal to the threshold also fires the rule.

  Default: unset.
- `mem-below` (num; unset): Alert when RAM load is below the given percent value (0..100); it fires only for values strictly below the threshold.

  Default: unset.
- `health-above` (num; unset): Alert when the health sensor named by `health-value` goes above the given value; a value equal to the threshold also fires the rule. Devices that do not report the sensor are ignored.

  Default: unset.
- `health-below` (num; unset): Alert when the health sensor named by `health-value` goes below the given value; it fires only for values strictly below the threshold. Devices that do not report the sensor are ignored.

  Default: unset.
- `health-value` (string; unset): Name of the health sensor to compare, matching a name from `/system/health/print`, for example `cpu-temperature`. Uses the `[cpu-temperature]` style placeholder in the action text.
- `interface-change` (alt { change: enum (any) , change: ubit (running, not-running, added, removed) }; unset): Alert on an interface state change:

  - `any` (default) - Any state change.
  - `running` - An interface's link comes up.
  - `not-running` - An interface's link goes down.
  - `added` - An interface is first seen.
  - `removed` - An interface is no longer seen.

  `running` and `not-running` follow the link state of the interface, not its admin state: enabling or disabling an interface with no connection does not fire, while an actual link loss or recovery does.
- `interface-type` (alt { type: enum (any) , type: ubit (ethernet, wifi, bridge) }; unset): Restrict `interface-change` alerts to one interface type:

  - `any` (default) - Interfaces of any type.
  - `ethernet` - Ethernet ports.
  - `wifi` - Wireless interfaces.
  - `bridge` - Bridge interfaces.
- `upgrade-available` (bool; unset): Alert when a newer RouterOS version is available for the device.

  Default: no.
- `disconnected-more-than` (time; unset): Alert when a device has been disconnected for longer than the given time.

  Default: unset.
- `upgrade-job-done` (alt { cond: enum (yes) , cond: ubit (success, fail) }; unset): Alert when an upgrade job finishes; the rule fires once for the whole job, when the last device of the job is done:

  - `yes` (default) - Any outcome.
  - `success` - The job finished successfully.
  - `fail` - The job failed.

  A job that ends without installing an upgrade is treated as a failed job, so the `yes` and `fail` variants both fire.
- `upgrade-done` (alt { cond: enum (yes) , cond: ubit (success, fail) }; unset): Alert when the upgrade of a device finishes; the rule fires once for every device that finished its upgrade:

  - `yes` (default) - Any outcome.
  - `success` - The upgrade finished successfully.
  - `fail` - The upgrade failed.

  When no newer version is available for a device, its upgrade still finishes as a failure (the `[upgrade-error]` is `no upgrade available`), so the `yes` and `fail` variants both fire.
- `unpaired-device-connected` (bool; unset): Alert when a device that is not paired to the controller connects.

  Default: no.
- `rebooted` (bool; unset): Event condition that fires when the device unexpectedly reboots.

  Default: no.
- `log-topics` (multi { array-id, array-id, topic: super { ! , topic: enum } }; unset): Log topics to follow; prefix a topic with `!` to exclude it. Together with `log-regex`, defines a log-message event condition. CMR automatically instructs the device to forward matching log messages.
- `log-regex` (string; unset): Match log messages against the given regular expression. Each message matching the configured topics and regular expression fires the actions without creating a persistent active alert.
- `action.log` (string; unset): Write a message to the log when the alert fires. The message may contain placeholders such as `[device]` or `[cpu-usage]`, replaced with the values of the device that fired; an inapplicable placeholder is rendered as `unknown`.
- `action.log-topics` (multi { array-id, topic: enum }; unset): Log topics to write the message to.

  Default: `cmr,info`.
- `action.log-prefix` (string; unset): Prefix for the log message. When set, the prefix is prepended to the message without a separator; when unset the message is written as it is.
- `action.script` (enum; unset): Run a named system script when the alert fires. The script must allow itself to run with reduced rights; otherwise the action fails with `executing script ... from cmr failed ... (not enough permissions)`. Set the script's `dont-require-permissions` to yes.
- `action.script-vars` (multi { array-id, script-var: string }; unset): List of variable names to make available to the `action.script`: each variable is filled with the value for the device that fired. For example `device`, `identity`, `address`, `board`, `version` become `$device`, `$identity`, and so on in the script. A name with a hyphen (for example `cpu-usage`) cannot be read as an ordinary script variable.
- `action.http-url` (string; unset): HTTP webhook URL to call when the alert fires. On a failed call the alert writes `alert "<name>" HTTP action failed: <reason>` to the `cmr` topic with `warning` severity and counts the failure in `action-failures`; the other actions still run.
- `action.http-method` (enum: get | post | put | delete | head | patch; unset): HTTP method used for the webhook:

  - `get`
  - `post`
  - `put`
  - `delete`
  - `head`
  - `patch`
- `action.http-body` (string; unset): HTTP request body sent to the webhook. Supports the same placeholders as the log message, substituted per device (for example `[device]` and `[version]`). No `Content-Type` header is added automatically; add one with `action.http-headers` when the receiver expects it, for example `Content-Type: application/json` for a JSON body.
- `action.http-headers` (multi { header: string }; unset): Additional HTTP headers sent with the webhook, each as `Header: value`. The request also carries the controller's `RouterOS <version>` user-agent.
- `reset-on-disconnect` (enum: yes | no; unset): Clear (reset) a state alert when the device disconnects, so a reconnecting device fires the rule again if it still matches: `yes` or `no`. Default: `no` (the state is kept across a disconnect). Event alerts have no persistent state to reset.
- `severity` (enum: critical | high | medium | low; unset): Severity of the alert:

  - `critical`
  - `high`
  - `medium` (default)
  - `low`
- `category` (multi { array-id, category: enum }; unset): Categories assigned to the alert. The category is a grouping label: the server assigns one according to the rule's conditions (for example `performance`, `availability`, `version`, `network`, or `logging`), and it can be changed to any value.

**Read-only arguments**

- `devices` (num): Number of devices the alert rule matches (the devices selected by `labels`). When the rule covers all devices, this count includes the controller itself.
- `devices-on` (num): Number of devices with an active state alert. Event occurrences do not add to this count.
- `fired` (num): Total number of times the alert has fired.
- `action-failures` (num): Number of times an alert action has failed, for example a webhook that could not be reached.

## Commands

### /cmr/alert/show-devices

Package: cmr; Type: Command

Lists the devices on which the state alert of an alert rule is active, with a status flag for each (see the following flags). Event alerts never stay active, so they list no devices.

**Flags**

- `p` (remote-pending): Controller requests pairing.
- `I` (inactive): Device is inactive.
- `S` (stale): No connection (stale).
- `L` (controller): The CMR server itself (self-client).
- `C` (connected): Device is connected.
- `U` (upgrade-available): A newer update is available.

**Arguments**

- `on-only` (bool): Show only the devices on which the alert rule is active.

### /cmr/alert/test

Package: cmr; Type: Command

Runs the actions of the alert rule immediately, as if the rule had fired, with `[placeholder]` values in place of the real device data. Use it to verify that the actions work without waiting for a condition to appear on a device.
