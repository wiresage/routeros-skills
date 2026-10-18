# /interface/wireless

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless

Package: wireless-rep; Type: Directory

**Flags**

- `X`: disabled
- `R`: running

**Arguments**

- `name` (string)
- `mtu` (num)
- `l2mtu` (num)
- `mac-address` (macAddr)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `disable-running-check` (bool)
- `prism-cardtype` (enum: 200mW | 100mW | 30mW)
- `master-interface` (iface_enum; mandatory)
- `radio-name` (string)
- `mode` (enum: station | station-wds | ap-bridge | bridge | alignment-only | nstreme-dual-slave | wds-slave | station-pseudobridge | station-pseudobridge-clone | station-bridge)
- `ssid` (string)
- `area` (string)
- `frequency-mode` (enum)
- `country` (enum)
- `installation` (enum: any | indoor | outdoor)
- `antenna-gain` (num)
- `frequency` (alt { frequency-mhz: num , frequency-name: enum (auto) })
- `band` (enum: 2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)
- `channel-width` (enum: 20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC | 20/40/80/160mhz-Ceeeeeee | 20/40/80/160mhz-eCeeeeee | 20/40/80/160mhz-eeCeeeee | 20/40/80/160mhz-eeeCeeee | 20/40/80/160mhz-eeeeCeee | 20/40/80/160mhz-eeeeeCee | 20/40/80/160mhz-eeeeeeCe | 20/40/80/160mhz-eeeeeeeC | 20/40mhz-XX | 20/40/80mhz-XXXX | 20/40/80/160mhz-XXXXXXXX)
- `secondary-frequency` (multi { array-id, secondary-channel: enum (auto) { auto:0xffffffff } })
- `scan-list` (object { entry: alt { default: enum (default) , range: super { range-start: num , [range-end] -num , [range-step] [ :num] } , name: enum () } })
- `wireless-protocol` (enum: unspecified | any | 802.11 | nstreme | nv2 | nv2-nstreme-802.11 | nv2-nstreme)
- `rate-set` (enum: default | configured)
- `supported-rates-b` (ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps))
- `supported-rates-a/g` (ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps))
- `basic-rates-b` (ubit (1Mbps, 2Mbps, 5.5Mbps, 11Mbps))
- `basic-rates-a/g` (ubit (6Mbps, 9Mbps, 12Mbps, 18Mbps, 24Mbps, 36Mbps, 48Mbps, 54Mbps))
- `max-station-count` (num)
- `distance` (enum (indoors | dynamic) { indoors:0, dynamic:0xffffffff })
- `tx-power` (num)
- `tx-power-mode` (enum: default | all-rates-fixed | card-rates | manual-table)
- `noise-floor-threshold` (alt { default: enum (default) , threshold: num [-128 .. 127] })
- `nv2-noise-floor-offset` (alt { default: enum (default) , threshold: num [0 .. 20] })
- `burst-time` (enum: disabled)
- `dfs-test-mode` (ubit (only-detect, duty-cycle, short-search); syscap=dfstest)
- `antenna-mode` (enum: ant-a | ant-b | txa-rxb | rxa-txb)
- `vlan-mode` (enum: no-tag | use-tag | use-service-tag)
- `vlan-id` (num)
- `wds-mode` (enum: disabled | static | dynamic | static-mesh | dynamic-mesh)
- `wds-default-bridge` (iface_enum { none:0xffffffff })
- `wds-default-cost` (num)
- `wds-cost-range` (range)
- `wds-ignore-ssid` (bool)
- `update-stats-interval` (alt { disabled: enum (disabled) , interval: time [10 .. 18000] })
- `bridge-mode` (enum: enabled | disabled)
- `default-authentication` (bool)
- `default-forwarding` (bool)
- `default-ap-tx-limit` (num)
- `default-client-tx-limit` (num)
- `wmm-support` (enum: disabled | enabled | required)
- `hide-ssid` (bool)
- `security-profile` (enum)
- `interworking-profile` (enum: disabled)
- `wps-mode` (enum: disabled | push-button | push-button-virtual-only | push-button-5s)
- `station-roaming` (enum: disabled | enabled)
- `disconnect-timeout` (time)
- `on-fail-retry-time` (time)
- `preamble-mode` (enum: long | short | both)
- `compression` (bool)
- `allow-sharedkey` (bool)
- `station-bridge-clone-mac` (macAddr)
- `ampdu-priorities` (ubit (0, 1, 2, 3, 4, 5, 6, 7))
- `guard-interval` (enum: any | long)
- `ht-supported-mcs` (ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23, mcs-24, mcs-25, mcs-26, mcs-27, mcs-28, mcs-29, mcs-30, mcs-31))
- `ht-basic-mcs` (ubit (mcs-0, mcs-1, mcs-2, mcs-3, mcs-4, mcs-5, mcs-6, mcs-7, mcs-8, mcs-9, mcs-10, mcs-11, mcs-12, mcs-13, mcs-14, mcs-15, mcs-16, mcs-17, mcs-18, mcs-19, mcs-20, mcs-21, mcs-22, mcs-23, mcs-24, mcs-25, mcs-26, mcs-27, mcs-28, mcs-29, mcs-30, mcs-31))
- `vht-supported-mcs` (multi { array-id, mcs-set: enum (none | mcs0-7 | mcs0-8 | mcs0-9) })
- `vht-basic-mcs` (multi { array-id, mcs-set: enum (none | mcs0-7 | mcs0-8 | mcs0-9) })
- `tx-chains` (ubit (0, 1, 2, 3))
- `rx-chains` (ubit (0, 1, 2, 3))
- `amsdu-limit` (num)
- `amsdu-threshold` (num)
- `tdma-period-size` (enum: auto | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10)
- `nv2-queue-count` (num)
- `nv2-qos` (enum: default | frame-priority)
- `nv2-cell-radius` (num)
- `nv2-security` (enum: disabled | enabled)
- `nv2-preshared-key` (string)
- `nv2-mode` (enum: dynamic-downlink | fixed-downlink | sync-master | sync-slave)
- `nv2-downlink-ratio` (num)
- `nv2-sync-secret` (string)
- `hw-retries` (num)
- `frame-lifetime` (num)
- `adaptive-noise-immunity` (enum: none | client-mode | ap-and-client-mode)
- `hw-fragmentation-threshold` (num)
- `hw-protection-mode` (enum: none | rts-cts | cts-to-self)
- `hw-protection-threshold` (num)
- `frequency-offset` (num)
- `rate-selection` (enum: advanced)
- `multicast-helper` (enum: default | disabled | full | dhcp)
- `multicast-buffering` (enum: enabled | disabled)
- `keepalive-frames` (enum: enabled | disabled)
- `skip-dfs-channels` (enum: disabled | all | 10min-cac)

**Read-only arguments**

- `default-name` (string)
- `interface-type` (enum: virtual | Atheros AR5212 | Atheros AR5211 | Atheros AR5210 | Prism | Atheros AR5213 | Atheros AR5413 | Atheros 11N | Atheros AR9271 | Atheros AR9300 | Atheros AR92xx | Atheros AR9888 | IPQ4019 | QCA9984 | QCA9888)
- `pci-info` (string)

## Commands

### /interface/wireless/frequency-monitor

Package: wireless-rep; Type: Command

**Read-only arguments**

- `freq` (num)
- `use` (num)
- `nf` (num)

### /interface/wireless/monitor

Package: wireless-rep; Type: Command

**Read-only arguments**

- `status` (enum: disabled | searching-for-network | connected-to-ess | initializing | searching-for-frequency | radar-detecting | running-ap | tkip-countermeasures | nstreme-dual-slave)
- `status-reason` (string)
- `channel` (string)
- `wireless-protocol` (enum: 802.11 | nstreme | nv2)
- `nstreme-status` (enum: ok | degraded)
- `tx-rate` (string)
- `rx-rate` (string)
- `ssid` (string)
- `bssid` (macAddr)
- `radio-name` (string)
- `signal-strength` (num)
- `signal-strength-ch0` (num)
- `signal-strength-ch1` (num)
- `signal-strength-ch2` (num)
- `signal-strength-ch3` (num)
- `tx-signal-strength` (num)
- `tx-signal-strength-ch0` (num)
- `tx-signal-strength-ch1` (num)
- `tx-signal-strength-ch2` (num)
- `tx-signal-strength-ch3` (num)
- `noise-floor` (num)
- `signal-to-noise` (num)
- `tx-ccq` (num)
- `rx-ccq` (num)
- `p-throughput` (num)
- `overall-tx-ccq` (num)
- `registered-clients` (num)
- `authenticated-clients` (num)
- `current-ack-timeout` (num)
- `current-distance` (num)
- `wds-link` (bool)
- `bridge` (bool)
- `nstreme` (bool)
- `polling` (bool)
- `csma-disabled` (bool)
- `framing-mode` (enum: none | best-fit | exact-size)
- `framing-limit` (num)
- `framing-current-size` (num)
- `routeros-version` (string)
- `last-ip` (ipAddr)
- `802.1x-port-enabled` (bool)
- `authentication-type` (enum: wpa-psk | wpa2-psk | wpa-eap | wpa2-eap)
- `encryption` (enum)
- `group-encryption` (enum)
- `management-protection` (bool)
- `compression` (bool)
- `wmm-enabled` (bool)
- `nv2-sync-state` (enum: searching | syncing | synced)
- `nv2-sync-master` (macAddr)
- `nv2-sync-distance` (num)
- `nv2-sync-period-size` (num)
- `nv2-sync-downlink-ratio` (num)
- `current-tx-powers` (multi { current-tx-power: super { rate: enum () , [tx-power] :num , [tx-power-real] (num , tx-power-total: num } })
- `current-ofdm-errors` (num)
- `current-cck-errors` (num)
- `1s-frames` (composite { compressed: num , total: num })
- `1s-compressed-frames` (num)
- `1s-bytes` (composite { compressed: num , total: num })
- `1s-length-of-orig` (num)
- `total-frames` (composite { compressed: num , total: num })
- `total-compressed-frames` (num)
- `total-bytes` (composite { compressed: num , total: num })
- `total-length-of-orig` (num)
- `notify-external-fdb` (bool)
- `cloned-mac-address` (macAddr)
- `searching-for-address-to-clone` (bool)

### /interface/wireless/reset-configuration

Package: wireless-rep; Type: Command

### /interface/wireless/reset-mac-address

Package: wireless-rep; Type: Command

### /interface/wireless/scan

Package: wireless-rep; Type: Command

**Flags**

- `A`: active
- `P`: privacy
- `R`: routeros-network
- `N`: nstreme
- `T`: tdma
- `W`: wds
- `B`: bridge

**Arguments**

- `background` (bool)
- `save-file` (string)
- `rounds` (num)
- `passive` (bool)

**Read-only arguments**

- `address` (macAddr)
- `ssid` (string)
- `channel` (string)
- `sig` (num)
- `nf` (num)
- `snr` (num)
- `radio-name` (string)
- `routeros-version` (string)

### /interface/wireless/setup-repeater

Package: wireless-rep; Type: Command

**Arguments**

- `address` (macAddr)
- `ssid` (string)
- `passphrase` (string)
- `country` (enum)

**Read-only arguments**

- `status` (string)

### /interface/wireless/spectral-scan

Package: wireless-rep; Type: Command

**Arguments**

- `range` (alt { range: range [ .. 7000] , band: enum (2.4ghz | 5ghz | current-channel) })
- `show-interference` (bool)
- `samples` (num)
- `buckets` (num)
- `peak-hold-time` (time)
- `save-file-name` (string)

**Read-only arguments**

- `freq` (num)
- `interference` (composite { type: enum (none | bluetooth-headset | bluetooth-stereo | cordless-phone | microwave-oven | cwa | video-bridge | wifi) { none:0xffffffff, bluetooth-headset:0, bluetooth-stereo:1, cordless-phone:2, microwave-oven:3, cwa:4, video-bridge:5, wifi:6 } , rssi: num })
- `dbm` (num)
- `graph` (meter)

### /interface/wireless/wps-client

Package: wireless-rep; Type: Command

**Arguments**

- `ssid` (string)
- `mac-address` (macAddr)
- `create-profile` (string)

**Read-only arguments**

- `status` (string)
- `ssid` (string)
- `mac-address` (macAddr)
- `passphrase` (string)
- `authentication` (string)
- `encryption` (string)

### /interface/wireless/wps-push-button

Package: wireless-rep; Type: Command
