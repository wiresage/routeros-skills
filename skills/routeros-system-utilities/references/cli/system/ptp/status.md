# /system/ptp/status

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ptp/status

Conditions: !smips; Syscap: ptp; Type: Directory

Current PTP port state per instance and interface.

**Read-only arguments**

- `interface` (iface_enum): Interface of the PTP port
- `state` (string): Current port state (for example `listening`, `master` or `slave`)
- `delay` (num): Measured path delay on slave ports, in nanoseconds
- `port-nr` (num): Port number of this port within the PTP data set
- `as-capable` (bool): Whether the port is asCapable per IEEE 802.1AS
- `neigh-freq-drift` (num): Measured frequency drift of the neighbour clock, in parts per billion
