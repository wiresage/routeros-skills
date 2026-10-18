# /system/dashboard/show

> Source: https://manual.mikrotik.com/docs/cli-reference/system/dashboard/show

Type: Command

**Read-only arguments**

- `model` (string)
- `board-name` (string)
- `identity` (string)
- `version` (string)
- `uptime` (time)
- `cpu-usage` (num)
- `memory-usage` (composite { used: num , total: num })
- `hdd-usage` (composite { used: num , total: num })
- `ether` (super { running: num , [enabled] /num , [total] /num })
- `wifi` (super { running: num , [enabled] /num , [total] /num })
- `total-bw` (super { tx: num , [rx] /num })
- `uplink-bw` (super { tx: num , [rx] /num })
- `ether-bw` (super { tx: num , [rx] /num })
- `wifi-bw` (super { tx: num , [rx] /num })
- `lte-bw` (super { tx: num , [rx] /num })
