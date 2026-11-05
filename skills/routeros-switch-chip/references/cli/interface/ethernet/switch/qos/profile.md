# /interface/ethernet/switch/qos/profile

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/profile

Syscap: rbswitch and crs_prestera; Type: Directory

QoS profiles determine priority field values (PCP, DSCP) for the forwarded/routed packets. Congestion avoidance/resolution is based on QoS profiles. Each packet gets a QoS profile assigned based on the ingress switch port QoS settings (see `/in/eth/sw/port`).

**Flags**

- `*`: default
- `D`: dynamic
- `X`: disabled
- `I`: inactive
- `H`: hw-offloaded

**Arguments**

- `name` (string; mandatory): The user-defined name of the QoS profile.
- `pcp` (num): VLAN priority value (IEEE 802.1q PCP - Priority Code Point). Used only if the egress packets assigned to the QoS profile are VLAN-tagged (have the 802.1q header). The value can be further altered via the QoS Egress Map.
- `dscp` (num): IPv4/IPv6 DSCP field value for the egress packets assigned to the QoS profile.
- `traffic-class` (num): The traffic class determines the packet priority and the egress queue. The queue number is usually the same as the traffic class (packets with tc0 go into queue0, tc1 - queue1, ... tc7 - queue7). TC0 always selects the lowest priority.
- `automap` (bool): Automatically maps packets with matching PCP or DSCP values to this QoS profile. Only applies to **trusted** ports.

**Read-only arguments**

- `hw-id` (num)
