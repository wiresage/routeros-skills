# /ipv6/dhcp-server/option

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-server/option

Type: Directory

Additional options the DHCPv6 server can send, assigned with `dhcp-option` to a server or a binding, or grouped in option sets. For details, see [DHCPv6 Server](../../../guides/network-management/dhcp/dhcpv6-server.md).

**Arguments**

- `name` (string; mandatory): Name of the option, used where options are assigned.
- `code` (num; mandatory): DHCPv6 option code, for example 23 for DNS servers.
- `value` (string): Value of the option, in the same syntax as DHCP server option values. An IPv6 address in quotes is sent as 16 bytes, for example `'2001:db8::53'`.

**Read-only arguments**

- `raw-value` (string): The option value as it is sent, in hex.
