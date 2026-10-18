# /ip/socksify

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/socksify

Type: Directory

Service that forwards traffic redirected to it by a firewall NAT rule (`action=socksify`, typically in the `dstnat` chain) through an upstream SOCKS5 server. Changes to a record's properties apply after you disable and re-enable the record.

See [Socksify](../../guides/network-management/socks/socksify.md) for the full documentation.

**Flags**

- `X` (disabled): disabled (set by default)
- `D`: dynamic

**Arguments**

- `name` (string): Name of the socksify service record.
- `connection-timeout` (num): Time in seconds (0 to 3000) to wait for the SOCKS server and the destination during connection setup before aborting with an error. Set to 0 to disable the timeout. Default: `60`.
- `port` (num): Local TCP port the service listens on; the `socksify` NAT action redirects intercepted connections to this port. Default: `952`.
- `socks5-server` (ipAddr): IPv4 address of the upstream SOCKS5 server. IPv6 addresses are not accepted. Default: `0.0.0.0`.
- `socks5-port` (num): Listening port of the SOCKS5 server. Default: `1080`.
- `socks5-user` (string): Username for the upstream SOCKS5 server. Shown as plain text in `print detail` output. Default: empty.
- `socks5-password` (string): Password for the upstream SOCKS5 server. Shown as plain text in `print detail` output. Default: empty.
