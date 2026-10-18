# /ip/service

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/service

Type: Directory

The management and service listeners of the router: WinBox, SSH, Telnet, FTP, the web server (`www` for HTTP, `www-ssl` for HTTPS), the API (`api`, `api-ssl`) and the reverse proxy. Each entry sets the port, the addresses and VRF a service accepts clients from, and the certificate of the TLS services. You cannot add services, only change and disable the existing ones. The list also shows dynamic entries: ports other features and containers listen on, and established connections to the services. For the web server parts (WebFig, REST API, graphs), see [`/ip/service/webserver`](service/webserver.md). For an overview and the list of ports RouterOS uses, see [Services](../../guides/system-information-and-utilities/services.md).

**Flags**

- `D` (dynamic): Dynamic entry created by RouterOS: a port that another feature or a container listens on (for example `btest`, `discover`, `resolver`, `dhcp`, `upnp`), or, together with the `c` flag, an established connection to a service.
- `X` (disabled): The service is disabled and does not listen on its port.
- `I` (invalid): The service cannot run with its settings, for example because another service already uses the port. The reason is shown as a comment, such as `cannot bind to port 80: Address in use (12)`.
- `c` (connection): The entry is an established connection to a service. `local` and `remote` show the addresses of the connection.

**Arguments**

- `port` (num): TCP port the service listens on, `1..65535`. When another service already listens on the port, the entry becomes invalid (`I`). The default depends on the service: `ftp` 21, `ssh` 22, `telnet` 23, `www` 80, `www-ssl` 443, `winbox` 8291, `api` 8728, `api-ssl` 8729, `reverse-proxy` 443.
- `address` (object { address: alt { address: ipPrefix , address: ip6Prefix } }; deprecated): Deprecated name of `available-from`. A value set with `address` is written to `available-from`.
- `available-from` (object { address: alt { address: ipPrefix , address: ip6Prefix } }): IPv4 and IPv6 prefixes of the clients allowed to use the service. A client from another address can still open the TCP connection, and the router then closes it without serving the client, so the port stays visible. To hide a service from untrusted networks, drop the traffic in the firewall input chain as well. Empty means any address. Default: empty.
- `certificate` (enum: none): Certificate the service presents to TLS clients. Applies to `www-ssl`, `api-ssl` and `reverse-proxy`. With `none`, `www-ssl` and `api-ssl` accept only anonymous Diffie-Hellman ciphers: the connection is encrypted, but the router does not prove its identity, and browsers and tools such as cURL cannot connect. Set a certificate for HTTPS. For `reverse-proxy`, the certificate is used by the rules that have none of their own (see [`/ip/reverse-proxy`](https://manual.mikrotik.com/docs/cli-reference/ip/reverse-proxy)). Default: none.
- `tls-version` (enum: any | only-1.2): TLS versions the service accepts. Applies to the TLS services.
  - `any` (default) - TLS 1.0, 1.1 and 1.2.
  - `only-1.2` - Only TLS 1.2.
- `vrf` (enum): VRF the service listens in. Default: main.
- `max-sessions` (num): Maximum number of simultaneous sessions of the service, `1..1000`. Default: 20.

**Read-only arguments**

- `container` (enum): Name of the container that listens on the port, for dynamic entries created by containers.
- `netns` (num): Network namespace number of the container that listens on the port, for dynamic entries created by containers.
- `name` (string): Name of the service. For dynamic entries, the feature or program that listens on the port or holds the connection.
- `proto` (enum): Transport protocol of the port: `tcp` or `udp`.
- `local` (ip6Addr): Router address of an established connection (entries with the `c` flag).
- `remote` (composite { ip: ip6Addr , port: num }): Client address and port of an established connection (entries with the `c` flag).
