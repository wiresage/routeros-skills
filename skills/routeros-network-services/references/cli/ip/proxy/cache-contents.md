# /ip/proxy/cache-contents

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/cache-contents

Type: Directory

Objects in the cache of the web proxy. Remove an entry to make the proxy fetch the object from the server on the next request. To empty the whole cache, use [`clear-cache`](../proxy.md). For an overview of caching, see [Web Proxy](../../../guides/network-management/proxy/web-proxy.md).

**Read-only arguments**

- `uri` (string): URL of the object.
- `file-size` (num): Size of the object, in KiB.
- `last-modified` (date): Date the proxy stored the object. It is not the `Last-Modified` header of the response.
- `last-modified-time` (date): Time the proxy stored the object.
- `last-accessed` (date)
- `last-accessed-time` (date)
