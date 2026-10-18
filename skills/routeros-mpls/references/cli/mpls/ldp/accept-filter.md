# /mpls/ldp/accept-filter

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp/accept-filter

Conditions: !smips; Type: Directory

List of label bindings that should be accepted from LDP neighbors.

**Flags**

- `X`: disabled

**Arguments**

- `vrf` (enum (any) { any:0xffffffff }; unset)
- `prefix` (address (flags=46/); unset): Prefix to match.
- `neighbor` (address (flags=46/); unset): Neighbor to which this filter applies.
- `accept` (bool; unset): Whether to accept label bindings from the neighbors for the specified prefix. If parameter is unset then matching prefix is not accepted.
