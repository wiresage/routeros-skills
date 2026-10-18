# /interface/ethernet/switch/rule

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/rule

Syscap: rbswitch; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic

**Arguments**

- `switch` (enum; mandatory): Matching the switch group on which the rule will apply.
- `ports` (multi { array-id, port: enum }; syscap=!crs_prestera): Matching switch interfaces where the rule will apply to incoming traffic. Multiple ports and [hardware-offloaded bonding](../../../../guides/bridging-and-switching/l3-hardware-offloading.md#l3hw-feature-support) interfaces can be selected. Note that the `switch1-cpu` port cannot be selected. If `ports` property is left empty, the rule will apply to all switch interfaces.
- `src-mac-address` (super { address: macAddr , [mask] /macAddr }): Matching source MAC address and mask.
- `dst-mac-address` (super { address: macAddr , [mask] /macAddr }): Matching destination MAC address and mask.
- `mac-protocol` (alt { protocol-name: enum () , protocol-number: num [ .. 65535] }): Matching a particular MAC protocol specified by protocol name or number (skips VLAN tags if any).
- `vlan-header` (enum: not-present | present): Matching VLAN header, whether the VLAN header is present or not. Requires `vlan-filtering=yes`.
- `vlan-id` (num): Matching VLAN ID. Requires `vlan-filtering=yes`.
- `vlan-priority` (num): Matching VLAN priority (priority code point).
- `src-address` (super { address: ipAddr , [mask] /alt { bitmask: ipAddr , netmask: num [ .. 32] } }): Matching source IPv4 address and mask. If `mac-protocol=arp` is specified, matches the source IP in ARP packets. Without `mac-protocol`, matches only IPv4 packets.
- `dst-address` (super { address: ipAddr , [mask] /alt { bitmask: ipAddr , netmask: num [ .. 32] } }): Matching destination IPv4 address and mask. If `mac-protocol=arp` is specified, matches the destination IP in ARP packets. Without `mac-protocol`, matches only IPv4 packets.
- `protocol` (alt { protocol-name: enum () , protocol-number: num [ .. 255] }): Matching a particular IP protocol specified by protocol name or number. Only applies to IPv4 packets if `mac-protocol` is not specified. To match certain IPv6 protocols, use the `mac-protocol=ipv6` setting.
- `src-port` (range): Matching source protocol port number (applies to IPv4 and IPv6 packets if `mac-protocol` is not specified).
- `dst-port` (range): Matching destination protocol port number or range (applies to IPv4 and IPv6 packets if mac-protocol is not specified).
- `dscp` (num): Matching the DSCP field of the packet (only applies to IPv4 packets).
- `src-address6` (super { address: ip6Addr , [mask] /alt { bitmask: ip6Addr , netmask: num } }): Matching source IPv6 address and mask.
- `dst-address6` (super { address: ip6Addr , [mask] /alt { bitmask: ip6Addr , netmask: num } }): Matching destination IPv6 address and mask.
- `traffic-class` (num): Matching IPv6 traffic class.
- `flow-label` (num): Matching IPv6 flow label.
- `copy-to-cpu` (bool): Clones the matching packet and sends it to the CPU.
- `redirect-to-cpu` (bool): Changes the destination port of a matching packet to the switch CPU.
- `mirror` (bool; syscap=switch-mirror-prestera): Clones the matching packet and sends it to the `mirror-target` port.
- `new-dst-ports` (multi { array-id, port: alt { port: enum , bond: iface_enum } }): Changes the destination port as specified, multiple ports allowed, including a switch CPU port.
  - If the setting is left empty (e.g. `new-dst-ports=""`), the packet will be dropped;
  - If a port or [hardware-offloaded bonding](../../../../guides/bridging-and-switching/marvell-prestera-switch-chip-features.md#bonding) interface is specified, the packet will be redirected to that port. Only a single port or bond interface is supported;
  - if you use the `all` argument, packet will be allowed to pass through to the egress processing without being dropped;
  - If this parameter is not used, the packet will be accepted as is.
- `mirror-ports` (multi { array-id, port: enum }; syscap=switch-mv88e6xxx): Selects multiple mirroring target ports, only available on the **88E6393X** switch chip. Matched packets in the ACL rule will be copied and sent to selected ports.
- `new-qos-profile` (enum; syscap=crs_prestera): The name of the QoS profile to assign to the matched packets.
- `keep-qos-fields` (bool; syscap=crs_prestera): Should the original values of QoS fields (PCP, DSCP) be kept (`yes`), or replaced with the ones from the assigned QoS profile (`no`)? Relevant only if `new-qos-profile` is set.
- `new-vlan-id` (num): Changes the VLAN ID to the specified value. Requires `vlan-filtering=yes`.
- `new-vlan-priority` (num): Changes the VLAN priority (priority code point). Requires `vlan-filtering=yes`.
- `new-vrf` (enum; syscap=crs_prestera): Assigns ingress traffic to a specified VRF. Requires [hardware-offloaded VRF](../../../../guides/bridging-and-switching/l3-hardware-offloading.md#l3hw-feature-support) support on the switch chip. On VRF-unaware switches (98DX3xxx and 98DX2xxx series), setting `new-vrf` to anything other than `main` will be treated as `redirect-to-cpu=yes`.
- `rate` (num): Sets ingress traffic limitation (bits per second) for matched traffic.

**Read-only arguments**

- `packets` (num; syscap=crs_prestera)
- `bytes` (num; syscap=crs_prestera)
- `internal-priority` (num)

## Commands

### /interface/ethernet/switch/rule/reset-counters

Syscap: rbswitch and crs_prestera; Type: Command

### /interface/ethernet/switch/rule/reset-counters-all

Syscap: rbswitch and crs_prestera; Type: Command
