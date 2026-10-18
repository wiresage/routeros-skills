# /routing/bgp/instance

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/instance

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `name` (string)
- `routing-table` (enum; unset): Name of the routing table, to install routes in.
- `vrf` (enum; unset): Name of the VRF BGP connections operate on. By default always uses the "main" routing table.
- `router-id` (alt { ip: ipAddr , name: enum }; unset): BGP Router ID to be used. Use the ID from the `/routing/router-id` configuration by specifying the reference name, or set the ID directly by specifying IP.Equal router-ids are also used to group peers into one instance.
- `as` (super { as: as , [sub-as] [ /as] }; unset): 32-bit BGP autonomous system number. Enter the value in AS-Plain or AS-Dot formats. Configure BGP confederation using the following format: _`confederation_as/as`_. For example, if your AS is 34 and your confederation AS is 43, set `as=43/34`.
- `cluster-id` (ipAddr; unset): For route reflector instances, specify the cluster ID of the route reflector cluster. This attribute identifies routing updates from other route reflectors in the cluster to avoid routing information loops. Typically, only one route reflector exists per cluster; in this case, do not configure 'cluster-id' and BGP router ID is used instead.
- `ignore-as-path-len` (bool; unset): Ignore the **AS_PATH** attribute in the BGP route selection algorithm. Applies to input.
- `multipath` (num; unset): Install the specified number of ECMP routes received by add-path or selected by [best path selection](../../../guides/user-guides/routing-and-networking-protocols/unicast/bgp/understanding-bgp.md#best-path-selection).
- `always-compare-med` (bool; unset)
