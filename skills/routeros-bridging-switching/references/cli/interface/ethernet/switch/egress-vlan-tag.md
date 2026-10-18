# /interface/ethernet/switch/egress-vlan-tag

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/egress-vlan-tag

Syscap: musicswitch; Type: Directory

Egress packets can be assigned different VLAN tag formats. The VLAN tags can be removed, added, or left as is when the packet is sent to the egress port (destination port). Each port has dedicated control of the egress VLAN tag format. The tag formats include:
- Untagged
- Tagged
- Unmodified

The Egress VLAN Tag table includes 4096 entries for VLAN tagging selection.

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic

**Arguments**

- `vlan-id` (num; mandatory): VLAN ID which is tagged in egress.
- `tagged-ports` (multi { array-id }): Ports that are tagged in egress.
