# /system/backup/cloud

> Source: https://manual.mikrotik.com/docs/cli-reference/system/backup/cloud

Type: Directory

Backup of this device stored on the MikroTik cloud server. Each device has one slot. Every command in this menu, including `print`, connects to `cloud2.mikrotik.com`. For examples, see [Cloud backup](https://manual.mikrotik.com/docs/network-management/cloud/cloud-backup).

**Read-only arguments**

- `name` (string): Name of the backup, set with `name` in `upload-file`. `download-file` saves the backup as `<name>.backup` unless `dst-file` is given.
- `size` (num): Size of the encrypted backup file.
- `ros-version` (string): RouterOS version that created the backup.
- `date` (date): Time of the upload.
- `status` (string): State of the stored backup. `ok` when the backup can be downloaded.
- `secret-download-key` (string): Key that downloads this backup on any router, with `download-file secret-download-key=<key>`. Replacing the backup generates a new key. Anyone who has the key can download the file, but cannot read it without the backup password.

## Commands

### /system/backup/cloud/download-file

Type: Command

Downloads a backup from the cloud server: this device's backup by its number in the list (`number=0`), or any backup by its `secret-download-key`.

**Arguments**

- `secret-download-key` (string): Key of the backup to download, shown as `secret-download-key` on the router that uploaded it. Use it to download the backup to another router.
- `action` (enum: download | download-and-apply): What to do with the backup:
  - `download` - Save the backup file to the router's storage.
  - `download-and-apply` - Save the backup file, restore the configuration from it with `password`, and reboot.
- `dst-file` (string): Name of the saved file; `.backup` is added. Without it, the file is saved as `<name>.backup`.
- `password` (string): Password of the backup, for `action=download-and-apply`.

**Read-only arguments**

- `status` (string): Progress of the command: `working...` while it runs, `finished` when it is done, or the error message, for example from the cloud server.

### /system/backup/cloud/remove-file

Type: Command

Deletes the backup from the cloud server and frees the slot of this device. Give the backup by its number in the list, for example `remove-file number=0`.

**Read-only arguments**

- `status` (string): Progress of the command: `working...` while it runs, `finished` when it is done, or the error message, for example from the cloud server.

### /system/backup/cloud/upload-file

Type: Command

Uploads an AES-encrypted backup to this device's slot on the cloud server. When the slot is used, the upload fails with `Server error: All slots used. Delete file to free up space.`, unless `replace` names the stored backup.

**Arguments**

- `action` (enum: upload | create-and-upload): What to upload:
  - `create-and-upload` - Create a backup of the current configuration, encrypt it with `password` and upload it.
  - `upload` - Upload the backup file given in `src-file`.
- `name` (string): Name of the backup in the cloud list. It does not have to match a file name.
- `replace` (enum): Name of the stored backup to overwrite. The new backup gets a new `secret-download-key`.
- `src-file` (file): Backup file to upload with `action=upload`. The file must be saved with a password (`/system/backup/save password=...`), otherwise the command fails with `src file must be AES encrypted`.
- `password` (string): Password that encrypts the backup with `action=create-and-upload`. Required for that action; you need it to restore the backup.

**Read-only arguments**

- `status` (string): Progress of the command: `working...` while it runs, `finished` when it is done, or the error message, for example from the cloud server.
