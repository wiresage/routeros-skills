# /interface/l2tp-client

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/l2tp-client

Type: Directory

**Flags**

- `X` (disabled): Whether an item is disabled.
- `R` (running): Whether the interface is running.

**Arguments**

- `name` (string): Descriptive name of the interface.
- `max-mtu` (num): Maximum Transmission Unit. Maximum packet size that the L2TP interface can send without packet fragmentation.
- `max-mru` (num): Maximum Receive Unit. Maximum packet size that the L2TP interface can receive without packet fragmentation.
- `mrru` (num): Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.
- `connect-to` (address (flags=D46v); mandatory): Remote address of the L2TP server. If the address is in the VRF table, VRF should be specified, for example, `192.168.88.1@vrf1` .
- `user` (string; mandatory): User name used for authentication.
- `password` (string): Password used for authentication.
- `profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
- `keepalive-timeout` (enum: disabled): Keepalive timeout in seconds.
- `src-address` (ipAddr): Source address used for the L2TP connection.
- `use-peer-dns` (enum: no | yes | exclusively): Whether to use DNS settings from the peer.
- `use-ipsec` (bool): When this option is enabled, dynamic IPSec peer configuration and policy (transport mode) is added to encapsulate the L2TP connection into an IPSec tunnel.

  Multiple L2tp/ipsec clients behind the same NAT will not work in this mode. To achieve such a scenario, disable use-ipsec and set static policies for clients with enabled tunnel=yes, level=unique settings.
- `ipsec-secret` (string): IPsec pre-shared key.
- `allow-fast-path` (bool): Whether to allow FastPath processing. Must be disabled if IPsec is used.
- `add-default-route` (bool): Whether to add the L2TP remote address as a default route.
- `default-route-distance` (num): Distance value applied to the auto-created default route when add-default-route is enabled.
- `dial-on-demand` (bool): Connects to the L2TP server only when outbound traffic is generated. If enabled, a route with a gateway address from 10.112.112.0/24 network is added while the connection is not established.
- `allow` (ubit (pap, chap, mschap1, mschap2)): Allowed authentication methods.
- `random-source-port` (bool): Whether to randomize the source port for L2TP connections.
- `l2tp-proto-version` (enum: l2tpv2 | l2tpv3-ip | l2tpv3-udp): L2TP protocol version to use.
- `l2tpv3-circuit-id` (string): L2TPv3 circuit identifier.
- `l2tpv3-cookie-length` (enum: 0 | 4-bytes | 8-bytes): L2TPv3 cookie length.
- `l2tpv3-digest-hash` (enum: none | md5 | sha1): L2TPv3 digest hash algorithm.

## Commands

### /interface/l2tp-client/monitor

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
