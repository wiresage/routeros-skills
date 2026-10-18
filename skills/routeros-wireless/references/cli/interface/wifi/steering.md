# /interface/wifi/steering

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/steering

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `neighbor-group` (multi { array-id, neighbor-group: string }; unset)
- `rrm` (bool; unset)
- `wnm` (bool; unset)
- `2g-probe-delay` (bool; unset)
- `transition-threshold` (num; unset)
- `transition-threshold-time` (time; unset)
- `transition-request-period` (time; unset)
- `transition-request-count` (num; unset)
- `transition-time` (alt { value: enum (unlimited | immediate) , time: time }; unset)
