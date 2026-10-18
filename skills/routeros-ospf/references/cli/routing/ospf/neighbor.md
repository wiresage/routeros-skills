# /routing/ospf/neighbor

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/neighbor

Type: Directory

List of currently active OSPF neighbors.

**Flags**

- `V`: virtual
- `D`: dynamic

**Read-only arguments**

- `instance` (enum)
- `area` (enum)
- `interface` (iface_enum): Name of the interface this neighbor was discovered.
- `address` (address (flags=46i)): An IP address of the OSPF neighbor router.
- `priority` (num)
- `router-id` (ipAddr): Neighbor router's **RouterID**
- `dr` (ipAddr): An IP address of the Designated Router.
- `bdr` (ipAddr): An IP address of the Backup Designated Router.
- `state` (string): - `Down` - No Hello packets have been received from a neighbor.
  - `Attempt` - Applies only to NBMA clouds. The state indicates that no recent information was received from a neighbor.
  - `Init` - Hello packet received from the neighbor, but bidirectional communication is not established (Its own RouterID is not listed in the Hello packet).
  - `2-way` - This state indicates that bi-directional communication is established. DR and BDR elections occur during this state. Routers build adjacencies based on whether the router is DR or BDR, and the link is point-to-point or a virtual link.
  - `ExStart` - Routers try to establish the initial sequence number that is used for the packet information exchange. The router with a higher ID becomes the master and starts the exchange.
  - `Exchange` - Routers exchange database description (DD) packets.
  - `Loading` - In this state, actual link state information is exchanged. Link State Request packets are sent to neighbors to request any new LSAs that were found during the Exchange state.
  - `Full` - Adjacency is complete, and neighbor routers are fully adjacent. LSA information is synchronized between adjacent routers. Routers achieve the full state with their DR and BDR only. An exception is P2P links.
- `state-changes` (num)
- `ls-retransmits` (num)
- `ls-requests` (num)
- `db-summaries` (num)
- `adjacency` (time): Elapsed time since adjacency was formed.
- `timeout` (time)
