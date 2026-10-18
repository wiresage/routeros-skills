# /ip/hotspot/user

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/user

Type: Directory

**Flags**

- `*`: default
- `X`: disabled
- `D`: dynamic

**Arguments**

- `server` (enum: all)
- `name` (string; mandatory)
- `password` (string)
- `otp-secret` (string)
- `address` (ipAddr)
- `mac-address` (macAddr)
- `profile` (enum)
- `routes` (string)
- `email` (string)
- `limit-uptime` (time)
- `limit-bytes-in` (num)
- `limit-bytes-out` (num)
- `limit-bytes-total` (num)

**Read-only arguments**

- `uptime` (time)
- `bytes-in` (num)
- `bytes-out` (num)
- `packets-in` (num)
- `packets-out` (num)

## Commands

### /ip/hotspot/user/reset-counters

Type: Command
