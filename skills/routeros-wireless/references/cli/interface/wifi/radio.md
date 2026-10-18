# /interface/wifi/radio

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/radio

Type: Directory

**Flags**

- `L`: local

**Read-only arguments**

- `cap` (string)
- `radio-mac` (macAddr)
- `tx-chains` (ubit ())
- `rx-chains` (ubit ())
- `bands` (object { band: composite { band-band: enum () , band-widths: ubit (20mhz, 20/40mhz, 20/40/80mhz, 20/40/80/160mhz, 20/40/80+80mhz, 20/40/80/160/320mhz, 1mhz, 1/2mhz, 1/2/4mhz, 1/2/4/8mhz, 1/2/4/8/16mhz, 2160mhz) } })
- `ciphers` (ubit (tkip, ccmp, gcmp, ccmp-256, gcmp-256, cmac, gmac, cmac-256, gmac-256))
- `min-antenna-gain` (num; unset)
- `countries` (multi { array-id, country: string }; unset)
- `2g-channels` (multi { array-id, frequency: num }; unset)
- `5g-channels` (multi { array-id, frequency: num }; unset)
- `6g-channels` (multi { array-id, frequency: num }; unset)
- `60g-channels` (multi { array-id, frequency: num }; unset)
- `s1g-channels` (multi { array-id, frequency: num }; unset)
- `max-vlans` (num; unset)
- `max-interfaces` (num; unset)
- `max-station-interfaces` (num; unset)
- `max-peers` (num; unset)
- `hw-type` (string; unset)
- `hw-caps` (multi { array-id, hw-cap: enum (sniffer | qos-classifier-dscp | spectral | channel-switch | mlo | hw-protection-mode | beacon-protection) }; unset)
- `ml-group` (string; unset)
- `interface` (iface_enum; unset)
- `current-country` (enum; unset)
- `current-halow-regdom` (string; unset)
- `current-channels` (multi { array-id, channel: string }; unset)
- `current-gopclasses` (multi { array-id, gopclass: num }; unset)
- `current-max-reg-power` (num; unset)
- `afc-deployment` (string; unset)

## Commands

### /interface/wifi/radio/provision

Type: Command

### /interface/wifi/radio/reg-info

Type: Command

**Arguments**

- `country` (enum)

**Read-only arguments**

- `ranges` (multi { array-id, range: string })
