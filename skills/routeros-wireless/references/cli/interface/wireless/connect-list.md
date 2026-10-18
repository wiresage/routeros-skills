# /interface/wireless/connect-list

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/connect-list

Package: wireless-rep; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `interface` (iface_enum; mandatory)
- `connect` (bool)
- `mac-address` (macAddr)
- `ssid` (string)
- `signal-range` (composite { min: num [-120 .. 120] , max: num [-120 .. 120] })
- `allow-signal-out-of-range` (alt { signal-out-of-range-always: enum (always) , signal-out-of-range-time: time })
- `area-prefix` (string)
- `security-profile` (enum (none) { none:0xffffffff })
- `wireless-protocol` (enum: any | 802.11 | nstreme | tdma)
- `interworking` (enum)
- `iw-network-type` (enum: private | private-with-guest | public-chargeable | public-free | personal-device | emergency-only | test | wildcard)
- `iw-venue` (enum (any | assembly | business | educational | industrial | institutional | mercantile | residential | storage | utility | vehicular | outdoor) { any:0xffffffff, assembly:0x0001ffff, business:0x0002ffff, educational:0x0003ffff, industrial:0x0004ffff, institutional:0x0005ffff, mercantile:0x0006ffff, residential:0x0007ffff, storage:0x0008ffff, utility:0x0009ffff, vehicular:0x000affff, outdoor:0x000bffff })
- `iw-hessid` (macAddr)
- `iw-internet` (enum)
- `iw-asra` (enum)
- `iw-esr` (enum)
- `iw-uesa` (enum)
- `iw-hotspot20` (enum)
- `iw-hotspot20-dgaf` (enum)
- `iw-roaming-ois` (multi { array-id, iw-roaming-oi: string })
- `iw-authentication-types` (object { iw-authentication-type-indicator: enum (terms-and-conditions | online-enrollment | https-redirection | dns-redirection) })
- `iw-ipv4-availability` (enum (any | not-available | public | port-restricted | single-nated | double-nated | port-restricted-single-nated | port-restricted-double-nated | unknown) { any:0xffffffff, not-available:0, public:1, port-restricted:2, single-nated:3, double-nated:4, port-restricted-single-nated:5, port-restricted-double-nated:6, unknown:7 })
- `iw-ipv6-availability` (enum (any | not-available | available | unknown) { any:0xffffffff, not-available:0, available:1, unknown:2 })
- `iw-realms` (object { realm: composite { iw-realm-name: string , iw-realm-authentication: enum (not-specified | eap-sim | eap-tls | eap-aka) } })
- `3gpp` (string)
- `iw-connection-capabilities` (object { iw-connection-cap: composite { protocol: num , port: num } })
