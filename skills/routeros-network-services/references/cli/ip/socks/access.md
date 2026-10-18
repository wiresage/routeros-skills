# /ip/socks/access

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/socks/access

Type: Directory

Access control list the server evaluates before it dials the requested destination. The rules are checked in order and the first matching rule decides. A request that matches no rule is allowed, so an empty list allows everything and a restrictive list needs a trailing `deny` rule. For more information, see [SOCKS](../../../guides/network-management/socks.md).

**Flags**

- `X` (disabled): disabled. The rule is not used.

**Arguments**

- `src-address` (super { ! , alt-address: alt { range: ipRange , src-ipv6: ip6Prefix } }): Address or subnet of the SOCKS client, the requester. Unset matches any.
- `src-port` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] }): Source TCP port of the client's connection. Unset matches any.
- `dst-address` (super { ! , alt-address: alt { range: ipRange , dst-ipv6: ip6Prefix , dst-domain: string } }): Destination requested by the client: an IP address, a range or a domain name. A domain name matches only clients that request the destination by name (the SOCKS5 domain address type). The [`socksify`](../socksify.md) client always requests by IP address, so a domain-name rule does not match socksified traffic.
- `dst-port` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] }): Requested destination port or range, for example `21` or `1024-65535`. Unset matches any.
- `action` (enum: deny | allow): What the server does with a matching request.
  - `allow` (default) - Forward the connection to the destination.
  - `deny` - Reject the connection.
