# /ipv6/dhcp-relay/routes

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-relay/routes

Type: Directory

Bindings found in the servers' replies by DHCPv6 relays with `store-relayed-bindings=yes`. The relay adds a route to each delegated prefix through the client. For details, see [DHCP Relay](../../../guides/network-management/dhcp/relay.md).

**Read-only arguments**

- `relay` (enum): DHCPv6 relay that saw the binding.
- `prefix` (ip6Prefix): Delegated prefix or assigned address.
- `peer-address` (ip6Addr): Address of the client, usually its link-local address, used as the gateway of the route.
- `life-time` (time): Lifetime of the binding.
- `last-seen` (time): Time since the relay last saw the binding in a reply.
