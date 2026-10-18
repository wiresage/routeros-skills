# /openflow/meter

> Source: https://manual.mikrotik.com/docs/cli-reference/openflow/meter

Package: openflow; Type: Directory

The sub-menu lists the traffic meters installed by the controller. Meters enable rate monitoring before output and applying action instructions.

**Flags**

- `I`: inactive

**Read-only arguments**

- `switch` (enum): Controller name that installed the meter.
- `id` (num): Identifier of the meter.
- `band-count` (num): Number of meter bands in the meter.
- `bands` (string): List of meter bands that define the rate and how packets are processed.
- `bytes` (num): Number of bytes processed by the meter.
- `packets` (num): Number of packets processed by the meter.
- `duration` (time): Time since the meter was installed.
