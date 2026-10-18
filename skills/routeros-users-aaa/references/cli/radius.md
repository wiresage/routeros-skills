# /radius

> Source: https://manual.mikrotik.com/docs/cli-reference/radius

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `service` (ubit (ppp, login, hotspot, wireless, dhcp, ipsec, dot1x))
- `called-id` (string)
- `domain` (string)
- `address` (address (flags=46v); mandatory)
- `secret` (string)
- `authentication-port` (num)
- `accounting-port` (num)
- `timeout` (time)
- `radsec-timeout` (time)
- `accounting-backup` (bool)
- `realm` (string)
- `src-address` (alt { ip-address: ipAddr , ipv6-address: ip6Addr })
- `protocol` (enum: udp | radsec)
- `certificate` (enum: none)
- `require-message-auth` (enum: no | yes-for-request-resp)

**Read-only arguments**

- `status` (string)

## Commands

### /radius/monitor

Type: Command

**Read-only arguments**

- `pending` (num)
- `requests` (num)
- `accepts` (num)
- `rejects` (num)
- `resends` (num)
- `timeouts` (num)
- `bad-replies` (num)
- `last-request-rtt` (time)

### /radius/reset-counters

Type: Command
