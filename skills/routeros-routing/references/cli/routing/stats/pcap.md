# /routing/stats/pcap

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/stats/pcap

Conditions: !smips; Type: Directory

**Read-only arguments**

- `file` (string)
- `timestamp` (time)
- `src` (address (flags=46))
- `dst` (address (flags=46))
- `protocol` (string)
- `data` (string)
- `bgp.type` (num)
- `bgp.notification.code` (num)
- `bgp.notification.subcode` (num)
- `bgp.route-refresh.afi` (num)
- `bgp.route-refresh.safi` (num)
- `bgp.route-refresh.subtype` (num)
- `bgp.update.local-pref` (num)
- `bgp.update.med` (num)
- `bgp.update.nexthop` (multi { prefix: address (flags=46) })
- `bgp.update.nlri` (multi { prefix: address (flags=46i/SR) })
- `bgp.update.withdrawn` (multi { prefix: address (flags=46i/SR) })
- `bgp.update.origin` (num)
- `bgp.update.as-path` (multi { value: string })
- `bgp.update.as4-path` (multi { value: string })
- `bgp.update.communities` (multi { value: string })
- `bgp.update.ext-communities` (multi { value: string })
- `bgp.update.large-communities` (multi { value: string })
- `bgp.update.atomic-aggregate` (bool)
- `bgp.update.aggregator` (string)
- `bgp.update.as4-aggregator` (string)
- `bgp.update.originator-id` (ipAddr)
- `bgp.update.cluster-list` (multi { value: ipAddr })
