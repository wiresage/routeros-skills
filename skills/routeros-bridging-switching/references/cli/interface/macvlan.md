# /interface/macvlan

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/macvlan

Type: Directory

**Flags**

- `X`: disabled
- `R`: running

**Arguments**

- `name` (string)
- `mac-address` (macAddr)
- `mtu` (num)
- `interface` (iface_enum): Only interfaces with a MAC address are supported for macvlan
- `mode` (enum: private | bridge): In bridge mode macvlan interfaces are allowed to talk to eachother
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `arp-accept` (bool)
- `loop-protect` (enum: default | off | on)
- `loop-protect-send-interval` (time)
- `loop-protect-disable-time` (time)

**Read-only arguments**

- `l2mtu` (num)
- `loop-protect-status` (enum: off | on | disabled)
