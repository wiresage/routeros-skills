# /ip/ipsec/active-peers

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/active-peers

Type: Directory

This menu provides various statistics about remote peers that currently have established a phase 1 connection.

**Flags**

- `R` (responder): Whether the peer is a responder.
- `N` (natt-peer): Whether NAT traversal is used for the peer.
- `P` (ppk): Whether post-quantum preshared key is used.

**Read-only arguments**

- `id` (string): Peer identifier.
- `local-address` (alt { ipv6: ip6Addr , ip: ipAddr }): Local IP address.
- `port` (num): Remote port.
- `remote-address` (alt { ipv6: ip6Addr , ip: ipAddr }): Remote IP address.
- `state` (enum: spawning | starting | message-1-received | message-1-sent | message-2-received | message-2-sent | message-3-received | message-3-sent | message-4-received | established | expired | no-phase1 | eap | crypto | qkd): Current IKE phase 1 state.
- `side` (enum: initiator | responder): Whether the peer acts as a responder.
- `dynamic-address` (alt { ip: ipAddr }): Dynamically assigned address.
- `uptime` (time): Connection uptime.
- `last-seen` (time): Time since the last received packet.
- `ph2-total` (num): Total number of phase 2 exchanges.
- `spii` (string): Initiator SPI value.
- `spir` (string): Responder SPI value.
- `rx-packets` (num): Number of received packets.
- `rx-bytes` (num): Number of received bytes.
- `tx-packets` (num): Number of transmitted packets.
- `tx-bytes` (num): Number of transmitted bytes.

## Commands

### /ip/ipsec/active-peers/kill-connections

Type: Command

Manually disconnects all remote peers.
