# /ip/ipsec/key/rsa

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/key/rsa

Type: Directory

**Flags**

- `P` (private-key): Whether the item contains a private key.
- `R` (rsa): Whether the item uses an RSA key.

**Arguments**

- `name` (string): Key name.

**Read-only arguments**

- `key-size` (num): RSA key size in bits.

## Commands

### /ip/ipsec/key/rsa/export-pub-key

Type: Command

Export public key to file from one of the existing private keys.

**Arguments**

- `key` (enum): Name of the RSA key to export.
- `file-name` (string): Name of the file to export the public key to.

### /ip/ipsec/key/rsa/generate-key

Type: Command

Generate a private key. Takes two parameters, name of the newly generated key and key size 1024,2048 and 4096.

**Arguments**

- `name` (string): Name for the generated key.
- `key-size` (alt { key-size: enum (2048 | 4096 | 8192) }): RSA key size in bits.

### /ip/ipsec/key/rsa/import

Type: Command

Import key from file.

**Arguments**

- `file-name` (file): Name of the file to import the key from.
- `name` (string): Name for the imported key.
- `passphrase` (string): Passphrase for the key file.
