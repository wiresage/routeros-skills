# /ip/ipsec/installed-sa

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/installed-sa

Type: Directory

This menu provides information about installed security associations including the keys.

**Flags**

- `S` (seen-traffic): Whether traffic has passed through the SA.
- `H` (hw-aead): Whether hardware AEAD acceleration is used.
- `A` (AH): Whether the SA uses AH protocol.
- `E` (ESP): Whether the SA uses ESP protocol.

**Arguments**

- `spi` (num): Security Parameter Index value.
- `state` (enum: larval | mature | dying | dead): Current SA state.
- `auth-algorithm` (enum: none | md5 | sha1 | sha256 | sha512): Authentication algorithm.
- `enc-algorithm` (enum: none | des | 3des | null | aes-cbc | aes-ctr | aes-gcm | blowfish | twofish | camellia | chacha20poly1305): Encryption algorithm.
- `enc-key-size` (num): Encryption key size in bits.
- `auth-key` (string): Authentication key value.
- `enc-key` (string): Encryption key value.
- `addtime` (date): Time when the SA was added.
- `expires-in` (time): Time until the SA expires.
- `add-lifetime` (composite { soft: time , hard: time }): Added lifetime for the SA in the format soft/hard:
  - soft - time period after which IKE will try to establish a new SA;
  - hard - time period after which the SA is deleted.
- `current-bytes` (num): Number of bytes processed by the SA.
- `current-packets` (num): Number of packets processed by the SA.
- `invalid-packets` (num): Number of invalid packets.
- `replay` (num): Replay window size.

**Read-only arguments**

- `src-address` (super { src-address: alt { ipv6: ip6Addr , ip: ipAddr } , [port] :num }): Source address and port.
- `dst-address` (super { dst-address: alt { ipv6: ip6Addr , ip: ipAddr } , [port] :num }): Destination address and port.

## Commands

### /ip/ipsec/installed-sa/flush

Type: Command

Manually removes all installed security associations.
