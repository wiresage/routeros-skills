# /file/sync

> Source: https://manual.mikrotik.com/docs/cli-reference/file/sync

Package: rose-storage; Type: Directory

**Flags**

- `X` (disabled): The sync entry is disabled.
- `I` (invalid): The entry is invalid, for example it references a missing or unusable path.
- `D` (dynamic): The entry is created automatically.

**Arguments**

- `remote-address` (multi { array-id, address: string }; mandatory): IP address of the remote RouterOS device to synchronize with. The remote device must have the rsync daemon enabled ([`rsync-daemon`](rsync-daemon.md)).
- `mode` (enum: upload | download; mandatory): Direction of the synchronization:
  - `upload` - send the `local-path` file or folder to the remote device.
  - `download` - fetch `remote-path` from the remote device to this router.
- `local-path` (file): File or folder path on this router; the source for `mode=upload` and the destination for `mode=download`.
- `remote-path` (string): File or folder path on the remote device.
- `user` (string): RouterOS user on the remote device used for authentication.
- `password` (string): Password of the user on the remote device. When it is set, the transfers run over automatically created IPsec.

**Read-only arguments**

- `status` (string): Status of the synchronization, for example `in sync`, `making control connection to <ip>` or `initializing transfer`.

## Commands

### /file/sync/monitor

Package: rose-storage; Type: Command

**Read-only arguments**

- `status` (string): Synchronization status of the monitored entry, for example `in sync`, `making control connection to <ip>` or `initializing transfer`.
