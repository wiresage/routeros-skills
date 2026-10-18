# /ip/proxy/inserts

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/inserts

Type: Settings Directory

Counters of the objects the proxy writes to its cache. For an overview of caching, see [Web Proxy](../../../guides/network-management/proxy/web-proxy.md).

**Read-only arguments**

- `successes` (num): Objects stored in the cache.
- `denied` (num): Responses not stored because a [`/ip/proxy/cache`](cache.md) rule with `action=deny` matched the request.
- `too-large` (num)
- `no-memory` (num)
- `errors` (num)
