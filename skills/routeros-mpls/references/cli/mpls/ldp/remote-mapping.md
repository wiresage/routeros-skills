# /mpls/ldp/remote-mapping

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp/remote-mapping

Conditions: !smips; Type: Directory

The Sub-menu shows label bindings for routes received from other routers. Static mapping can be configured if there is no intention to use LDP dynamically. This table is used to build the Forwarding Table

**Flags**

- `X`: disabled
- `I` (inactive): Whether binding is active and can be selected as a candidate for forwarding.
- `D` (dynamic): Whether entry was dynamically added.
- `V`: vpls

**Arguments**

- `vrf` (enum; unset): Name of the VRF table this mapping belongs to.
- `dst-address` (address (flags=46/); mandatory): Destination prefix the label is assigned to.
- `label` (alt { label-enum: enum (expl-null | alert | expl-null6 | impl-null) , label-num: num [16 .. 1048576] }; mandatory): Label number assigned to destination.
- `nexthop` (address (flags=46i); mandatory)

**Read-only arguments**

- `peer` (object { peer-id: composite { id: ipAddr , namespace: num } })
- `path` (string)
- `pw-fec` (string)
