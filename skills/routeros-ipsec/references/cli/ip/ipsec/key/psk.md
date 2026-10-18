# /ip/ipsec/key/psk

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/key/psk

Type: Directory

**Arguments**

- `peer` (enum; mandatory): Peer name to associate the PSK with.
- `id` (string; mandatory): Peer identifier string.
- `key` (string; mandatory): Pre-shared key value.

## Commands

### /ip/ipsec/key/psk/generate

Type: Command

**Arguments**

- `peer` (enum): Peer name to generate a PSK for.
- `size` (num): Key size in bytes.
- `count` (num): Number of keys to generate.
