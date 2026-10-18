# /caps-man/provisioning

> Source: https://manual.mikrotik.com/docs/cli-reference/caps-man/provisioning

Package: wireless-rep; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `radio-mac` (macAddr)
- `hw-supported-modes` (multi { array-id, hw-supported-mode: enum (a | a-turbo | an | ac | b | g | g-turbo | gn) { a:1, a-turbo:2, an:3, ac:5, b:0x11, g:0x12, g-turbo:0x13, gn:0x14 } })
- `identity-regexp` (string)
- `common-name-regexp` (string)
- `ip-address-ranges` (multi { ip-address-range: ipRange })
- `action` (enum: none | create-enabled | create-disabled | create-dynamic-enabled)
- `master-configuration` (enum)
- `slave-configurations` (multi { array-id, slave-configuration: enum })
- `name-format` (enum: cap | prefix | identity | prefix-identity)
- `name-prefix` (string)
