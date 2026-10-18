# /ipv6/dhcp-relay/option

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-relay/option

Type: Directory

Options a DHCPv6 relay can add to the Relay-Forward messages it sends. A relay adds the options listed in its `dhcp-options` property. For details, see [DHCP Relay](../../../guides/network-management/dhcp/relay.md).

**Flags**

- `*` (default): Predefined option.

**Arguments**

- `name` (string; mandatory): Name of the option, used in the `dhcp-options` property of the relay.
- `code` (num; mandatory): DHCPv6 option code.
- `value` (string): Value of the option, in the same syntax as DHCP server option values. The predefined `client_mac` option (code 79) uses `0x0001$(CLIENT_MAC)`, the link-layer type Ethernet followed by the MAC address of the client.
- `only-if-mac-available` (bool): Whether to add the option only when the message came directly from a client (not from another relay) and the client's MAC address is known.

**Read-only arguments**

- `raw-value` (string): The option value as it is sent, in hex.
