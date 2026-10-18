# /ip/ipsec/peer

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/peer

Type: Directory

Peer configuration settings are used to establish connections between IKE daemons. This connection is then used to negotiate keys and algorithms for SAs. Exchange mode is the only unique identifier between the peers, meaning that multiple peer configurations can exist with the same remote-address as long as a different exchange-mode is used.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `D` (dynamic): Whether the item was created dynamically.
- `R` (responder): Whether this peer will act as a responder only (listen to incoming requests) and not initiate a connection.

**Arguments**

- `name` (string): Peer name.
- `address` (alt { prefix6: ip6Prefix , prefix4: ipPrefix , dns: string }): Remote address of the peer. If the remote peer's address matches this prefix, then the peer configuration is used in authentication and establishment of Phase 1. If several peer's addresses match several configuration entries, the most specific one (i.e. the one with the largest netmask) will be used.
- `local-address` (alt { ipv6: ip6Addr , ip: ipAddr }): Local address to use for the connection.
- `passive` (bool): Passive peer does not initiate the connection. The enabled passive mode also indicates that the peer is an xauth responder, and disabled passive mode - xauth initiator.
- `port` (num): Communication port used (when the router is an initiator) to connect to the remote peer when the remote peer uses a non-default port.
- `profile` (enum): IPsec profile to use.
- `exchange-mode` (enum: main | aggressive | ike2): ISAKMP phase 1 exchange modes according to [RFC 2408](https://datatracker.ietf.org/doc/html/rfc2408#section-4.1). The `main` mode relaxes [rfc2409 section 5.4](https://datatracker.ietf.org/doc/html/rfc2409#section-5.4), to allow pre-shared-key authentication in the `main` mode. `ike2` mode enables Ikev2 [RFC 7296](https://datatracker.ietf.org/doc/html/rfc7296).

  Parameters that are ignored by IKEv2: `proposal-check`, `compatibility-options`, `lifebytes`, `dpd-maximum-failures`, `nat-traversal`.
- `send-initial-contact` (bool): Specifies whether to send an "initial contact" IKE packet or wait for the remote side, this packet should trigger the removal of old peer SAs for the current source address. Usually, in road warrior setups clients are initiators and this parameter should be set to no. Initial contact is not sent if modecfg or xauth is enabled for ikev1.
- `ppk-secret` (string): Static PPK secret with "static-ppk-secret" ID used when no one-time key/psk exist for this peer, ensure the key has 256 bits of entropy.

**Read-only arguments**

- `current-address` (alt { ipv6: ip6Addr , ip: ipAddr }): Current remote address of the peer.
