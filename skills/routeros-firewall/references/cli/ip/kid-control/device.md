# /ip/kid-control/device

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/kid-control/device

Type: Directory

**Flags**

- `X`: disabled
- `D`: dynamic
- `B`: blocked
- `L`: limited
- `I`: inactive

**Arguments**

- `all` (switch)
- `static` (switch)
- `dynamic` (switch)
- `name` (string)
- `mac-address` (macAddr; mandatory)
- `user` (enum () { :0xffffffff }; mandatory)

**Read-only arguments**

- `ip-address` (object { server: alt { ip: ipAddr , ipv6: ip6Addr } })
- `activity` (string)
- `rate-down` (num)
- `rate-up` (num)
- `bytes-down` (num)
- `bytes-up` (num)
- `idle-time` (time)

## Commands

### /ip/kid-control/device/reset-counters

Type: Command
