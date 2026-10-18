# /routing/rip/interface-template

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/rip/interface-template

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `instance` (enum; mandatory)
- `interfaces` (object { interface: iface_enum }; unset)
- `source-addresses` (object { address: address (flags=46) }; unset)
- `cost` (num)
- `split-horizon` (bool)
- `poison-reverse` (bool)
- `key-chain` (enum; unset): Name of the key-chain which contains the MD5 key. Should be set only when MD5 authentication is needed.
- `password` (string; unset): Password for plain-text authentication. Should be set only when plain-text authentication is needed.
- `mode` (enum: passive | strict; unset)
- `use-bfd` (bool; unset)
