# /cmr/device

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/device

Package: cmr; Type: Directory

Devices managed by this CMR server. A device appears in the list as soon as it connects to the server, with the **P** flag until the pairing is approved. The server itself is shown as the device with the **L** flag. Use the commands in this menu to operate on the fleet, for example `run-script`, `upgrade`, `reboot`, or `pair`. See [CMR](../../guides/management-tools/cmr.md) for how devices connect and pair.

**Flags**

- `P` (pending): Pairing pending.
- `p` (remote-pending): Controller requests pairing.
- `I` (inactive): Device is inactive.
- `S` (stale): No connection (stale).
- `L` (controller): The CMR server itself (self-client).
- `C` (connected): Device is connected.
- `U` (upgrade-available): The upgrade channel of the device offers a different version than the installed one. The offered version can also be earlier than the installed version.

**Arguments**

- `ids` (object { ids: super { his-id: string , [our-id] [ /string] } }): Identities (his-id / our-id) of the managed device.
- `pairing-requirement` (enum: none | password | confirm): Pairing requirement applied to this device, overriding the server default: `none`, `password`, or `confirm`.
- `labels` (multi { array-id, label: enum }; unset): User labels assigned to the device (grouping/filtering).
- `port-labels` (object { port-and-labels: super { port: string , labels: multi { array-id, label: string } } }; unset): Labels per port. Quote the label, for example `port-labels=ether1:"uplink"`. `/cmr/vlan` rules can select ports by these labels.
- `identity` (string): System identity (editable) of the device.

**Read-only arguments**

- `peer` (enum): The management peer this device is connected to.
- `board` (string): Board name.
- `version` (string): RouterOS version of the device.
- `minimum-version` (string): Minimum supported version.
- `allowed-versions` (string): Safe (safepkg) upgrade indicator.
- `address` (address (flags=46)): Current connection address.
- `auto-labels` (multi { array-id, label: string }; unset): Automatically assigned labels.
- `packages` (multi { array-id, label: string }; unset): Installed packages.
- `state` (string): Device state.
- `upgrade-rule` (enum): Upgrade rule covering this device. The first rule in the [`/cmr/upgrade`](upgrade.md) rule list that covers the device claims it, so a `labels=all` rule placed at the top covers every device.
- `channel` (alt): Current upgrade channel/version.
- `available-version` (string): Newest available upgrade.
- `connected-time` (time; unset): Time the device has been connected.
- `uptime` (time; unset): Device uptime.
- `disconnected-since` (date; unset): Time since the device disconnected.
- `alerts` (super { on: num , [all] /num , [critical] num , [high] /num , [medium] /num , [low] /num }): Enabled/total alert counts by severity.
- `serial` (string): Factory serial number.

## Commands

### /cmr/device/apptraffic

Package: cmr; Type: Command

Application traffic monitor for the selected devices.

**Arguments**

- `labels` (object; unset): Select the devices to monitor using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.

### /cmr/device/dashboard

Package: cmr; Type: Command

Opens a live view of the selected devices: devices, resources, interfaces, curves, and AP/station data.

**Arguments**

- `labels` (object; unset): Select the devices to show in the dashboard using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.

### /cmr/device/pair

Package: cmr; Type: Command

Starts pairing with the selected devices.

**Arguments**

- `labels` (object; unset): Select the devices to pair using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.
- `username` (string; unset): Username used for pairing when the device requires it.
- `password` (string; unset): Password used for pairing when the device requires it.

**Read-only arguments**

- `device` (enum): Device being paired.
- `status` (string): Pairing status.

### /cmr/device/reboot

Package: cmr; Type: Command

Reboots the selected devices. The command returns right away, and the server logs `<device> rebooted` when a device has restarted, where `<device>` is `identity@address`.

**Arguments**

- `labels` (object; unset): Select the devices to reboot using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.

### /cmr/device/run-script

Package: cmr; Type: Command

Runs a script on the selected devices.

**Arguments**

- `script` (alt { script: string }): The script to run on the selected devices.
- `labels` (object; unset): Select the devices to run the script on using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.
- `order` (object): Execution order (by labels).
- `strategy` (enum; unset): How devices are processed: `parallel` or `sequential`.
- `fail-policy` (enum; unset): Behaviour if a device fails: `continue`, `stop`, or `continue-order`.
- `timeout` (time; unset): Script execution timeout.

**Read-only arguments**

- `device` (enum): Device the script is running on.
- `status` (string): Execution status.
- `output` (string): Script output.

### /cmr/device/upgrade

Package: cmr; Type: Command

Starts an upgrade (job) for the selected devices. The upgrade runs as a job in [`/cmr/upgrade/job`](upgrade/job.md), with the same job states and result counters. On the console, the command shows the job's devices and their states until you press <kbd>Control</kbd>+<kbd>C</kbd> or the time given in `duration` ends; the job continues on the server. With `order`, the label groups are upgraded one after another; list the devices that others connect through, such as switches and gateways, last.

**Flags**

- `L` (controller): Include the CMR server itself (self-client).

**Arguments**

- `labels` (object; unset): Select the devices to upgrade using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.
- `order` (object; unset): Execution order (by labels).
- `channel` (alt; unset): Upgrade channel (`long-term`, `stable`, `testing`, or `development`) or a pinned version, for example `channel=7.24.4`. When not set, each device upgrades on its own upgrade channel, the `channel` value shown in `/cmr/device`.
- `schedule-time` (super { time: date , [day] [ @enum (sun | mon | tue | wed | thu | fri | sat)] }; unset): When the upgrade starts: a time with an optional weekday given after `@`, for example `14:00:00` or `00:00:00@sat`. The job waits in the `scheduled` state until the next occurrence of that time.
- `strategy` (enum: parallel | sequential; unset): How devices are upgraded: `parallel` upgrades all covered devices at the same time; `sequential` upgrades them one after another and waits for each to finish. With `continue-order` the devices are processed per label group in the order given by `order`: in `parallel` the devices of each group are upgraded together, in `sequential` one at a time. Default: `parallel`.
- `fail-policy` (enum: continue | stop | continue-order; unset): Behaviour if a device fails: `continue` skips the failed device and continues with the rest; `stop` stops the whole upgrade on the first failure and does not continue with the remaining devices or with the next label group; `continue-order` skips the failed device and continues with the next label group, processing the labels one group after another in the order given by `order`. With `sequential` the rest of the failed device's group is skipped; with `parallel` only the failed device is abandoned and devices already in progress in the group finish. Default: `stop`.
- `packages` (multi { package: string }; unset): Packages to upgrade.

### /cmr/device/wifi-logs

Package: cmr; Type: Command

WiFi log monitor for the selected devices.

**Arguments**

- `labels` (object; unset): Select the devices to monitor using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.
- `address` (macAddr; unset): Filter by client MAC address.
- `bssid` (macAddr; unset): Filter by BSSID.
- `time` (time; unset): Filter by time.
- `time-start` (date; unset): Filter logs from this time.
- `time-end` (date; unset): Filter logs up to this time.
- `event` (enum: connected | disconnected | failed; unset): Filter by event: `connected`, `disconnected`, or `failed`.
