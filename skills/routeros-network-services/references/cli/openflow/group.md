# /openflow/group

> Source: https://manual.mikrotik.com/docs/cli-reference/openflow/group

Package: openflow; Type: Directory

**Flags**

- `I`: inactive

**Read-only arguments**

- `switch` (enum): Controller name that installed the group.
- `id` (num): Identifier of the group.
- `type` (enum: all | select | indirect | ff): Group type that determines how the action buckets are processed: all, select, indirect, or fast failover.
- `bucket-count` (num): Number of action buckets in the group.
- `flow-count` (num): Number of flow entries that reference the group.
- `buckets` (string): List of action buckets in the group.
- `bytes` (num): Number of bytes processed by the group.
- `packets` (num): Number of packets processed by the group.
- `duration` (time): Time since the group was installed.
- `bucket-stats` (string): Per-bucket packet and byte statistics.
