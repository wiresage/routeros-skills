# /routing/rip/neighbor

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/rip/neighbor

Type: Directory

This submenu is used to define neighboring routers to exchange routing information with. Normally there is no need to add the neighbors, if multicasting is working properly within the network. If there are problems with exchanging routing information, neighbor routers can be added to the list. It will force the router to exchange the routing information with the neighbor using regular unicast packets.

**Flags**

- `D`: dynamic

**Read-only arguments**

- `instance` (enum)
- `address` (address (flags=46i))
- `routes` (num)
- `packets-total` (num)
- `packets-bad` (num)
- `entries-bad` (num)
- `last-update` (time): Time from last update.
