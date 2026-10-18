# /interface/bridge/port/mst-override

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge/port/mst-override

Type: Directory

**Flags**

- `X`: disabled
- `D`: dynamic

**Arguments**

- `interface` (iface_enum; mandatory)
- `identifier` (num; mandatory)
- `priority` (enum (0x00 | 0x10 | 0x20 | 0x30 | 0x40 | 0x50 | 0x60 | 0x70 | 0x80 | 0x90 | 0xa0 | 0xb0 | 0xc0 | 0xd0 | 0xe0 | 0xf0) { 0x00:0x00, 0x10:0x10, 0x20:0x20, 0x30:0x30, 0x40:0x40, 0x50:0x50, 0x60:0x60, 0x70:0x70, 0x80:0x80, 0x90:0x90, 0xa0:0xa0, 0xb0:0xb0, 0xc0:0xc0, 0xd0:0xd0, 0xe0:0xe0, 0xf0:0xf0 })
- `internal-path-cost` (num)

**Read-only arguments**

- `debug-info` (string)

## Commands

### /interface/bridge/port/mst-override/monitor

Type: Command

**Read-only arguments**

- `port` (iface_enum)
- `status` (enum: inactive | in-bridge | in-bridge | disabled)
- `identifier` (num)
- `port-id` (composite { priority: num , number: num })
- `role` (enum: disabled-port | root-port | designated-port | alternate-port | backup-port | master-port)
- `learning` (bool)
- `forwarding` (bool)
- `internal-root-path-cost` (num)
- `designated-bridge-id` (composite { number: num , address: macAddr })
- `designated-cost` (num)
- `designated-internal-cost` (num)
- `designated-port-id` (composite { priority: num , number: num })
- `designated-remaining-hops` (num)
- `tx-rx-bpdu` (composite { tx: num , rx: num })
- `discard-transitions` (num)
- `forward-transitions` (num)
- `tx-rx-tc` (composite { tx: num , rx: num })
- `topology-changes` (num)
- `last-topology-change` (time)
