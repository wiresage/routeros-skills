# /interface/ethernet/switch/reserved-fdb

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/reserved-fdb

Syscap: musicswitch; Type: Directory

Cloud Router Switch supports 256 RFDB entries. Each RFDB entry can store either a Layer2 unicast or multicast MAC address with specific commands.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `mac-address` (macAddr; mandatory): Matching MAC address for Reserved FDB entry.
- `action` (enum: forward | redirect-to-cpu | copy-to-cpu | drop): Action for RFDB entry.
  - `copy-to-cpu` - packets are copied to the CPU when their destination MAC matches the entry.
  - `drop` - packets are dropped when their destination MAC matches the entry.
  - `forward` - packets are forwarded when their destination MAC matches the entry.
  - `redirect-to-cpu` - packets are redirected to the CPU when their destination MAC matches the entry.
- `bypass-ingress-vlan-filter` (bool): Allows bypassing VLAN filtering for matching packets.
- `bypass-ingress-port-policing` (bool): Allows bypassing Ingress Port Policer for matching packets.
- `qos-group` (enum (none) { none:0xffffffff }): Defined QoS group from QoS group menu.
