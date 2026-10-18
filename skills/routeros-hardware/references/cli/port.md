# /port

> Source: https://manual.mikrotik.com/docs/cli-reference/port

Type: Directory

**Flags**

- `I`: inactive

**Arguments**

- `name` (string)
- `baud-rate` (enum: auto | 50 | 75 | 110 | 134 | 150 | 200 | 300 | 600 | 1200 | 1800 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200 | 230400 | 460800 | 500000 | 576000 | 921600 | 1000000 | 1152000 | 1500000 | 2000000 | 2500000 | 3000000 | 3500000 | 4000000)
- `data-bits` (enum: 7 | 8)
- `parity` (enum: none | odd | even)
- `stop-bits` (enum: 1 | 2)
- `flow-control` (enum: xon-xoff | hardware | none)
- `latency-timer` (num; unset)
- `rts` (enum: off | on)
- `dtr` (enum: off | on)

**Read-only arguments**

- `used-by` (string)
- `device` (string)
- `channels` (num)
- `line-state` (multi { array-id, line: enum (dtr | rts | cts | dcd | ri | dsr) })
