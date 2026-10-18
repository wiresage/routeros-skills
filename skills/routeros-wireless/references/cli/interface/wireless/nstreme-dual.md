# /interface/wireless/nstreme-dual

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/nstreme-dual

Package: wireless-rep; Type: Directory

**Flags**

- `X`: disabled
- `R`: running

**Arguments**

- `name` (string)
- `mtu` (num)
- `l2mtu` (num)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `disable-running-check` (bool)
- `tx-radio` (iface_enum)
- `rx-radio` (iface_enum)
- `remote-mac` (macAddr)
- `tx-band` (enum: 2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n)
- `tx-channel-width` (enum: 20mhz | 40mhz | 10mhz | 5mhz)
- `tx-frequency` (num)
- `rx-band` (enum: 2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n)
- `rx-channel-width` (enum: 20mhz | 40mhz | 10mhz | 5mhz)
- `rx-frequency` (num)
- `disable-csma` (bool)
- `rates-b` (ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps))
- `rates-a/g` (ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps))
- `ht-rates` (ubit (1, 2, 3, 4, 5, 6, 7, 8))
- `ht-guard-interval` (enum: long | short | both)
- `ht-channel-width` (enum: 20mhz | 40mhz | 2040mhz)
- `ht-streams` (enum: single | double | both)
- `framer-policy` (enum: none | best-fit | exact-size)
- `framer-limit` (num)

**Read-only arguments**

- `mac-address` (macAddr)

## Commands

### /interface/wireless/nstreme-dual/monitor

Package: wireless-rep; Type: Command

**Read-only arguments**

- `rx-signal-strength` (num)
- `tx-signal-strength` (num)
- `rx-rate` (string)
- `tx-rate` (string)
- `connected` (bool)
- `packets` (composite { tx: num , rx: num })
- `bytes` (composite { tx: num , rx: num })
- `frames` (composite { tx: num , rx: num })
- `frame-bytes` (composite { tx: num , rx: num })
- `hw-frames` (composite { tx: num , rx: num })
- `hw-frame-bytes` (composite { tx: num , rx: num })
- `tx-retries-timeout` (num)
- `tx-retries-lost` (num)
- `rx-bad-seqs` (num)
- `rx-duplicates` (num)

### /interface/wireless/nstreme-dual/reset-counters

Package: wireless-rep; Type: Command
