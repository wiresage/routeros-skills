# /mpls/ldp/local-mapping

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp/local-mapping

Conditions: !smips; Type: Directory

This sub-menu shows labels bound to the routes locally in the router. In this menu, static mappings can also be configured if there is no intention to use LDP dynamically.

**Flags**

- `X`: disabled
- `I` (inactive): Whether binding is active and can be selected as a candidate for forwarding.
- `D` (dynamic): Whether the entry was dynamically added.
- `E`: egress
- `G` (gateway): Whether the destination is reachable through the gateway.
- `L` (local): Whether the destination is locally reachable on the router.
- `V`: vpls

**Arguments**

- `vrf` (enum; unset): Name of the VRF table this mapping belongs to.
- `dst-address` (address (flags=46/); mandatory; unset): Destination prefix the label is assigned to.
- `label` (alt { label-enum: enum (expl-null | alert | expl-null6 | impl-null) , label-num: num [16 .. 1048576] }; mandatory): Label number assigned to destination.

**Read-only arguments**

- `adv-path` (string)
- `peers` (object { peer-id: composite { id: ipAddr , namespace: num } }): IP address and label space of the peer to which this entry was advertised.
- `pw-fec` (string)
