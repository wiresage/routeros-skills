# /system/routerboard

> Source: https://manual.mikrotik.com/docs/cli-reference/system/routerboard

Conditions: !i386; Type: Settings Directory

This menu allows you to view basic hardware and firmware information on RouterBOARD devices.

**Read-only arguments**

- `routerboard` (bool): Indicates whether the device is a RouterBOARD unit.
- `board-name` (string)
- `model` (string): The RouterBOARD model number.
- `revision` (string)
- `serial-number` (string): The unique serial number of the device.
- `firmware-type` (string): The type of bootloader firmware used by the device.
- `minimum-firmware` (string): The firmware version installed at the factory.
- `current-firmware` (string): The version of the RouterBOOT loader currently in use. This should not be confused with the RouterOS operating system version.
- `upgrade-firmware` (string): RouterOS upgrades may include a new RouterBOOT version file, but it must be applied manually. This line indicates whether a new RouterBOOT file has been found on the device. The file may be included with a recent RouterOS upgrade or uploaded manually as an FWF file. In both cases, the newest available version is shown here.

## Commands

### /system/routerboard/upgrade

Conditions: !i386; Type: Command
