# /system/package/local-update/mirror

> Source: https://manual.mikrotik.com/docs/cli-reference/system/package/local-update/mirror

Type: Settings Directory

You can mirror packages (for all architectures) from your main local package server by using this menu. Downloaded packages are saved into the `packs` folder in the root directory.

**Arguments**

- `enabled` (bool): Whether to enable periodic check and download of packages from the local package server.
- `primary-server` (alt { ipv6: ip6Addr , ip: ipAddr }): IP address of the primary local package server.
- `secondary-server` (alt { ipv6: ip6Addr , ip: ipAddr }): IP address of the secondary local package server.
- `check-interval` (time): Time interval at which the device checks the local package server for new package availability. If a new package is located, the package download begins. Only downloads the packages that are not already present on the device.
- `user` (string): Username for accessing the local package server.
- `password` (string): Password for accessing the local package server.

**Read-only arguments**

- `software-id` (string): Software ID of the device.

## Commands

### /system/package/local-update/mirror/force-check

Type: Command
