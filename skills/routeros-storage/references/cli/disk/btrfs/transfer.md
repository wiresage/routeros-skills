# /disk/btrfs/transfer

> Source: https://manual.mikrotik.com/docs/cli-reference/disk/btrfs/transfer

Conditions: !smips; Syscap: storage; Type: Directory

**Arguments**

- `type` (enum: receive | send; mandatory): Direction of the Btrfs transfer:
  - `receive` - receive a Btrfs send stream at `file`, for example the destination side of a snapshot backup between two RouterOS devices.
  - `send` - send subvolumes (snapshots) of the file system `fs` to a remote RouterOS device over SSH.

  Transfers use the SSH user key authentication of `/user/ssh-keys`. See [Btrfs subvolumes and snapshots](../../../guides/storage/btrfs/snapshots.md) for a working send/receive example.
- `fs` (enum): Label of the Btrfs file system the transfer operates on, as shown in [`filesystem`](filesystem.md).
- `send-parent` (enum): Snapshot of a previous successful send to base an incremental `send` on; only the changes since that snapshot are transferred.
- `send-subvolumes` (multi { array-id, subvolume: enum }): Snapshots to send, for a `send` transfer. Snapshot names (not paths), as shown under [`subvolume`](subvolume.md).
- `file` (file): Destination (or source) path of the transfer, for example the mount path `BackupBtrfsDisk/Snapshots` where received snapshots are stored.
- `ssh-address` (string): Address of the remote RouterOS device for a `send` transfer.
- `ssh-receive-mount` (string): Mount path on the remote device under which the snapshots are received, for example `BackupBtrfsDisk/Snapshots`.
- `ssh-port` (num): SSH port of the remote device. Default: 22.
- `ssh-user` (string): SSH user to authenticate with on the remote device; the SSH key of the local user must be imported for `ssh-user` on the remote device.

**Read-only arguments**

- `bytes` (num): Number of bytes transferred so far.
- `status` (string): Status of the transfer, for example `done`, or an error message.
