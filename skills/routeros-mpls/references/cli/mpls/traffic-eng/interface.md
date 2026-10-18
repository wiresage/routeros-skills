# /mpls/traffic-eng/interface

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/traffic-eng/interface

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `interface` (iface_enum; mandatory)
- `bandwidth` (num; unset)
- `k-factor` (num; unset)
- `resource-class` (num; unset)
- `refresh-time` (time; unset)
- `use-udp` (bool; unset)
- `blockade-k-factor` (num; unset)
- `te-metric` (num; unset)
- `igp-flood-period` (time; unset)
- `up-flood-thresholds` (multi { array-id, up-flood-threshold: num [0 .. 100] }; unset)
- `down-flood-thresholds` (multi { array-id, down-flood-threshold: num [0 .. 100] }; unset)

**Read-only arguments**

- `remaining-bw` (num)
- `remaining-bw-prios` (multi { array-id, remaining-bw-prio: num })
- `lih` (num)
- `local-address-ip` (address (flags=46))
- `local-address-ip6` (address (flags=46))
