# /interface/wireless/interworking-profiles

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/interworking-profiles

Package: wireless-rep; Type: Directory

**Arguments**

- `name` (string; mandatory)
- `network-type` (enum: private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard)
- `internet` (bool)
- `asra` (bool)
- `esr` (bool)
- `uesa` (bool)
- `venue` (enum (unspecified | disabled) { unspecified:0, disabled:0xffffffff })
- `hessid` (macAddr)
- `hotspot20` (bool)
- `hotspot20-dgaf` (bool)
- `roaming-ois` (multi { array-id, roaming-oi: string })
- `venue-names` (object { venue-name: composite { venue-name-name: string , venue-name-lang: string } })
- `authentication-types` (object { authentication-type: composite { authentication-type-indicator: enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) , authentication-type-url: string } })
- `ipv4-availability` (enum: not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown)
- `ipv6-availability` (enum: not-available | available | unknown)
- `realms` (object { realm: composite { realm-name: string , realm-authentication: enum (not-specified | eap-sim | eap-tls | eap-aka) } })
- `realms-raw` (multi { array-id, realm-raw: string })
- `3gpp-raw` (string)
- `3gpp-info` (object { 3gpp: composite { 3gpp-mcc: string , 3gpp-mnc: string } })
- `domain-names` (multi { array-id, domain-name: string })
- `operator-names` (object { operator-name: composite { operator-name-name: string , operator-name-lang: string } })
- `wan-status` (enum: reserved | up | down | test)
- `wan-symmetric` (bool)
- `wan-at-capacity` (bool)
- `wan-downlink` (num)
- `wan-uplink` (num)
- `wan-downlink-load` (num)
- `wan-uplink-load` (num)
- `wan-measurement-duration` (num)
- `connection-capabilities` (object { connection-cap: composite { protocol: num , connection-cap2: composite { port: num , status: enum (closed | open | unknown) } } })
- `operational-classes` (multi { array-id, operational-class: num })
