# /ip/ipsec/profile

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/profile

Type: Directory

Profiles define a set of parameters used for IKE negotiation during Phase 1. These parameters can be shared with other peer configurations.

**Flags**

- `*` (default): Whether the item is the default.

**Arguments**

- `name` (string; mandatory): Profile name.
- `hash-algorithm` (enum: md5 | sha1 | sha256 | sha384 | sha512): Hash algorithm.
- `prf-algorithm` (enum: auto | sha1 | sha256 | sha384 | sha512): PRF algorithm (IKEv2 only).
- `enc-algorithm` (ubit (aes-256, aes-192, aes-128, 3des, des)): Encryption algorithm.
- `dh-group` (ubit (x25519, ecp256, ecp384, ecp521, modp6144, modp4096, modp3072, modp2048, modp1536, modp1024, modp768)): Diffie-Hellman group.
- `lifetime` (time): Phase 1 lifetime (IKEv1 only).
- `lifebytes` (num): Phase 1 lifetime in bytes (IKEv1 only). It is used only as an administrative value which is added to the proposal. Used in cases where the remote peer requires a specific lifebytes value to establish phase 1.
- `proposal-check` (enum: obey | strict | claim | exact): Phase 2 lifetime check logic:
  - `claim` - take the shortest of proposed and configured lifetimes and notify the initiator about it.
  - `exact` - require lifetimes to be the same.
  - `obey` - accept whatever is sent by an initiator.
  - `strict` - if the proposed lifetime is longer than the default then reject the proposal otherwise accept a proposed lifetime.
- `nat-traversal` (bool): Use Linux NAT-T mechanism to solve IPsec incompatibility with NAT routers between IPsec peers. This can only be used with the ESP protocol (AH is not supported by design, as it signs the complete packet, including the IP header, which is changed by NAT, rendering the AH signature invalid). The method encapsulates IPsec ESP traffic into UDP streams in order to overcome some minor issues that make ESP incompatible with NAT.
- `ppk` (enum: no | psk | qkd | psk-ike-initial): Post-quantum preshared key (IKEv2 only).
- `dpd-interval` (alt { special: enum (disable-dpd) , num: time [ .. 3600] }): Dead peer detection interval.
- `dpd-maximum-failures` (num): Maximum DPD failures before peer is considered dead (IKEv1 only).
