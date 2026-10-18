# /dude/ros/health

> Source: https://manual.mikrotik.com/docs/cli-reference/dude/ros/health

Package: dude; Type: Directory

**Arguments**

- `device` (enum; mandatory)
- `fan-mode` (enum: manual | auto)
- `use-fan` (enum: auxiliary | main)
- `use-fan2` (enum: auxiliary | main)
- `fan-switch` (enum: auto | on | off)
- `fan-on-threshold` (num)
- `cpu-overtemp-check` (bool)
- `cpu-overtemp-threshold` (num)
- `cpu-overtemp-startup-delay` (time)
- `psu1-state` (enum: ok | fail)
- `psu2-state` (enum: ok | fail)

**Read-only arguments**

- `active-fan` (enum: auxiliary | main | none)
- `active-fan2` (enum: auxiliary | main | none)
- `voltage` (num)
- `battery` (num)
- `current` (num)
- `fan-speed` (num)
- `fan-speed2` (num)
- `temperature` (num)
- `cpu-temperature` (num)
- `power-consumption` (num)
- `board-temperature1` (num)
- `board-temperature2` (num)
- `board-temperature3` (num)
- `psu1-voltage` (num)
- `psu2-voltage` (num)
- `psu1-current` (num)
- `psu2-current` (num)
- `fan1-speed` (num)
- `fan2-speed` (num)
- `fan3-speed` (num)
- `fan4-speed` (num)
- `fan5-speed` (num)
- `fan6-speed` (num)
