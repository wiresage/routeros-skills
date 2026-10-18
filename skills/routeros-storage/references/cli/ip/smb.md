# /ip/smb

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/smb

Conditions: !smips; Type: Settings Directory

**Arguments**

- `enabled` (enum: no | auto | yes): Whether the built-in SMB server runs:
  - `no` - the server is disabled.
  - `auto` (default) - the server starts automatically when the first non-disabled share is configured in [`shares`](smb/shares.md).
  - `yes` - the server is enabled.
- `domain` (string): Name of the Windows workgroup the SMB server belongs to. Default: MSHOME.
- `comment` (string): Comment of the SMB server. Default: MikrotikSMB.
- `interfaces` (multi { array-id, interface: iface_enum }): Interfaces on which the SMB service listens. Default: all.

**Read-only arguments**

- `status` (string): Actual state of the SMB server, for example `enabled`.
