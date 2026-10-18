# /routing/pimsm/uib-g

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/uib-g

Conditions: !smips; Type: Directory

The upstream information base menus show the any-source multicast (\*,G) and source-specific multicast (S,G) groups and their statuses. These menus contain only read-only entries.

**Flags**

- `R` (rp-local): The router itself is the Rendezvous Point (RP) for this group.

**Read-only arguments**

- `instance` (enum): Name of the PIM instance the multicast group is created on.
- `group` (address (flags=46i)): The multicast group address.
- `rp` (address (flags=46i)): The address of the Rendezvous Point for this group.
- `rpf` (address (flags=46i)): The Reverse Path Forwarding (RPF) indicates the router address and outgoing interface that a Join message for that group is directed to.
