# /ip/proxy/lookups

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/lookups

Type: Settings Directory

Counters of the requests the proxy looks up in its cache. For an overview of caching, see [Web Proxy](../../../guides/network-management/proxy/web-proxy.md).

**Read-only arguments**

- `successes` (num): Requests answered from the cache.
- `not-found` (num): Requests for objects that are not in the cache.
- `non-cacheable` (num): Requests the proxy does not look up in the cache because of their method, for example `POST` and `HEAD`.
- `denied` (num): Requests matched by a [`/ip/proxy/cache`](cache.md) rule with `action=deny`.
- `expired` (num): Requests for an object found in the cache that the proxy fetched from the server again.
- `no-expiration-info` (num)
