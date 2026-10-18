# /caps-man/security

> Source: https://manual.mikrotik.com/docs/cli-reference/caps-man/security

Package: wireless-rep; Type: Directory

**Arguments**

- `name` (string; mandatory)
- `authentication-types` (ubit (wpa-psk, wpa2-psk, wpa-eap, wpa2-eap); unset)
- `encryption` (ubit (aes-ccm, tkip); unset)
- `group-encryption` (enum: aes-ccm | tkip; unset)
- `group-key-update` (time)
- `passphrase` (string; unset)
- `eap-methods` (multi { array-id, method: enum (eap-tls | passthrough) { eap-tls:13, passthrough:0xffffffff } }; unset)
- `eap-radius-accounting` (bool; unset)
- `tls-mode` (enum: verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl)
- `tls-certificate` (enum (none) { none:0xffffffff })
- `disable-pmkid` (bool; unset)
