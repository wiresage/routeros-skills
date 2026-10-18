# /interface/ethernet/switch/acl

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/acl

Syscap: musicswitch; Type: Directory

Access Control List consists of ingress policy and egress policy engines and allows configuration of up to 128 policy rules (limited by RouterOS). It is an advanced tool for wire-speed packet filtering, forwarding, shaping, and modifying based on Layer2, Layer3, and Layer4 protocol header field conditions.

> **Note**
>
> Due to hardware limitations, it is not possible to match broadcast/multicast traffic on specific ports. You should use port isolation, drop traffic on ingress ports, or use VLAN filtering to prevent certain broadcast/multicast traffic from being forwarded.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `table` (enum: ingress | egress): Selects the policy table for incoming or outgoing packets.
- `invert-match` (bool): Inverts the whole ACL rule matching.
- `src-ports` (multi { array-id }): Matching physical source ports or trunks.
- `dst-ports` (multi { array-id }): Matching physical destination ports or trunks. It is not possible to match broadcast/multicast traffic on the egress port due to a hardware limitation.
- `service-vid` (super { ! , service-vid: range [ .. 4095] }): Matching service VLAN ID.
- `service-pcp` (num): Matching service PCP.
- `service-dei` (num): Matching service DEI.
- `customer-vid` (super { ! , customer-vid: range [ .. 4095] }): Matching customer VLAN ID.
- `customer-pcp` (num): Matching customer PCP.
- `customer-dei` (num): Matching customer DEI.
- `src-l3-port` (super { ! , src-l3-port: range [ .. 65535] }): Matching Layer3 source port.
- `dst-l3-port` (super { ! , dst-l3-port: range [ .. 65535] }): Matching Layer3 destination port.
- `custom-fields` (object { custom-field: super { ! , custom-field: super { base: enum (start-of-frame | end-of-l2-header | end-of-l3-header) , [offset] :num [ .. 127] , [range] :range [ .. 65535] , [mask] [ /num [ .. 65535]] } } })
- `priority` (num): Matching internal priority. Valid only in the egress table.
- `drop-precedence` (enum: green | yellow | red | drop): Matching internal drop precedence. Valid only in the egress table.
- `dst-addr-registered` (bool): Defines whether to match packets with a registered state - packets whose destination MAC address is in UFDB/MFDB/RFDB. Valid only in the egress table.
- `service-tag` (enum: untagged | priority-tagged | tagged | tagged-or-priority-tagged): Format of the service tag.
- `customer-tag` (enum: untagged | priority-tagged | tagged | tagged-or-priority-tagged): Format of the customer tag.
- `mac-src-address` (super { address: macAddr , [mask] [ /macAddr] }): Source MAC address and mask.
- `mac-dst-address` (super { address: macAddr , [mask] [ /macAddr] }): Destination MAC address and mask.
- `mac-protocol` (alt { protocol-name: enum (ip-or-ipv6 | non-ip) { ip-or-ipv6:0x10000, non-ip:0x10001 } , protocol-number: num [ .. 65535] }): Ethernet payload type (MAC-level protocol).
  - `802.2` - 802.2 Frames (0x0004)
  - `arp` - Address Resolution Protocol (0x0806)
  - `capsman` - CAPsMAN to CAP MAC layer connection (0x88BB)
  - `dot1x` - EAPoL IEEE 802.1X (0x888E)
  - `homeplug-av` - HomePlug AV MME (0x88E1)
  - `ip` - Internet Protocol version 4 (0x0800)
  - `ip-or-ipv6` - IPv4 or IPv6 (0x0800 or 0x86DD)
  - `ipv6` - Internet Protocol Version 6 (0x86DD)
  - `ipx` - Internetwork Packet Exchange (0x8137)
  - `lacp` - Link Aggregation Control Protocol (0x8809)
  - `lldp` - Link Layer Discovery Protocol (0x88CC)
  - `loop-protect` - Loop Protect Protocol (0x9003)
  - `macsec` - MAC security IEEE 802.1AE (0x88E5)
  - `mpls-multicast` - MPLS multicast (0x8848)
  - `mpls-unicast` - MPLS unicast (0x8847)
  - `mvrp` - Multiple VLAN Registration protocol (0x88F5)
  - `non-ip` - Not Internet Protocol version 4 (not 0x0800)
  - `packing-compr` - Encapsulated packets with compressed [IP packing](https://manual.mikrotik.com/docs/cli-reference/ip/packing) (0x9001)
  - `packing-simple` - Encapsulated packets with simple [IP packing](https://manual.mikrotik.com/docs/cli-reference/ip/packing) (0x9000)
  - `pppoe` - PPPoE Session Stage (0x8864)
  - `pppoe-discovery` - PPPoE Discovery Stage (0x8863)
  - `rarp` - Reverse Address Resolution Protocol (0x8035)
  - `romon` - Router Management Overlay Network [RoMON](https://manual.mikrotik.com/docs/management-tools/romon) (0x88BF)
  - `service-vlan` - Provider Bridging IEEE 802.1ad and Shortest Path Bridging IEEE 802.1aq (0x88A8)
  - `vlan` - VLAN-tagged frame IEEE 802.1Q and Shortest Path Bridging IEEE 802.1aq with NNI compatibility (0x8100)
- `lookup-vid` (num): VLAN ID used in lookup. It can be changed before reaching the egress table.
- `ip-protocol` (enum: tcp | udp | udp-lite | other): IP protocol type.
- `fragmented` (bool): Whether to match fragmented packets.
- `first-fragment` (bool): YES matches not fragmented and the first fragments, NO matches other fragments.
- `ttl` (enum: 0 | 1 | max | other): Matching TTL field of the packet.
- `ip-dst` (composite { address: ipAddr , netmask: [ num [ .. 32]] }): Matching destination IPv4 address.
- `ip-src` (composite { address: ipAddr , netmask: [ num [ .. 32]] }): Matching source IPv4 address.
- `dscp` (num): Matching DSCP field of the packet.
- `ecn` (num): Matching ECN field of the packet.
- `ipv6-dst` (ip6Prefix): Matching destination IPv6 address.
- `ipv6-src` (ip6Prefix): Matching source IPv6 address.
- `mac-isolation-profile` (enum: promiscuous | isolated | community1 | community2): Matches isolation profile based on UFDB. Valid only in the egress policy table.
- `src-mac-addr-state` (enum: sa-found | sa-not-found | dynamic-station-move | static-station-move): Defines whether to match packets with registered state - packets whose destination MAC address is in UFDB/MFDB/RFDB. Valid only in the egress policy table.
- `flow-id` (num)
- `action` (enum: forward | redirect-to-cpu | copy-to-cpu | send-to-new-dst-ports | drop): Action for matching ACL packets.
  - `copy-to-cpu` - packets are copied to the CPU.
  - `drop` - packets are dropped.
  - `forward` - packets are forwarded.
  - `redirect-to-cpu` - packets are redirected to the CPU.
  - `send-to-new-dst-ports` - packets are sent to new destination ports.
- `new-dst-ports` (multi { array-id }): If the action is `send-to-new-dst-ports`, then this property sets which ports/trunks are the new destinations.
- `new-flow-id` (num)
- `attack-filter-bypass` (bool)
- `ingress-vlan-filter-bypass` (bool): Allows bypassing ingress VLAN filtering in the VLAN table for matching packets. This applies only to the ingress policy table.
- `egress-vlan-filter-bypass` (bool): Allows bypassing egress VLAN filtering in the VLAN table for matching packets. This applies only to the ingress policy table.
- `isolation-filter-bypass` (bool): Allows bypassing the Isolation table for matching packets. This applies only to the ingress policy table.
- `new-registered-state` (bool): Whether to modify packet status. YES sets packet status to registered, NO - unregistered. Valid only in the ingress policy table.
- `src-mac-learn` (bool): Whether to learn the source MAC of the matched ACL packets. Valid only in the ingress policy table.
- `mirror-to` (enum: mirror0 | mirror1): Mirroring destination for ACL packets.
- `new-service-vid` (num): New service VLAN ID for ACL packets.
- `new-customer-vid` (num): New customer VLAN ID for ACL packets. If set to 4095, then traffic is dropped.
- `egress-vlan-translate-bypass` (bool): Allows bypassing the egress VLAN translation table for matching packets.
- `new-service-pcp` (num): New service PCP for ACL packets.
- `new-service-dei` (num): New service DEI for ACL packets.
- `new-customer-pcp` (num): New customer PCP for ACL packets.
- `new-customer-dei` (num): New customer DEI for ACL packets.
- `new-dscp` (num): New DSCP for ACL packets.
- `new-priority` (num): New internal priority for ACL packets.
- `new-drop-precedence` (enum: green | yellow | red | drop): New internal drop precedence for ACL packets.
- `policer` (enum): Applied ACL Policer for ACL packets.
