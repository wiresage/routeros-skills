# /interface/bridge/host

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge/host

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic
- `L`: local
- `E`: external
- `A`: aged
- `a`: aged-peer

**Arguments**

- `mac-address` (macAddr; mandatory)
- `vid` (num)
- `interface` (iface_enum; mandatory)
- `bridge` (iface_enum; mandatory)

**Read-only arguments**

- `on-interface` (iface_enum)
- `remote-ip` (alt { ipv4: ipAddr , ipv6: ip6Addr })
- `dhcpv4-ip` (ipAddr)
- `dhcpv4-server-id` (ipAddr)
- `dhcpv4-status` (enum: bound | requesting | searching | renewing | rebinding | expired | relay-agent)
- `dhcpv4-expires-after` (time)
