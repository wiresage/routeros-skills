# /ip/proxy/direct

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/direct

Type: Directory

Rules that decide which requests go directly to the server when a parent proxy is set with `parent-proxy` and `parent-proxy-port` in [`/ip/proxy`](../proxy.md). The proxy checks the rules from top to bottom, and the first matching rule decides. A request that matches no rule goes through the parent proxy. Without a parent proxy, every request goes directly to the server and the list has no effect. The matchers work as in [`/ip/proxy/access`](access.md). Prefix a matcher value with `!` to negate it, for example `src-address=!192.168.88.0/24`. For an example, see [Web Proxy](../../../guides/network-management/proxy/web-proxy.md).

**Flags**

- `X` (disabled): disabled. The rule is not used. New rules are created enabled.

**Arguments**

- `src-address` (super { ! , range: alt { ip4: ipRange , ip6: ip6Prefix } }): Address of the client: an IPv4 address, range or prefix, or an IPv6 prefix.
- `dst-address` (super { ! , range: alt { ip4: ipRange , ip6: ip6Prefix } }): Address of the server the proxy connects to, which is the resolved address of the host name in the request. Same format as `src-address`.
- `dst-port` (super { ! , ports: multi { ports: range [ .. 65535] } }): Port of the server, for HTTPS requests the port of the `CONNECT` tunnel. A port, a range or a comma-separated list, for example `dst-port=!443`.
- `local-port` (super { ! , port: num [0 .. 65535] }): Port of the proxy the request arrived on. Use it when `port` in [`/ip/proxy`](../proxy.md) lists several ports.
- `dst-host` (super { ! , host: string }): Host name of the request, for HTTPS requests the host of the `CONNECT` tunnel. The value must match the whole name and is not case-sensitive, so `example.com` does not match `www.example.com`.
  - Wildcards: `*` matches any characters and `?` one character, for example `*.example.com`.
  - A value that starts with `:` is a regular expression, which can match any part of the name: `:mail` matches `mail.example.com`. Anchor it with `^` and `$`, for example `:^www`.
- `path` (super { ! , path: string }): Path of the requested URL, including the query string, for example `/music/a.mp3?x=1`. Wildcards and regular expressions work as in `dst-host`.
  - Wildcards must match the whole path including the query string, so `*.mp3` matches `/music/a.mp3` but not `/music/a.mp3?x=1`.
  - The path always starts with `/`, so the router refuses a value such as `music/*`, which could never match.
  - HTTPS requests have no path, so a rule with `path` never matches them.
- `method` (super { ! , method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE) }): HTTP method of the request: `GET`, `HEAD`, `POST`, `PUT`, `CONNECT`, `OPTIONS`, `DELETE` or `TRACE`. Clients of the proxy request HTTPS pages with `CONNECT`. The methods are defined in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110#name-methods).
- `action` (enum: allow | deny): How the proxy sends a matching request.
  - `allow` (default) - Connect directly to the server.
  - `deny` - Send the request through the parent proxy.

**Read-only arguments**

- `hits` (num): Number of requests the rule matched. Reset it with [`reset-counters`](direct.md) or [`reset-counters-all`](direct.md).

## Commands

### /ip/proxy/direct/reset-counters

Type: Command

Resets the `hits` counter of the given rules in [`/ip/proxy/direct`](direct.md), for example `/ip/proxy/direct/reset-counters [find comment=test]`. For an overview, see [Web Proxy](../../../guides/network-management/proxy/web-proxy.md).

### /ip/proxy/direct/reset-counters-all

Type: Command

Resets the `hits` counter of all rules in [`/ip/proxy/direct`](direct.md). For an overview, see [Web Proxy](../../../guides/network-management/proxy/web-proxy.md).
