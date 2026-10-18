# /certificate/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/certificate/settings

Type: Settings Directory

**Arguments**

- `builtin-trust-store` (alt { all-none: enum (default | all | untrusted) , component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging) }): RouterOS provided CA certificates
- `current-defaults` (ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging))
- `crl-download` (bool): auto CRL download and update
- `crl-use` (bool): perform CRL checking when validating trust chain
- `crl-store` (enum: system | ram): CRL storage location
