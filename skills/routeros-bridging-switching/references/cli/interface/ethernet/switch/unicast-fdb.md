# /interface/ethernet/switch/unicast-fdb

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/unicast-fdb

Syscap: musicswitch; Type: Directory

The unicast forwarding database supports up to 16K MAC entries.

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic
- `A`: active

**Arguments**

- `mac-address` (macAddr; mandatory): The action command applies to the packet when the destination MAC or source MAC matches the entry.
- `port` (alt { port: enum , trunk: enum }; mandatory): Matching port for the Unicast FDB entry.
- `vlan-id` (num): Unicast FDB lookup/learning VLAN id.
- `action` (enum: forward | src-drop | dst-drop | src-and-dst-drop | ingress-port-policing-bypass | src-redirect-to-cpu | dst-redirect-to-cpu | src-and-dst-redirect-to-cpu): Action for UFDB entry.
  - `dst-drop` - packets are dropped when their destination MAC matches the entry.
  - `dst-redirect-to-cpu` - packets are redirected to the CPU when their destination MAC matches the entry.
  - `forward` - packets are forwarded.
  - `src-and-dst-drop` - packets are dropped when their source MAC or destination MAC matches the entry.
  - `src-and-dst-redirect-to-cpu` - packets are redirected to CPU when their source MAC or destination MAC matches the entry.
  - `src-drop` - packets are dropped when their source MAC matches the entry.
  - `src-redirect-to-cpu` - packets are redirected to the CPU when their source MAC matches the entry.
- `mirror` (bool): Enables or disables mirroring based on source MAC or destination MAC.
- `isolation-profile` (enum: promiscuous | isolated | community1 | community2): MAC level isolation profile.
- `svl` (bool): Unicast FDB learning mode.
  - `svl` - Shared VLAN Learning, learning/lookup is based on MAC addresses - not on VLAN IDs.
  - `ivl` - Independent VLAN Learning, learning/lookup is based on both MAC addresses and VLAN IDs.
- `qos-group` (enum (none) { none:0xffffffff }): Defined QoS group from the QoS group menu.

**Read-only arguments**

- `age` (num)

## Commands

### /interface/ethernet/switch/unicast-fdb/flush

Syscap: musicswitch; Type: Command
