# /system/routerboard/usb

> Source: https://manual.mikrotik.com/docs/cli-reference/system/routerboard/usb

Conditions: !i386, !i386, !powerpc; Type: Settings Directory

**Arguments**

- `type` (enum: USB-type-A | mini-PCIe | auto)
- `usb-mode` (enum: automatic | force-host)

**Read-only arguments**

- `auto-type` (enum: USB-type-A | mini-PCIe)
- `bootstrap` (enum: host-mode | device-mode)

## Commands

### /system/routerboard/usb/power-reset

Conditions: !i386, !i386, !powerpc; Type: Command

**Arguments**

- `duration` (time)
- `bus` (num)
