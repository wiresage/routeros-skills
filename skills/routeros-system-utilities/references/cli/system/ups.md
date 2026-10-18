# /system/ups

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ups

Package: ups; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `name` (string)
- `port` (enum)
- `offline-time` (time)
- `min-runtime` (alt { never: enum (never) { never:0xffffffff } , min-runtime: time })
- `alarm-setting` (enum: immediate | delayed | low-battery | none)
- `check-capabilities` (bool)

**Read-only arguments**

- `model` (string)
- `version` (string)
- `serial` (string)
- `manufacture-date` (string)
- `load` (num)
- `on-line` (bool)
- `nominal-battery-voltage` (num)
- `offline-after` (time)

## Commands

### /system/ups/beep

Package: ups; Type: Command

### /system/ups/monitor

Package: ups; Type: Command

**Read-only arguments**

- `on-line` (bool)
- `on-battery` (bool)
- `transfer-cause` (string)
- `rtc-running` (bool)
- `runtime-left` (time)
- `offline-after` (time)
- `battery-charge` (num)
- `battery-voltage` (num)
- `line-voltage` (num)
- `output-voltage` (num)
- `load` (num)
- `temperature` (num)
- `frequency` (num)
- `replace-battery` (bool)
- `smart-boost` (bool)
- `smart-trim` (bool)
- `overload` (bool)
- `low-battery` (bool)
- `self-test` (string)
- `hid-self-test` (enum: done-and-passed | done-and-warning | done-and-error | aborted | in-progress | no-test-initiated)

### /system/ups/rtc

Package: ups; Type: Command

### /system/ups/self-test

Package: ups; Type: Command

**Arguments**

- `hid-test-type` (enum: quick | deep | abort)
