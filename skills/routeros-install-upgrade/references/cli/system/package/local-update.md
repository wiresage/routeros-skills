# /system/package/local-update

> Source: https://manual.mikrotik.com/docs/cli-reference/system/package/local-update

Type: Directory

Instead of connecting directly to MikroTik servers, you can upload package files to one of your local RouterOS devices and use it as a local package server.

**Arguments**

- `download` (bool): Whether to download available packages from the local package server.

**Read-only arguments**

- `source` (alt { ipv6: ip6Addr , ip: ipAddr }): IP address of the local package server.
- `name` (string): Name of the package.
- `version` (string): Version of the package.
- `status` (enum: installed | downloaded | downloading | scheduled | available): Current status of the package.
- `completed` (num): Download completion percentage.

## Commands

### /system/package/local-update/download

Type: Command

Download specific compatible (matching device architecture) packages that are available on the local package server. Downloaded packages are saved in the root directory.

### /system/package/local-update/download-all

Type: Command

Download all compatible (matching device architecture) packages that are available on the local package server. Downloaded packages are saved in the root directory.

**Arguments**

- `download-beta` (bool): Whether to include beta packages when downloading all compatible packages.
- `reboot-after-download` (bool): Whether to automatically reboot the device after all packages finish downloading.

### /system/package/local-update/refresh

Type: Command

Refresh and check the list of available compatible (matching device architecture) packages on the local package server.
