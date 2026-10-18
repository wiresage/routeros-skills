# /interface/wireless/security-profiles

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/security-profiles

Package: wireless-rep; Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string; mandatory)
- `mode` (enum: none | static-keys-optional | static-keys-required | dynamic-keys)
- `authentication-types` (ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap))
- `unicast-ciphers` (ubit (tkip, aes-ccm))
- `group-ciphers` (ubit (tkip, aes-ccm))
- `wpa-pre-shared-key` (string)
- `wpa2-pre-shared-key` (string)
- `supplicant-identity` (string)
- `eap-methods` (multi { array-id, method: enum (eap-tls | eap-ttls-mschapv2 | peap | passthrough) { eap-tls:13, eap-ttls-mschapv2:21, peap:25, passthrough:0xffffffff } })
- `tls-mode` (enum: verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)
- `tls-certificate` (enum (none) { none:0xffffffff })
- `mschapv2-username` (string)
- `mschapv2-password` (string)
- `disable-pmkid` (bool)
- `static-algo-0` (enum)
- `static-key-0` (string)
- `static-algo-1` (enum)
- `static-key-1` (string)
- `static-algo-2` (enum)
- `static-key-2` (string)
- `static-algo-3` (enum)
- `static-key-3` (string)
- `static-transmit-key` (enum: key-0 | key-1 | key-2 | key-3)
- `static-sta-private-algo` (enum)
- `static-sta-private-key` (string)
- `radius-mac-authentication` (bool)
- `radius-mac-accounting` (bool)
- `radius-eap-accounting` (bool)
- `interim-update` (time)
- `radius-mac-format` (enum (XX:XX:XX:XX:XX:XX | XXXX:XXXX:XXXX | XXXXXX:XXXXXX | XX-XX-XX-XX-XX-XX | XXXXXX-XXXXXX | XXXXXXXXXXXX | XX XX XX XX XX XX | xx:xx:xx:xx:xx:xx | xxxx:xxxx:xxxx | xxxxxx:xxxxxx | xx-xx-xx-xx-xx-xx | xxxxxx-xxxxxx | xxxxxxxxxxxx | xx xx xx xx xx xx) { XX:XX:XX:XX:XX:XX:0, XXXX:XXXX:XXXX:1, XXXXXX:XXXXXX:2, XX-XX-XX-XX-XX-XX:3, XXXXXX-XXXXXX:4, XXXXXXXXXXXX:5, XX XX XX XX XX XX:6, xx:xx:xx:xx:xx:xx:7, xxxx:xxxx:xxxx:8, xxxxxx:xxxxxx:9, xx-xx-xx-xx-xx-xx:10, xxxxxx-xxxxxx:11, xxxxxxxxxxxx:12, xx xx xx xx xx xx:13 })
- `radius-mac-mode` (enum: as-username | as-username-and-password)
- `radius-called-format` (enum: mac:ssid | mac | ssid)
- `radius-mac-caching` (alt { radius-mac-caching-disable: enum (disabled) , radius-mac-caching-time: time })
- `group-key-update` (time)
- `management-protection` (enum: allowed | required | disabled)
- `management-protection-key` (string)
