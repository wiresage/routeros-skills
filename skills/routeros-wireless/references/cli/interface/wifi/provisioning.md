# /interface/wifi/provisioning

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/provisioning

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `radio-mac` (macAddr; unset)
- `identity-regexp` (string; unset)
- `common-name-regexp` (string; unset)
- `address-ranges` (object { address-range: super { address-range-start: address (flags=46) , [address-range-end] -address (flags=46) } }; unset)
- `supported-bands` (multi { array-id, supported-band: enum () }; unset)
- `supported-hw-caps` (multi { array-id, supported-hw-cap: enum () }; unset)
- `action` (enum: none | create-enabled | create-disabled | create-dynamic-enabled | use-network-config; mandatory)
- `master-configuration` (enum; unset)
- `slave-configurations` (multi { array-id, slave-configuration: enum }; unset)
- `multi-link-mode` (enum: auto | disabled | master | all; unset)
- `name-format` (string)
- `slave-name-format` (string)
