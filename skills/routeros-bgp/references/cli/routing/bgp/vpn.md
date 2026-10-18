# /routing/bgp/vpn

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/vpn

Conditions: !smips; Type: Directory

L3VPN VPNv4/VPNv6 instance configuration

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `name` (string; unset)
- `instance` (enum; mandatory): Name of the instance this VPN is assigned to.
- `route-distinguisher` (string; mandatory): Specifies the value that gets attached to route so that receiving routers can distinguish advertisements that may otherwise look the same. Used to distinguish between tenants using overlapping IP ranges. Also can be used to simplify convergence and redundancy within Virtual Network. RDs from MLAG pairs should be unique, too.
- `vrf` (enum; mandatory): Name of the VRF table that this VPN instance will use.
- `label-allocation-policy` (enum: per-vrf | per-prefix; mandatory)
- `import.route-targets` (object { route-target: address (flags=R) }; unset): List of route targets that will be used to import VPNv4 routes. The accepted RT format is similar to the one for Route Distinguishers.
- `export.route-targets` (object { route-target: address (flags=R) }; unset): List of route targets added when exporting VPNv4 routes. The accepted RT format is similar to the one for Route Distinguishers.
- `import.filter-chain` (enum; unset)
- `export.filter-select` (enum; unset): The name of the `routing/filter/select-chain` that is used to select prefixes to be exported.
- `export.filter-chain` (enum; unset): The name of the `routing/filter/chain` that is used to filter prefixes before exporting.
- `export.redistribute` (ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac); unset): Enable redistribution of specified route types from a VRF to VPNv4.
