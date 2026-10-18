# /ip/dhcp-server/option/sets

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/option/sets

Type: Directory

Groups of DHCP server options that can be assigned together with `dhcp-option-set` to a network, a server, a lease or a matcher. For details, see [DHCP Server](../../../../guides/network-management/dhcp/server.md).

**Arguments**

- `name` (string; mandatory): Name of the option set.
- `options` (multi { array-id, option: enum }; mandatory): Options (`/ip/dhcp-server/option`) in the set.
