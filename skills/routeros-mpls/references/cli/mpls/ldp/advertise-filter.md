# /mpls/ldp/advertise-filter

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp/advertise-filter

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `vrf` (enum (any) { any:0xffffffff }; unset)
- `prefix` (address (flags=46/); unset): Prefix to match.
- `neighbor` (address (flags=46/); unset): Neighbor to which this filter applies.
- `advertise` (bool; unset): Whether to advertise label bindings to the neighbors for the specified prefix. If parameter is unset then matching prefix is not advertised.
