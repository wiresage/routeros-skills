# /routing/bfd/session

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bfd/session

Type: Directory

**Flags**

- `U`: up
- `I`: inactive

**Read-only arguments**

- `multihop` (bool)
- `vrf` (enum)
- `remote-address` (address (flags=46i))
- `local-address` (address (flags=46i))
- `state` (enum: admin-down | down | init | up)
- `state-changes` (num)
- `uptime` (time)
- `desired-tx-interval` (time)
- `actual-tx-interval` (time): real-time frequency at which the device currently sends BFD control packets.
- `required-min-rx` (time)
- `remote-min-rx` (time)
- `remote-min-tx` (time)
- `multiplier` (num)
- `hold-time` (time)
- `packets-rx` (num)
- `packets-tx` (num)
