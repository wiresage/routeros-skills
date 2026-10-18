# /interface/ethernet/switch/one2one-vlan-switching

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/one2one-vlan-switching

Syscap: musicswitch; Type: Directory

1:1 VLAN switching can be used to replace the regular L2 bridging for matched packets. When a packet hits a 1:1 VLAN switching table entry, the destination port information in the entry is assigned to the packet. The matched destination information in the UFDB and MFDB entries no longer applies to the packet.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `dst-port` (alt { port: enum , trunk: enum }; mandatory): Destination port for matched 1:1 VLAN switching packets.
- `service-vid` (num): Matching service VLAN id for 1:1 VLAN switching.
- `customer-vid` (num): Matching customer VLAN id for 1:1 VLAN switching.
