# /interface/wireless/align

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/align

Package: wireless-rep; Type: Settings Directory

**Arguments**

- `frame-size` (num)
- `active-mode` (bool)
- `receive-all` (bool)
- `audio-monitor` (macAddr)
- `filter-mac` (macAddr)
- `ssid-all` (bool)
- `frames-per-second` (num)
- `audio-min` (num)
- `audio-max` (num)

## Commands

### /interface/wireless/align/monitor

Package: wireless-rep; Type: Command

**Flags**

- `A`: access-point

**Arguments**

- `interface` (iface_enum)

**Read-only arguments**

- `address` (macAddr)
- `ssid` (string)
- `rxq` (num)
- `avg-rxq` (num)
- `last-rx` (num)
- `txq` (num)
- `last-tx` (num)
- `correct` (num)

### /interface/wireless/align/test-audio

Package: wireless-rep; Type: Command

**Arguments**

- `test-value` (num)
