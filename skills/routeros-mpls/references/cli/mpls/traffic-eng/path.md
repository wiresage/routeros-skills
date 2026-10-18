# /mpls/traffic-eng/path

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/traffic-eng/path

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `use-cspf` (bool; unset)
- `setup-priority` (num; unset)
- `holding-priority` (num; unset)
- `record-route` (bool; unset)
- `affinity-include-all` (num; unset)
- `affinity-include-any` (num; unset)
- `affinity-exclude` (num; unset)
- `reoptimize-interval` (time; unset)
- `hops` (multi { array-id, array-id, hop: super { address: address (flags=46) , [strict] /enum (loose | strict) } }; unset)
