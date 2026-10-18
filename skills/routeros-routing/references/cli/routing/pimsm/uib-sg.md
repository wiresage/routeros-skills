# /routing/pimsm/uib-sg

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/uib-sg

Conditions: !smips; Type: Directory

**Flags**

- `K`: keepalive
- `S` (spt-bit): The Shortest Path Tree (SPT) bit indicates whether forwarding is taking place on the (S,G) Shortest Path Tree or on the (\*,G) tree. A router can have an (S,G) state and still be forwarding on a (\*,G) state during the interval when the source-specific tree is being constructed. When the SPT bit is false, only the (\*,G) forwarding state is used to forward packets from S to G. When the SPT bit is true, both (\*,G) and (S,G) forwarding states are used.

**Read-only arguments**

- `instance` (enum): Name of the PIM instance the multicast group is created on.
- `group` (address (flags=46i)): The multicast group address.
- `source` (address (flags=46i)): The source IP address of the multicast group.
- `rpf` (address (flags=46i)): The Reverse Path Forwarding (RPF) indicates the router address and outgoing interface that a Join message for that group is directed to.
- `register` (enum: join | join-pending | prune)
