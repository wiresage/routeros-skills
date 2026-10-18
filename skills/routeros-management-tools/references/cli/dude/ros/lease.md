# /dude/ros/lease

> Source: https://manual.mikrotik.com/docs/cli-reference/dude/ros/lease

Package: dude; Type: Directory

**Flags**

- `X`: disabled
- `R`: radius
- `D`: dynamic
- `B`: blocked

**Arguments**

- `device` (enum; mandatory)
- `address` (alt { ip-address: ipAddr , prefix: ip6Addr , pool: enum })
- `mac-address` (macAddr)
- `use-src-mac` (bool)
- `client-id` (string)
- `rate-limit` (string)
- `insert-queue-before` (super { queue: enum (bottom | first) { bottom:0xffffffff, first:0 } })
- `address-lists` (multi { array-id, address-list: string })
- `server` (enum: all)
- `block-access` (bool)
- `lease-time` (time)
- `always-broadcast` (bool)
- `dhcp-option` (multi { array-id, option: enum })
- `dhcp-option-set` (enum: none)

**Read-only arguments**

- `status` (enum: waiting | testing | busy | offered | bound | authorizing)
- `expires-after` (time)
- `last-seen` (alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe } , time: time })
- `active-address` (alt { active-address: ipAddr , active-address6: ip6Addr })
- `active-mac-address` (macAddr)
- `active-client-id` (string)
- `active-server` (enum)
- `host-name` (string)
- `src-mac-address` (macAddr)
- `agent-circuit-id` (string)
- `agent-remote-id` (string)
