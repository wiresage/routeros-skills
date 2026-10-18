# /interface/dot1x/server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/dot1x/server

Conditions: !smips; Type: Directory

**Flags**

- `I`: inactive
- `X`: disabled

**Arguments**

- `interface` (iface_enum; mandatory)
- `accounting` (bool)
- `interim-update` (time)
- `auth-types` (ubit (dot1x, mac-auth))
- `mac-auth-mode` (enum: mac-as-username | mac-as-username-and-password)
- `radius-mac-format` (enum (XX:XX:XX:XX:XX:XX | XX-XX-XX-XX-XX-XX | XXXXXXXXXXXX | xx:xx:xx:xx:xx:xx | xx-xx-xx-xx-xx-xx | xxxxxxxxxxxx) { XX:XX:XX:XX:XX:XX:0, XX-XX-XX-XX-XX-XX:3, XXXXXXXXXXXX:5, xx:xx:xx:xx:xx:xx:7, xx-xx-xx-xx-xx-xx:10, xxxxxxxxxxxx:12 })
- `reauth-timeout` (time; deprecated)
- `reauth-period` (time)
- `auth-timeout` (time)
- `retrans-timeout` (time)
- `reject-vlan-id` (num)
- `guest-vlan-id` (num)
- `server-fail-vlan-id` (num)
