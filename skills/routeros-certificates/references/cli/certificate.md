# /certificate

> Source: https://manual.mikrotik.com/docs/cli-reference/certificate

Type: Directory

**Flags**

- `K`: private-key
- `L`: crl
- `C`: smart-card-key
- `A`: authority
- `I`: issued
- `R`: revoked
- `E`: expired
- `T`: trusted
- `a`: acme-managed
- `D`: dynamic

**Arguments**

- `active` (switch)
- `inactive` (switch)
- `name` (string)
- `trust-store` (alt { all: enum (all) , component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging) })
- `digest-algorithm` (enum: md5 | sha1 | sha256 | sha384 | sha512)
- `trusted` (bool)
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

- `ca-crl-host` (string)
- `ca` (enum)
- `scep-url` (string)
- `fingerprint` (string)
- `req-fingerprint` (string)
- `ca-fingerprint` (string)
- `expires-after` (time)
- `challenge-password` (string)
- `domain-names` (string)
- `directory-url` (string)
- `acme-status` (string)
- `revoked` (date)
- `status` (string)
- `issuer` (multi { array-id, issuer: string })
- `key-type` (enum: rsa | dsa | ec)
- `invalid-before` (date)
- `invalid-after` (date)
- `serial-number` (string)
- `akid` (string)
- `skid` (string)

## Commands

### /certificate/acme-renew

Type: Command

Renew an existing ACME certificate.

### /certificate/add-acme

Type: Command

**Arguments**

- `name` (string)
- `domain-names` (string): comma separated list of domain names or a wildcard domain
- `directory-url` (string)
- `eab-kid` (string)
- `eab-key-b64` (string)

### /certificate/add-scep

Type: Command

**Arguments**

- `name` (string)
- `ca-identity` (string)
- `template` (enum)
- `scep-url` (string)
- `challenge-password` (string)
- `on-smart-card` (bool): stores private key on smart card if hardware supports it
- `refresh` (bool): check certificate expiry and refresh it if expired

### /certificate/card-reinstall

Type: Command

**Arguments**

- `pin` (string)

### /certificate/card-verify

Type: Command

**Arguments**

- `pin` (string)

### /certificate/create-certificate-request

Type: Command

**Arguments**

- `template` (enum)
- `key-passphrase` (string)
- `challenge-passphrase` (string)

**Read-only arguments**

- `progress` (string)

### /certificate/enable-ssl-certificate

Type: Command

**Arguments**

- `dns-name` (string): domain name for SSL certificate
- `directory-url` (string): ACME directory url
- `eab-hmac-key` (string): base64url encoded EAB hmac key
- `eab-kid` (string): EAB account id
- `reset-private-key` (bool): initialize new private key

**Read-only arguments**

- `progress` (string)

### /certificate/export-certificate

Type: Command

**Arguments**

- `export-passphrase` (string)
- `type` (enum: pem | pkcs12)
- `file-name` (file)

### /certificate/import

Type: Command

**Arguments**

- `name` (string)
- `file-name` (file)
- `passphrase` (string)
- `trusted` (bool): mark as trusted
- `trust-store` (alt { all: enum (all) , component: ubit (ipsec, wpa-eap, capsman, fetch, sstp, ovpn, mqtt, email, netwatch, radius, container, userman, lora, wiliot, openflow, tr069, dot1x, dns, www, api, reverse-proxy, logging) })
- `no-key-export` (bool): disallow private key export

**Read-only arguments**

- `certificates-imported` (num)
- `private-keys-imported` (num)
- `files-imported` (num)
- `decryption-failures` (num)
- `keys-with-no-certificate` (num)
- `keys-decrypted` (num)

### /certificate/issued-revoke

Type: Command

### /certificate/scep-renew

Type: Command

### /certificate/sign

Type: Command

**Arguments**

- `name` (string)
- `ca-crl-host` (multi { array-id, host: string }): adds CRL URL to created certificate
- `ca-on-smart-card` (bool): stores CA's private key on smart card
- `ca` (enum): issuer CA

**Read-only arguments**

- `progress` (string)

### /certificate/sign-certificate-request

Type: Command

**Arguments**

- `ca` (enum)
- `file-name` (file)
- `days-valid` (num)
- `digest-algorithm` (enum: md5 | sha1 | sha256 | sha384 | sha512)
