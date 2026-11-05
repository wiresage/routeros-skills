# /interface/ethernet/switch/multicast-fdb

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/multicast-fdb

Syscap: musicswitch; Type: Directory

CRS125 switch-chip supports up to 1024 entries in the MFDB for multicast forwarding. For each multicast packet, destination MAC or destination IP lookup is performed in the MFDB. MFDB entries are not automatically learned and can only be configured.

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic

**Arguments**

- `address` (alt { mac-address: macAddr , ip-address: ipAddr }; mandatory): Matching IP address or MAC address for multicast packets.
- `ports` (multi { array-id }; mandatory): Member ports for multicast traffic.
- `vlan-id` (num): Multicast FDB lookup VLAN ID. If the VLAN learning mode is IVL, VLAN id is lookup id, otherwise VLAN id = 0.
- `svl` (bool): Multicast FDB learning mode.
  - `svl` - Shared VLAN Learning, learning/lookup is based on MAC addresses - not on VLAN IDs.
  - `ivl` - Independent VLAN Learning, learning/lookup is based on both MAC addresses and VLAN IDs.
- `bypass-vlan-filter` (bool): Allows bypassing VLAN filtering for matching multicast packets.
- `qos-group` (enum (none) { none:0xffffffff }): Defined QoS group from QoS group menu.
