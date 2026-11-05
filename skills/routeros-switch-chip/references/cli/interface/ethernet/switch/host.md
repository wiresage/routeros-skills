# /interface/ethernet/switch/host

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/host

Syscap: rbswitch and oldswitch; Type: Directory

**Flags**

- `D`: dynamic
- `I`: invalid

**Arguments**

- `switch` (enum; mandatory): Name of the switch to which the MAC address is going to be assigned.
- `mac-address` (macAddr): Host's MAC address.
- `ports` (multi { array-id, port: alt { port: enum , trunk: iface_enum } }; mandatory): Name of the interface, a static MAC address can be mapped to more than one port, including the switch CPU port.
- `copy-to-cpu` (bool): Whether to send a frame copy to the switch CPU port from a frame with a matching MAC destination address (matching destination or source address for CRS3xx series switches).
- `redirect-to-cpu` (bool): Whether to redirect a frame to the switch CPU port from a frame with a matching MAC destination address (matching destination or source address for CRS3xx series switches).
- `drop` (bool): Whether to drop a frame with a matching MAC source address received on a certain port (matching destination or source address for CRS3xx series switches).
- `mirror` (bool): Whether to send a frame copy to the `mirror-target` port from a frame with a matching MAC destination address (matching destination or source address for CRS3xx series switches).
- `vlan-id` (num): VLAN ID for the statically added MAC address entry.
- `share-vlan-learned` (bool): Whether the static host MAC address lookup is used with shared-VLAN-learning (SVL) or independent-VLAN-learning (IVL).

**Read-only arguments**

- `timeout` (time)
