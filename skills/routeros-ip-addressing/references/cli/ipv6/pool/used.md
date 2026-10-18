# /ipv6/pool/used

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/pool/used

Type: Directory

**Read-only arguments**

- `pool` (enum): Name of the pool the prefix is reserved from.
- `prefix` (ip6Prefix): IPv6 prefix that is assigned to the client from the pool.
- `owner` (string): What reserved the prefix ("DHCP", etc.)
- `info` (string): Shows DUID related information received from the client (value in hex). Can contain also a raw timestamp in hex.
