# /interface/l2tp-server/server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/l2tp-server/server

Type: Settings Directory

**Arguments**

- `enabled` (bool): Enables or disables the L2TP server.
- `max-mtu` (num): Maximum Transmission Unit. Maximum packet size that the L2TP interface can send without packet fragmentation.
- `max-mru` (num): Maximum Receive Unit. Maximum packet size that the L2TP interface can receive without packet fragmentation.
- `mrru` (num): Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.
- `authentication` (ubit (pap, chap, mschap1, mschap2)): Allowed authentication methods.
- `keepalive-timeout` (enum: disabled): Keepalive timeout in seconds.
- `max-sessions` (num): Maximum number of concurrent L2TP sessions.
- `default-profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
- `use-ipsec` (enum: no | yes | required): Whether to use IPsec encryption. `required` forces all clients to use IPsec.
- `ipsec-secret` (string): IPsec pre-shared key.
- `caller-id-type` (enum: ip-address | number): Caller ID type reported to the client.
- `one-session-per-host` (bool): Whether to allow only one session per host.
- `allow-fast-path` (bool): Whether to allow FastPath processing.
- `l2tpv3-circuit-id` (string): L2TPv3 circuit identifier.
- `l2tpv3-cookie-length` (enum: 0 | 4-bytes | 8-bytes): L2TPv3 cookie length.
- `l2tpv3-digest-hash` (enum: none | md5 | sha1): L2TPv3 digest hash algorithm.
- `l2tpv3-ether-interface-list` (enum): Interface list for L2TPv3 Ethernet pseudowire endpoints.
- `accept-pseudowire-type` (enum: all | ether | ppp): Accepted pseudowire types.
- `accept-proto-version` (enum: all | l2tpv2 | l2tpv3): Accepted L2TP protocol versions.
