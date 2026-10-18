# /iot/lora/servers

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/lora/servers

Package: iot; Type: Directory

**Arguments**

- `name` (string; mandatory)
- `address` (string; mandatory)
- `up-port` (num)
- `down-port` (num)
- `key` (string)
- `port` (num)
- `interval` (num)
- `ssl` (bool)
- `certificate` (enum: none)
- `protocol` (enum: UDP | LNS | CUPS; mandatory)
- `netid` (multi { netid: enum })
- `joineui` (multi { joineui: enum })

## Commands

### /iot/lora/servers/reset-servers

Package: iot; Type: Command
