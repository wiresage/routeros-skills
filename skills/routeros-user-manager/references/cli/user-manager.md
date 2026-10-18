# /user-manager

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager

Package: userman-5; Type: Settings Directory

**Arguments**

- `enabled` (bool)
- `authentication-port` (num)
- `accounting-port` (num)
- `certificate` (enum: none)
- `radsec-certificate` (enum: none)
- `use-profiles` (bool)
- `require-message-auth` (enum: no | yes-access-request)

## Commands

### /user-manager/generate-report

Package: userman-5; Type: Command

**Arguments**

- `columns` (ubit (username, session-start, session-end, user-ip, calling-station-id, uptime, download, upload, acct-session-id, nas-ip-address, nas-port-type, nas-port-id, terminate-cause, nas-identifier))
- `report-template` (enum)

### /user-manager/monitor

Package: userman-5; Type: Command

**Read-only arguments**

- `active-sessions` (num)
