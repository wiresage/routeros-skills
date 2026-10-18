# /openflow/port

> Source: https://manual.mikrotik.com/docs/cli-reference/openflow/port

Package: openflow; Type: Directory

This menu lists the ports controlled by OpenFlow.

**Flags**

- `X`: disabled
- `I`: inactive
- `D`: dynamic

**Arguments**

- `interface` (enum; mandatory): Name of the interface to be controlled by OpenFlow.
- `switch` (enum; mandatory): Name of the switch able to control the port.
- `port-id` (num): Port ID used to identify the interface in flow rules.

**Read-only arguments**

- `tx-bytes` (num): Number of bytes transmitted on the interface.
- `tx-packets` (num): Number of packets transmitted on the interface.
- `rx-bytes` (num): Number of bytes received on the interface.
- `rx-packets` (num): Number of packets received on the interface.
