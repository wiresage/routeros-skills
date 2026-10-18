# /routing/ospf/interface-template

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/interface-template

Type: Directory

The interface template defines common network and interface matches and what parameters to assign to a matched interface.

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `area` (enum; mandatory): The OSPF area to which the matching interface will be associated.
- `interfaces` (object { interface: iface_enum }; unset): Matcher. Interfaces to match. Accepts specific interface names or the name of the interface list.
- `instance-id` (num)
- `networks` (object { network: address (flags=46/) }; unset): Matcher. The network prefix associated with the area. OSPF will be enabled on all interfaces that have at least one address falling within this range. Note that the network prefix of the address is used for this check (i.e. not the local address). For point-to-point interfaces, this means the address of the remote endpoint.
- `prefix-list` (enum; unset): Name of the address list containing networks that should be advertised to the v3 interface.
- `type` (enum: broadcast | nbma | ptp | ptp-unnumbered | ptmp | ptmp-broadcast): The OSPF network type on this interface. Note that if interface configuration does not exist, the default network type is 'ptp' on PtP interfaces and 'broadcast' on all other interfaces.
  - `broadcast` - Network type suitable for Ethernet and other multicast capable link layers. Elects designated router.
  - `nbma` - Non-Broadcast Multiple Access. Protocol packets are sent to each neighbor's unicast address. Requires manual configuration of neighbors. Elects designated router.
  - `ptp` - Suitable for networks that consist only of two nodes. Does not elect a designated router.
  - `ptmp` - Point-to-Multipoint. Easier to configure than NBMA because it requires no manual configuration of a neighbor. Does not elect a designated router. This is the most robust network type and as such suitable for wireless networks, if 'broadcast' mode does not work well enough for them
  - `ptp-unnumbered` - Works the same as ptp, except that the remote neighbor does not have an associated IP address to a specific PTP interface. For example, in case IP unnumbered is used on Cisco devices.
- `retransmit-interval` (time): Time interval after which the lost link state advertisement will be resent. When a router sends a link state advertisement (LSA) to its neighbor, the LSA is kept until the acknowledgment is received. If the acknowledgment was not received in time (see transmit-delay), the router will try to retransmit the LSA.
- `transmit-delay` (time): Link-state transmit delay is the estimated time it takes to transmit a link-state update packet on the interface.
- `hello-interval` (time): The interval between **HELLO** packets that the router sends out on this interface. The smaller this interval is, the faster topological changes will be detected; the tradeoff is more OSPF protocol traffic. This value must be the same for all the routers on a specific network, otherwise, adjacency between them will not form.
- `dead-interval` (time): Specifies the interval after which a neighbor is declared dead. This interval is advertised in hello packets. This value must be the same for all routers on a specific network, otherwise, adjacency between them will not form.
- `priority` (num): Router's priority. Used to determine the designated router in a broadcast network. The router with the highest priority value takes precedence. Priority value 0 means the router is not eligible to become a designated or backup designated router at all.

  Default value is 128, keep this in mind if you had strict priorities set for DR/BDR election.
- `cost` (num): Interface cost expressed as link state metric.
- `passive` (switch): If enabled, then the router does not send or receive OSPF traffic on the matching interfaces.
- `auth` (enum: simple | md5 | sha1 | sha256 | sha384 | sha512; unset): Specifies authentication method for OSPF protocol messages.

  - `simple` - plain text authentication.
  - `md5` - keyed Message Digest 5 authentication.
  - `sha*` - HMAC-SHA authentication RFC5709.

  If the parameter is unset, then authentication is not used.
- `auth-key` (string; unset): The authentication key to be used, should match on all the neighbors of the network segment.
- `auth-id` (num; unset): The key id is used to calculate a message digest (used when MD5 or SHA authentication is enabled). The value should match all OSPF routers from the same region.
- `use-bfd` (bool; unset)
