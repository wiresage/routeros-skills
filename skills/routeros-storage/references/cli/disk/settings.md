# /disk/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/disk/settings

Conditions: !smips; Type: Settings Directory

**Arguments**

- `default-mount-point-template` (string): Mount point template that new disks and partitions get in place of their own `mount-point-template` when they are added. The template variables are the same as on a disk item (`[slot]`, `[model]`, `[serial]`, `[fw-version]`, `[fs-label]`, `[fs-uuid]`, `[fs]`). Default: [slot].
- `auto-smb-sharing` (bool): Whether a new disk or partition automatically gets an SMB share (see the SMB page). New items created by a later format get the share as well, and so do new `tmpfs` folders. The default configuration of some routers, for example the hAP ax², sets it to `yes`, so new disks and folders are shared on the LAN. Default: no.
- `auto-smb-user` (enum): Default user of the automatic SMB share created by `auto-smb-sharing=yes`. Default: guest.
- `auto-media-sharing` (bool): Whether a new disk or partition, including a new `tmpfs` folder, is automatically added to the DLNA media server (`/ip/media`). The default configuration of some routers, for example the hAP ax², sets it to `yes`. Default: no.
- `auto-media-interface` (iface_enum { none }): Interface used in the dynamic `/ip/media` entry created for a new disk when `auto-media-sharing=yes`. The default configuration of some routers, for example the hAP ax², sets it to `bridge`. Default: none.
