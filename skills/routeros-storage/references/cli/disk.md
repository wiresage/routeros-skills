# /disk

> Source: https://manual.mikrotik.com/docs/cli-reference/disk

Conditions: !smips; Type: Directory

**Flags**

- `X` (disabled): The device is disabled and is not used.
- `A`: acquired
- `E` (empty): The slot is empty, with no disk present. After `eject`, the slot stays empty until the disk is rescanned with `scan` or replugged.
- `B` (block-device): The device is a block device, that is, it can be used as storage: formatted or used in a RAID array. Devices without this flag only describe the disk layout.
- `M` (mounted): The device is mounted and its files appear in `/file`.
- `F` (formatting): The device is currently being formatted.
- `S` (swap-enabled): Swap is enabled on the device (`swap=yes`); the device is used as swap space, for example by containers.
- `f` (raid-member-failed): A member of the RAID array is in failed state.
- `r` (raid-member): The device is a member of a RAID array.
- `c` (encrypted): The device is encrypted, for example with `type=crypted` (dm-crypt).
- `g` (guid-partition-table): The device has a GUID partition table (GPT).
- `p` (partition): The device is a partition of a disk.
- `t` (nvme-tcp-export): The device is exported as an NVMe-over-TCP target.
- `i` (iscsi-export): The device is exported as an iSCSI target.
- `s` (smb-sharing): The device is shared through the built-in SMB server.
- `n` (nfs-sharing): The device is shared with the NFS server.
- `m` (media-sharing): The device is shared through the DLNA media server.
- `L`: self-encrypted-and-locked
- `O` (self-encryption-enabled): TCG-Opal self-encryption is active on the drive.
- `o` (self-encryption-supported): The drive supports TCG-Opal self-encryption, but it is not enabled.

**Arguments**

- `type` (enum: raid | nvme-tcp | iscsi | nfs | smb | partition | tmpfs | ramdisk | crypted | sshfs | file | hardware; mandatory): Type of the item:
  - `hardware` - a physical disk attached to the router, for example in a USB, SATA or NVMe slot.
  - `partition` - a partition on a hardware disk (see `parent`).
  - `file` - a file mounted as a block device (loop), for example a swap file or a mounted `.iso` / `.squashfs` image.
  - `tmpfs` - a folder in RAM, see [Tmpfs](../guides/storage/tmpfs.md).
  - `ramdisk` - part of RAM used as a block device, see [Ramdisk](../guides/storage/ramdisk.md) (storage package).
  - `raid` - a RAID array built from several disks, see [RAID](../guides/storage/raid.md) (storage package).
  - `crypted` - a dm-crypt encrypted block device, see [Encrypted storage](../guides/storage/encrypted-storage.md) (storage package).
  - `nvme-tcp` - a disk mounted over NVMe over TCP, see [NVMe over TCP](../guides/storage/nvme-over-tcp.md) (storage package).
  - `iscsi` - an iSCSI target mounted as a disk, see [iSCSI](../guides/storage/iscsi.md) (storage package).
  - `nfs` - an NFS share mounted as a disk, see [NFS](../guides/storage/nfs.md) (storage package).
  - `smb` - an SMB share mounted as a disk, see [SMB](../guides/storage/smb.md) (storage package).
  - `sshfs` - a remote folder mounted over SSH.
- `slot` (string): Name of the disk item, normally based on where the device is physically connected, for example `nvme1` or `usb1`. The name is assigned automatically and can be set manually. Other commands and `parent` refer to the disk by this name.
- `parent` (enum): Parent device of the item. On a `type=partition` item it selects the hardware disk the partition is created on, for example `add type=partition parent=nvme9 ...`; on `type=crypted` it is the drive or partition that is encrypted.
- `mount-point-template` (string): Template of the mount point, the folder under which the file system appears in `/file`. The following variables are replaced:
  - `[slot]` (default) - the slot name.
  - `[model]` - the device model.
  - `[serial]` - the device serial number.
  - `[fw-version]` - the device firmware version.
  - `[fs-label]` - the file system label.
  - `[fs-uuid]` - the file system UUID.
  - `[fs]` - the file system type.
  Variables can be combined, for example `[model]-[fs]`. An empty template is rejected, and `unset mount-point-template` restores the default `[slot]`. The default for newly added disks is set by `default-mount-point-template` in [`settings`](disk/settings.md). See [Disks](../guides/hardware/disks.md).
- `mount-filesystem` (bool): Whether the device's file system is mounted, so its files are available in `/file`. `mount-filesystem=no` unmounts the file system, which is required before `/disk check` or `/disk repair`. Default: yes.
- `mount-read-only` (bool): Whether the mounted file system is read-only. Default: no.
- `compress` (bool): Whether the device's file system is mounted with compression. Only supported on `btrfs` file systems; RouterOS reports `compression only available for btrfs` when it is set on other file systems. Default: no.
- `partition-number` (num): Number of the partition on the parent disk, for example `partition-number=1` for the first partition.
- `partition-offset` (num): Start offset of the partition on the disk, in bytes. Use it to adjust where the partition begins.
- `partition-size` (num): Size of the partition in bytes. When it is not set, the partition takes the remaining space on the disk. See [Disks](../guides/hardware/disks.md).
- `raid-type` (enum: 0 | 1 | 4 | 5 | 6 | linear; syscap=storage): RAID level of the array:
  - `0` - striping: data is spread evenly over all disks, no fault tolerance, best performance.
  - `1` - mirroring: the same data is written to all disks, best fault tolerance.
  - `4` - block-level striping with parity stored on a dedicated disk.
  - `5` - block-level striping with distributed parity, survives one disk failure.
  - `6` - block-level striping with double parity, survives two disk failures.
  - `linear` - the disks are joined into one large disk without redundancy.
  See [RAID](../guides/storage/raid.md).
- `raid-device-count` (num; syscap=storage): Number of devices (disks) in the RAID array, set when the array is created.
- `raid-max-component-size` (num; syscap=storage): Maximum size of an individual device in the RAID array.
- `raid-chunk-size` (enum: 64K | 128K | 256K | 512K | 1M | 2M | 4M; syscap=storage): Size of the chunks (stripes) written across the disks of the array, for example `1M`.
- `raid-master` (enum: none; syscap=storage): RAID block device a disk belongs to. Set it together with `raid-role` on the member disks to add them to an array created with `add type=raid ...`. On the RAID item itself it is `none`.
- `raid-role` (num; syscap=storage): Position of the disk within the RAID array, set with `raid-master`, starting from 0, or `spare` to mark the disk as a hot spare.
- `raid-member-failed` (bool; syscap=storage): Marks a drive as failed in the RAID array. Used when a non-failed drive needs to be replaced.
- `nvme-tcp-export` (bool; syscap=storage): Whether the device is exported as an NVMe-over-TCP target, so other devices can mount it. Default: no. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-server-port` (num; syscap=storage): Port on which the NVMe-over-TCP server accepts connections from initiators. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-server-nqn` (string; syscap=storage): NVMe Qualified Name (NQN) of the exported device, used by initiators to connect. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-server-allow-host-name` (string; syscap=storage): Hostnames allowed to connect to the NVMe-over-TCP server, for host-based access control. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-server-password` (string; syscap=storage): Password the NVMe-over-TCP server requires from initiators. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-address` (ipAddr; syscap=storage): IP address of the NVMe-over-TCP target (host) to mount, on the `nvme-tcp` client. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-nqn` (string; syscap=storage): NVMe Qualified Name (NQN) of the target on the server to mount, on the `nvme-tcp` client. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-host-name` (string; syscap=storage): Hostname the `nvme-tcp` initiator (client) identifies itself with; used for identification and authentication on the server. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-password` (string; syscap=storage): Password used to authenticate the NVMe-over-TCP connection to the server. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `nvme-tcp-port` (num; syscap=storage): Port the NVMe-over-TCP target listens on for connections from initiators. Default: 4420. See [NVMe over TCP](../guides/storage/nvme-over-tcp.md).
- `iscsi-export` (bool; syscap=storage): Whether the device is exported as an iSCSI target. Default: no. See [iSCSI](../guides/storage/iscsi.md).
- `iscsi-server-port` (num; syscap=storage): Port the iSCSI server listens on. See [iSCSI](../guides/storage/iscsi.md).
- `iscsi-server-iqn` (string; syscap=storage): iSCSI Qualified Name (IQN) of the iSCSI server, by default `iqn.2000-02.com.mikrotik:<slot>`. See [iSCSI](../guides/storage/iscsi.md).
- `iscsi-port` (num; syscap=storage): Port the iSCSI target listens on for connections from initiators. Default: 3260. See [iSCSI](../guides/storage/iscsi.md).
- `iscsi-address` (ipAddr; syscap=storage): IP address of the iSCSI target (host) to mount, on the `iscsi` client. See [iSCSI](../guides/storage/iscsi.md).
- `iscsi-iqn` (string; syscap=storage): iSCSI Qualified Name (IQN) of the target to mount, on the `iscsi` client. See [iSCSI](../guides/storage/iscsi.md).
- `nfs-sharing` (bool; syscap=storage): Whether the device is shared with NFS, so network clients can mount it. Default: no. See [NFS](../guides/storage/nfs.md).
- `nfs-address` (ipAddr; syscap=storage): IP address of the NFS server to mount, on the `nfs` client. See [NFS](../guides/storage/nfs.md).
- `nfs-share` (string; syscap=storage): Folder to mount on the NFS server, on the `nfs` client. See [NFS](../guides/storage/nfs.md).
- `smb-sharing` (bool): Whether the device is shared through the built-in SMB server (`/ip/smb`) when it is mounted. With `auto-smb-sharing=yes` in [`settings`](disk/settings.md) it is enabled automatically. Default: no.
- `smb-server-user` (enum): SMB user of the auto-created share of this disk; the default for new disks is taken from `auto-smb-user` in [`settings`](disk/settings.md).
- `smb-server-password` (string): Password of the SMB user of the auto-created share.
- `smb-server-encryption` (bool): Whether connections to the SMB share of this disk must be encrypted.
- `smb-address` (ipAddr): IP address of the SMB server to mount, on the `smb` client. See [SMB](../guides/storage/smb.md).
- `smb-share` (string): Name of the share to mount on the server, on the `smb` client. See [SMB](../guides/storage/smb.md).
- `smb-user` (string): SMB user to authenticate with, on the `smb` client. See [SMB](../guides/storage/smb.md).
- `smb-password` (string): Password of the SMB user, on the `smb` client.
- `smb-encryption` (bool): Whether the connection to the remote SMB share is encrypted, on the `smb` client.
- `media-sharing` (bool): Whether the device is shared through the DLNA media server (`/ip/media`) when it is mounted. With `auto-media-sharing=yes` in [`settings`](disk/settings.md) it is enabled automatically. Default: no.
- `media-interface` (iface_enum { none }): Interface the DLNA media server uses for the share of this disk, set together with `media-sharing=yes`.
- `tmpfs-max-size` (num): Maximum size of a `tmpfs` folder, in decimal units (`100M` is 100 000 000 bytes). The folder uses RAM only for the files stored in it. When the size is not set (it reads `0`), the folder can grow to about half of the RAM. RouterOS adds up the maximum sizes of all tmpfs folders, counting a folder without `tmpfs-max-size` as half of the RAM, and refuses a new size when the total is more than the router can provide (`too much memory requested for tmpfs/ramdisk`). The size in `print` is rounded up to whole 4 KiB memory pages. A new value applies at once, also to a mounted folder. The contents of a `tmpfs` are lost on reboot or power loss. See [Tmpfs](../guides/storage/tmpfs.md). Default: not set.
- `ramdisk-size` (num; syscap=storage): Size of the RAM block device created with `type=ramdisk`, rounded up to a multiple of 16 KiB. The RAM is not reserved when the ramdisk is added. A reboot or power loss clears it: the ramdisk stays, but empty and without a file system, so format it again. Needs the `rose-storage` package. See [Ramdisk](../guides/storage/ramdisk.md).
- `crypted-backend` (enum: none; syscap=storage): The drive or partition to encrypt with `type=crypted`. See [Encrypted storage](../guides/storage/encrypted-storage.md).
- `encryption-key` (string; syscap=storage): The key used to decrypt the `crypted` device. See [Encrypted storage](../guides/storage/encrypted-storage.md).
- `self-encryption-password` (string; syscap=storage): Password that enables TCG-Opal self-encryption on a supported (SED) drive; unsetting it disables self-encryption. See [Self-encrypting drives](../guides/storage/self-encrypting-drives.md).
- `sshfs-address` (string): Address (IP address or hostname) of the SSH server to mount, for `type=sshfs`. See [SSHFS](../guides/storage/sshfs.md).
- `sshfs-port` (num): Port of the SSH server to connect to, for `type=sshfs` (default: 22). See [SSHFS](../guides/storage/sshfs.md).
- `sshfs-user` (string): User to log in to the remote SSH server with, for `type=sshfs`. See [SSHFS](../guides/storage/sshfs.md).
- `sshfs-password` (string): Password of the remote SSH user, for `type=sshfs`. See [SSHFS](../guides/storage/sshfs.md).
- `sshfs-path` (string): Path on the remote SSH server to mount, for `type=sshfs`. See [SSHFS](../guides/storage/sshfs.md).
- `swap` (bool): Use the device as swap space. Swap is used only by containers, and its usable size is limited to 10 times the device's RAM. It applies to a whole disk or partition, or to a file with `type=file`. See [Disks](../guides/hardware/disks.md).
- `file-path` (file): Path and name of the file mounted as a block device with `type=file`, for example a swap file (`swap=yes`) or a mounted `.iso` / `.squashfs` image. Removing the disk item does not delete the file. See [Disks](../guides/hardware/disks.md).
- `file-size` (num): Size of the file, for example `file-size=1G`, when creating a `type=file` device.
- `file-offset` (num): Offset in the file at which the block device starts, for example `file-offset=0`.

**Read-only arguments**

- `slot-default` (string): Default slot name of the device, shown when no custom `slot` name is set.
- `fs-label` (string): Label of the file system. Formatting sets it automatically to `<slot>-fs`, unless a `label` is given to `/disk format`.
- `fs-uuid` (string): UUID of the file system, for example `58470fe2-...`.
- `fs` (enum: fat32 | ext4 | btrfs | xfs | nfs | smb | wipe | wipe-quick | tmpfs | exfat | ntfs | sshfs | squashfs | iso | discard | discard-secure | -): File system of the device: `ext4`, `btrfs`, `xfs`, `fat32`, `exfat` and `ntfs` for local file systems, `tmpfs` for RAM folders, `nfs`, `smb` and `sshfs` for network mounts, and `iso` / `squashfs` for mounted images. `-` means the device has no recognised file system. The values `wipe`, `wipe-quick`, `discard` and `discard-secure` correspond to the file systems of `/disk format`.
- `model` (string): Model name of the device, for example `TS1TUTE210T`.
- `serial` (string): Serial number of the device.
- `fw-version` (string): Firmware version of the device.
- `size` (num): Total size of the device in bytes.
- `free` (num): Free space on the mounted file system in bytes.
- `total-inodes` (num): Total number of inodes of the file system.
- `free-inodes` (num): Number of free inodes of the file system.
- `use` (num): Used space of the file system in percent, for example `4%`.
- `mount-point` (string): Mount point of the file system, the folder under which it appears in `/file`, driven by `mount-point-template`.
- `sector-size` (num): Sector size of the device, for example 512 bytes.
- `interface` (string): Interface the device is connected to, for example `PCIe 2x8 GT/s` or `USB 2.00 480Mbps`.
- `interface-speed` (num): Speed of the interface the device is connected to, for example `15.7Gbps`.
- `raid-member-state` (string; syscap=storage): State of the disk as a member of its RAID array, for example `0:in_sync`; when the disk is not part of an assembled array, the details of the RAID superblock found on it are shown instead.
- `state` (string): State of a RAID array, for example `clean`.
- `last-seen` (string): Model and serial number of the disk that last occupied this slot, shown after the disk was ejected or removed, for example `TS1TUTE210T J398770033`.
- `raid-uuid` (string; syscap=storage): UUID of the RAID array.
- `nvme-tcp-server-secret` (string; syscap=storage): Secret the NVMe-over-TCP server uses to authenticate connections from initiators.
- `nvme-tcp-secret` (string; syscap=storage): Secret used to authenticate the connection to the NVMe-over-TCP server.
- `sshfs-local-user` (string): Local RouterOS user the SSHFS mount runs under, for example `admin`. Read-only.
- `io-ops` (num): Total number of I/O operations on the device, as shown by [`monitor-traffic`](disk.md).
- `io-errors` (num): Total number of I/O errors on the device.
- `read-ops` (num): Total number of read operations.
- `read-ops-per-second` (num): Number of read operations per second.
- `read-bytes` (num): Total number of bytes read.
- `read-rate` (num): Rate of reads, for example in bytes per second.
- `read-merges` (num): Number of adjacent read operations merged.
- `read-time` (time): Time spent on read operations.
- `write-ops` (num): Total number of write operations.
- `write-ops-per-second` (num): Number of write operations per second.
- `write-bytes` (num): Total number of bytes written.
- `write-rate` (num): Rate of writes, for example in bytes per second.
- `write-merges` (num): Number of adjacent write operations merged.
- `write-time` (time): Time spent on write operations.
- `in-flight-ops` (num): Number of I/O operations currently in flight.
- `active-time` (time): Time the device was busy handling requests.
- `wait-time` (time): Time requests spent waiting in the queue.
- `discard-ops` (num): Total number of discard (trim) operations.
- `discard-bytes` (num): Total number of bytes discarded.
- `discard-merges` (num): Number of adjacent discard operations merged.
- `discard-time` (time): Time spent on discard operations.
- `flush-ops` (num): Total number of flush operations.
- `flush-time` (time): Time spent on flush operations.
- `temperature` (num): Temperature of the drive in Celsius, reported by S.M.A.R.T. (storage package). See the [S.M.A.R.T. info](../guides/hardware/disks/smart.md) guide and [`smart-info`](disk.md).
- `temperatures` (multi { array-id, slot: num }): Temperatures of the drive's sensors in Celsius, one entry per sensor slot.
- `critical-warning` (ubit (spare-space, temperature, reliability-degraded, read-only, volatile-backup-failed)): Bitmask of critical warnings the drive reports: `spare-space` (available spare is below `available-spare-threshold`), `temperature` (temperature out of range), `reliability-degraded`, `read-only` (the device entered read-only mode) and `volatile-backup-failed`.
- `available-spare` (num): Remaining spare blocks of the drive in percent, for example 100%. Below `available-spare-threshold` the drive reports a warning.
- `available-spare-threshold` (num): Threshold in percent below which the available spare space of the drive is reported as a warning.
- `percentage-used` (num): Estimated percentage of the drive's life used, based on how many spare blocks have been consumed.
- `host-read-bytes` (num): Total number of bytes read by the host from the drive.
- `host-write-bytes` (num): Total number of bytes written by the host to the drive.
- `host-read-cmds` (num): Total number of read commands the host sent to the drive.
- `host-write-cmds` (num): Total number of write commands the host sent to the drive.
- `controller-busy-time` (time): Total time the drive controller was busy with commands.
- `power-cycles` (num): Number of power cycles of the drive.
- `power-on-time` (time): Total time the drive was powered on.
- `unsafe-shutdowns` (num): Number of unsafe (unexpected) shutdowns of the drive.
- `unrecovered-integrity-errors` (num): Number of unrecovered media and data integrity errors of the drive.
- `warning-temperature` (num): Temperature in Celsius at which the drive starts reporting a warning.
- `warning-temperature-time` (time): Time the drive spent above `warning-temperature`.
- `critical-temperature` (num): Temperature in Celsius at which the drive reports a critical condition.
- `critical-temperature-time` (time): Time the drive spent above `critical-temperature`.

## Commands

### /disk/blink

Conditions: !smips; Type: Command

**Arguments**

- `slots` (multi { array-id, slot: enum }): Disks whose LED should blink, if device supports it.

### /disk/check

Conditions: !smips; Syscap: storage; Type: Command

**Read-only arguments**

- `output` (string): The check tool output: for ext4, the `e2fsck` passes and a summary line with file and block usage.

### /disk/copy

Conditions: !smips; Type: Command

**Arguments**

- `src` (enum): Source disk, partition or file.
- `dst` (enum): Destination disk, partition or file. It must be at least as large as the copied data.
- `src-offset` (num): Byte offset in the source where the copy starts. Default: 0.
- `dst-offset` (num): Byte offset in the destination where the data is written. Default: 0.
- `size` (num): Number of bytes to copy. Without it, the whole source is copied.

**Read-only arguments**

- `status` (string): Progress of the copy: `<bytes copied> / <total bytes> (<percent>%)`.

### /disk/eject

Conditions: !smips; Type: Command

### /disk/format

Conditions: !smips; Type: Command

**Arguments**

- `file-system` (enum: fat32 | ext4 | btrfs | xfs | wipe | wipe-quick | exfat | discard | discard-secure): What filesystem to format the disk.
  - `ext4` - Format with ext4; the default for most use cases.
  - `fat32` - Format with FAT32, readable by almost any device.
  - `exfat` - Format with exFAT, for large files on memory cards and USB drives.
  - `btrfs` - Format with Btrfs (data checksums, snapshots, RAID); needs the [Storage](../guides/storage.md) package.
  - `xfs` - Format with XFS; needs the [Storage](../guides/storage.md) package.
  - `discard` - Discard all blocks of the disk (the equivalent of `blkdiscard`) without writing a file system.
  - `discard-secure` - Same, but with a secure discard that also erases the underlying data.
  - `wipe` - Overwrite all data on the disk so it cannot be recovered.
  - `wipe-quick` - Remove the file system without overwriting the data; fast, but data can be recovered with tools.
- `label` (string): File system label. Default: `<slot>-fs`.
- `mbr-partition-table` (bool): Write an MBR partition table to the disk as part of the format. Without it the disk receives no partition table; use `add type=partition` afterwards to create partitions, which are stored in a GUID partition table. Default: no.

**Read-only arguments**

- `output` (string): Progress of the format: the `mkfs` command line and its output, a progress percentage or byte counter, and a final `format done` line.

### /disk/monitor-traffic

Conditions: !smips; Type: Command

**Read-only arguments**

- `io-ops` (num): Total number of I/O operations since the last `reset-counters`.
- `io-errors` (num): Total number of I/O errors.
- `slot` (string): The disk that is being monitored.
- `read-ops` (num): Total number of read operations.
- `read-ops-per-second` (num): Read operations per second.
- `read-bytes` (num): Total bytes read.
- `read-rate` (num): Current read speed.
- `read-merges` (num): Total number of merged read operations (adjacent requests the driver combined).
- `read-time` (time): Total time spent reading.
- `write-ops` (num): Total number of write operations.
- `write-ops-per-second` (num): Write operations per second.
- `write-bytes` (num): Total bytes written.
- `write-rate` (num): Current write speed.
- `write-merges` (num): Total number of merged write operations.
- `write-time` (time): Total time spent writing.
- `in-flight-ops` (num): Operations currently queued on the disk.
- `active-time` (time): Total time the disk was busy with requests.
- `wait-time` (time): Total time requests waited in the queue before being processed.
- `discard-ops` (num): Total number of discard (TRIM) operations.
- `discard-bytes` (num): Total bytes discarded.
- `discard-merges` (num): Total number of merged discard operations.
- `discard-time` (time): Total time spent discarding.
- `flush-ops` (num): Total number of flush operations.
- `flush-time` (time): Total time spent flushing.

### /disk/nvme-discover

Conditions: !smips; Syscap: storage; Type: Command

**Arguments**

- `address` (ipAddr): IP address of the NVMe over TCP controller.
- `port` (num): TCP port of the controller's discovery service. Default: 4420.
- `host-name` (string): Host NQN this router presents to the controller, used for identification and host-based access control.

**Read-only arguments**

- `nqn` (string): NVMe Qualified Name of a subsystem the controller exposes.

### /disk/raid-scrub

Conditions: !smips; Syscap: storage; Type: Command

### /disk/raid-scrub-cancel

Conditions: !smips; Syscap: storage; Type: Command

### /disk/repair

Conditions: !smips; Syscap: storage; Type: Command

**Read-only arguments**

- `output` (string): The repair tool output, ending in a summary line such as `...: clean, 12/61056 files, 139612/244140 blocks`.

### /disk/reset-counters

Conditions: !smips; Type: Command

### /disk/scan

Conditions: !smips; Type: Command

### /disk/smart-info

Conditions: !smips; Syscap: storage; Type: Command

**Read-only arguments**

- `output` (string): The full smartctl output for the disk.

### /disk/test

Conditions: !smips; Type: Command

**Flags**

- `N` (initializing): The test is initializing (preparing, clearing the caches) and has not started reading or writing yet.
- `R` (running): The test is running.
- `F` (failed): The test failed.

**Arguments**

- `disk` (multi { array-id, disk: enum }): Disk or partition to test.
- `block-size` (num): Size of one read or write block. Default: 64 KiB.
- `thread-count` (num): Number of parallel test threads. Default: 1.
- `direction` (enum: read | write): What the test does with the data.
  - `read` (default) - Read the disk; does not change its content.
  - `write` - Write to the disk; destroys all data on it.
- `type` (enum: device | filesystem): Test target: `device` reads or writes the raw block device, `filesystem` goes through the mounted file system. Default: device.
- `pattern` (enum: sequential | random): Access pattern.
  - `sequential` (default) - Read or write consecutive blocks.
  - `random` - Read or write blocks at random positions.
- `entries-to-show` (num): How many of the most recent result rows to keep and show.

**Read-only arguments**

- `seq` (enum (TOT) { TOT:0xffffffff }): Sequence number of the result row; the `TOT` row aggregates all threads.
- `rate` (num): Current throughput of this row.
- `iops` (num): Input/output operations per second.
- `bytes` (num): Bytes transferred for this row so far.
- `disk` (enum (TOT) { TOT:0xffffffff }): The tested disk.
- `thread` (enum (TOT) { TOT:0xffffffff }): Thread this row belongs to; `TOT` aggregates all threads.
- `type` (enum: device | filesystem): Test type as given when the test was started.
- `pattern` (enum: sequential | random): Access pattern as given when the test was started.
- `dir` (enum: read | write): Direction (`read` or `write`) as given when the test was started.
- `bsize` (num): Block size as given when the test was started.
- `state` (string): State of a running test, for example `clear caches` while it prepares and `run` while it works.

### /disk/trim

Conditions: !smips; Type: Command
