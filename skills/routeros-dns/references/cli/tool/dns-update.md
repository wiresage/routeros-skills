# /tool/dns-update

> Source: https://manual.mikrotik.com/docs/cli-reference/tool/dns-update

Type: Command

Sends one dynamic DNS update (RFC 2136), signed with a TSIG hmac-md5 key, to the authoritative DNS server of a zone, and points a name in the zone at an IPv4 address. The update replaces the A records of the name. The command prints nothing when the server accepts the update. See [DNS update](../../guides/diagnostics-monitoring-and-troubleshooting/dynamic-dns.md).

**Arguments**

- `dns-server` (ipAddr): IPv4 address of the DNS server that is authoritative for `zone`. The update goes to its TCP port 53.
- `zone` (string): DNS zone that holds the name, for example `example.com`.
- `name` (string): Name to update, relative to `zone`: `name=office` with `zone=example.com` updates `office.example.com`. A full name is added to the zone again, and a name with a trailing dot fails with `failure: bad name`.
- `address` (multi { addr: ipAddr }): IPv4 address for the A record of the name. Required. Only one address is accepted (`failure: only one address allowed`), and IPv6 addresses are refused.
- `key-name` (string): Name of the TSIG key, as configured on the DNS server. Without `key-name` and `key`, the update is sent unsigned.
- `key` (string): Secret of the TSIG key in base64, as configured on the DNS server. The algorithm is hmac-md5. Put the value in quotes, because a base64 value can end in `=`.
- `ttl` (num): Time to live of the record, in seconds. For an address that changes, use a short value such as `300`. Default: 86400.
