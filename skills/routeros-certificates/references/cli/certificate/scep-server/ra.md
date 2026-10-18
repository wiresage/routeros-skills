# /certificate/scep-server/ra

> Source: https://manual.mikrotik.com/docs/cli-reference/certificate/scep-server/ra

Type: Directory

**Flags**

- `X`: disabled
- `C`: smart-card-key

**Arguments**

- `name` (string; mandatory)
- `server-url` (string; mandatory)
- `template` (enum; mandatory)
- `challenge-password` (string)
- `ca-identity` (string)
- `fingerprint-algorithm` (enum: sha256 | sha1 | md5)
- `ra-path` (string)
- `ra-transaction-lifetime` (time)
- `on-smart-card` (bool): stores private key on smart card

**Read-only arguments**

- `req-fingerprint` (string)
- `ca-fingerprint` (string)
- `status` (string)

## Commands

### /certificate/scep-server/ra/renew

Type: Command
