# /interface/bridge/port

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge/port

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive
- `D`: dynamic
- `H`: hw-offload
- `Y`: managed

**Arguments**

- `interface` (alt { interface: iface_enum , interface-list: enum }; mandatory)
- `bridge` (iface_enum; mandatory)
- `priority` (enum (0x00 | 0x10 | 0x20 | 0x30 | 0x40 | 0x50 | 0x60 | 0x70 | 0x80 | 0x90 | 0xa0 | 0xb0 | 0xc0 | 0xd0 | 0xe0 | 0xf0) { 0x00:0x00, 0x10:0x10, 0x20:0x20, 0x30:0x30, 0x40:0x40, 0x50:0x50, 0x60:0x60, 0x70:0x70, 0x80:0x80, 0x90:0x90, 0xa0:0xa0, 0xb0:0xb0, 0xc0:0xc0, 0xd0:0xd0, 0xe0:0xe0, 0xf0:0xf0 })
- `path-cost` (num)
- `internal-path-cost` (num)
- `edge` (enum: auto | yes | no | yes-discover | no-discover)
- `point-to-point` (enum: auto | yes | no)
- `learn` (enum: auto | yes | no)
- `horizon` (num)
- `hw` (bool)
- `auto-isolate` (bool)
- `restricted-role` (bool)
- `restricted-tcn` (bool)
- `pvid` (num)
- `frame-types` (enum: admit-all | admit-only-vlan-tagged | admit-only-untagged-and-priority-tagged)
- `ingress-filtering` (bool)
- `unknown-unicast-flood` (bool)
- `unknown-multicast-flood` (bool)
- `broadcast-flood` (bool)
- `tag-stacking` (bool)
- `bpdu-guard` (bool)
- `trusted` (bool)
- `trusted-ra` (bool)
- `trusted-dhcpv6` (bool)
- `trusted-arp` (bool)
- `mvrp-registrar-state` (enum: normal | fixed)
- `mvrp-applicant-state` (enum: normal-participant | non-participant)
- `multicast-router` (enum: disabled | temporary-query | permanent)
- `fast-leave` (bool)

**Read-only arguments**

- `parent` (enum)
- `status` (enum: inactive | in-bridge | in-bridge | disabled)
- `port-id` (composite { priority: num , number: num })
- `role` (enum: disabled-port | root-port | designated-port | alternate-port | backup-port)
- `edge-port` (bool)
- `edge-port-discovery` (bool)
- `point-to-point-port` (bool)
- `external-fdb-status` (bool)
- `sending-rstp` (bool)
- `learning` (bool)
- `forwarding` (bool)
- `actual-path-cost` (num)
- `root-path-cost` (num)
- `internal-root-path-cost` (num)
- `designated-bridge-id` (composite { number: num , address: macAddr })
- `designated-cost` (num)
- `designated-port-id` (composite { priority: num , number: num })
- `tx-bpdu` (num)
- `rx-bpdu` (num)
- `discard-transitions` (num)
- `forward-transitions` (num)
- `tx-tc` (num)
- `rx-tc` (num)
- `topology-changes` (num)
- `last-topology-change` (time)
- `multicast-router` (bool)
- `hw-offload-group` (enum)
- `declared-vlan-ids` (multi { vlan-range: range })
- `registered-vlan-ids` (multi { vlan-range: range })
- `hw-offload` (bool)
- `debug-info` (string)

## Commands

### /interface/bridge/port/monitor

Type: Command

**Read-only arguments**

- `interface` (alt { interface: iface_enum , interface-list: enum })
- `status` (enum: inactive | in-bridge | in-bridge | disabled)
- `port-id` (composite { priority: num , number: num })
- `role` (enum: disabled-port | root-port | designated-port | alternate-port | backup-port)
- `edge-port` (bool)
- `edge-port-discovery` (bool)
- `point-to-point-port` (bool)
- `external-fdb` (bool)
- `sending-rstp` (bool)
- `learning` (bool)
- `forwarding` (bool)
- `actual-path-cost` (num)
- `root-path-cost` (num)
- `internal-root-path-cost` (num)
- `designated-bridge-id` (composite { number: num , address: macAddr })
- `designated-cost` (num)
- `designated-internal-cost` (num)
- `designated-port-id` (composite { priority: num , number: num })
- `designated-message-age` (num)
- `designated-max-age` (num)
- `designated-remaining-hops` (num)
- `tx-rx-bpdu` (composite { tx: num , rx: num })
- `discard-transitions` (num)
- `forward-transitions` (num)
- `tx-rx-tc` (composite { tx: num , rx: num })
- `topology-changes` (num)
- `last-topology-change` (time)
- `multicast-router` (bool)
- `hw-offload-group` (enum)
- `declared-vlan-ids` (multi { vlan-range: range })
- `registered-vlan-ids` (multi { vlan-range: range })
