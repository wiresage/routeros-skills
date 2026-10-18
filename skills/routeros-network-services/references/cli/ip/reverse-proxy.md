# /ip/reverse-proxy

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/reverse-proxy

Conditions: !smips; Type: Directory

Each rule forwards the HTTPS requests for one host name to an HTTP server. The reverse proxy accepts HTTPS connections on the port of the `reverse-proxy` service in [`/ip/service`](https://manual.mikrotik.com/docs/cli-reference/ip/service), selects the rule whose `sni` matches the server name the client sends, terminates TLS with the certificate of that rule and forwards the requests as HTTP to `ip-address` and `port`. The service port is open only while at least one enabled rule exists. For an overview and examples, see [Reverse Proxy](../../guides/network-management/proxy/reverse-proxy.md).

**Flags**

- `X` (disabled): The rule is disabled. New rules are created enabled.
- `D` (dynamic): The rule was created by RouterOS for a container app with `use-https=yes` and a web interface (see [`/app`](https://manual.mikrotik.com/docs/cli-reference/app)). Its `sni` is the host name of the app URL, and its certificate is the one set in `/app/settings`.

**Arguments**

- `sni` (string; mandatory): Host name the rule serves. It is compared with the server name (SNI) the client sends in the TLS handshake and must match it exactly; a wildcard such as `*.example.com` matches nothing. The router closes a connection whose server name matches no rule, and the `rproxy` log shows `no matching rule for <name>`.
- `ip-address` (alt { ipv6: ip6Addr , ip: ipAddr }; mandatory): IPv4 or IPv6 address of the server the requests are forwarded to. The router connects from its own address and forwards each request as HTTP/1.1. It keeps the `Host` header and adds `X-Forwarded-For` and `X-Real-Ip` with the address of the client, `X-Forwarded-Proto: https`, `X-Forwarded-Host` and `Forwarded`.
- `port` (num; mandatory): TCP port of the server. The router always connects with plain HTTP, also when the port is 443, so the server must accept HTTP on this port.
- `certificate` (enum: none): Certificate the router presents to clients of this rule, for example one issued for the `sni` host name. With `none`, the certificate of the `reverse-proxy` service in [`/ip/service`](https://manual.mikrotik.com/docs/cli-reference/ip/service) is used. When that is also `none`, the TLS handshake fails, and the `rproxy` log shows `certificate missing for rule <sni>`. Default: none.
- `vrf` (enum)
