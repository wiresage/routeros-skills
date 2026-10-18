# /interface/ppp-server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ppp-server

Type: Directory

**Flags**

- `X`: disabled
- `R`: running

**Arguments**

- `name` (string)
- `max-mtu` (num)
- `max-mru` (num)
- `mrru` (num)
- `port` (enum)
- `data-channel` (num)
- `authentication` (ubit (pap, chap, mschap1, mschap2))
- `profile` (enum)
- `modem-init` (string)
- `ring-count` (num)
- `null-modem` (bool)

## Commands

### /interface/ppp-server/monitor

Type: Command

**Read-only arguments**

- `status` (string)
- `uptime` (time)
- `user` (string)
- `caller-id` (string)
- `encoding` (string)
- `connect-speed` (num)
- `mtu` (num)
- `mru` (num)
- `local-address` (ipAddr)
- `remote-address` (ipAddr)
- `local-ipv6-address` (ip6Addr)
- `remote-ipv6-address` (ip6Addr)
