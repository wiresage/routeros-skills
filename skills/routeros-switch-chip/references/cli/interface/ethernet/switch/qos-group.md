# /interface/ethernet/switch/qos-group

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos-group

Syscap: musicswitch; Type: Directory

The global QoS group table is used for VLAN-based, Protocol-based, and MAC-based QoS group assignment configuration.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `name` (string): Name of the QoS group.
- `pcp` (num): The new value of PCP for the QoS group.
- `dei` (num): The new value of DEI for the QoS group.
- `dscp` (num): The new value of DSCP for the QoS group.
- `priority` (num): Internal priority is of local significance for classifying traffic to different egress queues on a port (1 is highest, 15 is lowest).
- `drop-precedence` (enum: green | yellow | red | drop): Drop precedence is an internal QoS attribute used for packet enqueuing or dropping.
