# /routing/igmp-proxy/interface

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/igmp-proxy/interface

Type: Directory

Configure what interfaces will participate as IGMP proxy interfaces on the router. If an interface is not configured as an IGMP proxy interface, then all IGMP traffic received on it will be ignored.

**Flags**

- `X`: disabled
- `I`: inactive
- `D`: dynamic

**Arguments**

- `interface` (iface_enum): Name of the interface.
- `upstream` (bool): The interface is called "upstream" if it's in the direction of the root of the multicast tree. An IGMP forwarding router must have exactly one upstream interface configured. The upstream interface is used to send out IGMP membership requests.
- `threshold` (num): Minimal TTL. Packets received with a lower TTL value are ignored
- `alternative-subnets` (multi { numbers: super { as: ipAddr , [netmask] /num } }): By default, only packets from directly attached subnets are accepted. This parameter can be used to specify a list of alternative valid packet source subnets, both for data and IGMP packets. Has an effect only on the upstream interface. Should be used when the source of multicast data often is in a different IP network.
- `robustness` (num): The robustness value for this interface. Overrides the global robustness setting in the `/routing/igmp-proxy` menu.
- `query-interval` (time): How often to send out IGMP Query messages over this interface. Overrides the global query-interval setting in the `/routing/igmp-proxy` menu.
- `query-response-interval` (time): How long to wait for responses to an IGMP Query message on this interface. Overrides the global query-response-interval setting in the `/routing/igmp-proxy` menu.
- `last-member-query-interval` (time): The timeout for group-specific queries on this interface. Overrides the global last-member-query-interval setting in the `/routing/igmp-proxy` menu.

**Read-only arguments**

- `state.querier` (bool): Whether this interface is currently the elected IGMP querier.
- `state.source-ip-address` (ipAddr): The source IP address used by this interface for IGMP messages.
- `state.rx-bytes` (num): The total amount of received multicast traffic on the interface, in bytes.
- `state.rx-packets` (num): The total amount of received multicast traffic on the interface, in packets.
- `state.tx-bytes` (num): The total amount of transmitted multicast traffic on the interface, in bytes.
- `state.tx-packets` (num): The total amount of transmitted multicast traffic on the interface, in packets.
- `state.robustness` (num): The effective robustness value in use on the interface. When this interface is not the elected querier, it adopts the robustness value announced by the elected querier in its IGMP queries.
- `state.query-interval` (time): The effective query interval in use on the interface. When this interface is not the elected querier, it adopts the query interval announced by the elected querier in its IGMP queries.
