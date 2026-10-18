# /user-manager/attribute

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/attribute

Package: userman-5; Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string; mandatory)
- `vendor-id` (enum: standard | Cisco | Microsoft | Mikrotik)
- `type-id` (num; mandatory)
- `value-type` (enum: ip-address | string | uint32 | hex | ip6-prefix | macro; mandatory)
- `packet-types` (ubit (access-accept, access-challenge))

**Read-only arguments**

- `default-name` (string)
- `standard-name` (string)
