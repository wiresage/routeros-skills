# /caps-man/actual-interface-configuration

> Source: https://manual.mikrotik.com/docs/cli-reference/caps-man/actual-interface-configuration

Package: wireless-rep; Type: Directory

**Flags**

- `M`: master
- `D`: dynamic
- `B`: bound
- `X`: disabled
- `I`: inactive
- `R`: running

**Arguments**

- `name` (string)
- `mac-address` (macAddr)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `disable-running-check` (bool)
- `radio-mac` (macAddr)
- `master-interface` (iface_enum { none })
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
- `security.authentication-types` (ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap); unset)
- `security.encryption` (ubit (aes-ccm, tkip); unset)
- `security.group-encryption` (enum: aes-ccm | tkip; unset)
- `security.group-key-update` (time)
- `security.passphrase` (string; unset)
- `security.eap-methods` (multi { array-id, method: enum (eap-tls | passthrough) { eap-tls:13, passthrough:0xffffffff } }; unset)
- `security.eap-radius-accounting` (bool; unset)
- `security.tls-mode` (enum: verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)
- `security.tls-certificate` (enum (none) { none:0xffffffff })
- `security.disable-pmkid` (bool; unset)
- `mtu` (num)
- `l2mtu` (num)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `client-to-client-forwarding` (bool; unset)
- `bridge` (iface_enum; unset)
- `bridge-cost` (num; unset)
- `bridge-horizon` (num; unset)
- `openflow-switch` (enum; unset)
- `local-forwarding` (bool; unset)
- `vlan-mode` (enum: no-tag | use-tag | use-service-tag; unset)
- `vlan-id` (num; unset)
- `interface-list` (enum; unset)
- `channel.frequency` (multi { array-id, frequency: num }; unset)
- `channel.secondary-frequency` (multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled) , secondary-frequency-num: num } }; unset)
- `channel.control-channel-width` (enum: 5mhz | 10mhz | 20mhz | 40mhz-turbo; unset)
- `channel.band` (enum: 2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac; unset)
- `channel.extension-channel` (enum: disabled | Ce | eC | Ceee | eCee | eeCe | eeeC | XX | XXXX | Ceeeeeee | eCeeeeee | eeCeeeee | eeeCeeee | eeeeCeee | eeeeeCee | eeeeeeCe | eeeeeeeC | XXXXXXXX; unset)
- `channel.tx-power` (num; unset)
- `channel.save-selected` (bool; unset)
- `channel.reselect-interval` (super { reselect-interval-min: time [1 .. 60*60*24*300] , [reselect-interval-max] ..time [1 .. 60*60*24*300] }; unset)
- `channel.skip-dfs-channels` (bool; unset)
