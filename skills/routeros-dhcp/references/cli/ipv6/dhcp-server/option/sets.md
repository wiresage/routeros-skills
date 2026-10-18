# /ipv6/dhcp-server/option/sets

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-server/option/sets

Type: Directory

Groups of DHCPv6 server options that can be assigned together. For details, see [DHCPv6 Server](../../../../guides/network-management/dhcp/dhcpv6-server.md).

**Arguments**

- `name` (string; mandatory): Name of the option set.
- `options` (multi { array-id, option: enum }; mandatory): Options (`/ipv6/dhcp-server/option`) in the set.
