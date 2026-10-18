# /lcd

> Source: https://manual.mikrotik.com/docs/cli-reference/lcd

Conditions: !smips; Syscap: lcd; Type: Settings Directory

## Commands

### /lcd/backlight

Conditions: !smips; Syscap: lcd; Type: Command

**Arguments**

- `state` (enum: off | on)

### /lcd/recalibrate

Conditions: !smips; Syscap: lcd; Type: Command

### /lcd/show

Conditions: !smips; Syscap: lcd; Type: Command

**Arguments**

- `screen` (enum: main-menu | interfaces | stats | stat-slideshow | informative-slideshow | log | stats-all | wireless-info)

### /lcd/take-screenshot

Conditions: !smips; Syscap: lcd; Type: Command

**Arguments**

- `file-name` (string)
