# /interface/ethernet/switch/dscp-qos-map

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/dscp-qos-map

Syscap: musicswitch; Type: Directory

The global DSCP to QOS mapping table is used for mapping from the DSCP of the packet to new QoS attributes configured in the table.

**Flags**

- `I`: invalid

**Arguments**

- `drop-precedence` (enum: green | yellow | red | drop): The new value of Drop precedence for the DSCP to QoS mapping entry.
- `dei` (num): The new value of DEI for the DSCP to QoS mapping entry.
- `pcp` (num): The new value of PCP for the DSCP to QoS mapping entry.
- `priority` (num): The new value of internal priority for the DSCP to QoS mapping entry.

**Read-only arguments**

- `dscp` (num)
- `hex` (num)
