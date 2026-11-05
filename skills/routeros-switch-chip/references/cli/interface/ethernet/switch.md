# /interface/ethernet/switch

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch

## /interface/ethernet/switch

Conditions: !smips; Syscap: musicswitch; Type: Settings Directory

Global parameters for CRS1xx and 2xx series switches.

**Arguments**

- `name` (string): Name of the switch.
- `bridge-type` (enum: customer-vid-used-as-lookup-vid | service-vid-used-as-lookup-vid): Defines which VLAN tag is used as Lookup-VID. Lookup-VID serves as the VLAN key for all VLAN-based lookups.
- `drop-if-no-vlan-assignment-on-ports` (multi { array-id }): Ports which drop frames if no MAC-based, Protocol-based VLAN assignment or Ingress VLAN Translation is applied.
- `drop-if-invalid-or-src-port-not-member-of-vlan-on-ports` (multi { array-id, port: enum }): Ports that drop invalid and other port VLAN ID frames.
- `unknown-vlan-lookup-mode` (enum: ivl | svl): Lookup and learning mode for packets with an invalid VLAN.
   - `ivl` - use Independent VLAN Learning,
   - `svl` - use Shared VLAN Learning.
- `forward-unknown-vlan` (bool): Whether to allow forwarding VLANs that are not members of the VLAN table.
- `use-svid-in-one2one-vlan-lookup` (bool): Whether to use service VLAN ID for 1:1 VLAN switching lookup.
- `use-cvid-in-one2one-vlan-lookup` (bool): Whether to use customer VLAN ID for 1:1 VLAN switching lookup.
- `mac-level-isolation` (bool): Globally enables or disables MAC level isolation. Once enabled, the switch will check the source and destination MAC address entries and their `isolation-profile` from the unicast forwarding table. By default, the switch will learn MAC addresses and place them into a `promiscuous` isolation profile. Other isolation profiles can be used when creating static unicast entries. If the source or destination MAC address is located on a `promiscuous` isolation profile, the packet is forwarded. If both source and destination MAC addresses are located on the same `community1` or `community2` isolation profile, the packet is forwarded. The packet is dropped when the source and destination MAC address isolation profile is `isolated`, or when the source and destination MAC address isolation profiles are from different communities (e.g. source MAC address is `community1` and destination MAC address is `community2`). When MAC level isolation is globally disabled, the isolation is bypassed.
- `multicast-lookup-mode` (enum: dst-mac-and-vid-always | dst-ip-and-vid-for-ipv4): Lookup mode for IPv4 multicast bridging.
  - `dst-mac-and-vid-always` - for all packet types the lookup key is the destination MAC and VLAN ID.
  - `dst-ip-and-vid-for-ipv4` - for IPv4 packets the lookup key is the destination IP and VLAN ID.
- `override-existing-when-ufdb-full` (bool): Enable or disable overriding an existing entry which has the lowest aging value when UFDB is full.
- `unicast-fdb-timeout` (time): Timeout for Unicast FDB entries.
- `ingress-mirror0` (composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff } , trunk: enum } , packet-format: [ enum (unmodified | analyzer-configured)] }): The first ingress mirroring analyzer port or trunk and mirroring format.
   - `analyzer-configured` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the analyzer port.
   - `unmodified` - traffic is mirrored without any change to the original incoming packet format, but the service VLAN tag is stripped in the edge port.
- `ingress-mirror1` (composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff } , trunk: enum } , packet-format: [ enum (unmodified | analyzer-configured)] }): The second ingress mirroring analyzer port or trunk and mirroring format.
   - `analyzer-configured` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the analyzer port.
   - `unmodified` - traffic is mirrored without any change to the original incoming packet format, but the service VLAN tag is stripped in the edge port.
- `ingress-mirror-ratio` (enum: 1/1 | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 | 1/512 | 1/1024 | 1/2048 | 1/4096 | 1/8192 | 1/16384 | 1/32768): The proportion of ingress mirrored packets compared to all packets.
- `egress-mirror0` (composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff } , trunk: enum } , packet-format: [ enum (modified | analyzer-configured | original)] }): The first egress mirroring analyzer port or trunk and mirroring format.
   - `analyzer-configured` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the analyzer port.
   - `modified` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the egress port.
   - `original` - traffic is mirrored without any change to the original incoming packet format, but the service VLAN tag is stripped in the edge port.
- `egress-mirror1` (composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff } , trunk: enum } , packet-format: [ enum (modified | analyzer-configured | original)] }): The second egress mirroring analyzer port or trunk and mirroring format.
   - `analyzer-configured` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the analyzer port.
   - `modified` - packet is the same as the packet to the destination, VLAN format is modified based on the VLAN configurations of the egress port.
   - `original` - traffic is mirrored without any change to the original incoming packet format, but the service VLAN tag is stripped in the edge port.
- `egress-mirror-ratio` (enum: 1/1 | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 | 1/512 | 1/1024 | 1/2048 | 1/4096 | 1/8192 | 1/16384 | 1/32768): The proportion of egress mirrored packets compared to all packets.
- `fdb-uses` (enum: mirror0 | mirror1): Analyzer port used for FDB-based mirroring.
- `vlan-uses` (enum: mirror0 | mirror1): Analyzer port used for VLAN-based mirroring.
- `mirror-egress-if-ingress-mirrored` (bool): When a packet is applied to both ingress and egress mirroring, only ingress mirroring is performed on the packet, if this setting is disabled. If enabled, both mirroring types are applied.
- `mirror-tx-on-mirror-port` (bool)
- `mirrored-packet-qos-priority` (num): Remarked priority in mirrored packets.
- `mirrored-packet-drop-precedence` (enum: green | yellow | red | drop): Remarked drop precedence in mirrored packets. This QoS attribute is used for mirrored packet enqueuing or dropping.
- `bypass-vlan-ingress-filter-for` (ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)): Protocols that are excluded from Ingress VLAN filtering. These protocols are not dropped if they have an invalid VLAN. (arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1).
- `bypass-ingress-port-policing-for` (ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)): Protocols that are excluded from Ingress Port Policing. (arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1).
- `bypass-l2-security-check-filter-for` (ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)): Protocols that are excluded from Policy rule security check. (arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1).

**Read-only arguments**

- `type` (enum: QCA-8513L | QCA-8519 | QCA-8511)

## /interface/ethernet/switch

Syscap: rbswitch; Type: Directory

Global parameters for switches with Marwell Prestera chips.

**Flags**

- `I`: invalid

**Arguments**

- `name` (string)
- `mirror-source` (iface_enum; syscap=switch-mirror1): Selects a single mirroring source port. Ingress and egress traffic will be sent to the `mirror-target` port. Note that the `mirror-target` port has to belong to the same switch.
- `mirror-target` (iface_enum { none:0, cpu:0xffffffff }; syscap=switch-mirror-prestera): Selects a single mirroring target port. Mirrored packets from [`mirror-egress`](switch/port.md#mirror-egress), [`mirror-ingress`](switch/port.md#mirror-ingress) and [`mirror`](switch/rule.md#mirror) will be sent to the selected port.
- `mirror-egress-target` (enum: none; syscap=switch-mv88e6xxx): Selects a single mirroring egress target port. Mirrored packets from `mirror-egress` (see the property in the port menu) will be sent to the selected port.
- `rspan` (bool; syscap=switch-mirror-prestera): Enables the Remote Switch Port Analyzer (RSPAN) feature on `mirror-target`. Traffic marked for ingress or egress mirroring is carried over a specified remote analyzer VLAN - `rspan-egress-vlan-id` and `rspan-ingress-vlan-id`.
- `rspan-ingress-vlan-id` (num; syscap=switch-mirror-prestera): Selects the VLAN ID for marked ingress traffic. Only applies when `rspan` is enabled.
- `rspan-egress-vlan-id` (num; syscap=switch-mirror-prestera): Selects the VLAN ID for marked egress traffic. Only applies when `rspan` is enabled.
- `switch-all-ports` (bool): Changes the ether1 switch group only on RB450G/RB435G/RB850Gx2 devices. `yes` - ether1 is part of the switch and supports all advanced features including extended statistics. `no` - ether1 is not part of the switch, effectively making it a stand-alone ethernet port, increasing throughput but removing switching capability.
- `cpu-flow-control` (bool; syscap=switch-mv88e6xxx): Disables or enables the CPU Flow Control feature. The switch chip ensures the CPU port is not congested by sending out Pause Frames when link capacity is exceeded. Without this feature, packets crucial for routing or management may be dropped.
- `l3-hw-offloading` (bool; syscap=crs_prestera): Layer 3 hardware offloading. Allows offloading routing features onto the switch chip to reach wire speeds.
- `qos-hw-offloading` (bool; syscap=crs_prestera): Quality of Service hardware offloading. Allows enabling QoS for the given switch chip (if it supports QoS). Turning off the this setting will not completely revert to the previous functionality. It is recommended to reboot the device after disabling it.

**Read-only arguments**

- `type` (enum: ADMtek | IC-Plus-175C | IC-Plus-178C | IC-Plus-175D | Atheros-8316 | Atheros-7240 | Atheros-8227 | Atheros-8327 | Atheros-8236 | QCA-8513L | Atheros-8327N | QCA-8519 | QCA-8511 | QCA-8337 | MediaTek-MT7621 | Realtek-RTL8367 | Marvell-98DX3236 | Marvell-98DX8216 | Marvell-98DX8208 | Marvell-98DX8332 | Marvell-98DX8212 | Marvell-98DX3257 | IPQ-PPE | Marvell-98DX8525 | Marvell-98PX1012 | Marvell-98DX4310 | Marvell-98DX224S | Marvell-98DX226S | Marvell-88E6393X | Marvell-98DX3255 | Marvell-88E6191X | Marvell-98DX2528 | Marvell-98CX8410 | Marvell-88E6341 | MediaTek-MT7531 | Marvell-88E6190 | Marvell-98DX7335 | Marvell-98DX3510 | Marvell-98DX3550 | MediaTek-MT7531AE | Marvell-98DX1508M | IPQ-9570 | Marvell-98DX3530 | Marvell-98DX4550M | QCA-8386 | EN7523 | Marvell-98DX2521 | Marvell-98DX2556 | Marvell-98DX2588 | Marvell-98DX7335M)
- `driver-rx-byte` (multi { counter: num })
- `driver-rx-packet` (multi { counter: num })
- `driver-tx-byte` (multi { counter: num })
- `driver-tx-packet` (multi { counter: num })
- `rx-bytes` (multi { counter: num })
- `rx-packet` (multi { counter: num })
- `rx-too-short` (multi { counter: num })
- `rx-64` (multi { counter: num })
- `rx-65-127` (multi { counter: num })
- `rx-128-255` (multi { counter: num })
- `rx-256-511` (multi { counter: num })
- `rx-512-1023` (multi { counter: num })
- `rx-1024-1518` (multi { counter: num })
- `rx-1519-max` (multi { counter: num })
- `rx-too-long` (multi { counter: num })
- `rx-broadcast` (multi { counter: num })
- `rx-pause` (multi { counter: num })
- `rx-multicast` (multi { counter: num })
- `rx-fcs-error` (multi { counter: num })
- `rx-align-error` (multi { counter: num })
- `rx-fragment` (multi { counter: num })
- `rx-overflow` (multi { counter: num })
- `rx-control` (multi { counter: num })
- `rx-unknown-op` (multi { counter: num })
- `rx-length-error` (multi { counter: num })
- `rx-code-error` (multi { counter: num })
- `rx-carrier-error` (multi { counter: num })
- `rx-jabber` (multi { counter: num })
- `rx-drop` (multi { counter: num })
- `rx-ip-header-checksum-error` (multi { counter: num })
- `rx-tcp-checksum-error` (multi { counter: num })
- `rx-udp-checksum-error` (multi { counter: num })
- `tx-bytes` (multi { counter: num })
- `tx-packet` (multi { counter: num })
- `tx-too-short` (multi { counter: num })
- `tx-64` (multi { counter: num })
- `tx-65-127` (multi { counter: num })
- `tx-128-255` (multi { counter: num })
- `tx-256-511` (multi { counter: num })
- `tx-512-1023` (multi { counter: num })
- `tx-1024-1518` (multi { counter: num })
- `tx-1519-max` (multi { counter: num })
- `tx-too-long` (multi { counter: num })
- `tx-broadcast` (multi { counter: num })
- `tx-pause` (multi { counter: num })
- `tx-multicast` (multi { counter: num })
- `tx-underrun` (multi { counter: num })
- `tx-collision` (multi { counter: num })
- `tx-excessive-collision` (multi { counter: num })
- `tx-multiple-collision` (multi { counter: num })
- `tx-single-collision` (multi { counter: num })
- `tx-excessive-deferred` (multi { counter: num })
- `tx-deferred` (multi { counter: num })
- `tx-late-collision` (multi { counter: num })
- `tx-total-collision` (multi { counter: num })
- `tx-pause-honored` (multi { counter: num })
- `tx-drop` (multi { counter: num })
- `tx-jabber` (multi { counter: num })
- `tx-fcs-error` (multi { counter: num })
- `tx-control` (multi { counter: num })
- `tx-fragment` (multi { counter: num })
- `tx-carrier-sense-error` (multi { counter: num })
- `tx-rx-64` (multi { counter: num })
- `tx-rx-65-127` (multi { counter: num })
- `tx-rx-128-255` (multi { counter: num })
- `tx-rx-256-511` (multi { counter: num })
- `tx-rx-512-1023` (multi { counter: num })
- `tx-rx-1024-1518` (multi { counter: num })
- `tx-rx-1519-max` (multi { counter: num })
- `tx-queue-custom0-drop-packet` (multi { counter: num })
- `tx-queue-custom0-drop-byte` (multi { counter: num })
- `tx-queue-custom1-drop-packet` (multi { counter: num })
- `tx-queue-custom1-drop-byte` (multi { counter: num })
- `policy-drop-packet` (multi { counter: num })
- `custom-drop-packet` (multi { counter: num })
- `current-learned` (multi { counter: num })
- `not-learned` (multi { counter: num })
- `rx-unicast` (multi { counter: num })
- `tx-unicast` (multi { counter: num })
- `rx-error-events` (multi { counter: num })
- `tx-rx-1024-max` (multi { counter: num })
- `rx-1024-max` (multi { counter: num })
- `tx-1024-max` (multi { counter: num })
- `rs-fec-codewords` (multi { counter: num })
- `rs-fec-corrected` (multi { counter: num })
- `rs-fec-uncorrected` (multi { counter: num })
- `rs-fec-symbol-error` (multi { counter: num })
- `fc-fec-rx-block` (multi { counter: num })
- `fc-fec-block-corrected` (multi { counter: num })
- `fc-fec-block-uncorrected` (multi { counter: num })
- `tx-queue0-packet` (multi { counter: num })
- `tx-queue0-byte` (multi { counter: num })
- `tx-queue1-packet` (multi { counter: num })
- `tx-queue1-byte` (multi { counter: num })
- `tx-queue2-packet` (multi { counter: num })
- `tx-queue2-byte` (multi { counter: num })
- `tx-queue3-packet` (multi { counter: num })
- `tx-queue3-byte` (multi { counter: num })
- `tx-queue4-packet` (multi { counter: num })
- `tx-queue4-byte` (multi { counter: num })
- `tx-queue5-packet` (multi { counter: num })
- `tx-queue5-byte` (multi { counter: num })
- `tx-queue6-packet` (multi { counter: num })
- `tx-queue6-byte` (multi { counter: num })
- `tx-queue7-packet` (multi { counter: num })
- `tx-queue7-byte` (multi { counter: num })
- `tx-drop-packet` (multi { counter: num })
- `tx-drop-byte` (multi { counter: num })
- `tx-drop-queue0-packet` (multi { counter: num })
- `tx-drop-queue0-byte` (multi { counter: num })
- `tx-drop-queue1-packet` (multi { counter: num })
- `tx-drop-queue1-byte` (multi { counter: num })
- `tx-drop-queue2-packet` (multi { counter: num })
- `tx-drop-queue2-byte` (multi { counter: num })
- `tx-drop-queue3-packet` (multi { counter: num })
- `tx-drop-queue3-byte` (multi { counter: num })
- `tx-drop-queue4-packet` (multi { counter: num })
- `tx-drop-queue4-byte` (multi { counter: num })
- `tx-drop-queue5-packet` (multi { counter: num })
- `tx-drop-queue5-byte` (multi { counter: num })
- `tx-drop-queue6-packet` (multi { counter: num })
- `tx-drop-queue6-byte` (multi { counter: num })
- `tx-drop-queue7-packet` (multi { counter: num })
- `tx-drop-queue7-byte` (multi { counter: num })

## Commands

### /interface/ethernet/switch/reset-counters

Conditions: !smips; Syscap: musicswitch; Type: Command

### /interface/ethernet/switch/reset-counters

Syscap: rbswitch; Type: Command
