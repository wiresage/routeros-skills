# /system/package

> Source: https://manual.mikrotik.com/docs/cli-reference/system/package

Type: Directory

Commands executed in this menu will take place only on the restart of the router. Until then, you can freely schedule or revert the set actions.

**Flags**

- `X`: disabled
- `A`: available

**Read-only arguments**

- `name` (string): Name of the package.
- `version` (string): Version of the package.
- `build-time` (date): Date and time the package was built.
- `scheduled` (enum: | scheduled for uninstall | scheduled for disable | scheduled for enable | Use `apply-changes` to proceed with install): Scheduled action for the package after the next reboot.
- `bundle` (enum): The bundle package this package belongs to.
- `size` (num): Size of the package in bytes.

## Commands

### /system/package/apply-changes

Type: Command

Apply scheduled changes and reboot the device.

**Arguments**

- `ignore-missing` (bool; unset): Upgrade only the RouterOS main package, omitting packages that are missing or not uploaded.

### /system/package/disable

Type: Command

Schedule the package to be disabled after the next reboot. No features provided by the package will be accessible.

### /system/package/downgrade

Type: Command

Prompt for a reboot. During the reboot process, the router will try to downgrade RouterOS to the oldest version possible by checking the packages that are uploaded to the router.

### /system/package/enable

Type: Command

### /system/package/uninstall

Type: Command

Schedule the package to be removed from the router. That will take place during the reboot.

### /system/package/unschedule

Type: Command
