# /routing/rip/instance

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/rip/instance

Type: Directory

The maximum metric of a RIP route is 15. A metric higher than 15 is considered 'infinity' and routes with such a metric are considered unreachable. Thus RIP cannot be used on networks with more than 15 hops between any two routers, and using redistribute metrics larger than 1 further reduces this maximum hop count.

**Flags**

- `X`: disabled

**Arguments**

- `name` (string): Name of the instance.
- `vrf` (enum): Name of the VRF to be used for connections.
- `afi` (enum: ip | ipv6)
- `in-filter-chain` (enum; unset)
- `out-filter-select` (enum; unset)
- `out-filter-chain` (enum; unset)
- `redistribute` (ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac); unset)
- `originate-default` (enum: never | always | if-installed; unset): Whether to originate default route.
- `route-timeout` (num): Specifies the time interval after which the route is considered invalid.
- `route-gc-timeout` (num)
- `update-interval` (num)
- `routing-table` (enum; unset): Routing table name where routes will be installed.
