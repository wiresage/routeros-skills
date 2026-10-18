# /interface/vpls

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/vpls

Conditions: !smips; Type: Directory

List of all VPLS interfaces. This menu also shows dynamically created BGP-based VPLS interfaces.

**Flags**

- `X`: disabled
- `R`: running
- `D`: dynamic
- `B`: bgp-signaled
- `C`: cisco-bgp-signaled

**Arguments**

- `name` (string): Name of the interface.
- `mtu` (num): Layer 3 Maximum Transmission Unit.
- `mac-address` (macAddr): Static MAC address of the interface. Automatically generated when not set.
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp): Address Resolution Protocol.
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time }): Time until an ARP entry expires. Set to `auto` to use the interface-type default value.
- `disable-running-check` (bool): Specifies whether to detect if an interface is running. If set to `no`, the interface will always have the `running` flag.
- `peer` (address (flags=46v); mandatory): The IP address of the remote peer (RFC 4762 Section 3.1).
- `vpls-id` (address (flags=R); unset): A unique number that identifies the VPLS tunnel. Encoding is a 2byte+4byte or 4byte+2byte number (RFC 4762 Section 3.2).
- `cisco-static-id` (num; unset): Cisco-style VPLS tunnel ID (RFC 4447 FEC type 0x80).
- `pw-type` (enum: tagged-ethernet | raw-ethernet | vpls; unset): Pseudowire type (RFC 4447 Section 5.2). By default, `raw-ethernet` is used.
- `pw-l2mtu` (num; unset): L2MTU value advertised to a remote peer (RFC 4447 Section 5.2).
- `pw-control-word` (enum: default | enabled | disabled; unset): Enables or disables Control Word usage (RFC 4623 Section 4). Default values for regular and Cisco-style VPLS tunnels differ. Cisco-style by default has Control Word usage disabled. Read more in the [VPLS Control Word](../../guides/user-guides/routing-and-networking-protocols/mpls/vpls/control-word.md) article.
- `bridge` (iface_enum; unset): Bridge the VPLS interface belongs to.
- `bridge-cost` (num; unset): Cost of the bridge port.
- `bridge-horizon` (num; unset): When set to `none`, bridge `horizon` is not used.
- `bridge-pvid` (num; unset): Port VLAN ID (pvid) assigned to a dynamically bridged interface. Applies only when bridge `vlan-filtering` is set to `yes`.

**Read-only arguments**

- `bgp-vpls` (enum): Name of the [BGP VPLS](https://manual.mikrotik.com/docs/cli-reference/routing/bgp/vpls) instance used to create a dynamic VPLS interface (RFC 4761 Section 3.2).
- `bgp-vpls-prfx` (string): Prefix of the [BGP VPLS](https://manual.mikrotik.com/docs/cli-reference/routing/bgp/vpls) instance used to create a dynamic VPLS interface (RFC 4761 Section 3.2).

## Commands

### /interface/vpls/monitor

Conditions: !smips; Type: Command

Command displays the current VPLS interface status.

For example:

```ros
[admin@10.0.11.23] /interface/vpls> monitor vpls2
remote-label: 800000
local-label: 43
remote-status:
transport: 10.255.11.201/32
transport-nexthop: 10.0.11.201
imposed-labels: 800000
```

**Read-only arguments**

- `remote-label` (num): MPLS label assigned by the remote peer for this pseudowire (RFC 4447 Section 5.1).
- `local-label` (num): MPLS label assigned locally for this pseudowire (RFC 4447 Section 5.1).
- `remote-status` (ubit (not-forwarding, attachment-circuit-rx-fault, attachment-circuit-tx-fault, pw-rx-fault, pw-tx-fault)): Pseudowire status received from the remote peer via LDP status signaling (RFC 4447 Section 5.4).
- `remote-group` (num): Group ID of the remote peer, used for LDP status withdrawal aggregation (RFC 4447 Section 5.3).
- `te-tunnel` (enum): Name of the transport interface. Shown when VPLS is running over a [Traffic Engineering](../../guides/user-guides/routing-and-networking-protocols/mpls/traffic-eng.md) tunnel.
- `nexthops` (object { label: enum (expl-null | alert | expl-null6 | impl-null) , nh: address , interface: iface_enum }): Transport nexthops in use.
