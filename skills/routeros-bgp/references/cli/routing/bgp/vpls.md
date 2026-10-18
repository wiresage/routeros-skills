# /routing/bgp/vpls

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/vpls

Conditions: !smips; Type: Directory

This menu lists all the configured BGP-based VPLS instances. These instances allow the router to advertise VPLS BGP NLRI and indicate that the router belongs to a specific customer VPLS network.

MP-BGP-based autodiscovery and signaling (RFC 4761).

Cisco VPLS BGP-based auto-discovery (draft-ietf-l2vpn-signaling-08).

Support for multiple import/export route target extended communities for BGP-based VPLS (both, RFC 4761 and draft-ietf-l2vpn-signaling-08).

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `name` (string; unset)
- `vrf` (enum; unset)
- `rd` (address (flags=R); unset): Specifies the value that gets attached to VPLS NLRI so that receiving routers can distinguish advertisements that may otherwise look the same. This implies that a unique route-distinguisher for every VPLS must be used. It is not necessary to use the same route distinguisher for some VPLS on all routers forming that VPLS as distinguisher is not used for determining if some BGP NLRI is related to a particular VPLS (Route Target attribute is used for this), but it is mandatory to have different distinguishers for different VPLSes. Accepts 3 types of formats. [Read more>>](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/route-distinguisher-and-route-target)
- `site-id` (num; unset): Unique site identifier. Each site must have a unique site-id. A parameter must be set for RFC 4761 style VPLS signaling.
- `cisco-id` (address; unset): Unique identifier. A parameter must be set for cisco-style VPLS signaling. In most cases this should not be used, any modern software supports RFC 4761 style signaling (see site-id parameter). Parameter is a merge of l2-router-id and RD, for example: 10.155.155.1&6550:123
- `import-route-targets` (multi { array-id, rt: address (flags=R) }; unset): The setting is used to determine if BGP NLRI is related to a particular VPLS, by comparing route targets received from BGP NLRI.
- `export-route-targets` (multi { array-id, rt: address (flags=R) }; unset): The setting is used to tag BGP NLRI with one or more route targets which on the remote side is used by `import-route-targets`.
- `local-pref` (num; unset)
- `interface-list` (enum; unset)
- `pw-type` (enum: tagged-ethernet | raw-ethernet | vpls; unset): Pseudowire type (RFC 4447 Section 5.2). By default, `raw-ethernet` is used.
- `pw-l2mtu` (num; unset): L2MTU value advertised to a remote peer (RFC 4447 Section 5.2).
- `pw-control-word` (enum: default | enabled | disabled; unset): Enables or disables Control Word usage (RFC 4623 Section 4). Default values for regular and Cisco-style VPLS tunnels differ. Cisco-style by default has Control Word usage disabled. Read more in the [VPLS Control Word](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/mpls/vpls/control-word) article.
- `bridge` (iface_enum; unset): Bridge the VPLS interface belongs to.
- `bridge-cost` (num; unset): Cost of the bridge port.
- `bridge-horizon` (num; unset): When set to `none`, bridge `horizon` is not used.
- `bridge-pvid` (num; unset): Port VLAN ID (pvid) assigned to a dynamically bridged interface. Applies only when bridge `vlan-filtering` is set to `yes`.

**Read-only arguments**

- `current-peers` (string)
