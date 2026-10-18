# /system/gps

> Source: https://manual.mikrotik.com/docs/cli-reference/system/gps

Package: gps; Type: Settings Directory

**Arguments**

- `enabled` (bool)
- `port` (alt { serial: enum (none) , interface: iface_enum })
- `channel` (num)
- `init-channel` (num)
- `init-string` (multi { array-id, string: string })
- `set-system-time` (bool)
- `coordinate-format` (enum: dms | dd | ddmm)
- `gps-antenna-select` (enum: internal | external; syscap=rb-gps)

## Commands

### /system/gps/monitor

Package: gps; Type: Command

**Read-only arguments**

- `date-and-time` (date)
- `latitude` (string)
- `longitude` (string)
- `altitude` (string)
- `speed` (string)
- `destination-bearing` (string)
- `true-bearing` (string)
- `magnetic-bearing` (string)
- `valid` (bool)
- `satellites` (num)
- `fix-quality` (num)
- `horizontal-dilution` (num)
- `data-age` (alt { never: enum (never) , time: time })
