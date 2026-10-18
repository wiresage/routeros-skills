# /interface/l2tp-ether

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/l2tp-ether

Type: Directory

Layer 2 Tunnel Protocol Version 3 (L2TPv3).

**Flags**

- `X` (disabled): Whether an item is disabled.
- `D` (dynamic): Whether the interface was created dynamically.
- `R` (running): Whether the interface is running.
- `u` (unmanaged): Whether the interface is unmanaged.

**Arguments**

- `name` (string): Interface name.
- `mtu` (num)
- `connect-to` (address (flags=D46v)): Remote server address. Set to 0.0.0.0 for incoming connections.
- `mac-address` (macAddr): MAC address of the L2TP interface.
- `use-ipsec` (bool): Ignored for passive (incoming) connections. For incoming connections use l2tp-server settings.
- `ipsec-secret` (string): Ignored for passive (incoming) connections. For incoming connections use l2tp-server settings.
- `allow-fast-path` (bool): Whether to allow FastPath processing.
- `l2tp-proto-version` (enum: l2tpv3-ip | l2tpv3-udp): L2TPv3 encapsulation mode (IP or UDP).
- `circuit-id` (string): L2TPv3 remote end identifier (virtual circuit ID).
- `cookie-length` (enum: 0 | 4-bytes | 8-bytes): Ignored for passive (incoming) connections. For incoming connections use l2tp-server settings.
- `digest-hash` (enum: none | md5 | sha1): Ignored for passive (incoming) connections. For incoming connections use l2tp-server settings.
- `use-l2-specific-sublayer` (bool): Enables L2TPv3 Ethernet pseudowire Level 2 default sublayer.
- `local-address` (alt { local-ipv4-address: ipAddr , local-ipv6-address: ip6Addr }): Local IPv4 or IPv6 address for unmanaged L2TP connections.
- `local-tunnel-id` (num): Local tunnel ID for unmanaged L2TP connections.
- `local-session-id` (num): Local session ID for unmanaged L2TP connections.
- `remote-tunnel-id` (num): Remote tunnel ID for unmanaged L2TP connections.
- `remote-session-id` (num): Remote session ID for unmanaged L2TP connections.
- `peer-cookie` (string): Cookie hex value for received packets (8 or 16 characters or empty) for unmanaged L2TP connections.
- `send-cookie` (string): Cookie hex value for sent packets (8 or 16 characters or empty) for unmanaged L2TP connections.
- `unmanaged-mode` (bool): Enables or disables unmanaged (static) tunnel mode.

**Read-only arguments**

- `actual-mtu` (num): Actual maximum transmission unit of the tunnel.

## Commands

### /interface/l2tp-ether/monitor

Type: Command

**Read-only arguments**

- `status` (string): Current connection status.
- `circuit-id` (string): L2TPv3 circuit identifier.
- `cookie-length` (num): L2TPv3 cookie length.
- `header-format` (string): L2TPv3 header format.
- `l2-sublayer` (bool): Whether L2 sublayer is enabled.
- `remote-sess-id` (num): Remote session ID.
- `local-sess-id` (num): Local session ID.
- `control-conn-id` (num): Control connection ID.
- `peer-address` (string): IP address of the connected peer.
- `encoding` (string): Encryption encoding used.
- `uptime` (time): Connection uptime.
