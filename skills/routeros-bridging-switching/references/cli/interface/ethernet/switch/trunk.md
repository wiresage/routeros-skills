# /interface/ethernet/switch/trunk

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/trunk

Syscap: musicswitch; Type: Directory

Trunking in the Cloud Router Switches provides static link aggregation groups with hardware automatic failover and load balancing. IEEE802.3ad and IEEE802.1ax compatible Link Aggregation Control Protocol is not supported. Up to 8 Trunk groups are supported with up to 8 Trunk member ports per Trunk group. CRS Port Trunking calculates transmit-hash based on all of the following parameters: L2 src-dst MAC + L3 src-dst IP + L4 src-dst Port.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `name` (string): Name of the Trunk group.
- `member-ports` (multi { array-id, port: enum }; mandatory): Member ports of the Trunk group.
