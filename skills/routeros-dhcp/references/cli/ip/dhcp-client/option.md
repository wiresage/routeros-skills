# /ip/dhcp-client/option

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-client/option

Type: Directory

Options the DHCP client can send to the DHCP server. A client sends the options listed in its `dhcp-options` property. For details, see [DHCP Client](../../../guides/network-management/dhcp/client.md).

**Flags**

- `*` (default): Predefined option.

**Arguments**

- `name` (string; mandatory): Name of the option, used in the `dhcp-options` property of the client.
- `code` (alt { number: num [1 .. 254] , option: enum (hostname | vendor-specific | vendor-class-id | client-id) }; mandatory): DHCP option code (1-254), or one of the names `hostname` (12), `vendor-specific` (43), `vendor-class-id` (60) or `client-id` (61).
- `value` (string): Value of the option, in the same syntax as DHCP server option values. The value can contain these variables:
  - `$(HOSTNAME)` - The router's identity.
  - `$(CLIENT_MAC)` - MAC address of the client interface.
  - `$(CLIENT_DUID)` - The router's DUID, the same DUID the DHCPv6 client uses.

**Read-only arguments**

- `raw-value` (string): The option value as it is sent, in hex.
