# /disk/btrfs/subvolume

> Source: https://manual.mikrotik.com/docs/cli-reference/disk/btrfs/subvolume

Conditions: !smips; Syscap: storage; Type: Directory

**Flags**

- `*` (default): The entry is the root subvolume of the file system, shown as `<FS_ROOT>`; it is created automatically with the file system.
- `S` (snapshot): The subvolume is a snapshot, created with the `parent` argument.
- `r` (read-only): The subvolume is read-only.
- `D` (dead): The subvolume is dead, for example it is being removed.
- `M` (mounted): The subvolume is mounted (`mount=yes`) under its `mountpoint`.

**Arguments**

- `fs` (enum; mandatory): Label of the Btrfs file system the subvolume belongs to, as shown in [`filesystem`](filesystem.md).
- `parent` (enum): Subvolume the new subvolume is created from. With `parent`, the new subvolume becomes a snapshot of the parent and shares its content at the time of creation. See [Btrfs subvolumes and snapshots](../../../guides/storage/btrfs/snapshots.md).
- `name` (string): Name of the subvolume. A path-like name, for example `Snapshots/backup-10`, places the subvolume inside another subvolume; `top-level` then shows the containing subvolume.
- `read-only` (bool): Whether the subvolume is read-only (`r - READ-ONLY` flag). Default: no.
- `mount` (bool): Whether the subvolume is mounted under its `mountpoint` (`M - MOUNTED` flag). Default: no.
- `mountpoint` (string): Mount point the subvolume is mounted under, relative to the file system mount point. Defaults to the name of the subvolume.

**Read-only arguments**

- `top-level` (enum): Top-level subvolume the subvolume is located in, for example `Snapshots`; `<FS_ROOT>` when the subvolume sits directly under the file system root.
- `fullname` (string): Full path of the subvolume within the file system, for example `Snapshots/backup-10`.
- `uuid` (string): UUID of the subvolume.
- `received-uuid` (string): UUID of the subvolume on the sender when the subvolume was received with a Btrfs [`transfer`](transfer.md); empty for locally created subvolumes.
- `creation-time` (date): Date and time the subvolume was created.
- `subvolume-id` (num): Btrfs ID number of the subvolume.
- `generation` (num): Btrfs transaction generation of the subvolume.
- `dead` (bool): Whether the subvolume is dead (`D - DEAD` flag).
- `snapshot` (bool): Whether the subvolume is a snapshot (`S - SNAPSHOT` flag).
- `send-trans-id` (num): Btrfs transaction ID of the last send the subvolume was part of.
- `send-time` (date): Time the subvolume was last sent with a Btrfs transfer.
- `recv-trans-id` (num): Btrfs transaction ID of the receive that created the subvolume.
- `recv-time` (date): Time the subvolume was received with a Btrfs transfer.
- `snapshots` (multi { array-id, snapshot: enum }): Snapshots that were created from this subvolume.
- `path` (string): Path the subvolume was received into by a Btrfs [`transfer`](transfer.md) (`file=` on the receiver); empty for locally created subvolumes.
