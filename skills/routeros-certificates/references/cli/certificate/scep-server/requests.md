# /certificate/scep-server/requests

> Source: https://manual.mikrotik.com/docs/cli-reference/certificate/scep-server/requests

Type: Directory

**Read-only arguments**

- `authority` (alt { ca: enum , ra: enum })
- `status` (enum: pending | granted | denied | authorized | waiting | failed | issued | invalid)
- `created` (date)
- `transaction-id` (string)
- `req-fingerprint` (string)
- `country` (string)
- `state` (string)
- `locality` (string)
- `organization` (string)
- `unit` (string)
- `common-name` (string)
- `serial-number` (string)
- `subject-alt-name` (object { alt-name: composite { type: enum (IP | DNS | email) , value: alt { ip: alt { ipv6: ip6Addr , ip: ipAddr } , string: string } } })

## Commands

### /certificate/scep-server/requests/grant

Type: Command
