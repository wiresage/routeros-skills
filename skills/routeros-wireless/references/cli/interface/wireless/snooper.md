# /interface/wireless/snooper

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/snooper

Package: wireless-rep; Type: Settings Directory

**Arguments**

- `multiple-channels` (bool)
- `channel-time` (time)
- `receive-errors` (bool)

## Commands

### /interface/wireless/snooper/flat-snoop

Package: wireless-rep; Type: Command

**Arguments**

- `interface` (iface_enum)

**Read-only arguments**

- `type` (enum: frequency | network | station)
- `channel` (string)
- `use` (num)
- `bitrate` (alt { station-bandwidth: num , network-bandwidth: num , frequency-bandwidth: num })
- `frequency-network-count` (num)
- `noise-floor` (num)
- `frequency-station-count` (num)
- `active` (alt { station-active: bool , network-active: bool })
- `frequency-known` (bool)
- `beacon-seen` (bool)
- `address` (alt { station-address: macAddr , network-address: macAddr })
- `network-ssid` (string)
- `beacon-hides-ssid` (bool)
- `beacon-interval` (num)
- `beacon-rate` (string)
- `last-beacon` (time)
- `beacon-strength` (num)
- `signal-to-noise` (alt { network-signal-to-noise: num , station-signal-to-noise: num })
- `ssid-source` (enum: none | association-discussion | probe-response | beacon)
- `supported-rates` (multi { array-id, rate: enum () })
- `basic-rates` (multi { array-id, rate: enum () })
- `network-capabilities` (multi { array-id, cap: enum (ess | ibss | cf-pollable | cf-pollreq | privacy | short-preamble | pbcc | channel-agility) })
- `mt-network` (bool)
- `mt-info` (multi { array-id, cap: enum (nstreme | doing-wds | without-polling | dynamic-packing-size) })
- `mt-name` (alt { station-mt-name: string , network-mt-name: string })
- `mt-routeros-version` (alt { station-mt-routeros-version: string , network-mt-routeros-version: string })
- `mt-mru` (alt { station-mt-mru: num , network-mt-mru: num })
- `mt-framing-mode` (enum: none | best-fit | exact-size)
- `network-station-count` (num)
- `use-of-freq` (alt { station-use-of-freq: num , network-use-of-freq: num })
- `use-of-traffic` (alt { station-use-of-traffic: num , network-use-of-traffic: num })
- `freq-source` (enum: seen-frame-on-freq | network-on-freq)
- `last-seen` (time)
- `signal-strength` (num)
- `network-source` (enum: none | seen-data-frame | seen-successful-auth | seen-successful-assoc | forms-network)
- `seen-wep` (bool)
- `station-rates` (multi { array-id, rate: enum () })
- `station-capabilities` (multi { array-id, cap: enum (ess | ibss | cf-pollable | cf-pollreq | privacy | short-preamble | pbcc | channel-agility) })
- `mt-station` (bool)
- `assoc-capabilities` (multi { array-id, cap: enum (ess | ibss | cf-pollable | cf-pollreq | privacy | short-preamble | pbcc | channel-agility) })
- `assoc-id` (num)
- `assoc-mt-info` (multi { array-id, cap: enum (nstreme | doing-wds | without-polling | dynamic-packing-size) })
- `assoc-mt-ap-tx-limit` (num)
- `assoc-mt-client-tx-limit` (num)
- `assoc-mt-framing-mode` (enum: none | best-fit | exact-size)
- `assoc-mt-framing-limit` (num)

### /interface/wireless/snooper/snoop

Package: wireless-rep; Type: Command

**Arguments**

- `interface` (iface_enum)
