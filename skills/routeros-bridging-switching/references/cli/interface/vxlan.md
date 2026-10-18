# /interface/vxlan

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/vxlan

Type: Directory

**Flags**

- `X`: disabled
- `R`: running
- `H`: hw-offloaded

**Arguments**

- `name` (string)
- `mtu` (num)
- `mac-address` (macAddr)
- `vni` (num; mandatory)
- `group` (alt { address: ipAddr , ipv6-address: ip6Addr })
- `interface` (iface_enum)
- `port` (num)
- `local-address` (address (flags=46))
- `dont-fragment` (enum: disabled | enabled | auto | inherit)
- `vtep-vrf` (enum)
- `vteps-ip-version` (enum: ipv4 | ipv6)
- `allow-fast-path` (bool)
- `max-fdb-size` (num)
- `ttl` (num)
- `learning` (bool)
- `checksum` (bool)
- `rem-csum` (enum: none | rx | tx | both)
- `hw` (bool)
- `bridge` (iface_enum)
- `bridge-pvid` (num)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `arp-accept` (bool)
- `loop-protect` (enum: default | off | on)
- `loop-protect-send-interval` (time)
- `loop-protect-disable-time` (time)

**Read-only arguments**

- `l2mtu` (num)
- `loop-protect-status` (enum: off | on | disabled)
