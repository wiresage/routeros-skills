# /interface/bridge/vlan

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge/vlan

Type: Directory

**Flags**

- `Y`: managed
- `X`: disabled
- `D`: dynamic

**Arguments**

- `bridge` (iface_enum; mandatory)
- `vlan-ids` (multi { vlan-range: range [1 .. 4094] }; mandatory)
- `tagged` (multi { array-id, interface: alt { interface: iface_enum , interface-list: enum } })
- `untagged` (multi { array-id, interface: alt { interface: iface_enum , interface-list: enum } })
- `mvrp-forbidden` (multi { array-id, interface: alt { interface: iface_enum , interface-list: enum } })

**Read-only arguments**

- `current-tagged` (multi { array-id, interface: iface_enum })
- `current-untagged` (multi { array-id, interface: iface_enum })
