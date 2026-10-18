# /interface/wireguard/peers

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireguard/peers

Type: Directory

**Flags**

- `X` (disabled): Whether an item is disabled.
- `D` (dynamic): Whether the peer was created dynamically.

**Arguments**

- `interface` (iface_enum; mandatory): Name of the WireGuard interface the peer belongs to.
- `name` (string): Adds a name to a peer, used as a reference in WireGuard logs. Available from RouterOS version 7.15.
- `public-key` (string): A base64 public key calculated from the private key. Public keys are used by peers to authenticate each other.
- `private-key` (alt { private-key: num , private-key: string }): A base64 private key. `auto` generates the key automatically, `none` disables it.
- `endpoint-address` (address (flags=46D)): The IP address or hostname used by WireGuard to establish a secure connection between two peers.
- `endpoint-port` (num): The UDP port on which a WireGuard peer listens for incoming traffic.
- `allowed-address` (multi { allowed-address: address (flags=46/) }; mandatory): List of IP (v4 or v6) addresses with CIDR masks from which incoming traffic for this peer is allowed and to which outgoing traffic for this peer is directed. Allowed-address ranges cannot overlap on one interface.
- `preshared-key` (alt { preshared-key: num , preshared-key: string }): A base64 preshared key. Adds an additional layer of symmetric-key cryptography for post-quantum resistance. `auto` generates the key automatically.
- `persistent-keepalive` (time): Interval in seconds of how often to send an authenticated empty packet to the peer to keep a stateful firewall or NAT mapping valid. A value of 0 disables the keepalive.
- `client-address` (multi { client-address: address (flags=46/) }): When imported with a QR code by a client, this address for the WireGuard interface is set on that device.
- `client-dns` (multi { client-dns: address (flags=46D) }): DNS servers included in the generated client configuration. This does not change the DNS configuration on this router.
- `client-endpoint` (address (flags=46D)): IP address or hostname included as the endpoint in the generated client configuration. The WireGuard interface's listen port is appended to it.
- `client-keepalive` (time): Same as persistent-keepalive but from the peer side.
- `client-listen-port` (num): The local port on which the WireGuard tunnel listens for incoming traffic from peers and from which it sources outgoing packets.
- `client-allowed-address` (multi { client-allowed-address: address (flags=46/) }): Allowed IPs configured for the client. Available from RouterOS version 7.21.
- `client-mtu` (num): MTU value set on the client when importing configuration.
- `responder` (bool): Specifies if the peer is a connection initiator or only a responder. Use on WireGuard devices that act as servers for client devices. Otherwise the router repeatedly tries to connect to endpoint-address or current-endpoint-address.

**Read-only arguments**

- `current-endpoint-address` (address (flags=46)): The most recent source IP address of correctly authenticated packets from the peer.
- `current-endpoint-port` (num): The most recent source IP port of correctly authenticated packets from the peer.
- `rx` (num): The total amount of bytes received from the peer.
- `tx` (num): The total amount of bytes transmitted to the peer.
- `last-handshake` (time): Time in seconds after the last successful handshake.

## Commands

### /interface/wireguard/peers/show-client-config

Type: Command

**Arguments**

- `file` (file): Name of the file to save the client configuration to.

**Read-only arguments**

- `conf` (string): The client configuration text.
- `qr` (pic): QR code generated from the client configuration for easier peer setup on a mobile device.
