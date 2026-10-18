# /interface/wifi/access-list

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/access-list

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `mac-address` (macAddr; unset)
- `mac-address-mask` (macAddr; unset)
- `interface` (iface_enum; unset)
- `signal-range` (composite { min: num [-120 .. 120] , max: num [-120 .. 120] }; unset)
- `allow-signal-out-of-range` (alt { signal-out-of-range-always: enum (always) , signal-out-of-range-time: time }; unset)
- `ssid-regexp` (string; unset)
- `time` (super { start: time [0 .. 86400] , [end] -time [0 .. 86400] }; unset)
- `days` (ubit (sun, mon, tue, wed, thu, fri, sat); unset)
- `action` (enum: accept | reject | query-radius; unset)
- `passphrase` (string; unset)
- `multi-passphrase-group` (enum; unset)
- `radius-accounting` (bool; unset)
- `client-isolation` (bool; unset)
- `vlan-id` (num; unset)

**Read-only arguments**

- `last-logged-in` (date; unset)
- `last-logged-out` (date; unset)
- `match-count` (num; unset)
