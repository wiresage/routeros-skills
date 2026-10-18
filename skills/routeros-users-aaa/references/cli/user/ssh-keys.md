# /user/ssh-keys

> Source: https://manual.mikrotik.com/docs/cli-reference/user/ssh-keys

Type: Directory

Public SSH keys assigned to users; the keys authenticate those users' incoming SSH logins. When a user has at least one key assigned, the SSH server refuses password authentication for that user and offers only public-key authentication. See [User](../../guides/authentication-authorization-accounting/user.md) for the full guide.

**Arguments**

- `user` (enum): System user the key is assigned to.
- `info` (string): Free-text label for the key. When adding a key with `key`, a trailing comment in the pasted OpenSSH key string becomes the key's `info` and overrides this parameter.
- `key` (string): Public key string, set only when adding a new key. Only the OpenSSH single-line format is accepted; PEM blocks are rejected.

**Read-only arguments**

- `key-type` (enum: rsa | ed25519 | ed25519-sk): Type of the key: `rsa`, `ed25519` or `ed25519-sk`.
- `bits` (num): Key length in bits.
- `fingerprint` (string): SHA256 fingerprint of the key in base64 (for example `SHA256:...`).

## Commands

### /user/ssh-keys/import

Type: Command

Imports a public SSH key from a file in the router's root directory and assigns it to a user. Accepted formats: OpenSSH single-line, PKCS#1 PEM ("BEGIN RSA PUBLIC KEY") and PKCS#8/SPKI PEM ("BEGIN PUBLIC KEY"). See [User](../../guides/authentication-authorization-accounting/user.md) for the full guide.

**Arguments**

- `public-key-file` (file): Name of the key file in the router's root directory.
- `user` (enum): System user to assign the key to.
- `info` (string): Free-text label for the key.
