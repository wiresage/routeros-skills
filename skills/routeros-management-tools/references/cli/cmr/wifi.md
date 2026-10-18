# /cmr/wifi

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/wifi

Package: cmr; Type: Directory

A WiFi network definition replicated to the selected devices. The arguments extend the standard RouterOS `/interface/wifi` configuration parameters.

**Flags**

- `X` (disabled): WiFi network is disabled.

**Arguments**

- `labels` (object; unset): Select the devices the WiFi network is replicated to using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.
- `vlan-id` (num; unset): VLAN ID applied to the network: none (default) or 1-4095.
- `mlo` (bool; unset): Enable MLO (Multi-Link Operation).
- `ssid` (string; unset): Network SSID.
- `mode` (enum: ap | station | station-bridge | station-pseudobridge; unset): Network operating mode.
- `hide-ssid` (bool; unset): Hide the SSID in beacon frames.
- `beacon-interval` (time; unset): Beacon interval.
- `dtim-period` (num; unset): DTIM period.
- `multicast-enhance` (enum: disabled | enabled; unset): Multicast enhancement: `disabled` or `enabled`.
- `qos-classifier` (enum: priority | dscp-high-3-bits; unset): QoS classifier: `priority` or `dscp-high-3-bits`.
- `station-roaming` (bool; unset): Enable station roaming.
- `max-clients` (num; unset): Maximum number of connected clients.
- `hw-protection-mode` (enum: none | rts-cts | cts-to-self; unset): Hardware protection mode: `none`, `rts-cts`, `cts-to-self`.
- `security.encryption` (ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256); unset): Allowed encryption ciphers.
- `security.group-encryption` (enum: tkip | ccmp | gcmp | ccmp-256 | gcmp-256; unset): Group encryption cipher.
- `security.group-key-update` (time; unset): Group key update interval.
- `security.passphrase` (string; unset): Network passphrase.
- `security.multi-passphrase-group` (enum; unset): Multi-passphrase group.
- `security.disable-pmkid` (bool; unset): Disable PMKID.
- `security.management-protection` (enum: disabled | allowed | required; unset): Management frame protection: `disabled`, `allowed`, `required`.
- `security.beacon-protection` (enum: disabled | enabled; unset): Beacon protection: `disabled` or `enabled`.
- `security.management-encryption` (enum: cmac | gmac | cmac-256 | gmac-256; unset): Management frame encryption cipher.
- `security.wps` (enum: disable | push-button; unset): WPS mode: `disable` or `push-button`.
- `security.dh-groups` (ubit (19, 20, 21); unset): SAE Diffie-Hellman groups.
- `security.sae-anti-clogging-threshold` (num; unset): SAE anti-clogging threshold.
- `security.sae-max-failure-rate` (num; unset): SAE maximum failure rate.
- `security.sae-pwe` (enum: hunting-and-pecking | hash-to-element | both; unset): SAE PWE derivation: `hunting-and-pecking`, `hash-to-element`, `both`.
- `security.owe-transition-interface` (iface_enum { auto }; unset): OWE transition interface.
- `security.eap-methods` (multi { array-id, method: enum (tls | ttls | peap) }; unset): Allowed EAP methods.
- `security.eap-certificate-mode` (enum: verify-certificate | dont-verify-certificate | no-certificates | verify-certificate-with-crl; unset): EAP certificate verification mode.
- `security.eap-tls-certificate` (enum; unset): EAP-TLS certificate.
- `security.eap-username` (string; unset): EAP username.
- `security.eap-anonymous-identity` (string; unset): EAP anonymous identity.
- `security.eap-password` (string; unset): EAP password.
- `security.eap-accounting` (bool; unset): Enable EAP accounting.
- `security.ft` (bool; unset): Enable Fast Transition (802.11r).
- `security.ft-mobility-domain` (num; unset): FT mobility domain.
- `security.ft-over-ds` (bool; unset): FT over the distribution system.
- `security.ft-reassociation-deadline` (time; unset): FT reassociation deadline.
- `security.ft-nas-identifier` (string; unset): FT NAS identifier.
- `security.ft-r0-key-lifetime` (time; unset): FT R0 key lifetime.
- `security.ft-preserve-vlanid` (bool; unset): FT preserve VLAN ID.
- `security.connect-group` (string; unset): Connect group.
- `security.connect-priority` (super { connect-accept-priority: num , [connect-hold-priority] /num }; unset): Connect priority.
- `security.authentication-types` (ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192); unset): Supported authentication types.
