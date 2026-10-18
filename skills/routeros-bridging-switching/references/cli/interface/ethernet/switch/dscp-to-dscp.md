# /interface/ethernet/switch/dscp-to-dscp

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/dscp-to-dscp

Syscap: musicswitch; Type: Directory

The global DSCP to DSCP mapping table is used for mapping from the packet's original DSCP to the new DSCP value configured in the table.

**Flags**

- `I`: invalid

**Arguments**

- `new-dscp` (num): The new value of DSCP for the DSCP to DSCP mapping entry.

**Read-only arguments**

- `original-dscp` (num)
- `hex` (num)
