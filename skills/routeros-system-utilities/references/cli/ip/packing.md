# /ip/packing

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/packing

Type: Directory

Packing rules aggregate the outgoing packets of an interface into larger packets, optionally with compression, and unpack them on the receiving side. Both routers need neighbor discovery on the interface. TCP connections that the router opens over a packed link fail, see [IP Packing](../../guides/system-information-and-utilities/ip-packing.md).

**Flags**

- `X` (disabled): Packing rule is disabled.

**Arguments**

- `interface` (iface_enum; mandatory): Interface on which to aggregate or compress outgoing packets and unpack incoming ones. The router packs only toward a neighbor that announces unpacking through neighbor discovery, so discovery must run on this interface on both routers. Both routers must be configured symmetrically.
- `packing` (enum (none | simple | compress-headers | compress-all) { none:0x00, simple:0x01, compress-headers:0x03, compress-all:0x07 }): Action to perform on outgoing packets:
  - `none` (default) - Send packets as they are.
  - `simple` - Aggregate packets only.
  - `compress-headers` - Aggregate packets and compress their headers; leave the payload unchanged.
  - `compress-all` - Aggregate packets and compress headers and payload.
- `unpacking` (enum (none | simple | compress-headers | compress-all) { none:0x00, simple:0x01, compress-headers:0x03, compress-all:0x07 }): Action to perform on incoming packets. The router announces this setting to its neighbors (the `unpack` field in `/ip/neighbor`):
  - `none` (default) - Do nothing with received packets.
  - `simple` - Unpack aggregated packets.
  - `compress-headers` - Unpack aggregated packets and decompress headers.
  - `compress-all` - Unpack aggregated packets and decompress headers and payload.
- `aggregated-size` (num): Size in bytes that packing tries to reach before it sends an aggregated packet. Packing waits to fill packets, so it adds delay on the link. Range: 20..16384. Default: 1500.
