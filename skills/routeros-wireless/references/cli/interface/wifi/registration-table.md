# /interface/wifi/registration-table

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/registration-table

Type: Directory

**Flags**

- `A`: authorized

**Read-only arguments**

- `interface` (iface_enum)
- `ssid` (string)
- `mac-address` (macAddr)
- `dhcp-address` (address)
- `dhcp-hostname` (string)
- `uptime` (time)
- `last-activity` (time)
- `signal` (num)
- `signal-per-link` (multi { array-id, signal-l: num })
- `auth-type` (enum: wpa2-eap | wpa2-psk | ft-eap | ft-wpa2-psk | wpa3-eap | wpa2-psk-sha2 | wpa3-psk | wpa3-psk-gd | ft-wpa3-psk | ft-wpa3-psk-gd | wpa3-eap-192 | ft-wpa3-eap-192 | owe | wpa-eap | wpa-psk | dpp)
- `mfp` (bool)
- `band` (multi { array-id, band: enum () })
- `mld-interfaces` (multi { array-id, iface: iface_enum })
- `mld-link-addresses` (multi { array-id, addr: macAddr })
- `tx-rate` (num)
- `rx-rate` (num)
- `tx-rate-per-link` (multi { array-id, tx-l-rate: num })
- `rx-rate-per-link` (multi { array-id, rx-l-rate: num })
- `packets` (composite { tx: num , rx: num })
- `tx-packets-per-link` (multi { array-id, tx-l-packets: num })
- `rx-packets-per-link` (multi { array-id, rx-l-packets: num })
- `bytes` (composite { tx: num , rx: num })
- `tx-bytes-per-link` (multi { array-id, tx-l-bytes: num })
- `rx-bytes-per-link` (multi { array-id, rx-l-bytes: num })
- `tx-bits-per-second` (num)
- `rx-bits-per-second` (num)
- `tx-bits-per-second-per-link` (multi { array-id, tx-l-bps: num })
- `rx-bits-per-second-per-link` (multi { array-id, rx-l-bps: num })
- `vlan-id` (num)
- `eap-identity` (string)
- `eap-username` (string)
