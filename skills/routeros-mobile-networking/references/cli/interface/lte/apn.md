# /interface/lte/apn

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/lte/apn

Conditions: !smips; Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string)
- `apn` (string; mandatory)
- `use-peer-dns` (bool)
- `use-network-apn` (bool): in LTE mode use APN provided by the network
- `add-default-route` (bool)
- `default-route-distance` (num)
- `ip-type` (enum: ipv4 | ipv6 | auto): requested PDN type
- `authentication` (enum: none | pap | chap)
- `user` (string)
- `password` (string)
- `passthrough-interface` (iface_enum)
- `passthrough-mac` (alt { auto: enum (static | auto) , passthrough-peer: macAddr }): auto will learn MAC from first packet
- `passthrough-subnet-size` (alt { subnet-enum: enum (auto | 32) , subnet-size: num [16 .. 32] })
- `ipv6-interface` (iface_enum): interface on which to advertise IPv6 prefix
