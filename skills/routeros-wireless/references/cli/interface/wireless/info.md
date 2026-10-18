# /interface/wireless/info

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/info

Package: wireless-rep; Type: Directory

## Commands

### /interface/wireless/info/allowed-channels

Package: wireless-rep; Type: Command

**Arguments**

- `interface` (iface_enum)
- `frequency-mode` (enum)
- `country` (enum)
- `band` (enum: 2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)
- `channel-width` (enum: 20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)
- `antenna-gain` (num)
- `dfs-mode` (enum: none | no-radar-detect | radar-detect)
- `installation` (enum: any | indoor | outdoor)

**Read-only arguments**

- `channels` (multi { array-id, channel: string })

### /interface/wireless/info/country-info

Package: wireless-rep; Type: Command

**Arguments**

- `country` (enum)

**Read-only arguments**

- `ranges` (multi { array-id, channel: string })

### /interface/wireless/info/country-list

Package: wireless-rep; Type: Command

**Read-only arguments**

- `countries` (multi { array-id, country: string })

### /interface/wireless/info/default-scan-list

Package: wireless-rep; Type: Command

**Arguments**

- `interface` (iface_enum)
- `frequency-mode` (enum)
- `country` (enum)
- `band` (enum: 2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)
- `channel-width` (enum: 20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)
- `antenna-gain` (num)
- `dfs-mode` (enum: none | no-radar-detect | radar-detect)
- `installation` (enum: any | indoor | outdoor)

**Read-only arguments**

- `channels` (multi { array-id, channel: string })

### /interface/wireless/info/hw-info

Package: wireless-rep; Type: Command

**Arguments**

- `interface` (iface_enum)

**Read-only arguments**

- `ranges` (multi { array-id, range: string })
- `tx-chains` (ubit (0, 1, 2, 3))
- `rx-chains` (ubit (0, 1, 2, 3))
- `extra-info` (string)
- `locked-countries` (multi { array-id, country: enum })

### /interface/wireless/info/scan-list

Package: wireless-rep; Type: Command

**Arguments**

- `interface` (iface_enum)
- `frequency-mode` (enum)
- `country` (enum)
- `band` (enum: 2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)
- `channel-width` (enum: 20mhz | 40mhz-turbo | 10mhz | 5mhz | 20/40mhz-Ce | 20/40mhz-eC | 20/40/80mhz-Ceee | 20/40/80mhz-eCee | 20/40/80mhz-eeCe | 20/40/80mhz-eeeC)
- `antenna-gain` (num)
- `dfs-mode` (enum: none | no-radar-detect | radar-detect)
- `installation` (enum: any | indoor | outdoor)

**Read-only arguments**

- `channels` (multi { array-id, channel: string })
