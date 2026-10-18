# /routing/pimsm/interface

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/interface

Conditions: !smips; Type: Directory

The interface menu shows all interfaces that are currently participating in PIM and their statuses. This menu contains dynamic and read-only entries that get created by defined interface templates.

**Flags**

- `D`: dynamic
- `P` (pim-enabled): The interface has PIM enabled on it.
- `G` (gmp-enabled): The interface is configured for GMP (IGMP/MLD) operation.
- `R` (designated-router): The router is the designated router (DR) on this interface's network.
- `J` (join-tracking): Join tracking is enabled on this interface.

**Read-only arguments**

- `instance` (enum): The PIM instance this interface belongs to.
- `interface` (iface_enum): The name of the interface.
- `address` (address (flags=46)): The IP address used by PIM on this interface.
- `pim.priority` (num): The DR priority of this router on the interface's network. The router with the highest DR priority is elected as the designated router.
- `pim.propagation-delay` (time): The propagation delay used by the DR on this interface's network, advertised in PIM hello messages.
- `pim.override-interval` (time): The override interval used by the DR on this interface's network, advertised in PIM hello messages.
- `gmp.robustness` (num): The configured robustness value of the IGMP/MLD querier on this interface.
- `gmp.query-interval` (time): The configured interval between IGMP/MLD General Queries sent on this interface.
- `gmp.query-response-interval` (time): The configured maximum response time advertised in IGMP/MLD General Queries on this interface.
- `gmp.last-member-query-interval` (time): The configured response time advertised in IGMP/MLD group-specific queries on this interface.
- `gmp.querier` (bool): Whether this router is currently the elected IGMP/MLD querier on this interface.
- `gmp.state.robustness` (num): The effective robustness value in use on this interface. When the router is not the elected querier, it adopts the robustness value announced by the elected querier in its queries.
- `gmp.state.query-interval` (time): The effective query interval in use on this interface. When the router is not the elected querier, it adopts the query interval announced by the elected querier in its queries.
