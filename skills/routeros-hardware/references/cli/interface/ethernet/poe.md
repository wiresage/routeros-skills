# /interface/ethernet/poe

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/poe

Syscap: (poe or poe-in); Type: Directory

**Arguments**

- `name` (string)
- `poe-out` (enum: off | auto-on | forced-on; syscap=(!poe-4p-power and poe))
- `poe-voltage` (enum: auto | low | high; syscap=poe)
- `poe-priority` (num; syscap=poe)
- `power-cycle-ping-enabled` (bool; syscap=poe)
- `power-cycle-ping-address` (alt { ip: ipAddr , ipv6: ip6Addr , mac: macAddr }; syscap=poe)
- `power-cycle-ping-timeout` (time; syscap=poe)
- `power-cycle-interval` (alt { symbolic-names: enum (none) , time-interval: time }; syscap=poe)

**Read-only arguments**

- `port-type` (enum: poe-out | poe-in | poe-in/poe-out; syscap=(poe or poe-in))

## Commands

### /interface/ethernet/poe/monitor

Syscap: (poe or poe-in); Type: Command

**Read-only arguments**

- `name` (string)
- `port-type` (enum: poe-out | poe-in | poe-in/poe-out; syscap=(poe or poe-in))
- `poe-out` (enum: off | auto-on | forced-on | forced-on-a | forced-on-bt; syscap=poe)
- `poe-voltage` (enum: auto | low | high; syscap=poe): PoE out voltage selection
- `poe-out-status` (enum: disabled | waiting-for-load | powered-on | overload | short-circuit | voltage-too-low | current-too-low | power-cycle | voltage-too-high | controller-error | controller-upgrade | voltage-on-poe-in | no-valid-PSU | controller-init | low-voltage-too-low | lldp-power-off | low-voltage-pd-detected)
- `poe-out-voltage` (num)
- `poe-out-current` (num)
- `poe-out-power` (num)
- `poe-out-power-pair` (enum: b | a | bt)
- `power-cycle-host-alive` (bool)
- `power-cycle-after` (time)

### /interface/ethernet/poe/power-cycle

Syscap: (poe or poe-in); Type: Command

**Arguments**

- `duration` (time)
