# /system/package/update

> Source: https://manual.mikrotik.com/docs/cli-reference/system/package/update

Type: Settings Directory

Manage the `check-for-updates` channel and perform RouterOS upgrades.

**Arguments**

- `channel` (enum: long-term | stable | testing | development): Upgrade [channel](#channel) to use when checking for new versions.
- `mode` (enum: https | http): Protocol for connecting to the MikroTik download server. Use `http` only if your network blocks HTTPS. HTTPS is recommended.
- `check-certificate` (enum: no | yes | yes-without-crl): Whether and how to validate the server SSL certificate. Always use `yes` to ensure a secure connection. `yes-without-crl` can be used to skip CRL validation.
- `ip-version` (enum: auto | ipv4 | ipv6): IP version preference for connecting to the MikroTik download server.

**Read-only arguments**

- `installed-version` (string): Currently installed RouterOS version.
- `latest-version` (string): Latest available RouterOS version in the selected [channel](#channel).
- `status` (string): Current status of the update process (for example, `New version is available`).

## Commands

### /system/package/update/cancel

Type: Command

Cancel a pending update download or installation.

### /system/package/update/check-for-updates

Type: Command

Check the MikroTik download server for a newer RouterOS version in the selected release channel.

**Arguments**

- `fetch-changelog` (switch): Whether to fetch the changelog along with the update check.

**Read-only arguments**

- `changelog` (string): Changelog text for the latest available version.

### /system/package/update/download

Type: Command

Download the latest available RouterOS packages without installing. A manual reboot is required to apply the update.

**Arguments**

- `ignore-missing` (bool; unset): Download only the RouterOS main package, omitting packages that are missing or not uploaded.

### /system/package/update/install

Type: Command

Download and install the latest available RouterOS packages, followed by an automatic reboot.

**Arguments**

- `ignore-missing` (bool; unset): Install only the RouterOS main package, omitting packages that are missing or not uploaded.
