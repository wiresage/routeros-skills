# /ip/proxy/connections

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/connections

Type: Directory

Open connections of the web proxy. Each connection from a client and each connection to a server is a row. The proxy keeps connections to servers open after a response and uses them for later requests. For an overview, see [Web Proxy](../../../guides/network-management/proxy/web-proxy.md).

**Flags**

- `S` (server): server. A connection from the proxy to a server.
- `C` (client): client. A connection from a client to the proxy.

**Read-only arguments**

- `src-address` (alt { ip4: ipAddr , ip6: ip6Addr }): Address of the client whose request the connection serves.
- `dst-address` (alt { ip4: ipAddr , ip6: ip6Addr }): Address of the server.
- `last-protocol` (enum: HTTP/1.0 | HTTP/1.1 | FTP): Protocol of the last request on the connection: `HTTP/1.0`, `HTTP/1.1` or `FTP`.
- `state` (enum: rx-header | resolving | connecting | waiting | rx-body | tx-header | tx-body | idle): State of the connection, for example:
  - `waiting` - A client connection waits for the response from the server.
  - `rx-header` - A server connection receives the header of the response.
  - `idle` - A server connection is open and has no request.
- `tx-bytes` (num): Bytes the router sent on the connection.
- `rx-bytes` (num): Bytes the router received on the connection.
