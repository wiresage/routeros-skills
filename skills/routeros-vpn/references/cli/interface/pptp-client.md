# /interface/pptp-client

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/pptp-client

Type: Directory

**Flags**

- `X` (disabled): Whether an item is disabled.
- `R` (running): Whether the interface is running.

**Arguments**

- `name` (string): Descriptive name of the interface.
- `max-mtu` (num): Maximum Transmission Unit. Maximum packet size that the PPTP interface can send without packet fragmentation.
- `max-mru` (num): Maximum Receive Unit. Maximum packet size that the PPTP interface can receive without packet fragmentation.
- `mrru` (num): Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.
- `connect-to` (alt { address: ipAddr , name: string }; mandatory): Remote address of the PPTP server.
- `user` (string; mandatory): User name used for authentication.
- `password` (string): Password used for authentication.
- `profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
- `keepalive-timeout` (enum: disabled): Keepalive timeout in seconds.
- `use-peer-dns` (enum: no | yes | exclusively): Whether to use DNS settings from the peer.
- `add-default-route` (bool): Whether to add the PPTP remote address as a default route.
- `default-route-distance` (num): Distance value applied to the auto-created default route when add-default-route is enabled.
- `dial-on-demand` (bool): Connects to the PPTP server only when outbound traffic is generated. If enabled, a route with a gateway address from 10.112.112.0/24 network is added while the connection is not established.
- `allow` (ubit (pap, chap, mschap1, mschap2)): Allowed authentication methods.

## Commands

### /interface/pptp-client/monitor

Type: Command

**Read-only arguments**

- `status` (string): Current connection status.
- `uptime` (time): Connection uptime.
- `encoding` (string): Encryption encoding used.
- `mtu` (num): Current MTU of the connection.
- `mru` (num): Current MRU of the connection.
- `local-address` (ipAddr): Local IP address of the connection.
- `remote-address` (ipAddr): Remote IP address of the connection.
- `local-ipv6-address` (ip6Addr): Local IPv6 address of the connection.
- `remote-ipv6-address` (ip6Addr): Remote IPv6 address of the connection.
