# /ppp/secret

> Source: https://manual.mikrotik.com/docs/cli-reference/ppp/secret

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `service` (enum: any | async | pptp | pppoe | l2tp | ovpn | sstp)
- `caller-id` (string)
- `password` (string)
- `profile` (enum)
- `local-address` (super { address: ipAddr })
- `remote-address` (super { remote-address: ipAddr })
- `routes` (string)
- `ipv6-routes` (string)
- `remote-ipv6-prefix` (super { remote-prefix: ip6Prefix })
- `limit-bytes-in` (num)
- `limit-bytes-out` (num)

**Read-only arguments**

- `last-logged-out` (date)
- `last-caller-id` (string)
- `last-disconnect-reason` (enum: peer-request | hung-up | idle-timeout | session-timeout | reset | reboot | port-error | nas-error | nas-request)
