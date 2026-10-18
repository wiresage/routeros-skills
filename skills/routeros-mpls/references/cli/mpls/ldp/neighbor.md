# /mpls/ldp/neighbor

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp/neighbor

Conditions: !smips; Type: Directory

List of discovered and statically configured LDP neighbors.

**Flags**

- `X`: disabled
- `D`: dynamic
- `I`: inactive
- `O` (operational): Indicates whether the peer is operational.
- `C` (active-connect): Indicates that active role has been selected and the router is trying to establish the session.
- `W` (passive-wait): Indicates whether the peer is in a passive role and currently is waiting for the session to be initialized.
- `T` (throttled): Indicates whether session is in throttled state. Session is throttled after initialization failure, max throttle time 120s.
- `t` (sending-targeted-hello): Whether targeted hellos are being sent to the neighbor.
- `v` (vpls): Whether neighbor is used by LDP signaled VPLS tunnel.
- `p` (passive): Indicates whether the peer is in a passive role.
- `d` (on-demand): Downstream On Demand label distribution.

**Arguments**

- `transport` (address (flags=46vi); mandatory): Remote transport address.
- `send-targeted` (bool; unset): Specifies whether to try to send targeted hellos, used for targeted (not directly connected) LDP sessions.

**Read-only arguments**

- `peer` (object { peer-id: composite { id: ipAddr , namespace: num } }): LSR-ID and label space of the neighbor.
- `local-transport` (address (flags=46)): Selected local transport address.
- `addresses` (multi { array-id, address: address (flags=46) }): List of discovered addresses on the neighbor.
- `path-vector-limit` (num)
- `on-demand` (bool): Downstream On Demand label distribution.
- `used-afi` (ubit (ip, ipv6)): Used transport AFI.
