# /ip/ipsec/proposal

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/proposal

Type: Directory

Proposal information that will be sent by IKE daemons to establish SAs for certain policies.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `*` (default): Whether the item is the default.

**Arguments**

- `name` (string): Proposal name.
- `auth-algorithms` (ubit (sha512, sha256, sha1, md5, null)): Allowed authentication algorithms. MD5 uses a 128-bit key, SHA1 uses a 160-bit key.
- `enc-algorithms` (ubit (chacha20poly1305, aes-256-cbc, aes-256-ctr, aes-256-gcm, camellia-256, aes-192-cbc, aes-192-ctr, aes-192-gcm, camellia-192, aes-128-cbc, aes-128-ctr, aes-128-gcm, camellia-128, 3des, blowfish, twofish, des, null)): Allowed encryption algorithms.
- `lifetime` (time): Phase 2 lifetime.
- `pfs-group` (enum: none | ecp256 | ecp384 | ecp521 | modp6144 | modp4096 | modp3072 | modp2048 | modp1536 | modp1024 | modp768): Perfect Forward Secrecy group.
