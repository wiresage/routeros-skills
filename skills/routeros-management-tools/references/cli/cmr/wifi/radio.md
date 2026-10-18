# /cmr/wifi/radio

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/wifi/radio

Package: cmr; Type: Directory

Radio configuration replicated to the selected devices. The arguments extend the standard RouterOS `/interface/wifi` radio configuration parameters.

**Flags**

- `X` (disabled): Radio configuration is disabled.

**Arguments**

- `labels` (object; unset): Select the devices the radio configuration is replicated to using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.
- `configuration.country` (enum; unset): Country code.
- `configuration.chains` (ubit (0, 1, 2, 3, 4, 5, 6, 7); unset): Radio chains to use.
- `configuration.tx-chains` (ubit (); unset): Transmit chains.
- `configuration.tx-power` (num; unset): Transmit power.
- `configuration.antenna-gain` (num; unset): Antenna gain.
- `configuration.distance` (num; unset): Distance to the farthest connected client.
- `configuration.installation` (enum: outdoor | indoor; unset): Installation type: `outdoor` or `indoor`.
- `security.authentication-types` (ubit (wpa-psk, wpa2-psk, wpa2-psk-sha2, wpa-eap, wpa2-eap, wpa3-psk, wpa3-psk-gd, owe, wpa3-eap, wpa3-eap-192); unset): Supported authentication types.
- `channel.frequency` (object; unset): Channel frequency.
- `channel.secondary-frequency` (multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled) , secondary-frequency-num: num } }; unset): Secondary channel frequency.
- `channel.band` (enum: 60ghz-ad | 5ghz-a | 5ghz-n | 5ghz-ac | 5ghz-ax | 5ghz-be | 2ghz-g | 2ghz-n | 2ghz-ax | 2ghz-be | s1ghz-ah | 6ghz-ax | 6ghz-be; unset): Operating band.
- `channel.width` (enum: 20mhz | 20/40mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz | 20/40/80+80mhz | 20/40/80/160mhz | 20/40/80/160/320mhz | 1mhz | 1/2mhz | 1/2/4mhz | 1/2/4/8mhz | 2160mhz; unset): Channel width.
- `channel.skip-dfs-channels` (enum: disabled | all | 10min-cac; unset): DFS channel handling: `disabled`, `all`, `10min-cac`.
- `channel.deprioritize-unii-3-4` (bool; unset): Deprioritize UNII-3/UNII-4 channels.
- `channel.reselect-interval` (super { reselect-interval-min: time [1 .. 60*60*24*300] , [reselect-interval-max] ..time [1 .. 60*60*24*300] }; unset): Channel reselection interval range.
- `channel.reselect-time` (super { reselect-time-min: date , [reselect-time-max] ..date }; unset): Channel reselection time range.
- `channel.preamble-puncturing` (alt { preamble-puncturing: enum (yes | no) }; unset): Preamble puncturing: `yes` or `no`.
- `channel.afc` (bool; unset): Enable AFC (Automatic Frequency Coordination).
