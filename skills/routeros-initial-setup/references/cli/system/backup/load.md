# /system/backup/load

> Source: https://manual.mikrotik.com/docs/cli-reference/system/backup/load

Type: Command

Loads a configuration saved with `/system/backup/save` from a [backup file](../../../guides/getting-started/configuration-management/backup.md), then reboots the router after confirmation.

**Arguments**

- `name` (file): Name of the backup file, as given to `save` (without the `.backup` extension).
- `password` (string): Password used to decrypt the backup file. When omitted, RouterOS asks for it. For an unencrypted backup, any password works.
- `force-v6-to-v7-configuration-upgrade` (bool): Whether to load a backup made on RouterOS v6 and convert its configuration to v7. The flag has no effect on a backup made on v7.
