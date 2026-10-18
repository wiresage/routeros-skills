# /ip/kid-control

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/kid-control

Type: Directory

**Flags**

- `X`: disabled
- `P`: paused
- `B`: blocked
- `L`: rate-limited

**Arguments**

- `name` (string)
- `sun` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `mon` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `tue` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `wed` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `thu` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `fri` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `sat` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `rate-limit` (string)
- `tur-sun` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } }): time with unlimited rate on Sunday
- `tur-mon` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `tur-tue` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `tur-wed` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `tur-thu` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `tur-fri` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })
- `tur-sat` (multi { time: composite { start: time [0 .. 86400] , end: time [0 .. 86400] } })

**Read-only arguments**

- `pause-left` (time)
- `pause-till` (date)

## Commands

### /ip/kid-control/pause

Type: Command

**Arguments**

- `duration` (time)
- `till` (date)

### /ip/kid-control/resume

Type: Command
