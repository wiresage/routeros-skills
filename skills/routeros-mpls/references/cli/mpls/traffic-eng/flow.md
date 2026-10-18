# /mpls/traffic-eng/flow

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/traffic-eng/flow

Conditions: !smips; Type: Directory

**Flags**

- `N`: ingress
- `E`: egress
- `F`: forwarding
- `R`: reservation

**Read-only arguments**

- `vrf` (enum)
- `session` (string)
- `sender` (string)
- `label` (num)
- `out-labels` (multi { array-id, out-label: num })
- `out-nexthop` (address (flags=46i))
- `bw` (num)
- `style` (enum: unknown | shared | fixed)
- `psb` (string)
- `blockade` (string)
- `resv` (string)
- `rsb` (string)
