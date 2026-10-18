# /interface/wifi/cap

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/cap

Type: Settings Directory

**Arguments**

- `enabled` (enum: yes | no)
- `discovery-interfaces` (multi { array-id, interface: iface_enum }; unset)
- `certificate` (enum: request | none; unset)
- `caps-man-addresses` (multi { array-id, address: address (flags=46iD) }; unset)
- `caps-man-names` (multi { array-id, name: string }; unset)
- `caps-man-certificate-common-names` (multi { array-id, common-name: string }; unset)
- `lock-to-caps-man` (bool; unset)
- `slaves-static` (bool; unset)
- `mld-static` (bool; unset)
- `slaves-datapath` (enum; unset)
- `mld-datapath` (enum; unset)

**Read-only arguments**

- `requested-certificate` (enum: none)
- `locked-caps-man-common-name` (string)
- `current-caps-man-address` (address (flags=46mi))
- `current-caps-man-identity` (string)
