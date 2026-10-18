# /iot/bluetooth/scanners

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/scanners

Package: iot; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `type` (enum: passive | active)
- `interval` (num)
- `window` (num)
- `own-address-type` (enum: public | random-static | rpa-fallback-to-public | rpa-fallback-to-random): Address type used in scan requests
- `filter-policy` (enum: default | whitelist)
- `filter-duplicates` (enum: off | keep-oldest | keep-newest | keep-unique): Discard duplicate advertisements from the same advertiser
- `phy` (enum: 1M | 2M | CODED)

**Read-only arguments**

- `device` (enum)
