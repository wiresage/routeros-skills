# /ipv6/pool

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/pool

Type: Directory

IP pools are used to define ipv6 prefixes that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Whenever possible, the same IPv6 prefix is given out to each client (OWNER/INFO pair).

**Flags**

- `D`: dynamic
- `I`: inactive

**Arguments**

- `name` (string; mandatory): Name of the pool.
- `prefix` (ip6Prefix)
- `from-pool` (enum): Name of another pool from which to acquire prefix dynamically.
- `prefix-length` (num; mandatory): The option represents the prefix size that will be given out to the client.

**Read-only arguments**

- `actual-prefix` (ip6Prefix)
- `valid-lifetime` (time)
- `preferred-lifetime` (time)
