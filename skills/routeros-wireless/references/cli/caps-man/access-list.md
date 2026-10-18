# /caps-man/access-list

> Source: https://manual.mikrotik.com/docs/cli-reference/caps-man/access-list

Package: wireless-rep; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `mac-address` (macAddr; unset)
- `mac-address-mask` (macAddr; unset)
- `interface` (iface_enum; unset)
- `signal-range` (composite { min: num [-120 .. 120] , max: num [-120 .. 120] }; unset)
- `allow-signal-out-of-range` (alt { signal-out-of-range-always: enum (always) , signal-out-of-range-time: time }; unset)
- `ssid-regexp` (string; unset)
- `time` (super { start: time [0 .. 86400] , [end] -time [0 .. 86400] , [day] ,ubit (sun, mon, tue, wed, thu, fri, sat) }; unset)
- `action` (enum: accept | reject | query-radius; unset)
- `ap-tx-limit` (num; unset)
- `client-tx-limit` (num; unset)
- `private-passphrase` (string; unset)
- `radius-accounting` (bool; unset)
- `client-to-client-forwarding` (bool; unset)
- `vlan-mode` (enum: no-tag | use-tag | use-service-tag; unset)
- `vlan-id` (num; unset)
