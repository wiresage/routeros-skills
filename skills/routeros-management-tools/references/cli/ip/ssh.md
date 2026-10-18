# /ip/ssh

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ssh

Type: Settings Directory

SSH server settings (ciphers, forwarding, authentication) and the settings controlling how the router verifies remote servers when it connects as an SSH client. See [SSH](../../guides/management-tools/ssh.md) for the full guide.

**Arguments**

- `ciphers` (multi { array-id, cipher: enum (aes-gcm | aes-ctr | aes-cbc | 3des-cbc | null | auto) }): Allowed cipher list.
- `forwarding-enabled` (enum: no | local | remote | both): Control which SSH forwarding method to allow: `no` - SSH forwarding is disabled, `local` - allow SSH clients to originate connections from the server (router), this also controls dynamic forwarding, `remote` - allow SSH clients to listen on the server (router) and forward incoming connections, `both` - allow both local and remote forwarding methods.
- `password-authentication` (enum: yes | no | yes-if-no-key): Whether to allow password login when public key authorization is configured for a user.
- `publickey-authentication-options` (enum: none | touch-required | verify-required): Public key authentication options. The `touch-required` option causes public key authentication by using a FIDO authenticator algorithm to always require the signature to attest that a physically present user explicitly confirmed the authentication (usually by touching the authenticator). The `verify-required` option requires a FIDO key signature to attest that the user was verified, for example, by using a PIN.
- `strong-crypto` (bool): Use stronger encryption, HMAC algorithms, use bigger DH primes and disallow weaker ones: use 256 and 192 bit encryption instead of 128 bits, disable null encryption, use sha256 for hashing instead of sha1, disable md5, use 2048bit prime for Diffie-Hellman exchange instead of 1024bit.
- `known-hosts-validation` (bool): Verify the server's host key against the keys stored in [`known-hosts`](ssh/known-hosts.md) whenever the router connects as an SSH client (fetch SFTP, [`/system/ssh`](../system/ssh.md), [`/system/ssh-exec`](../system/ssh-exec.md)). With validation enabled and no matching key stored, the interactive client shows the server's fingerprint and asks `do you want to trust this host key?`, while non-interactive commands fail with `host key not trusted`. On new installations validation is enabled; upgraded routers keep the previous value. Default: yes.
- `known-hosts-trusted-subnets` (object { subnets: ip6Prefix }): Skip host key validation for servers whose address belongs to these subnets, even when `known-hosts-validation` is enabled. Hosts outside the listed subnets are still validated.
- `host-key-size` (enum: 1024 | 1536 | 2048 | 4096 | 8192): RSA key size when host key is regenerated.
- `host-key-type` (enum: rsa | ed25519): Host key type.

**Read-only arguments**

- `host-key-fingerprint` (string): Fingerprint of the current host key. Can be used to verify that you are connecting to the correct router.

## Commands

### /ip/ssh/export-host-key

Type: Command

Export public and private RSA/Ed25519 keys to files.

> **Info**
>
> Host keys are exported in PKCS#8 format.
>
> Exporting the SSH host key requires "sensitive" user policy.

**Arguments**

- `key-file-prefix` (string): Prefix for the generated files: for example `my` produces `my_rsa.pem` (private key) and `my_rsa_pub.pem` (public key) for an RSA host key, or `my_ed25519.pem` and `my_ed25519_pub.pem` for an Ed25519 one. Both files are in PKCS#8 PEM format.
- `passphrase` (string): Private key passphrase.

### /ip/ssh/import-host-key

Type: Command

Import and replace the private RSA/Ed25519 key from a specified file

> **Info**
>
> The private key is supported in PEM or PKCS#8 format.

**Arguments**

- `private-key-file` (file): Name of the private RSA/Ed25519 key file in PEM or PKCS#8 format.
- `passphrase` (string): Private key passphrase.

### /ip/ssh/regenerate-host-key

Type: Command

Generates new and replaces the current set of private keys (RSA/Ed25519) on the router. Previously imported keys may stop working.
