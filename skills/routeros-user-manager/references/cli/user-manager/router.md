# /user-manager/router

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/router

Package: userman-5; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `address` (address (flags=46/); mandatory)
- `protocol` (enum: udp | radsec)
- `shared-secret` (string)
- `coa-port` (num)

## Commands

### /user-manager/router/monitor

Package: userman-5; Type: Command

**Read-only arguments**

- `broken-requests` (num)
- `unknown-requests` (num)
- `access-requests` (num)
- `access-failures` (num)
- `accounting-requests` (num)
- `accounting-failures` (num)
- `disconnect-ack` (num)
- `disconnect-nak` (num)
- `coa-ack` (num)
- `coa-nak` (num)
- `sent-from-cache` (num)

### /user-manager/router/reset-counters

Package: userman-5; Type: Command
