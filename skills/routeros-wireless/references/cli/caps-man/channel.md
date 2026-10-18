# /caps-man/channel

> Source: https://manual.mikrotik.com/docs/cli-reference/caps-man/channel

Package: wireless-rep; Type: Directory

**Arguments**

- `name` (string; mandatory)
- `frequency` (multi { array-id, frequency: num }; unset)
- `secondary-frequency` (multi { array-id, secondary-frequency: alt { secondary-frequency-disable: enum (disabled) , secondary-frequency-num: num } }; unset)
- `control-channel-width` (enum: 5mhz | 10mhz | 20mhz | 40mhz-turbo; unset)
- `band` (enum: 2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac; unset)
- `extension-channel` (enum: disabled | Ce | eC | Ceee | eCee | eeCe | eeeC | XX | XXXX | Ceeeeeee | eCeeeeee | eeCeeeee | eeeCeeee | eeeeCeee | eeeeeCee | eeeeeeCe | eeeeeeeC | XXXXXXXX; unset)
- `tx-power` (num; unset)
- `save-selected` (bool; unset)
- `reselect-interval` (super { reselect-interval-min: time [1 .. 60*60*24*300] , [reselect-interval-max] ..time [1 .. 60*60*24*300] }; unset)
- `skip-dfs-channels` (bool; unset)
