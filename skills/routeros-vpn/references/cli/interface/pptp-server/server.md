# /interface/pptp-server/server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/pptp-server/server

Type: Settings Directory

**Arguments**

- `enabled` (bool): Defines whether the PPTP server is enabled.
- `max-mtu` (num): Maximum Transmission Unit. Maximum packet size that the PPTP interface can send without packet fragmentation.
- `max-mru` (num): Maximum Receive Unit. Maximum packet size that the PPTP interface can receive without packet fragmentation.
- `mrru` (num): Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.
- `authentication` (ubit (pap, chap, mschap1, mschap2)): Authentication methods that the server accepts.
- `keepalive-timeout` (enum: disabled): If the server does not receive any packet during the keepalive period, it sends keepalive packets every second five times. If the server does not receive a response from the client, the connection is disconnected after 5 seconds.
- `default-profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
