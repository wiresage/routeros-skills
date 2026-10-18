# /interface/wireless/cap

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/cap

Package: wireless-rep; Type: Settings Directory

**Arguments**

- `enabled` (bool)
- `interfaces` (multi { array-id, interface: iface_enum })
- `certificate` (enum: request | none)
- `lock-to-caps-man` (bool)
- `discovery-interfaces` (multi { array-id, interface: iface_enum })
- `caps-man-addresses` (multi { array-id, address: ip6Addr })
- `caps-man-names` (multi { array-id, name: string })
- `caps-man-certificate-common-names` (multi { array-id, common-name: string })
- `bridge` (iface_enum { none:0xffffffff })
- `static-virtual` (bool)

**Read-only arguments**

- `requested-certificate` (enum: none)
- `locked-caps-man-common-name` (string)
