# /ipv6/dhcp-client/option

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-client/option

Type: Directory

Options the DHCPv6 client can send to the DHCPv6 server. A client sends the options listed in its `dhcp-options` property. For details, see [DHCPv6 Client](../../../guides/network-management/dhcp/dhcpv6-client.md).

**Flags**

- `*` (default): Predefined option.

**Arguments**

- `name` (string; mandatory): Name of the option, used in the `dhcp-options` property of the client.
- `code` (num; mandatory): DHCPv6 option code.
- `value` (string): Value of the option, in the same syntax as DHCP server option values. The predefined `fqdn` option uses the variables `$(HOSTNAME)` (the router's identity) and `$(HOSTNAME_LEN)` (its length): `0x00$(HOSTNAME_LEN)$(HOSTNAME)`.

**Read-only arguments**

- `raw-value` (string): The option value as it is sent, in hex.
