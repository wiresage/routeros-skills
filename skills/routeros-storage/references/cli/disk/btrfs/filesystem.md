# /disk/btrfs/filesystem

> Source: https://manual.mikrotik.com/docs/cli-reference/disk/btrfs/filesystem

Conditions: !smips; Syscap: storage; Type: Directory

**Flags**

- `I` (missing-devs): One or more devices of the file system are missing, so the file system is degraded.
- `b` (balancing): A balance operation is running on the file system.
- `r` (replacing): A device replace operation is running on the file system.
- `s` (scrubbing): A scrub operation is running on the file system.

**Arguments**

- `label` (string): Label of the Btrfs file system, used to address the file system in the btrfs menus, for example `btrfsdisk`.
- `default-subvolume` (enum): Subvolume that is presented as the root folder of the file system in `/file`. `<FS_ROOT>` (default) is the root of the Btrfs file system itself.

**Read-only arguments**

- `uuid` (string): UUID of the Btrfs file system.
- `total-devs` (num): Number of devices in the file system.
- `dev-ids` (multi { array-id, devid: num }): Numeric device IDs of the devices in the file system; needed by [`replace-device`](filesystem.md) when a device is missing.
- `devs` (multi { array-id, dev: enum }): Disk slots of the devices in the file system, for example `nvme8,nvme9`.
- `spaces` (multi { array-id, space: string }): Space allocation of the file system, per device and per storage profile (`data`, `system`, `meta`, `global-reserve`), for example `data,raid1:1.07GB nvme8:1.07GB nvme9:1.07GB, used:1%`.
- `balance-status` (string): Status of the balance operation, for example `done`, or an error message such as `BTRFS_IOC_BALANCE_V2 failed: ...`.
- `replace-status` (string): Status of the replace or device removal operation, for example `done`, or an error message such as `BTRFS_IOC_DEV_REPLACE failed: File exists` or `BTRFS_IOC_RM_DEV_V2 failed: Resource temporarily unavailable`.
- `scrub-status` (string): Status of the scrub operation, for example `done`.
- `write-errors` (multi { snapshot: num }): Write error counters, one value per device in the file system. Reset with [`reset-counters`](filesystem.md).
- `read-errors` (multi { snapshot: num }): Read error counters, one value per device.
- `flush-errors` (multi { snapshot: num }): Flush error counters, one value per device.
- `corruption-errors` (multi { snapshot: num }): Data corruption error counters, one value per device.
- `generation-errors` (multi { snapshot: num }): Generation mismatch error counters, one value per device.

## Commands

### /disk/btrfs/filesystem/add-device

Conditions: !smips; Syscap: storage; Type: Command

**Arguments**

- `device` (enum): Disk slot to add to the Btrfs file system, for example `nvme9`. After adding a device, run [`balance-start`](filesystem.md) with the desired profiles (for example `data-profile=raid1`) to actually use it for storage redundancy; otherwise the device is only listed under `devs`.

### /disk/btrfs/filesystem/balance-cancel

Conditions: !smips; Syscap: storage; Type: Command

### /disk/btrfs/filesystem/balance-start

Conditions: !smips; Syscap: storage; Type: Command

**Arguments**

- `data-profile` (enum: single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10): Profile to convert the `data` chunks to: `single` stores chunks once (only sensible with a single device), `dup` stores them twice on the same device, the `raid*` profiles spread them across multiple devices. Change the profiles after [`add-device`](filesystem.md) to turn a single-disk file system into a Btrfs RAID, for example `data-profile=raid1`.
- `metadata-profile` (enum: single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10): Profile to convert the `meta` (metadata) chunks to. Metadata is small compared to data, so `dup` (default for a single device) or `raid1` are the common choices.
- `system-profile` (enum: single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10): Profile to convert the `system` chunks to; keep it the same as `metadata-profile`.
- `data-usage` (range): Only relocate data chunks that are at most this percentage full, for example `data-usage=50` skips chunks that are more than half full. Balancing is faster but incomplete with a lower value.
- `metadata-usage` (range): Only relocate metadata chunks that are at most this percentage full.
- `system-usage` (range): Only relocate system chunks that are at most this percentage full.

### /disk/btrfs/filesystem/remove-device

Conditions: !smips; Syscap: storage; Type: Command

**Arguments**

- `device` (enum): Disk slot of the device to remove from the file system, for example `nvme9`. The data on the device is first migrated to the remaining devices; removal fails if the current profiles cannot be kept with fewer devices (for example `data,raid1` cannot be kept when the device count drops below two).
- `device-id` (num): Numeric device ID of the device to remove (see `dev-ids` in [`filesystem`](filesystem.md)); needed when the device is missing and has no slot anymore.

### /disk/btrfs/filesystem/replace-cancel

Conditions: !smips; Syscap: storage; Type: Command

### /disk/btrfs/filesystem/replace-device

Conditions: !smips; Syscap: storage; Type: Command

**Arguments**

- `device-to-remove` (enum): Disk slot of the device to replace in the Btrfs file system.
- `device-to-remove-id` (num): Numeric device ID of the device to replace; use this instead of `device-to-remove` when the device is missing from the system (the `I - MISSING-DEVS` flag), as the slot is then no longer available.
- `device-to-add` (enum): Disk slot of the new device that takes over the data of the removed device.

### /disk/btrfs/filesystem/reset-counters

Conditions: !smips; Syscap: storage; Type: Command

### /disk/btrfs/filesystem/scrub-cancel

Conditions: !smips; Syscap: storage; Type: Command

### /disk/btrfs/filesystem/scrub-start

Conditions: !smips; Syscap: storage; Type: Command
