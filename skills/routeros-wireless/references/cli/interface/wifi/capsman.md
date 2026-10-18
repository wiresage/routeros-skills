# /interface/wifi/capsman

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/capsman

Type: Settings Directory

**Arguments**

- `enabled` (enum: yes | no)
- `interfaces` (multi { array-id, interface: iface_enum }; unset)
- `ca-certificate` (enum: auto | none; unset)
- `certificate` (enum: auto; unset)
- `require-peer-certificate` (bool; unset)
- `package-path` (string; unset)
- `upgrade-policy` (enum: none | suggest-same-version | require-same-version; unset)

**Read-only arguments**

- `generated-ca-certificate` (enum: none)
- `generated-certificate` (enum: none)
