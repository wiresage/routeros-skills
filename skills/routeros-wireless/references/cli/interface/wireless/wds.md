# /interface/wireless/wds

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/wds

Package: wireless-rep; Type: Directory

**Flags**

- `X`: disabled
- `R`: running
- `D`: dynamic

**Arguments**

- `name` (string)
- `mtu` (num)
- `l2mtu` (num)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `disable-running-check` (bool)
- `master-interface` (iface_enum)
- `wds-address` (macAddr)

**Read-only arguments**

- `mac-address` (macAddr)

## Commands

### /interface/wireless/wds/monitor

Package: wireless-rep; Type: Command

**Read-only arguments**

- `active` (bool)
