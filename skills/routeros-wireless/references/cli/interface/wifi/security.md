# /interface/wifi/security

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/security

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `authentication-types` (ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192); unset)
- `encryption` (ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256); unset)
- `group-encryption` (enum: tkip | ccmp | gcmp | ccmp-256 | gcmp-256; unset)
- `group-key-update` (time; unset)
- `passphrase` (string; unset)
- `multi-passphrase-group` (enum; unset)
- `disable-pmkid` (bool; unset)
- `management-protection` (enum: disabled | allowed | required; unset)
- `beacon-protection` (enum: disabled | enabled; unset)
- `management-encryption` (enum: cmac | gmac | cmac-256 | gmac-256; unset)
- `wps` (enum: disable | push-button; unset)
- `dh-groups` (ubit (19, 20, 21); unset)
- `sae-anti-clogging-threshold` (num; unset)
- `sae-max-failure-rate` (num; unset)
- `sae-pwe` (enum: hunting-and-pecking | hash-to-element | both; unset)
- `owe-transition-interface` (iface_enum { auto }; unset)
- `eap-methods` (multi { array-id, method: enum (tls | ttls | peap) }; unset)
- `eap-certificate-mode` (enum: verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl; unset)
- `eap-tls-certificate` (enum; unset)
- `eap-username` (string; unset)
- `eap-anonymous-identity` (string; unset)
- `eap-password` (string; unset)
- `eap-accounting` (bool; unset)
- `ft` (bool; unset)
- `ft-mobility-domain` (num; unset)
- `ft-over-ds` (bool; unset)
- `ft-reassociation-deadline` (time; unset)
- `ft-nas-identifier` (string; unset)
- `ft-r0-key-lifetime` (time; unset)
- `ft-preserve-vlanid` (bool; unset)
- `connect-group` (string; unset)
- `connect-priority` (super { connect-accept-priority: num , [connect-hold-priority] /num }; unset)
