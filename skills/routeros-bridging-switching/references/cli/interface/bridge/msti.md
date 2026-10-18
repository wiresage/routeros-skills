# /interface/bridge/msti

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge/msti

Type: Directory

**Flags**

- `X`: disabled
- `D`: dynamic

**Arguments**

- `identifier` (num; mandatory)
- `bridge` (iface_enum; mandatory)
- `priority` (alt { priority: enum (0x0000 | 0x1000 | 0x2000 | 0x3000 | 0x4000 | 0x5000 | 0x6000 | 0x7000 | 0x8000 | 0x9000 | 0xa000 | 0xb000 | 0xc000 | 0xd000 | 0xe000 | 0xf000) { 0x0000:0x0000, 0x1000:0x1000, 0x2000:0x2000, 0x3000:0x3000, 0x4000:0x4000, 0x5000:0x5000, 0x6000:0x6000, 0x7000:0x7000, 0x8000:0x8000, 0x9000:0x9000, 0xa000:0xa000, 0xb000:0xb000, 0xc000:0xc000, 0xd000:0xd000, 0xe000:0xe000, 0xf000:0xf000 } , priority: num [0 .. 65535] })
- `vlan-mapping` (multi { vlan-range: range [1 .. 4094] }; mandatory)

## Commands

### /interface/bridge/msti/monitor

Type: Command

**Read-only arguments**

- `state` (enum: disabled | disabled | enabled | enabled)
- `identifier` (num)
- `current-mac-address` (macAddr)
- `bridge-id` (composite { prio: num , mac: macAddr })
- `root-bridge` (bool)
- `regional-root-bridge-id` (composite { prio: num , mac: macAddr })
- `root-path-cost` (num)
- `root-port` (iface_enum)
- `port-count` (num)
- `designated-port-count` (num)
