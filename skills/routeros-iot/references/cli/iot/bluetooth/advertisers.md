# /iot/bluetooth/advertisers

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/advertisers

Package: iot; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `min-interval` (num)
- `max-interval` (num)
- `own-address-type` (enum: public | random-static | rpa-fallback-to-public | rpa-fallback-to-random): Address type used in AdvA field
- `channel-map` (ubit (37, 38, 39))
- `phy` (enum: 1M | 2M | CODED)
- `legacy` (bool)
- `ad-structures` (multi { array-id, structure: enum })

**Read-only arguments**

- `device` (enum)
- `ad-size` (num)
