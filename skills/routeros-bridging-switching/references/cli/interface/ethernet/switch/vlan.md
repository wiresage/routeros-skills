# /interface/ethernet/switch/vlan

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/vlan

## /interface/ethernet/switch/vlan

Syscap: musicswitch; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic

**Arguments**

- `vlan-id` (num; mandatory): VLAN ID of the VLAN member entry.
- `ports` (multi { array-id }; mandatory): Member ports of the VLAN.
- `svl` (bool): FDB lookup mode for lookup in UFDB and MFDB.
  - `svl` - Shared VLAN Learning, learning/lookup is based on MAC addresses - not on VLAN IDs.
  - `ivl` - Independent VLAN Learning, learning/lookup is based on both MAC addresses and VLAN IDs.
- `learn` (bool): Enables or disables source MAC learning for VLAN.
- `flood` (bool): Enables or disables forced VLAN flooding per VLAN. If enabled, the result of the destination MAC lookup in the UFDB or MFDB is ignored, and the packet is forced to flood in the VLAN.
- `ingress-mirror` (bool): Enables the ingress mirror per VLAN to support the VLAN-based mirror function.
- `qos-group` (enum (none) { none:0xffffffff }): Defined QoS group from the QoS group menu.

## /interface/ethernet/switch/vlan

Syscap: rbswitch and oldswitch; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `switch` (enum; mandatory): Name of the switch for which the respective VLAN entry is intended.
- `vlan-id` (num; mandatory): VLAN ID of the VLAN member entry.
- `ports` (multi { array-id, port: enum }; mandatory): Member ports of the VLAN.
- `independent-learning` (bool): Whether to use shared-VLAN-learning (SVL) or independent-VLAN-learning (IVL).
