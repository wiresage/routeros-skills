# /system/license

> Source: https://manual.mikrotik.com/docs/cli-reference/system/license

Type: Settings Directory

**Read-only arguments**

- `software-id` (string; syscap=nochr): Unique identifier for MikroTik hardware and x86 systems, used for licensing. Bound to the device storage.
- `old-software-id` (string; syscap=nochr): The previous Software ID, shown when the ID has changed.
- `nlevel` (num; syscap=nochr): The license level number (0-6).
- `features` (ubit (AP, synchronous, radiolan, wireless, extra-channels, , ,); syscap=nochr): Bitmask of licensed features.
- `expires-in` (time; syscap=nochr): Time remaining until the trial license expires.
- `system-id` (string; syscap=chr): Unique identifier for CHR instances, used for licensing. The license is tied directly to the CHR system ID.
- `level` (enum: free | p1 | p10 | p-unlimited; syscap=chr): Current CHR license level.
- `limited-upgrades` (bool; syscap=chr): Indicates whether RouterOS upgrades are limited. When the value is `yes`, RouterOS cannot be upgraded and package changes are disabled.
- `next-renewal-at` (date; syscap=chr): The next time the router attempts to contact the MikroTik license server.
- `deadline-at` (date; syscap=chr): The latest time by which successful communication with the license server must occur.

## Commands

### /system/license/generate-new-id

Syscap: chr; Type: Command

Generates a new unique system ID for a CHR instance. Use after the first boot and before requesting a trial license when deploying multiple CHR instances from the same disk image to avoid identical system IDs.

> **Warning**
>
> This command must only be used on a CHR running the Free license level. Do not use it after a trial or paid license has been applied.

### /system/license/output

Syscap: nochr; Type: Command

Outputs license information in a format suitable for support requests.

### /system/license/renew

Syscap: chr; Type: Command

**Arguments**

- `account` (string): MikroTik.com account username.
- `password` (string): MikroTik.com account password.
- `level` (enum: p1 | p10 | p-unlimited): The desired CHR license level.

**Read-only arguments**

- `status` (string): Status of the renewal operation.
