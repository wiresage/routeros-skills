# /ip/smb/users

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/smb/users

Conditions: !smips; Type: Directory

**Flags**

- `D` (dynamic): The entry is created automatically.
- `X` (disabled): The user is disabled and cannot log in.
- `*` (default): The entry is a default entry created by the system.
- `r` (read-only): The user has read-only access to the shares.

**Arguments**

- `name` (string; mandatory): Login name of the SMB service user.
- `password` (string): Password of the SMB user.
- `read-only` (bool): Whether the user has read-only access to the shares. Default: yes.
