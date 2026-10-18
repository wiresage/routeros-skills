# /interface/macsec/profile

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/macsec/profile

Conditions: !smips; Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string; mandatory)
- `ciphers` (multi { cipher: enum (aes-gcm-128 | aes-gcm-xpn-128) }; mandatory)
- `server-priority` (num)

**Read-only arguments**

- `default-name` (string)
