# /mpls/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/settings

Conditions: !smips; Type: Settings Directory

**Arguments**

- `dynamic-label-range` (range): Range of Label numbers used for dynamic allocation. The first 16 labels are reserved for special purposes (as defined in RFC). If you intend to configure labels statically then adjust the dynamic default range not to include numbers that will be used in a static configuration.
- `propagate-ttl` (enum: yes | no): Whether to copy TTL values from IP header to MPLS header. If this option is set to **no** then hops inside the MPLS cloud will be invisible to traceroutes.
- `allow-fast-path` (enum: yes | no): Enable/disable MPLS fast-path support.

**Read-only arguments**

- `mpls-fast-path-packets` (num)
- `mpls-fast-path-bytes` (num)
