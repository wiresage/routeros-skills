# /interface/wireless/access-list

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/access-list

Package: wireless-rep; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `mac-address` (macAddr)
- `interface` (iface_enum)
- `signal-range` (composite { min: num [-120 .. 120] , max: num [-120 .. 120] })
- `allow-signal-out-of-range` (alt { signal-out-of-range-always: enum (always) , signal-out-of-range-time: time })
- `authentication` (bool)
- `forwarding` (bool)
- `ap-tx-limit` (num)
- `client-tx-limit` (num)
- `private-algo` (enum: none | 40bit-wep | 104bit-wep | aes-ccm | tkip)
- `private-key` (string)
- `private-pre-shared-key` (string)
- `time` (super { start: time [0 .. 86400] , [end] -time [0 .. 86400] , [day] ,ubit (sun, mon, tue, wed, thu, fri, sat) })
- `management-protection-key` (string)
- `vlan-mode` (enum: default | no-tag | use-tag | use-service-tag)
- `vlan-id` (num)
