# /mpls/ldp

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `lsr-id` (ipAddr; unset): Unique label switching router's ID.
- `path-vector-limit` (num; unset): Max path vector limit used for loop detection. Works in combination with the `loop-detect` property.
- `hop-limit` (num; unset): Max hop limit used for loop detection. Works in combination with the `loop-detect` property.
- `loop-detect` (bool; unset): Defines whether to run LSP loop detection. Will not work correctly if not enabled on all LSRs. Should be used only on non-TTL networks such as ATMs.
- `use-explicit-null` (bool; unset): Whether to distribute explicit-null label bindings.
- `distribute-for-default` (bool; unset): Defines whether to map label for the default route.
- `transport-addresses` (multi { array-id, transport-address: address (flags=46) }; unset): Specifies LDP session connection origin addresses and also advertises these addresses as transport addresses to LDP neighbors.
- `vrf` (enum; unset): Name of the VRF table this instance will operate on.
- `afi` (ubit (ip, ipv6); unset): Determines supported address families by the instance.
- `preferred-afi` (enum: ip | ipv6; unset): Determines which address family connection is preferred. Value is also set in dual-stack element (if used).
