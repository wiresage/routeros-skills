# /interface/sstp-client

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/sstp-client

Type: Directory

**Flags**

- `X` (disabled): Whether an item is disabled.
- `R` (running): Whether the interface is running.
- `H` (hw-crypto): Whether hardware encryption is active.

**Arguments**

- `name` (string): Descriptive name of the interface.
- `max-mtu` (num): Maximum Transmission Unit.
- `max-mru` (num): Maximum Receive Unit.
- `mrru` (num): Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.
- `connect-to` (address (flags=D46v); mandatory): Remote address of the SSTP server.
- `port` (num): Port to connect to.
- `http-proxy` (alt { address: ipAddr , ipv6-address: ip6Addr , name: string }): Proxy address.
- `proxy-port` (num): Proxy port.
- `certificate` (enum: none): Client certificate from the certificate store.
- `verify-server-certificate` (bool): Verifies the server certificate against the router's certificate store.
- `verify-server-address-from-certificate` (bool): Verifies the server address from the certificate.
- `user` (string; mandatory): User name used for authentication.
- `password` (string): Password used for authentication.
- `profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
- `keepalive-timeout` (enum: disabled): Keepalive timeout in seconds.
- `add-default-route` (bool): Whether to add the SSTP remote address as a default route.
- `default-route-distance` (num): Distance value applied to the auto-created default route when add-default-route is enabled.
- `dial-on-demand` (bool): Connects only when outbound traffic is generated. If enabled, a route with a gateway address from 10.112.112.0/24 network is added while the connection is not established.
- `authentication` (ubit (pap, chap, mschap1, mschap2)): Allowed authentication methods. By default all methods are allowed.
- `pfs` (enum: no | yes | required): Specifies which TLS authentication to use. `yes` - TLS uses ECDHE-RSA and DHE-RSA. `required` - uses only ECDHE.
- `tls-version` (enum: any | only-1.2): Specifies which TLS version to allow.
- `ciphers` (ubit (aes256-sha, aes256-gcm-sha384)): Allowed ciphers.
- `add-sni` (bool): Adds TLS SNI extension to client hello packets. Available from RouterOS version 7.15.

## Commands

### /interface/sstp-client/monitor

Type: Command

**Read-only arguments**

- `status` (string): Current connection status.
- `uptime` (time): Connection uptime.
- `encoding` (string): Encryption encoding used.
- `mtu` (num): Current MTU of the connection.
- `local-address` (ipAddr): Local IP address of the connection.
- `remote-address` (ipAddr): Remote IP address of the connection.
- `local-ipv6-address` (ip6Addr): Local IPv6 address of the connection.
- `remote-ipv6-address` (ip6Addr): Remote IPv6 address of the connection.
