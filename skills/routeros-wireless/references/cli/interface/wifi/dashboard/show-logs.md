# /interface/wifi/dashboard/show-logs

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/dashboard/show-logs

Type: Command

**Arguments**

- `interface` (multi { array-id, interface: iface_enum }; unset)
- `address` (macAddr; unset)
- `bssid` (macAddr; unset)
- `time` (time; unset)
- `time-start` (date; unset)
- `time-end` (date; unset)
- `event` (enum: connected | disconnected | failed; unset)

**Read-only arguments**

- `time` (date)
- `address` (macAddr)
- `event` (enum: connected | disconnected | failed)
- `bssid` (macAddr)
- `signal` (num)
- `auth-type` (enum: wpa2-eap | wpa2-psk | ft-eap | ft-wpa2-psk | wpa3-eap | wpa2-psk-sha2 | wpa3-psk | wpa3-psk-gd | ft-wpa3-psk | ft-wpa3-psk-gd | wpa3-eap-192 | ft-wpa3-eap-192 | owe | wpa-eap | wpa-psk | dpp)
- `tx-bytes` (num)
- `rx-bytes` (num)
- `reason` (string)
