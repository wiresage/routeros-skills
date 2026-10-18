# /interface/wireless/sniffer

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/sniffer

Package: wireless-rep; Type: Settings Directory

**Arguments**

- `multiple-channels` (bool)
- `channel-time` (time)
- `only-headers` (bool)
- `receive-errors` (bool)
- `memory-limit` (num)
- `file-name` (string)
- `file-limit` (num)
- `streaming-enabled` (bool)
- `streaming-server` (super { ip: ipAddr , [port] [ :num [1 .. 65535]] })
- `streaming-max-rate` (num)

## Commands

### /interface/wireless/sniffer/save

Package: wireless-rep; Type: Command

**Arguments**

- `file-name` (string)

### /interface/wireless/sniffer/sniff

Package: wireless-rep; Type: Command

**Arguments**

- `interface` (iface_enum)

**Read-only arguments**

- `processed-packets` (num)
- `file-size` (num)
- `file-saved-packets` (num)
- `file-over-limit-packets` (num)
- `memory-size` (num)
- `memory-saved-packets` (num)
- `memory-over-limit-packets` (num)
- `stream-dropped-packets` (num)
- `stream-sent-packets` (num)
- `real-file-limit` (num)
- `real-memory-limit` (num)
