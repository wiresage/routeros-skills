# /ip/tftp/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/tftp/settings

Type: Settings Directory

Settings of the TFTP server. See [TFTP](../../../guides/system-information-and-utilities/tftp.md).

**Arguments**

- `max-block-size` (enum: 512 | 1454 | 4096 | 8192): Largest block size the router agrees to when a client asks for one (the `blksize` option); a client that asks for more gets this size. Clients that do not ask use 512 bytes. Values: `512`, `1454`, `4096`, `8192`. Default: 4096.
- `vrf` (enum): VRF the TFTP server listens in. Default: main.
