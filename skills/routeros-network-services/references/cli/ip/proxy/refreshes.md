# /ip/proxy/refreshes

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/refreshes

Type: Settings Directory

Counters of the cached objects the proxy revalidated with the server before it answered the client. To revalidate an object, the proxy sends a conditional request with `If-Modified-Since` or `If-None-Match`. Each counter counts one reason. For an overview of caching, see [Web Proxy](../../../guides/network-management/proxy/web-proxy.md).

**Read-only arguments**

- `url-requests` (num): Objects whose URL has a query string. The proxy revalidates them on every request.
- `request-max-age` (num)
- `expired` (num)
- `response-max-age` (num)
- `config-max-fresh` (num)
- `heuristic` (num)
- `other` (num): Other reasons, for example an object that has an `ETag` header but no `Last-Modified` header.
