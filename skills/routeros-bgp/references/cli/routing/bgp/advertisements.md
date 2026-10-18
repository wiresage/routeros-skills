# /routing/bgp/advertisements

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/advertisements

Conditions: !smips; Type: Directory

**Read-only arguments**

- `peer` (enum)
- `dst` (address (flags=46/R))
- `afi` (enum: ip | ipv6 | l2vpn | l2vpn-cisco | vpnv4 | vpnv6)
- `local-pref` (num)
- `med` (num)
- `nexthop` (multi { prefix: address (flags=46) })
- `nlri` (multi { prefix: address (flags=46i/SR) })
- `withdrawn` (multi { prefix: address (flags=46i/SR) })
- `origin` (num)
- `as-path` (multi { value: string })
- `as4-path` (multi { value: string })
- `communities` (multi { value: string })
- `ext-communities` (multi { value: string })
- `large-communities` (multi { value: string })
- `atomic-aggregate` (bool)
- `aggregator` (string)
- `as4-aggregator` (string)
- `originator-id` (ipAddr)
- `cluster-list` (multi { value: ipAddr })
- `igp-metric` (num)
- `otc` (num)
