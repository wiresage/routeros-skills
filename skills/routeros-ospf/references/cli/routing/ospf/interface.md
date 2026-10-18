# /routing/ospf/interface

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/interface

Type: Directory

**Flags**

- `D`: dynamic
- `X`: disabled

**Arguments**

- `interface` (iface_enum; unset)
- `address` (address (flags=4i); unset)
- `area` (enum)
- `instance-id` (num; unset)
- `type` (enum: broadcast | nbma | ptp | ptp-unnumbered | ptmp | ptmp-broadcast | virtual-link): The OSPF network type on this interface. Note that if interface configuration does not exist, the default network type is 'ptp' on PtP interfaces and 'broadcast' on all other interfaces.
  - `broadcast` - Network type suitable for Ethernet and other multicast capable link layers. Elects designated router.
  - `nbma` - Non-Broadcast Multiple Access. Protocol packets are sent to each neighbor's unicast address. Requires manual configuration of neighbors. Elects designated router.
  - `ptp` - Suitable for networks that consist only of two nodes. Does not elect a designated router.
  - `ptmp` - Point-to-Multipoint. Easier to configure than NBMA because it requires no manual configuration of a neighbor. Does not elect a designated router. This is the most robust network type and as such suitable for wireless networks, if 'broadcast' mode does not work well enough for them
  - `ptp-unnumbered` - Works the same as ptp, except that the remote neighbor does not have an associated IP address to a specific PTP interface. For example, in case IP unnumbered is used on Cisco devices.
  - `virtual-link` - Interface for virtual link.
- `auth` (enum: simple | md5 | sha1 | sha256 | sha384 | sha512; unset)
- `auth-key` (string; unset)
- `auth-id` (num; unset)
- `cost` (num)
- `priority` (num)
- `passive` (switch)
- `use-bfd` (bool; unset)
- `retransmit-interval` (time)
- `transmit-delay` (time)
- `hello-interval` (time)
- `dead-interval` (time)
- `vlink-transit-area` (enum; unset): A non-backbone area the two routers have in common over which the virtual link will be established. Virtual links can not be established through stub areas.
- `vlink-neighbor-id` (ipAddr; unset): Specifies the **router-id** of the neighbor which should be connected over the virtual link.

**Read-only arguments**

- `state` (enum: down | loopback | ptp | passive | waiting | standby | dr-other | bdr | dr)
- `dr` (ipAddr)
- `bdr` (ipAddr)
- `vlink-remote-address` (address (flags=46))
