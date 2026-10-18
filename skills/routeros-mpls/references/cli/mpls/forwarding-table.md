# /mpls/forwarding-table

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/forwarding-table

Conditions: !smips; Type: Directory

**Flags**

- `L`: ldp
- `P`: vpn
- `T`: traffic-eng
- `V`: vpls

**Read-only arguments**

- `label` (enum: expl-null | alert | expl-null6 | impl-null)
- `type` (enum: ldp | vpn | traffic-eng | vpls)
- `vrf` (enum)
- `prefix` (address (flags=46/))
- `nexthops` (object { label: enum (expl-null | alert | expl-null6 | impl-null) , nh: address , interface: iface_enum })
- `te-sender` (string)
- `te-session` (string)
- `vpls` (iface_enum)
