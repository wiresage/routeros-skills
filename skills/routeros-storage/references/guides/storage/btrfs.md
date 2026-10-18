# Btrfs

> Source: https://manual.mikrotik.com/docs/storage/btrfs
>
> Btrfs is a stable copy-on-write file system with features like bitrot protection, subvolumes, and snapshots. It is available with the Storage package and supports RAID configurations, subvolume management, and...

> **Info**
>
> This feature requires the [Storage](../storage.md) package.

Btrfs is a feature-rich copy-on-write file system. It is the default file system for some popular Linux distributions such as [Fedora](https://en.wikipedia.org/wiki/Fedora_Linux) and is used by many large companies such as. Over the years it has proven itself to be stable and more flexible than other popular file systems. The most significant features are:

- Bitrot protection (when used in Btrfs-RAID mode).
- Subvolumes.
- Snapshots.
- Snapshot transfer between devices.

## Quickstart: format a disk as Btrfs

Format a single disk to Btrfs and use it under the default mount point:

```routeros
/disk/print
/disk/format <disk-name> file-system=btrfs
/disk/btrfs/filesystem/print
```

Once formatted, the disk appears with a new Btrfs filesystem entry under `/disk/btrfs/filesystem/print`, labelled `<disk-name>-fs` by default (the label can be changed with `/disk/btrfs/filesystem/set <label> label=MyLabel`). The disk mounts like any other drive and is accessible in `/file`. From here you can label the file system, create [subvolumes and snapshots](btrfs/snapshots.md), combine several disks into a [Btrfs RAID](btrfs/raid.md), or set up routine [maintenance](btrfs/maintenance.md).

The Btrfs functionality lives under three menus:

- [`/disk/btrfs/filesystem`](../../cli/disk/btrfs/filesystem.md) - one entry per formatted Btrfs file system: labels, device membership ([`add-device`](../../cli/disk/btrfs/filesystem.md), [`remove-device`](../../cli/disk/btrfs/filesystem.md), [`replace-device`](../../cli/disk/btrfs/filesystem.md)), RAID profiles and maintenance jobs ([`balance-start`](../../cli/disk/btrfs/filesystem.md), [`scrub-start`](../../cli/disk/btrfs/filesystem.md), [`reset-counters`](../../cli/disk/btrfs/filesystem.md)).
- [`/disk/btrfs/subvolume`](../../cli/disk/btrfs/subvolume.md) - subvolumes and snapshots of a file system.
- [`/disk/btrfs/transfer`](../../cli/disk/btrfs/transfer.md) - send and receive of snapshots to and from other devices.

## See also

- [Btrfs RAID](btrfs/raid.md) - RAID1 and RAID10 setups, disk replacement, and the BraidHealthCheck script.
- [Btrfs subvolumes and snapshots](btrfs/snapshots.md) - creating subvolumes, taking snapshots, transferring snapshots between devices.
- [Btrfs maintenance](btrfs/maintenance.md) - periodic scrubbing, balancing, automated snapshot rotation, and free-space management.
