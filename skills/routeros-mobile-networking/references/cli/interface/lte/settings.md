# /interface/lte/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/lte/settings

Conditions: !smips; Type: Settings Directory

**Arguments**

- `mode` (enum: auto | serial | mbim | user)
- `esim-channel` (enum: auto | at)
- `firmware-path` (string)
- `log-dir` (file; syscap=modemlog)
- `log-file-count` (num; syscap=modemlog): number of rotated modem log files kept in log-dir
- `log-filter-file` (file; syscap=modemlog): filter file to use for modem log capture
- `info-polling-interval` (num; syscap=tr069-client): info polling interval in seconds
- `link-recovery-timer` (num): in seconds
- `sim-slot` (enum; syscap=sim-slot)
- `sim-link` (enum; syscap=sim-link)
- `external-antenna` (enum: auto | main | div | both | none; syscap=modem-antenna-switch)

**Read-only arguments**

- `external-antenna-selected` (enum: main | div | both | none | none; syscap=modem-antenna-switch)
