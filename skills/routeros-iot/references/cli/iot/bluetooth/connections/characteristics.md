# /iot/bluetooth/connections/characteristics

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/connections/characteristics

Package: iot; Type: Directory

**Read-only arguments**

- `name` (string)
- `uuid` (string)
- `handle` (num)
- `service-name` (string)
- `service-uuid` (string)
- `props` (multi { array-id, props: enum (bcast | read | write-no-resp | write | notify | indicate | write-signed | ext) { bcast:0x01, read:0x02, write-no-resp:0x04, write:0x08, notify:0x10, indicate:0x20, write-signed:0x40, ext:0x80 } })
- `pdev` (enum)
