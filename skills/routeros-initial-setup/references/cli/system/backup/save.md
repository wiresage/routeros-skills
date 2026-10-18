# /system/backup/save

> Source: https://manual.mikrotik.com/docs/cli-reference/system/backup/save

Type: Command

Saves the whole router configuration in a binary [backup file](../../../guides/getting-started/configuration-management/backup.md). The backup file appears in the `/file` menu and can be copied off the router.

**Arguments**

- `name` (file): Name of the backup file. The file is saved as `<name>.backup` and appears in the `/file` menu.
- `password` (string): Password that encrypts the backup file. Without a password, the backup is saved unencrypted.
- `dont-encrypt` (bool): Save the backup unencrypted even when `password` is given. Default: no.
- `encryption` (enum: aes-sha256 | rc4): Encryption algorithm used when `password` is given.
  - `aes-sha256` (default) - Encryption with AES and SHA-256.
  - `rc4` - Legacy weak algorithm, kept for compatibility with older RouterOS versions.
