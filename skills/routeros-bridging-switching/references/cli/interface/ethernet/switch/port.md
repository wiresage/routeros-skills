# /interface/ethernet/switch/port

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/port

## /interface/ethernet/switch/port

Syscap: musicswitch; Type: Directory

**Flags**

- `I`: invalid

**Arguments**

- `ingress-customer-tpid-override` (num): Ingress customer TPID override allows accepting specific frames with a custom customer tag TPID. The default value is for the tag of 802.1Q frames.
- `egress-customer-tpid-override` (num): Egress customer TPID override allows custom identification for egress frames with a customer tag. The default value is for the tag of 802.1Q frames.
- `ingress-service-tpid-override` (num): Ingress service TPID override allows accepting specific frames with a custom service tag TPID. The default value is for the service tag of 802.1AD frames.
- `egress-service-tpid-override` (num): Egress service TPID override allows custom identification for egress frames with a service tag. The default value is for the service tag of 802.1AD frames.
- `drop-secure-static-mac-move` (bool): Prevents MAC relearning of static entries until UFDB timeout if the MAC is already learned on another port.
- `drop-dynamic-mac-move` (bool): Prevents MAC relearning until UFDB timeout if the MAC is already learned on another port.
- `learn-limit` (num): Enable or disable MAC address learning and set the MAC limit on the port. MAC learning limit is disabled by default.
- `allow-unicast-loopback` (bool): Unicast loopback on port. When enabled, it permits sending back when the source port and destination port are the same for known unicast packets.
- `allow-multicast-loopback` (bool): Multicast loopback on port. When enabled, it permits sending back when the source port and destination port are the same for registered multicast or broadcast packets.
- `action-on-static-station-move` (enum: forward | redirect-to-cpu | copy-to-cpu | drop): Action for packets when UFDB already contains a static entry with such a MAC but with a different port.
- `drop-when-ufdb-entry-src-drop` (bool): Enable or disable dropping packets when UFDB entry has action src-drop.
- `isolation-leakage-profile-override` (num): Custom port profile for port isolation/leakage configurations.
  - Port-level isolation profile 0. Uplink port - allows the port to communicate with all ports in the device.
  - Port-level isolation profile 1. Isolated port - allows the port to communicate only with uplink ports.
  - Port-level isolation profile 2 - 31. Community port - allows communication among the same community ports and uplink ports.
- `vlan-type` (enum: edge-port | network-port): Port VLAN type specifies whether VLAN ID is used in UFDB learning. The network port learns VLAN ID in UFDB, edge port does not - VLAN 0. It can be observed only in IVL learning mode.
- `allow-fdb-based-vlan-translate` (bool): Enable or disable MAC-based VLAN translation on the port.
- `allow-mac-based-service-vlan-assignment-for` (enum: none | untagged-and-priority-tagged-frame-only | tagged-frame-only | all): Frame type for which MAC-based service VLAN translation applies.
- `allow-mac-based-customer-vlan-assignment-for` (enum: none | untagged-and-priority-tagged-frame-only | tagged-frame-only | all): Frame type for which MAC-based customer VLAN translation applies.
- `filter-untagged-frame` (bool): Whether to filter untagged frames on the port.
- `filter-priority-tagged-frame` (bool): Whether to filter tagged frames with priority on the port.
- `filter-tagged-frame` (bool): Whether to filter tagged frames on the port.
- `egress-vlan-tag-table-lookup-key` (enum: egress-vid | according-to-bridge-type): Egress VLAN table (VLAN Tagging) lookup:
  - `egress-vid` - lookup VLAN ID is `CVID` when an Edge port is configured, `SVID` when a Network port.
  - `according-to-bridge-type` - lookup VLAN ID is `CVID` when a customer VLAN bridge is configured, `SVID` when a service VLAN bridge.
- `egress-vlan-mode` (enum: untagged | tagged | unmodified): Egress VLAN tagging action on the port.
- `ingress-mirror-to` (enum (none | mirror0 | mirror1) { none:0xffffffff, mirror0:0, mirror1:1 }): Analyzer port for port-based ingress mirroring.
- `ingress-mirroring-according-to-vlan` (bool)
- `egress-mirror-to` (enum (none | mirror0 | mirror1) { none:0xffffffff, mirror0:0, mirror1:1 }): Analyzer port for port-based egress mirroring.
- `qos-scheme-precedence` (multi { array-id, qos-type: enum (pcp-based | vlan-based | protocol-based | da-based | sa-based | dscp-based | ingress-acl-based) }): Specifies applied QoS assignment schemes on the ingress of the port.
- `default-customer-pcp` (num): Default customer PCP of the port.
- `default-service-pcp` (num): Default service PCP of the port.
- `pcp-propagation-for-initial-pcp` (bool): Enables or disables PCP propagation for initial PCP assignment on ingress.
  - If the port `vlan-type` is an Edge port, the service PCP is copied from the customer PCP.
  - If the port `vlan-type` is a Network port, the customer PCP is copied from the service PCP.
- `egress-pcp-propagation` (bool): Enables or disables egress PCP propagation. If the port `vlan-type` is an Edge port, the service PCP is copied from the customer PCP. If the port `vlan-type` is a Network port, the customer PCP is copied from the service PCP.
- `dscp-based-qos-dscp-to-dscp-mapping` (bool): Enables or disables DSCP to internal DSCP mapping on the port.
- `pcp-or-dscp-based-qos-change-dei` (bool): Enables or disables PCP or DSCP based DEI change on the port.
- `pcp-or-dscp-based-qos-change-pcp` (bool): Enables or disables PCP or DSCP based PCP change on the port.
- `pcp-or-dscp-based-qos-change-dscp` (bool): Enables or disables PCP or DSCP based DSCP change on the port.
- `pcp-based-qos-drop-precedence-mapping` (object { range-and-drop-precedence: composite { pcp-dei-range: range [ .. 15] , drop-precedence: enum (green | yellow | red | drop) } }): The new value of drop precedence for the PCP/DEI to drop precedence (drop | green | red | yellow) mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:yellow,8-15:red".
- `pcp-based-qos-dscp-mapping` (object { range-and-dscp: composite { pcp-dei-range: range [ .. 15] , dscp: num [ .. 63] } }): The new value of DSCP for the PCP/DEI to DSCP mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:25,8-15:50".
- `pcp-based-qos-dei-mapping` (object { range-and-dei: composite { pcp-dei-range: range [ .. 15] , dei: num [ .. 1] } }): The new value of DEI for the PCP/DEI to DEI mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:0,8-15:1".
- `pcp-based-qos-pcp-mapping` (object { range-and-pcp: composite { pcp-dei-range: range [ .. 15] , pcp: num [ .. 7] } }): The new value of PCP for the PCP/DEI to PCP mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:3,8-15:4".
- `pcp-based-qos-priority-mapping` (object { range-and-priority: composite { pcp-dei-range: range [ .. 15] , priority: num [ .. 15] } }): The new value of internal priority for the PCP/DEI to priority mapping. Multiple mappings are allowed separated by a comma e.g. "0-7:5,8-15:15".
- `priority-to-queue` (object { priority-range-and-queue: composite { priority-range: range [ .. 15] , queue: num [ .. 7] } }): Internal priority (0..15) mapping to queue (0..7) per port.
- `per-queue-scheduling` (object { scheduling-type-and-weight: composite { scheduling-type: enum (strict-priority | wrr-group0 | wrr-group1) , weight: [ num [ .. 255]] } }): Set port to use either strict or weighted round robin policy for traffic shaping for each queue group.
- `custom-drop-counter-includes` (ubit (device-loopback, fdb-hash-violation, exceeded-port-learn-limitation, dynamic-station-move, static-station-move, ufdb-source-drop, host-source-drop, unknown-host, ingress-vlan-filtered)): Custom include to count dropped packets for switch port custom-drop-packet counter.
- `queue-custom-drop-counter0-includes` (ubit (red, yellow, green, queue0, queue1, queue2, queue3, queue4, queue5, queue6, queue7)): Custom include to count dropped packets for switch port tx-queue-custom0-drop-packet and bytes for tx-queue-custom0-drop-byte counter.
- `queue-custom-drop-counter1-includes` (ubit (red, yellow, green, queue0, queue1, queue2, queue3, queue4, queue5, queue6, queue7)): Custom include to count dropped packets for switch port tx-queue-custom1-drop-packet and bytes for tx-queue-custom1-drop-byte counter.
- `policy-drop-counter-includes` (ubit (ingress-policing, ingress-acl, egress-policing, egress-acl)): Custom include to count dropped packets for switch port policy-drop-packet counter.

**Read-only arguments**

- `name` (string)
- `ingress-customer-tpid` (num)
- `egress-customer-tpid` (num)
- `ingress-service-tpid` (num)
- `egress-service-tpid` (num)
- `learn` (bool)
- `isolation-leakage-profile` (num)
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

## /interface/ethernet/switch/port

Syscap: rbswitch; Type: Directory

**Flags**

- `R`: running
- `I`: invalid

**Arguments**

- `vlan-mode` (enum: disabled | fallback | check | secure; syscap=oldswitch): Changes the VLAN lookup mechanism against the VLAN Table for ingress traffic. `disabled` - disables checking against the VLAN Table completely, no traffic is dropped. `fallback` - checks tagged traffic against the VLAN Table, forwards all untagged traffic. `check` - checks tagged traffic, drops all untagged traffic. `secure` - checks tagged traffic, drops all untagged traffic, both ingress and egress ports must be found in the VLAN Table otherwise traffic is dropped.
- `vlan-header` (enum: leave-as-is | always-strip | add-if-missing; syscap=oldswitch): Sets the action performed on the port for egress traffic. `add-if-missing` - adds a VLAN tag using `default-vlan-id` from the ingress port, used for trunk ports. `always-strip` - removes a VLAN tag, used for access ports. `leave-as-is` - does not add or remove a VLAN tag, used for hybrid ports.
- `default-vlan-id` (num; syscap=oldswitch): Adds a VLAN tag with the specified VLAN ID on all untagged ingress traffic on a port. Should be used with `vlan-header=always-strip` to configure the port as an access port. For hybrid ports `default-vlan-id` is used to tag untagged traffic. If two ports have the same `default-vlan-id`, the VLAN tag is not added since the switch chip assumes traffic is being forwarded between access ports.
- `mirror-ingress` (bool; syscap=switch-mirror-prestera): Whether to send ingress packet copy to the `mirror-target` port.
- `mirror-egress` (bool; syscap=switch-mirror-prestera): Whether to send egress packet copy to the `mirror-target` port.
- `mirror-ingress-target` (enum: none; syscap=switch-mv88e6xxx): Selects a single mirroring ingress target port. Mirrored packets from `mirror-ingress` will be sent to the selected port.
- `ingress-rate` (num; syscap=oldswitch): Limits the received (ingress) traffic with packet drops. Everything that exceeds the defined limit will be dropped.
- `egress-rate` (num; syscap=oldswitch): Limits the transmitted (egress) traffic. The shaper tries to queue packets that exceed the limit instead of dropping them.
- `storm-rate` (num; syscap=crs_prestera): Amount of broadcast, unknown multicast and/or unknown unicast traffic limited to a percentage of the link speed.
- `limit-unknown-unicasts` (bool; syscap=crs_prestera): Limit unknown unicast traffic on a switch port.
- `limit-unknown-multicasts` (bool; syscap=crs_prestera): Limit unknown multicast traffic on a switch port.
- `limit-broadcasts` (bool; syscap=crs_prestera): Limit broadcast traffic on a switch port.
- `l3-hw-offloading` (bool; syscap=crs_prestera): Layer 3 Hardware Offloading. Hardware routing via this port. Only disables hardware routing from/to this particular port when set to `no`.

**Read-only arguments**

- `name` (string)
- `switch` (enum)
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

### /interface/ethernet/switch/port/reset-counters

Syscap: musicswitch; Type: Command

### /interface/ethernet/switch/port/reset-counters

Syscap: rbswitch; Type: Command
