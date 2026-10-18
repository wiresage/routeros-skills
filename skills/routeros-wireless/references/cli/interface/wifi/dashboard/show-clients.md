# /interface/wifi/dashboard/show-clients

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/dashboard/show-clients

Type: Command

**Flags**

- `A`: active

**Arguments**

- `interface` (multi { array-id, interface: iface_enum }; unset)
- `address` (macAddr; unset)
- `bssid` (macAddr; unset)
- `time` (time; unset)
- `time-start` (date; unset)
- `time-end` (date; unset)
- `event` (enum: connected | disconnected | failed; unset)

**Read-only arguments**

- `address` (macAddr)
- `dhcp-address` (address)
- `dhcp-hostname` (string)
- `last-ap` (macAddr)
- `conn` (num)
- `disconn` (num)
- `fail` (num)
