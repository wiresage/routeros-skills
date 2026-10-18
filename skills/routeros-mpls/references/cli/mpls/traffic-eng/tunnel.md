# /mpls/traffic-eng/tunnel

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/traffic-eng/tunnel

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `F`: forwarding

**Arguments**

- `name` (string; mandatory)
- `vrf` (enum; unset)
- `from-address` (address (flags=46); unset)
- `to-address` (address (flags=46); mandatory)
- `bandwidth` (num; unset)
- `primary-path` (enum; unset)
- `secondary-paths` (multi { array-id, primary-path: enum }; unset)
- `primary-retry-interval` (time; unset)
- `secondary-standby` (bool; unset)
- `bandwidth-limit` (num; unset)
- `auto-bandwidth-range` (composite { min: num [1 .. ] , max: num [1 .. ] }; unset)
- `auto-bandwidth-reserve` (num; unset)
- `auto-bandwidth-avg-interval` (time; unset)
- `auto-bandwidth-update-interval` (time; unset)
- `setup-priority` (num; unset)
- `holding-priority` (num; unset)
- `record-route` (bool; unset)
- `affinity-include-all` (num; unset)
- `affinity-include-any` (num; unset)
- `affinity-exclude` (num; unset)
- `reoptimize-interval` (time; unset)

**Read-only arguments**

- `session` (string)
- `forwarding-on` (string)
- `primary` (string)
- `primary-pending` (string)
- `secondary` (string)
- `secondary-pending` (string)

## Commands

### /mpls/traffic-eng/tunnel/reoptimize

Conditions: !smips; Type: Command
