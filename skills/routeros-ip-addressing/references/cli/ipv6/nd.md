# /ipv6/nd

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/nd

Type: Directory

IPv6 Neighbor Discovery (ND) protocol is configured.

**Flags**

- `X`: disabled
- `I`: invalid
- `*`: default

**Arguments**

- `interface` (iface_enum): Interface on which to run neighbor discovery.
  -all - run ND on all running interfaces.
- `ra-interval` (super { min: time [3 .. 1250] , [max] -time [4 .. 1800] }): Minimum and maximum interval allowed between unsolicited multicast router advertisements from the interface.
- `ra-delay` (time): Minimum time between multicast router advertisements from the interface.
- `mtu` (alt { special: enum (unspecified) , value: num }): The MTU option in router advertisements ensures that all nodes on a link use the same MTU value when the link MTU is not well known.
  - **unspecified** - do not send the MTU option.
- `reachable-time` (alt { special: enum (unspecified) , value: time [ .. 3600] }): Time that RouterOS assumes a neighbor is reachable after receiving a reachability confirmation. Used by Neighbor Unreachability Detection (see Section 7.3 of [RFC 4861](https://tools.ietf.org/html/rfc4861)).
- `retransmit-interval` (alt { special: enum (unspecified) , value: time }): Time between retransmitted Neighbor Solicitation messages. Used by address resolution and Neighbor Unreachability Detection (see Sections 7.2 and 7.3 of [RFC 4861](https://tools.ietf.org/html/rfc4861)).
- `ra-lifetime` (alt { special: enum (none) , value: time [ .. 9000] }): Set the RA lifetime. A lifetime of 0 indicates that this router is not a default router. See Section 6.2.1 of [RFC 4861](https://tools.ietf.org/html/rfc4861).
- `ra-preference` (enum: low | medium | high): Specify the router preference communicated to IPv6 hosts in router advertisements. The `ra-preference` value helps hosts select a default router to reach a remote destination.
- `hop-limit` (alt { special: enum (unspecified) , value: num [ .. 255] }): Default value placed in the Hop Count field of the IPv6 header for outgoing unicast packets.
- `advertise-mac-address` (bool): When set, include the outgoing interface's link-layer address in router advertisements.
- `advertise-dns` (enum: no | yes | self): Redistribute DNS server information using RADVD.

  - `no` - do not advertise DNS servers.
  - `yes` - advertise DNS servers installed on the router.
  - `self` - advertise the interface link-local address as the DNS service provider.
- `managed-address-configuration` (bool): Indicates whether hosts should use stateful autoconfiguration (DHCPv6) to obtain addresses. See [RFC 3315](https://tools.ietf.org/html/rfc3315).
- `other-configuration` (bool): Indicates whether hosts should use stateful autoconfiguration to obtain additional information, excluding addresses. See [RFC 3315](https://tools.ietf.org/html/rfc3315).
- `dns` (multi { address: address (flags=6) }): Specify one or more IPv6 addresses that hosts receive for DNS server configuration.
- `pref64` (object { pref64: ip6Prefix }): Specify one or more IPv6 prefixes within /32, /40, /48, /56, /64, or /96 subnets that hosts receive as NAT64 prefixes.
