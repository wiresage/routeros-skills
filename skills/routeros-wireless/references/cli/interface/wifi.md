# /interface/wifi

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi

Type: Directory

**Flags**

- `M`: master
- `D`: dynamic
- `N`: network
- `B`: bound
- `X`: disabled
- `I`: inactive
- `R`: running

**Arguments**

- `test.sigmadut-params` (string; unset; syscap=ww2-sigmadut)
- `test.sigmadut-extra-params` (string; unset; syscap=ww2-sigmadut)
- `configuration` (enum; unset)
- `security` (enum; unset)
- `interworking` (enum; unset)
- `datapath` (enum; unset)
- `channel` (enum; unset)
- `aaa` (enum; unset)
- `steering` (enum; unset)
- `name` (string)
- `mtu` (num; unset)
- `l2mtu` (num; unset)
- `mac-address` (macAddr)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp; unset)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `disable-running-check` (bool; unset)
- `radio-mac` (macAddr; unset)
- `master-interface` (iface_enum; unset)
- `mld-name` (string; unset)
- `mld-interface` (iface_enum; unset)
- `test.dfs.ignore-radar` (bool; unset; syscap=dfstest)
- `test.dfs.ignore-cac` (bool; unset; syscap=dfstest)
- `test.dfs.duty-cycle` (bool; unset; syscap=dfstest)
- `configuration.mode` (enum: ap; unset)
- `configuration.ssid` (string; unset)
- `configuration.hide-ssid` (bool; unset)
- `configuration.max-sta-count` (num; unset)
- `configuration.multicast-helper` (enum: default | disabled | full | dhcp; unset)
- `configuration.tx-chains` (ubit (0, 1, 2, 3); unset)
- `configuration.rx-chains` (ubit (0, 1, 2, 3); unset)
- `configuration.guard-interval` (enum: any | long; unset)
- `configuration.country` (enum; unset)
- `configuration.installation` (enum: any | indoor | outdoor; unset)
- `configuration.load-balancing-group` (enum; unset)
- `configuration.distance` (enum (indoors | dynamic) { indoors:0, dynamic:0xffffffff }; unset)
- `configuration.hw-retries` (num; unset)
- `configuration.hw-protection-mode` (enum: none | rts-cts | cts-to-self; unset)
- `configuration.hw-protection-threshold` (num; unset)
- `configuration.frame-lifetime` (time; unset)
- `configuration.disconnect-timeout` (time; unset)
- `configuration.keepalive-frames` (enum: enabled | disabled; unset)
- `configuration.ssid` (string; unset)
- `configuration.mode` (enum: ap | station | station-bridge | station-pseudobridge; unset)
- `configuration.hide-ssid` (bool; unset)
- `configuration.beacon-interval` (time; unset)
- `configuration.dtim-period` (num; unset)
- `configuration.multicast-enhance` (enum: disabled | enabled; unset)
- `configuration.qos-classifier` (enum: priority | dscp-high-3-bits; unset)
- `configuration.station-roaming` (bool; unset)
- `configuration.max-clients` (num; unset)
- `configuration.hw-protection-mode` (enum: none | rts-cts | cts-to-self; unset)
- `configuration.country` (enum; unset)
- `configuration.chains` (ubit (0, 1, 2, 3, 4, 5, 6, 7); unset)
- `configuration.tx-chains` (ubit (); unset)
- `configuration.tx-power` (num; unset)
- `configuration.antenna-gain` (num; unset)
- `configuration.distance` (num; unset)
- `configuration.installation` (enum: outdoor | indoor; unset)
- `security.encryption` (ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256); unset)
- `security.group-encryption` (enum: tkip | ccmp | gcmp | ccmp-256 | gcmp-256; unset)
- `security.group-key-update` (time; unset)
- `security.passphrase` (string; unset)
- `security.multi-passphrase-group` (enum; unset)
- `security.disable-pmkid` (bool; unset)
- `security.management-protection` (enum: disabled | allowed | required; unset)
- `security.beacon-protection` (enum: disabled | enabled; unset)
- `security.management-encryption` (enum: cmac | gmac | cmac-256 | gmac-256; unset)
- `security.wps` (enum: disable | push-button; unset)
- `security.dh-groups` (ubit (19, 20, 21); unset)
- `security.sae-anti-clogging-threshold` (num; unset)
- `security.sae-max-failure-rate` (num; unset)
- `security.sae-pwe` (enum: hunting-and-pecking | hash-to-element | both; unset)
- `security.owe-transition-interface` (iface_enum { auto }; unset)
- `security.eap-methods` (multi { array-id, method: enum (tls | ttls | peap) }; unset)
- `security.eap-certificate-mode` (enum: verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl; unset)
- `security.eap-tls-certificate` (enum; unset)
- `security.eap-username` (string; unset)
- `security.eap-anonymous-identity` (string; unset)
- `security.eap-password` (string; unset)
- `security.eap-accounting` (bool; unset)
- `security.ft` (bool; unset)
- `security.ft-mobility-domain` (num; unset)
- `security.ft-over-ds` (bool; unset)
- `security.ft-reassociation-deadline` (time; unset)
- `security.ft-nas-identifier` (string; unset)
- `security.ft-r0-key-lifetime` (time; unset)
- `security.ft-preserve-vlanid` (bool; unset)
- `security.connect-group` (string; unset)
- `security.connect-priority` (super { connect-accept-priority: num , [connect-hold-priority] /num }; unset)
- `security.authentication-types` (ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192); unset)
- `interworking.network-type` (enum: private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard; unset)
- `interworking.internet` (bool; unset)
- `interworking.esr` (bool; unset)
- `interworking.uesa` (bool; unset)
- `interworking.venue` (enum (unspecified | disabled) { unspecified:0, disabled:0xffffffff }; unset)
- `interworking.hessid` (macAddr; unset)
- `interworking.hotspot20` (bool; unset)
- `interworking.hotspot20-dgaf` (bool; unset)
- `interworking.roaming-ois` (multi { array-id, roaming-oi: string }; unset)
- `interworking.venue-names` (object { venue-name: composite { venue-name-name: string , venue-name-lang: string } }; unset)
- `interworking.authentication-types` (object { authentication-type: composite { authentication-type-indicator: enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) , authentication-type-url: string } }; unset)
- `interworking.ipv4-availability` (enum: not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown; unset)
- `interworking.ipv6-availability` (enum: not-available | available | unknown; unset)
- `interworking.realms` (object { realm: composite { realm-name: string , realm-auth: enum (not-specified | eap-sim | eap-tls | eap-aka) } }; unset)
- `interworking.realms-raw` (multi { array-id, realm-raw: string }; unset)
- `interworking.3gpp-info` (object { 3gpp: composite { 3gpp-mcc: string , 3gpp-mnc: string } }; unset)
- `interworking.3gpp-info-raw` (string; unset)
- `interworking.domain-names` (multi { array-id, domain-name: string }; unset)
- `interworking.operator-names` (object { operator-name: composite { operator-name-name: string , operator-name-lang: string } }; unset)
- `interworking.wan-status` (enum: reserved | up | down | test; unset)
- `interworking.wan-symmetric` (bool; unset)
- `interworking.wan-at-capacity` (bool; unset)
- `interworking.wan-downlink` (num; unset)
- `interworking.wan-uplink` (num; unset)
- `interworking.wan-downlink-load` (num; unset)
- `interworking.wan-uplink-load` (num; unset)
- `interworking.wan-measurement-duration` (num; unset)
- `interworking.connection-capabilities` (object { connection-cap: composite { protocol: num , connection-cap2: composite { port: num , status: enum (closed | open | unknown) } } }; unset)
- `interworking.operational-classes` (multi { array-id, operational-class: num }; unset)
- `datapath.bridge` (iface_enum { none }; unset)
- `datapath.bridge-cost` (num; unset)
- `datapath.bridge-horizon` (num; unset)
- `datapath.openflow-switch` (enum; unset; syscap=openflow)
- `datapath.client-isolation` (bool; unset)
- `datapath.traffic-processing` (enum: on-cap | on-capsman | on-capsman-secure; unset)
- `datapath.vlan-id` (num; unset)
- `datapath.interface-list` (enum; unset)
- `channel.frequency` (object; unset)
- `channel.secondary-frequency` (multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled) , secondary-frequency-num: num } }; unset)
- `channel.band` (enum: 60ghz-ad | 5ghz-a | 5ghz-n | 5ghz-ac | 5ghz-ax | 5ghz-be | 2ghz-g | 2ghz-n | 2ghz-ax | 2ghz-be | s1ghz-ah | 6ghz-ax | 6ghz-be; unset)
- `channel.width` (enum: 20mhz | 20/40mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz | 20/40/80+80mhz | 20/40/80/160mhz | 20/40/80/160/320mhz | 1mhz | 1/2mhz | 1/2/4mhz | 1/2/4/8mhz | 2160mhz; unset)
- `channel.skip-dfs-channels` (enum: disabled | all | 10min-cac; unset)
- `channel.deprioritize-unii-3-4` (bool; unset)
- `channel.reselect-interval` (super { reselect-interval-min: time [1 .. 60*60*24*300] , [reselect-interval-max] ..time [1 .. 60*60*24*300] }; unset)
- `channel.reselect-time` (super { reselect-time-min: date , [reselect-time-max] ..date }; unset)
- `channel.preamble-puncturing` (alt { preamble-puncturing: enum (yes | no) }; unset)
- `channel.afc` (bool; unset)
- `aaa.username-format` (string; unset)
- `aaa.password-format` (string; unset)
- `aaa.called-format` (string; unset)
- `aaa.calling-format` (string; unset)
- `aaa.mac-caching` (alt { mac-caching-disable: enum (disabled) , mac-caching-time: time }; unset)
- `aaa.interim-update` (alt { interim-update-disable: enum (disabled) , interim-update-time: time [1 .. ] }; unset)
- `aaa.nas-identifier` (string; unset)
- `steering.neighbor-group` (multi { array-id, neighbor-group: string }; unset)
- `steering.rrm` (bool; unset)
- `steering.wnm` (bool; unset)
- `steering.2g-probe-delay` (bool; unset)
- `steering.transition-threshold` (num; unset)
- `steering.transition-threshold-time` (time; unset)
- `steering.transition-request-period` (time; unset)
- `steering.transition-request-count` (num; unset)
- `steering.transition-time` (alt { value: enum (unlimited | immediate) , time: time }; unset)

**Read-only arguments**

- `default-name` (string)
- `cap` (string)

## Commands

### /interface/wifi/devel

Type: Command

**Arguments**

- `mode` (enum (ap | sta) { ap:0x10000003, sta:0x10000004 }; unset)

### /interface/wifi/flat-snoop

Type: Command

**Flags**

- `M`: mikrotik-oui
- `L`: locally-administered-address
- `B`: multicast-address

**Arguments**

- `filter-type` (ubit (frequency, bsss, stas); unset)

**Read-only arguments**

- `num` (num)
- `type` (enum: freq | bss | sta)
- `address` (macAddr)
- `bss-address` (macAddr)
- `ssid` (string)
- `frequency` (num)
- `beacon-interval` (num)
- `rate-mbps` (string)
- `basic-rates-mbps` (string)
- `supported-rates-mbps` (string)
- `signal` (num)
- `snr` (num)
- `noise` (num)
- `seen-frame-count` (num)
- `beacon-size` (num)
- `first-beacon` (date)
- `last-seen` (time)
- `country` (string)
- `erp-info` (ubit (non-erp-present, use-protection, barker-preamble-mode))
- `rsn-capab` (ubit (preauth, no-pairwise, ptksa-rcntr-0, ptksa-rcntr-1, gtksa-rcntr-0, gtksa-rcntr-1, mfpr, mfpc, joint-multiband-assoc, peerkey, spp-amsdu-c, spp-amsdu-req, pbac, ext-keyid-unicast-frames, ocvc))
- `group-data-cipher` (enum: use-gcs | group-traffic-disallowed | wep40 | tkip | ccmp | wep104 | aes-cmac | gcmp | gcmp-256 | ccmp-256 | bip-gmac_128 | bip-gmac_256 | bip-cmac_256)
- `group-mgmt-cipher` (enum)
- `pairwise-ciphers` (multi { array-id, cipher: enum () })
- `rsn-akms` (multi { array-id, akm: enum (802.1x | psk | ft-802.1x | ft-psk | 802.1x-256 | psk-sha256 | tdls | sae | sae | ft-sae | ft-sae | ap-peerkey | 802.1x-b-256 | 802.1x-b-192 | ft-802.1x-sha384 | fils-sha256 | fils-sha384 | ft-fils-sha256 | ft-fils-sha384 | owe | ft-psk-sha384 | psk-sha384) { 802.1x:0xfac01, psk:0xfac02, ft-802.1x:0xfac03, ft-psk:0xfac04, 802.1x-256:0xfac05, psk-sha256:0xfac06, tdls:0xfac07, sae:0xfac08, sae:0xfac18, ft-sae:0xfac09, ft-sae:0xfac19, ap-peerkey:0xfac0a, 802.1x-b-256:0xfac0b, 802.1x-b-192:0xfac0c, ft-802.1x-sha384:0xfac0d, fils-sha256:0xfac0e, fils-sha384:0xfac0f, ft-fils-sha256:0xfac10, ft-fils-sha384:0xfac11, owe:0xfac12, ft-psk-sha384:0xfac13, psk-sha384:0xfac14 } })
- `pmkids` (multi { array-id, pmkid: string })
- `rsn` (string)
- `bss-on-time` (time)
- `sta-count` (num)
- `bss-count` (num)

### /interface/wifi/frequency-scan

Type: Command

**Flags**

- `R`: radar
- `P`: primary
- `S`: secondary

**Arguments**

- `rounds` (num)
- `save-file` (string)
- `frequency` (object; unset)

**Read-only arguments**

- `channel` (string)
- `networks` (num)
- `load` (num)
- `nf` (num)
- `max-signal` (num)
- `min-signal` (num)
- `srp-networks` (num)
- `srp-load` (num)

### /interface/wifi/liberate

Type: Command

### /interface/wifi/monitor

Type: Command

**Read-only arguments**

- `state` (string)
- `channel` (string)
- `ap-address` (macAddr)
- `registered-peers` (num)
- `authorized-peers` (num)
- `tx-power` (num)
- `channel-priorities` (multi { array-id, channel: string })
- `afc-status` (string)
- `afc-sp-rules` (multi { array-id, channel: string })
- `hw-protection-mode` (enum: none | rts-cts | cts-to-self)
- `mld-link-id` (num)

### /interface/wifi/reset-mac-address

Type: Command

### /interface/wifi/roam

Type: Command

**Arguments**

- `addr` (macAddr; unset)

### /interface/wifi/scan

Type: Command

**Flags**

- `A`: active

**Arguments**

- `rounds` (num)
- `save-file` (string)
- `frequency` (object; unset)

**Read-only arguments**

- `address` (macAddr)
- `ssid` (string)
- `channel` (string)
- `security` (multi { array-id, auth-type: enum (wpa2-eap | wpa2-psk | ft-eap | ft-wpa2-psk | wpa3-eap | wpa2-psk-sha2 | wpa3-psk | wpa3-psk-gd | ft-wpa3-psk | ft-wpa3-psk-gd | wpa3-eap-192 | ft-wpa3-eap-192 | owe | wpa-eap | wpa-psk | dpp) })
- `signal` (num)
- `nf` (num)
- `sta-count` (num)

### /interface/wifi/sniffer

Type: Command

**Arguments**

- `stream-address` (address (flags=46v))
- `stream-rate` (num)
- `stream-port` (num; unset)
- `pcap-file` (string; unset)
- `pcap-size-limit` (num; unset)
- `filter` (string; unset)
- `show-frame` (enum: no | yes | radiotap; unset)

**Read-only arguments**

- `num` (num)
- `wlan.addr1` (macAddr)
- `wlan.addr2` (macAddr)
- `wlan.addr3` (macAddr)
- `size` (num)
- `type` (string)
- `ssid` (string)
- `raw` (string)

### /interface/wifi/spectral-scan

Type: Command

**Arguments**

- `resolution` (enum: 312khz | 625khz | 1.25mhz | 2.5mhz | 5mhz | 10mhz | 20mhz | 40mhz | 80mhz)
- `data` (enum: min | max | avg)
- `range` (composite { start: num [2400000 .. 7000000] , end: num [2400000 .. 7000000] })
- `peak-mode` (enum: disabled | avg | max)
- `peak-hold-duration` (num)
- `show-interference` (bool)

**Read-only arguments**

- `freq` (num)
- `magn` (num)
- `peak` (num)
- `graph` (meter)
- `interference` (composite { type: enum (mwo | cw | wifi | cordless24 | cordless5 | bluetooth | fhss |) , rssi: num })

### /interface/wifi/trigger-radar

Syscap: dfstest; Type: Command

### /interface/wifi/wps-client

Type: Command

**Arguments**

- `ssid` (string)
- `mac-address` (macAddr)
- `create-profile` (string)
- `dpp-uri` (string)

**Read-only arguments**

- `status` (string)
- `ssid` (string)
- `mac-address` (macAddr)
- `manufacturer` (string)
- `model` (string)
- `passphrase` (string)
- `authentication` (string)
- `encryption` (string)

### /interface/wifi/wps-push-button

Type: Command
