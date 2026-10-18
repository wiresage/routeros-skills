# /port/remote-access

> Source: https://manual.mikrotik.com/docs/cli-reference/port/remote-access

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive
- `A`: active
- `B`: busy
- `L`: logging-active

**Arguments**

- `port` (enum)
- `channel` (num)
- `remote-addresses` (object { peer-spec: super { addr0: address (flags=46/) , [addr1] [ -address (flags=46)] , [port] [ @num] } })
- `local-address` (alt { ipv4: ipAddr , ipv6: ip6Addr })
- `ip-port` (num)
- `protocol` (enum: tcp-server | rfc2217 | tcp-client | udp)
- `log-file` (string)

**Read-only arguments**

- `active-peer` (ip6Addr)
- `active-peer-port` (num)
