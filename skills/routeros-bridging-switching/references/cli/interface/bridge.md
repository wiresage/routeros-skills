# /interface/bridge

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge

Type: Directory

**Flags**

- `Y`: managed
- `D`: dynamic
- `X`: disabled
- `R`: running

**Arguments**

- `name` (string)
- `mtu` (num)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `protocol-mode` (enum: none | stp | rstp | mstp)
- `fast-forward` (bool)
- `igmp-snooping` (bool)
- `multicast-router` (enum: disabled | temporary-query | permanent)
- `multicast-querier` (bool)
- `querier-uses-bridge-address` (bool)
- `startup-query-count` (num)
- `last-member-query-count` (num)
- `last-member-interval` (time; deprecated)
- `last-member-query-interval` (time)
- `membership-interval` (time)
- `querier-interval` (time)
- `query-interval` (time)
- `query-response-interval` (time)
- `startup-query-interval` (time)
- `igmp-version` (enum: 2 | 3)
- `mld-version` (enum: 1 | 2)
- `auto-mac` (bool)
- `admin-mac` (macAddr)
- `ageing-time` (time)
- `priority` (alt { priority: enum (0x0000 | 0x1000 | 0x2000 | 0x3000 | 0x4000 | 0x5000 | 0x6000 | 0x7000 | 0x8000 | 0x9000 | 0xa000 | 0xb000 | 0xc000 | 0xd000 | 0xe000 | 0xf000) { 0x0000:0x0000, 0x1000:0x1000, 0x2000:0x2000, 0x3000:0x3000, 0x4000:0x4000, 0x5000:0x5000, 0x6000:0x6000, 0x7000:0x7000, 0x8000:0x8000, 0x9000:0x9000, 0xa000:0xa000, 0xb000:0xb000, 0xc000:0xc000, 0xd000:0xd000, 0xe000:0xe000, 0xf000:0xf000 } , priority: num [0 .. 65535] })
- `max-message-age` (time)
- `forward-delay` (time)
- `transmit-hold-count` (num)
- `region-name` (string)
- `region-revision` (num)
- `max-hops` (num)
- `vlan-filtering` (bool)
- `ether-type` (enum (0x8100 | 0x88a8 | 0x9100) { 0x8100:0x8100, 0x88a8:0x88a8, 0x9100:0x9100 })
- `pvid` (num)
- `frame-types` (enum: admit-all | admit-only-vlan-tagged | admit-only-untagged-and-priority-tagged)
- `ingress-filtering` (bool)
- `dhcp-snooping` (bool)
- `dhcp-snooping-vlan-ids` (multi { vlan-id-range: range [1 .. 4094] })
- `dhcp-agent-circuit-id` (string): Specify the relay agent circuit-id suboption value of the option 82 to be added to the DHCP messages passing through the bridge.
  The string length is limited to 255 characters with the default value being: $(INTERFACE):$(VID).
  The string value can contain variables, whose names must be enclosed in parentheses and prepended by a dollar sign.
  Example: 'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'.
  The following variables are supported: HOSTNAME, INTERFACE, VID and BRIDGEMAC.
  For the compatibility with previous versions, where the remote-id value was fixed, the semicolon appearing in the default value expression is not
  included in the remote-id value, in the case when the vlan filtering is not enabled.
- `dhcp-agent-remote-id` (string): Specify the relay agent remote-id suboption value of the option 82 to be added to the DHCP messages passing through the bridge.
  The string length is limited to 255 characters with the default value being: $(BRIDGEMAC).
  The string value can contain variables, whose names must be enclosed in parentheses and prepended by a dollar sign.
  Example: 'some_arbitrary_text $(HOSTNAME) another_piece_of_text $(BRIDGEMAC)'.
  The following variables are supported: HOSTNAME, INTERFACE, VID and BRIDGEMAC.
- `arp-inspection` (bool)
- `dhcpv6-snooping` (bool)
- `dhcpv6-agent-circuit-id` (string): Specify the DHCPv6 option 18 value to be added to the DHCPv6 messages passing through the bridge.
  The string length is limited to 255 characters with the default value being: $(INTERFACE):$(VID).
  The string value can contain variables, whose names must be enclosed in parentheses and prepended by a dollar sign.
  Example: 'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'.
  The following variables are supported: HOSTNAME, INTERFACE, VID and BRIDGEMAC.
- `dhcpv6-agent-remote-id` (string): Specify the DHCPv6 option 37 value to be added to the DHCPv6 messages passing through the bridge.
  The string length is limited to 255 characters with the default value being: $(BRIDGEMAC).
  The string value can contain variables, whose names must be enclosed in parentheses and prepended by a dollar sign.
  Example: 'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'.
  The following variables are supported: HOSTNAME, INTERFACE, VID and BRIDGEMAC.
- `ip-source-guard` (bool)
- `ra-guard` (bool)
- `port-cost-mode` (enum: short | long)
- `mvrp` (bool)
- `forward-reserved-addresses` (bool)
- `max-learned-entries` (alt { max-learned-entries: enum (unlimited | auto) , max-learned-entries: num })
- `mlag-peer-port` (alt { interface: iface_enum { none } , interface-bond: iface_enum }): An interface that will be used as a peer port. Both peer devices are using inter-chassis communication over these peer ports to establish MLAG and update the host table.
  Peer ports can be configured as single Ethernet interfaces or bonding interfaces. However, using a bonding interface is recommended, as it helps prevent a single interface failure from affecting connectivity, especially when both MLAG nodes are still up and running.
  It is recommended to keep the untagged VLAN used by the peer ports separate from the rest of your network, either by assigning a dedicated untagged VLAN (using `pvid`), or by setting the peer port to only allow VLAN tagged frames (using `frame-types=admit-only-vlan-tagged`).
  All VLANs used for bridge slave ports must also be configured as tagged VLANs for peer-port (in the `/interface/bridge/vlan` table), so that peer-port is a member of those VLANs and can forward data.
- `mlag-priority` (num): This setting changes the priority for selecting the primary MLAG node. A lower number means higher priority. If both MLAG nodes have the same priority, the one with the lowest bridge MAC address will become the primary device.
- `mlag-heartbeat` (alt { mlag-heartbeat: enum (none) , mlag-heartbeat: time [1s .. 10s] }): This setting controls how often heartbeat messages are sent to check the connection between peers. If no heartbeat message is received for three intervals in a row, the peer logs a warning about potential communication problems. If set to `none`, heartbeat messages are not sent at all.
- `mlag-init-delay` (time)
- `mlag-lacp-fallback` (bool)

**Read-only arguments**

- `actual-mtu` (num)
- `l2mtu` (num)
- `mac-address` (macAddr)

## Commands

### /interface/bridge/monitor

Type: Command

**Read-only arguments**

- `state` (enum: disabled | disabled | enabled | enabled)
- `current-mac-address` (macAddr)
- `bridge-id` (composite { prio: num , mac: macAddr })
- `root-bridge` (bool)
- `root-bridge-id` (composite { prio: num , mac: macAddr })
- `regional-root-bridge-id` (composite { prio: num , mac: macAddr })
- `root-path-cost` (num)
- `root-port` (iface_enum)
- `port-count` (num)
- `designated-port-count` (num)
- `mst-config-digest` (string)
- `fast-forward` (bool)
- `multicast-router` (bool)
- `igmp-querier` (composite { interface: iface_enum , ip-address: ipAddr })
- `mld-querier` (composite { interface: iface_enum , ipv6-address: ip6Addr })
- `declared-vlan-ids` (multi { vlan-range: range })
- `registered-vlan-ids` (multi { vlan-range: range })
- `mlag-state` (string): Shows the MLAG connection state: `connected` when ICCP is established, `connecting` while the peers establish or re-establish the connection, or an error such as `peer port not running` when the configured peer port is unavailable.
- `mlag-active-role` (enum: primary | secondary): The peer with the lowest `priority` acts as the primary device. If the priorities are the same, the peer with the lowest bridge MAC address becomes the primary. The `system-id` of the primary device is used for sending the (R/M)STP BPDU bridge identifier and LACP system ID. The role is shown after a successful MLAG connection.
