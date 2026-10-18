# /interface/wifi/channel

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/channel

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `frequency` (object; unset)
- `secondary-frequency` (multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled) , secondary-frequency-num: num } }; unset)
- `band` (enum: 60ghz-ad | 5ghz-a | 5ghz-n | 5ghz-ac | 5ghz-ax | 5ghz-be | 2ghz-g | 2ghz-n | 2ghz-ax | 2ghz-be | s1ghz-ah | 6ghz-ax | 6ghz-be; unset)
- `width` (enum: 20mhz | 20/40mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz | 20/40/80+80mhz | 20/40/80/160mhz | 20/40/80/160/320mhz | 1mhz | 1/2mhz | 1/2/4mhz | 1/2/4/8mhz | 2160mhz; unset)
- `skip-dfs-channels` (enum: disabled | all | 10min-cac; unset)
- `deprioritize-unii-3-4` (bool; unset)
- `reselect-interval` (super { reselect-interval-min: time [1 .. 60*60*24*300] , [reselect-interval-max] ..time [1 .. 60*60*24*300] }; unset)
- `reselect-time` (super { reselect-time-min: date , [reselect-time-max] ..date }; unset)
- `preamble-puncturing` (alt { preamble-puncturing: enum (yes | no) }; unset)
- `afc` (bool; unset)
