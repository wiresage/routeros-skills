# /ip/firewall/connection/tracking

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/firewall/connection/tracking

Type: Settings Directory

**Arguments**

- `enabled` (enum: auto | yes | no)
- `tcp-syn-sent-timeout` (time)
- `tcp-syn-received-timeout` (time)
- `tcp-established-timeout` (time)
- `tcp-fin-wait-timeout` (time)
- `tcp-close-wait-timeout` (time)
- `tcp-last-ack-timeout` (time)
- `tcp-time-wait-timeout` (time)
- `tcp-close-timeout` (time)
- `tcp-max-retrans-timeout` (time)
- `tcp-unacked-timeout` (time)
- `loose-tcp-tracking` (bool)
- `liberal-tcp-tracking` (bool)
- `udp-timeout` (time)
- `udp-stream-timeout` (time)
- `icmp-timeout` (time)
- `generic-timeout` (time)

**Read-only arguments**

- `active-ipv4` (bool)
- `active-ipv6` (bool)
- `max-entries` (num)
- `total-entries` (num)
- `total-ip4-entries` (num)
- `total-ip6-entries` (num)
