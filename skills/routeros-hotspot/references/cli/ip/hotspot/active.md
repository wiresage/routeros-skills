# /ip/hotspot/active

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/active

Type: Directory

**Flags**

- `R`: radius
- `B`: blocked

**Read-only arguments**

- `server` (enum)
- `user` (string)
- `domain` (string)
- `address` (ipAddr)
- `mac-address` (macAddr)
- `login-by` (string)
- `uptime` (time)
- `session-time-left` (time)
- `idle-time` (time)
- `idle-timeout` (time)
- `keepalive-timeout` (time)
- `bytes-in` (num)
- `bytes-out` (num)
- `packets-in` (num)
- `packets-out` (num)
- `limit-bytes-in` (num)
- `limit-bytes-out` (num)
- `limit-bytes-total` (num)
- `advertisement` (enum (disabled | sleeping | pending | pending,block) { disabled:0, sleeping:1, pending:2, pending,block:3 })

## Commands

### /ip/hotspot/active/login

Type: Command

**Arguments**

- `ip` (ipAddr)
- `mac-address` (macAddr)
- `user` (string)
- `password` (string)
- `domain` (string)
