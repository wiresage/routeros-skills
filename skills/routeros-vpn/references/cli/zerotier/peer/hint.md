# /zerotier/peer/hint

> Source: https://manual.mikrotik.com/docs/cli-reference/zerotier/peer/hint

Package: zerotier; Type: Directory

**Flags**

- `X` (disabled): Whether an item is disabled.

**Arguments**

- `instance` (enum; mandatory): ZeroTier instance name.
- `identity` (string; mandatory): ZeroTier identity of the peer.
- `addresses` (multi { array-id, array-id, address: composite { addr: address (flags=46) , port: num [1 .. 65535] } }; mandatory): List of IP addresses and ports for the peer.
