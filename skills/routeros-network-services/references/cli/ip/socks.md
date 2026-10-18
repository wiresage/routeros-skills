# /ip/socks

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/socks

Type: Settings Directory

The SOCKS proxy server accepts SOCKS client connections on its TCP port and relays them to the requested destinations, applying the [`access`](socks/access.md) rules and, optionally, [`users`](socks/users.md) authentication. For more information, see [SOCKS](../../guides/network-management/socks.md).

**Arguments**

- `enabled` (bool): Whether the SOCKS proxy server runs. Default: `no`.
- `port` (num): TCP port the proxy listens on. Default: `1080`.
- `connection-idle-timeout` (time): Time after which an idle proxied connection is terminated. Default: `2m`.
- `max-connections` (num): Maximum number of simultaneous proxied connections, `1` to `500`. Default: `200`.
- `vrf` (enum): VRF the proxy listens in. With a VRF other than `main`, the port is reachable only inside that VRF. Default: `main`.
- `version` (enum: 4 | 5): SOCKS protocol version the server accepts.
  - `4` (default) - Accept only SOCKS4 clients.
  - `5` - Accept only SOCKS5 clients. Required for password authentication and for the [`socksify`](socksify.md) service, which always speaks SOCKS5.
- `auth-method` (enum: none | password): Authentication the server requires from clients.
  - `none` (default) - No authentication.
  - `password` - Clients must authenticate with a username and password from [`users`](socks/users.md). If no users exist, every connection is rejected.
