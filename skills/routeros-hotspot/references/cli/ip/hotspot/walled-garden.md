# /ip/hotspot/walled-garden

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/walled-garden

Type: Directory

**Flags**

- `X`: disabled
- `D`: dynamic

**Arguments**

- `server` (super { ! , server: enum })
- `src-address` (super { ! , range: ipRange })
- `method` (super { ! , method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE) })
- `dst-host` (super { ! , host: string })
- `dst-port` (super { ! , ports: multi { ports: range [ .. 65535] } })
- `path` (super { ! , path: string })
- `action` (enum: allow | deny)

**Read-only arguments**

- `dst-address` (super { ! , range: ipRange })
- `hits` (num)

## Commands

### /ip/hotspot/walled-garden/reset-counters

Type: Command

### /ip/hotspot/walled-garden/reset-counters-all

Type: Command
