# /interface/wifi/interworking

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/interworking

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `network-type` (enum: private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard; unset)
- `internet` (bool; unset)
- `esr` (bool; unset)
- `uesa` (bool; unset)
- `venue` (enum (unspecified | disabled) { unspecified:0, disabled:0xffffffff }; unset)
- `hessid` (macAddr; unset)
- `hotspot20` (bool; unset)
- `hotspot20-dgaf` (bool; unset)
- `roaming-ois` (multi { array-id, roaming-oi: string }; unset)
- `venue-names` (object { venue-name: composite { venue-name-name: string , venue-name-lang: string } }; unset)
- `authentication-types` (object { authentication-type: composite { authentication-type-indicator: enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) , authentication-type-url: string } }; unset)
- `ipv4-availability` (enum: not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown; unset)
- `ipv6-availability` (enum: not-available | available | unknown; unset)
- `realms` (object { realm: composite { realm-name: string , realm-auth: enum (not-specified | eap-sim | eap-tls | eap-aka) } }; unset)
- `realms-raw` (multi { array-id, realm-raw: string }; unset)
- `3gpp-info` (object { 3gpp: composite { 3gpp-mcc: string , 3gpp-mnc: string } }; unset)
- `3gpp-info-raw` (string; unset)
- `domain-names` (multi { array-id, domain-name: string }; unset)
- `operator-names` (object { operator-name: composite { operator-name-name: string , operator-name-lang: string } }; unset)
- `wan-status` (enum: reserved | up | down | test; unset)
- `wan-symmetric` (bool; unset)
- `wan-at-capacity` (bool; unset)
- `wan-downlink` (num; unset)
- `wan-uplink` (num; unset)
- `wan-downlink-load` (num; unset)
- `wan-uplink-load` (num; unset)
- `wan-measurement-duration` (num; unset)
- `connection-capabilities` (object { connection-cap: composite { protocol: num , connection-cap2: composite { port: num , status: enum (closed | open | unknown) } } }; unset)
- `operational-classes` (multi { array-id, operational-class: num }; unset)
