# /interface/w60g/station

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/w60g/station

Syscap: 60ghz; Package: wireless-rep; Type: Directory

**Flags**

- `X`: disabled
- `R`: running

**Arguments**

- `name` (string)
- `parent` (iface_enum)
- `remote-address` (macAddr)
- `mtu` (num)
- `mac-address` (macAddr)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `put-in-bridge` (iface_enum { none:0, parent:0xffffffff })

**Read-only arguments**

- `default-name` (string)
- `beamforming-event` (num)

## Commands

### /interface/w60g/station/monitor

Syscap: 60ghz; Package: wireless-rep; Type: Command

**Read-only arguments**

- `connected` (bool)
- `remote` (macAddr)
- `tx-mode` (enum: dmg | edmg-cb1 | edmg-cb2 | edmg-cb1-long-ldpc | edmg-cb2-long-ldpc)
- `tx-mcs` (num)
- `tx-phy-rate` (num)
- `signal` (num)
- `rssi` (num)
- `tx-sector` (num)
- `tx-sector-info` (string)
- `distance` (num)
