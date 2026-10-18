# /system/routerboard/reset-button

> Source: https://manual.mikrotik.com/docs/cli-reference/system/routerboard/reset-button

Conditions: !i386; Type: Settings Directory

**Arguments**

- `enabled` (bool): Enables or disables the button.
- `hold-time` (composite { min: time [0 .. 60] , max: time [0 .. 60] }): Triggers the button action only when the button is held for a duration within the specified range.
- `on-event` (alt { script: string }): The name of the script to run when the button is pressed. You must create and name the script in the [Script](https://manual.mikrotik.com/docs/developer-guides/scripting) menu. Reset is executed with `read,write,reboot,ftp,romon,test` permissions.
