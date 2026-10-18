# /certificate/builtin

> Source: https://manual.mikrotik.com/docs/cli-reference/certificate/builtin

Type: Directory

**Arguments**

- `common-name` (string)
- `organization` (string)
- `unit` (string)
- `locality` (string)
- `state` (string)
- `country` (string)
- `subject-alt-name` (object { alt-name: composite { type: enum (IP | DNS | email) , value: alt { ip: alt { ipv6: ip6Addr , ip: ipAddr } , string: string } } })
- `key-size` (enum: prime256v1 | secp384r1 | secp521r1 | 1024 | 1536 | 2048 | 4096 | 8192)
- `key-usage` (ubit (digital-signature, content-commitment, key-encipherment, data-encipherment, key-agreement, key-cert-sign, crl-sign, encipher-only, decipher-only, tls-server, tls-client, code-sign, email-protect, timestamp, ocsp-sign, dvcs))
- `days-valid` (num)

**Read-only arguments**

- `issuer` (multi { array-id, issuer: string })
- `key-type` (enum: rsa | dsa | ec)
- `invalid-before` (date)
- `invalid-after` (date)
- `serial-number` (string)
- `akid` (string)
- `skid` (string)
