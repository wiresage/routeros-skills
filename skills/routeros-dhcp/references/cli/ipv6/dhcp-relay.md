# /ipv6/dhcp-relay

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-relay

Type: Directory

The DHCPv6 relay forwards DHCPv6 messages from clients on its interface to DHCPv6 servers, wrapped in Relay-Forward messages, and delivers the servers' Relay-Reply messages back to the clients. For an overview, see [DHCP Relay](../../guides/network-management/dhcp/relay.md).

**Flags**

- `X` (disabled): The relay is disabled.
- `I` (invalid): The relay configuration is invalid.

**Arguments**

- `name` (string; mandatory): Name of the relay.
- `interface` (iface_enum; mandatory): Interface on which the relay listens for messages from clients.
- `dhcp-server` (object { server: alt { interface-address: composite { address6: ip6Addr , interface: iface_enum } , address6: ip6Addr } }; mandatory): DHCPv6 servers to forward Relay-Forward messages to. A link-local address is given with its interface, for example `fe80::1%ether1`.
- `dhcp-options` (multi { array-id, option: enum }): Options (`/ipv6/dhcp-relay/option`) added to Relay-Forward messages. The Interface-ID option (18) is always added. Default: client_mac, the client link-layer address (option 79).
- `link-address` (ip6Addr): Address sent in the link-address field of Relay-Forward messages, which a server can use to identify the client's link. With `::`, no address is sent. Default: ::.
- `delay-threshold` (alt { const: enum (none) , time: time }): Minimum value of the elapsed-time field a message must have to be forwarded. With `none`, all messages are forwarded. Default: none.
- `store-relayed-bindings` (bool): Whether to keep the bindings found in the servers' replies and add routes to them through the client, so traffic to delegated prefixes behind the relay is routed. The bindings are listed in `/ipv6/dhcp-relay/routes`. Default: no.

## Commands

### /ipv6/dhcp-relay/monitor

Type: Command

Shows the counters of a DHCPv6 relay.

**Read-only arguments**

- `requests` (num): Number of client messages the relay forwarded to the servers.
- `responses` (num): Number of server replies the relay delivered to clients.

### /ipv6/dhcp-relay/reset-counters

Type: Command

Resets the request and response counters of all DHCPv6 relays.
