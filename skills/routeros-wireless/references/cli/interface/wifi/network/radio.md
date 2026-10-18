# /interface/wifi/network/radio

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/network/radio

Type: Directory

**Flags**

- `Y`: managed
- `X`: disabled

**Arguments**

- `labels` (object; unset)
- `extra-labels` (multi { array-id, label: string }; unset)
- `configuration.country` (enum; unset)
- `configuration.chains` (ubit (0, 1, 2, 3, 4, 5, 6, 7); unset)
- `configuration.tx-chains` (ubit (); unset)
- `configuration.tx-power` (num; unset)
- `configuration.antenna-gain` (num; unset)
- `configuration.distance` (num; unset)
- `configuration.installation` (enum: outdoor | indoor; unset)
- `channel.frequency` (object; unset)
- `channel.secondary-frequency` (multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled) , secondary-frequency-num: num } }; unset)
- `channel.band` (enum: 60ghz-ad | 5ghz-a | 5ghz-n | 5ghz-ac | 5ghz-ax | 5ghz-be | 2ghz-g | 2ghz-n | 2ghz-ax | 2ghz-be | s1ghz-ah | 6ghz-ax | 6ghz-be; unset)
- `channel.width` (enum: 20mhz | 20/40mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz | 20/40/80+80mhz | 20/40/80/160mhz | 20/40/80/160/320mhz | 1mhz | 1/2mhz | 1/2/4mhz | 1/2/4/8mhz | 2160mhz; unset)
- `channel.skip-dfs-channels` (enum: disabled | all | 10min-cac; unset)
- `channel.deprioritize-unii-3-4` (bool; unset)
- `channel.reselect-interval` (super { reselect-interval-min: time [1 .. 60*60*24*300] , [reselect-interval-max] ..time [1 .. 60*60*24*300] }; unset)
- `channel.reselect-time` (super { reselect-time-min: date , [reselect-time-max] ..date }; unset)
- `channel.preamble-puncturing` (alt { preamble-puncturing: enum (yes | no) }; unset)
- `channel.afc` (bool; unset)
- `security.authentication-types` (ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192); unset)
