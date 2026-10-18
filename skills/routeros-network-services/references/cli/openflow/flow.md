# /openflow/flow

> Source: https://manual.mikrotik.com/docs/cli-reference/openflow/flow

Package: openflow; Type: Directory

This menu lists the installed flows responsible for packet forwarding between OpenFlow ports.

**Flags**

- `I`: inactive

**Read-only arguments**

- `switch` (enum): Controller name that installed the rule.
- `version` (num): OpenFlow protocol version of the switch that installed the flow.
- `match` (string): Match fields the flow entry matches against.
- `actions` (string): Actions applied to packets that match the flow entry.
- `info` (string): Additional flow entry information, such as priority, timeouts, and cookie.
- `table-id` (num): ID of the table where the rule is located.
- `bytes` (num): Number of bytes matched by the rule.
- `packets` (num): Number of packets matched by the rule.
- `duration` (time): Time since the flow entry was installed.
