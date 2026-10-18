# /ip/smb/shares

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/smb/shares

Conditions: !smips; Type: Directory

**Flags**

- `D` (dynamic): The entry is created automatically.
- `X` (disabled): The share is disabled and not accessible to clients.
- `*` (default): The entry is a default entry created by the system.
- `r` (read-only): The share only allows clients to read; write access is denied.
- `c` (require-encryption): The share accepts only encrypted connections.

**Arguments**

- `name` (string; mandatory): Name of the SMB share that clients connect to.
- `directory` (file): Directory on the router that the share points to. When it is not set, the value of `name` from the root directory is used. The directory is created automatically if it does not exist.
- `read-only` (bool): Whether clients can only read the share. Access can also be restricted per user with `read-only` in [`users`](users.md). Default: no.
- `require-encryption` (bool): Whether only encrypted connections can access the share; recommended for macOS clients. Default: no.
- `valid-users` (multi { array-id, user: enum }): List of SMB users allowed to access the share. When the list is empty, all users can access it.
- `invalid-users` (multi { array-id, user: enum }): List of SMB users explicitly denied access to the share.
