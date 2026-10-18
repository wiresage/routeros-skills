# /interface/ovpn-server/server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ovpn-server/server

Type: Directory

**Flags**

- `I` (inactive): Whether the server is inactive.
- `X` (disabled): Whether an item is disabled.

**Arguments**

- `name` (string): Name of the server.
- `port` (num): Port to run the server on.
- `mode` (enum: ip | ethernet): Layer3 or Layer2 tunnel mode (alternatively tun, tap).
- `protocol` (enum: tcp | udp): Transport protocol to use when connecting with the remote endpoint.
- `netmask` (num): Subnet mask applied to the client.
- `mac-address` (macAddr): Automatically generated MAC address of the server.
- `max-mtu` (num): Maximum Transmission Unit. Maximum packet size that the OVPN interface can send without packet fragmentation.
- `keepalive-timeout` (enum: disabled): Defines the time period (in seconds) after which the router starts sending keepalive packets every second. If no traffic and no keepalive responses are received for twice the keepalive-timeout, the non-responding client is disconnected.
- `default-profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
- `certificate` (enum): Certificate from the certificate store that the OVPN server uses.
- `require-client-certificate` (bool): If set to yes, the server checks whether the client's certificate belongs to the same certificate chain.
- `tls-version` (enum: any | only-1.2): Specifies which TLS versions to allow.
- `auth` (ubit (sha1, md5, sha256, sha384, sha512, null)): Authentication methods that the server accepts.
- `cipher` (ubit (blowfish128, aes128-cbc, aes192-cbc, aes256-cbc, aes128-gcm, aes192-gcm, aes256-gcm, null)): Allowed ciphers.
- `reneg-sec` (num): Encryption key re-negotiation interval in seconds. 0 disables re-negotiation.
- `redirect-gateway` (ubit (disabled, def1, ipv6)): Specifies which routes the OVPN client must add to the routing table. `def1` - overrides the default gateway with 0.0.0.0/1 and 128.0.0.0/1 instead of 0.0.0.0/0. `disabled` - does not push redirect-gateway flags. `ipv6` - redirects IPv6 routing into the tunnel by adding 2000::/4 and 3000::/4 routes.
- `push-routes` (string): Routes to push to the client. Maximum input is limited to 1400 characters or 37 routes. IPv6 support added in version 7.21.
- `push-routes-ipv6` (string): IPv6 routes to push to the client.
- `enable-tun-ipv6` (bool): Whether IPv6 tunneling is enabled for this OVPN server.
- `tun-server-ipv6` (ip6Addr): IPv6 prefix address used when generating the OVPN interface on the server side.
- `ipv6-prefix-len` (num): Prefix length used for the tunneled IPv6 address.
- `vrf` (enum): VRF in which to listen for connection attempts.
- `user-auth-method` (enum: pap | mschap2): By default PAP authentication is used. Set to mschap2 to use CHAP challenge authentication.

## Commands

### /interface/ovpn-server/server/export-client-configuration

Type: Command

**Arguments**

- `server` (enum): OVPN server name to export configuration from.
- `server-address` (string): Public IP address or DNS name clients use to connect to this VPN server.
- `ca-certificate` (file): CA certificate used by the client OVPN configuration.
- `client-certificate` (file): Client certificate used by the client OVPN configuration.
- `client-cert-key` (file): Client private key used by the client OVPN configuration.

**Read-only arguments**

- `progress` (string): Export progress status.
