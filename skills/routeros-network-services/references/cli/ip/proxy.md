# /ip/proxy

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy

Type: Settings Directory

Settings of the web proxy. The proxy forwards the requests of its clients, HTTP, HTTPS (`CONNECT`) and FTP, and of connections redirected to it with destination NAT, and it caches HTTP responses. Changing any setting in this menu clears the cache. For an overview and examples, see [Web Proxy](../../guides/network-management/proxy/web-proxy.md).

**Arguments**

- `enabled` (bool): Whether the web proxy runs. Default: no.
- `src-address` (object { address: alt { address: ipAddr , address6: ip6Addr } }): Source address of the connections the proxy opens to servers. It must be an address of the router; otherwise, and when it is not set, the router uses the source address chosen by routing. Default: `::` (not set).
- `port` (multi { port: num [1 .. 65535] }): TCP port the proxy listens on, or several ports as a comma-separated list, for example `8080,3128`. The proxy listens on all IPv4 and IPv6 addresses of the router, so protect the port with firewall rules. To tell the ports apart in rules, use `local-port` in the access, cache and direct lists. Default: 8080.
- `anonymous` (bool): Whether the proxy tells the server about the client.
  - `no` (default) - Add `Via: 1.1 <router address> (Mikrotik HttpProxy)`, `X-Forwarded-For: <client address>` and `X-Proxy-ID` to the requests sent to servers. When a request arrives with `Via` and `X-Forwarded-For` already set, for example from another proxy, the proxy adds its entries to them.
  - `yes` - Send none of these headers.
- `parent-proxy` (alt { host: ipAddr , host6: ip6Addr }): IPv4 or IPv6 address of another proxy that receives the requests, HTTPS (`CONNECT`) requests included, except those that [`/ip/proxy/direct`](proxy/direct.md) sends directly to the server. The parent proxy is used only when `parent-proxy-port` is not 0. When the parent proxy cannot be reached, the client gets an error page; the router does not fall back to a direct connection. Default: `::` (none).
- `parent-proxy-port` (num): TCP port of the parent proxy. With 0, no parent proxy is used, even when `parent-proxy` is set. Default: 0.
- `cache-administrator` (string): Name or email address shown on the error pages of the proxy as a `mailto:` link, the `$(admin)` variable of the error page template (see [`reset-html`](proxy.md)). Default: webmaster.
- `max-cache-size` (alt { special: enum (none | unlimited) { none:0, unlimited:0xffffffff } , value: num }): Largest total size of the cache, in KiB.
  - `unlimited` (default) - No limit. A RAM cache can then use most of the router's free memory, so set a limit on a router that runs other services.
  - `none` - Do not cache.
  - A number - Limit in KiB.
- `max-cache-object-size` (num): Largest response the proxy stores in the cache, in KiB. Larger responses reach the client without being stored. Default: 2048KiB.
- `cache-on-disk` (bool): Where the proxy keeps the cache.
  - `no` (default) - In RAM.
  - `yes` - On the storage of the router, in the store named by `cache-path`, which `/file` shows with the type `web-proxy store`.
- `max-client-connections` (num): Largest number of client connections the proxy serves at the same time. Further requests wait until a connection is free. Default: 600.
- `max-server-connections` (num): Default: 600.
- `max-fresh-time` (time): Default: 3d.
- `serialize-connections` (bool): Default: no.
- `always-from-cache` (bool): Default: no.
- `cache-hit-dscp` (num): DSCP value, 0 to 63, the router sets on the packets of responses it serves from the cache. Use it to recognise cache hits in queues and firewall rules. Default: 4.
- `cache-path` (string): Name of the cache directory. With `cache-on-disk=yes`, the router creates it on its storage as a `web-proxy store`. A path, for example `usb1/web-proxy` on a disk, needs an existing directory; otherwise the router refuses it with `bad cache path`. It cannot be empty. Default: web-proxy.

## Commands

### /ip/proxy/clear-cache

Type: Command

Deletes all objects from the cache of the web proxy. Changing any setting in [`/ip/proxy`](proxy.md) also clears the cache. For an overview of caching, see [Web Proxy](../../guides/network-management/proxy/web-proxy.md).

### /ip/proxy/monitor

Type: Command

Shows the state and the counters of the web proxy. Add `once` for a single reading, for example `/ip/proxy/monitor once`. For an overview, see [Web Proxy](../../guides/network-management/proxy/web-proxy.md).

**Read-only arguments**

- `status` (enum: stopped | running | invalid-address | building-cache | passthrough): State of the proxy, for example:
  - `running` - The proxy is enabled and serves requests.
  - `stopped` - The proxy is disabled.
- `uptime` (time): Time since the proxy started.
- `client-connections` (num): Open connections from clients.
- `server-connections` (num): Open connections to servers.
- `requests` (num): Number of requests the proxy received.
- `hits` (num): Number of requests answered from the cache.
- `cache-used` (num): Size of the objects in the cache, in KiB.
- `total-ram-used` (num)
- `received-from-servers` (num): Data received from servers, in KiB.
- `sent-to-clients` (num): Data sent to clients, in KiB.
- `hits-sent-to-clients` (num): Data sent to clients from the cache, in KiB.

### /ip/proxy/reset-html

Type: Command

Writes the default template of the proxy's error page to the file `webproxy/error.html` on the router and replaces a changed copy. The proxy builds its error pages, for example the page for a request denied by [`/ip/proxy/access`](proxy/access.md), from this file, so you can edit it; the proxy uses the changed file at once. Without the file, the proxy uses the same page built in. The template uses the variables `$(status)`, `$(url)`, `$(error)`, `$(admin)` (the `cache-administrator` setting) and `$(signature)`, and the block `$(if error)` ... `$(endif)`. For an overview, see [Web Proxy](../../guides/network-management/proxy/web-proxy.md).
