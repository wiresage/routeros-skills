# /user/ssh-keys/private

> Source: https://manual.mikrotik.com/docs/cli-reference/user/ssh-keys/private

Type: Directory

Private SSH keys that identify the router in outgoing SSH connections to other devices, for example with [`/system/ssh`](https://manual.mikrotik.com/docs/cli-reference/system/ssh) or [`/tool/fetch`](https://manual.mikrotik.com/docs/cli-reference/tool/fetch). All properties are read-only; keys are added with [`/user/ssh-keys/private/import`](private.md). See [User](../../../guides/authentication-authorization-accounting/user.md) for the full guide.

**Read-only arguments**

- `user` (enum): System user that owns the key.
- `key-type` (enum: rsa | ed25519): Type of the key: `rsa` or `ed25519`.
- `bits` (num): Key length in bits.
- `info` (string): Free-text label for the key.

## Commands

### /user/ssh-keys/private/import

Type: Command

Imports a private SSH key from a file in the router's root directory. Accepted formats: PKCS#1 PEM RSA ("BEGIN RSA PRIVATE KEY"), PKCS#8 ("BEGIN PRIVATE KEY") and encrypted PKCS#8 ("BEGIN ENCRYPTED PRIVATE KEY", requires `passphrase`). OpenSSH-format private keys ("BEGIN OPENSSH PRIVATE KEY") are rejected. See [User](../../../guides/authentication-authorization-accounting/user.md) for the full guide.

**Arguments**

- `private-key-file` (file): Name of the key file in the router's root directory.
- `user` (enum): System user that owns the key.
- `passphrase` (string): Passphrase of an encrypted key file.
- `info` (string): Free-text label for the key.
