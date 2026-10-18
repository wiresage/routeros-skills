# /system/ptp/port

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ptp/port

Conditions: !smips; Syscap: ptp; Type: Directory

PTP ports: the interfaces that join a [`/system/ptp`](../ptp.md) profile instance.

**Flags**

- `I`: inactive
- `X`: disabled

**Arguments**

- `ptp` (enum; mandatory): The [`/system/ptp`](../ptp.md) profile instance this port joins
- `interface` (iface_enum; mandatory): Interface used for PTP (the hardware must support PTP timestamping — see the supported device list in the [guide](../../../guides/system-information-and-utilities/precision-time-protocol.md))
- `role` (enum: bmca | master | slave): Port role selection: `bmca` (best master clock algorithm decides between master and slave), or a fixed `master` or `slave`
- `announce-interval` (num): Log2 interval between announce messages in seconds (for example -3...4 for 0.125s-16s)
- `sync-interval` (num): Log2 interval between sync messages in seconds
- `delay-interval` (num): Log2 interval between delay request messages in seconds (E2E mode)
- `pdelay-interval` (num): Log2 interval between peer delay messages in seconds (P2P mode)
- `vlan-id` (num): VLAN ID under which the port participates in PTP when the interface carries tagged PTP traffic
