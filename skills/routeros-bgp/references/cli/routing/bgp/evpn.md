# /routing/bgp/evpn

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/evpn

Conditions: !smips; Type: Directory

See EVPN documentation.

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; unset)
- `instance` (enum; mandatory): BGP instance this EVPN is assigned to.
- `vrf` (enum; unset): Name of the VRF table that this EVPN instance will use.
- `rd` (address (flags=R); unset): Specifies the value that gets attached to route so that receiving routers can distinguish advertisements that may otherwise look the same. Used to distinguish between tenants using overlapping IP ranges. Also can be used to simplify convergence and redundancy within Virtual Network. RDs from MLAG pairs should be unique, too.
- `vni` (object { range: range }; unset): Range of Virtual Network Identifiers.
- `import.route-targets` (object { route-target: address (flags=R) }; unset): List of route targets that will be used to import EVPN routes.
- `export.route-targets` (object { route-target: address (flags=R) }; unset): List of route targets that will be added to EVPN routes when exporting.
