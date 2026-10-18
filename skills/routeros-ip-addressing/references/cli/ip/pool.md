# /ip/pool

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/pool

Type: Directory

IP pools are used to define a range of IP addresses that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Separate lists for IPv4 and IPv6 are available. Whenever possible, the same IP address is given out to each client (OWNER/INFO pair).

**Arguments**

- `name` (string): Name of the pool.
- `ranges` (multi { range: ipRange }; mandatory): IP address list of non-overlapping IP address ranges in the form of: `from1-to1,from2-to2,...,fromN-toN`. For example, `10.0.0.1-10.0.0.27,10.0.0.32-10.0.0.47`.
- `next-pool` (enum: none): When IP address acquisition is performed from a pool that has no free addresses, and the next-pool property is set, then an IP address will be acquired from the next pool.

**Read-only arguments**

- `total` (num)
- `used` (num)
- `available` (num)
