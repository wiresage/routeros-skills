# /interface/vlan

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/vlan

Type: Directory

**Flags**

- `X`: disabled
- `R`: running
- `H`: hw-offloaded

**Arguments**

- `name` (string)
- `mtu` (num)
- `forced-mac-address` (macAddr)
- `vlan-id` (num; mandatory)
- `interface` (iface_enum; mandatory)
- `use-service-tag` (bool)
- `mvrp` (bool)
- `l3-hw-offloading` (bool; syscap=crs_prestera): Layer 3 hardware offloading
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `arp-accept` (bool)
- `loop-protect` (enum: default | off | on)
- `loop-protect-send-interval` (time)
- `loop-protect-disable-time` (time)

**Read-only arguments**

- `l2mtu` (num)
- `mac-address` (macAddr)
- `loop-protect-status` (enum: off | on | disabled)
