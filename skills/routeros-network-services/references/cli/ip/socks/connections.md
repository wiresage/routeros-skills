# /ip/socks/connections

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/socks/connections

Type: Directory

Read-only list of active proxied connections. An entry exists while a proxied connection is open. For more information, see [SOCKS](../../../guides/network-management/socks.md).

**Arguments**

- `src-address` (composite { address: alt { addr-ipv4: ipAddr , addr-ipv6: ip6Addr } , port: num }): Address and port of the SOCKS client.
- `dst-address` (composite { address: alt { addr-ipv4: ipAddr , addr-ipv6: ip6Addr , addr-domain: string } , port: num }): The requested destination address and port.
- `type` (enum: unknown | out | in): Type of the connection.
  - `unknown` - The connection was just initiated.
  - `out` - The connection is being relayed to the requested destination.
  - `in` - The connection is incoming.
- `tx` (num): Bytes relayed to the destination on this connection.
- `rx` (num): Bytes received from the destination on this connection.

**Read-only arguments**

- `user` (enum): Username from [`users`](users.md) the client authenticated with. Empty when `auth-method=none`.
