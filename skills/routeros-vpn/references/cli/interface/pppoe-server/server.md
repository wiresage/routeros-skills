# /interface/pppoe-server/server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/pppoe-server/server

Type: Directory

**Flags**

- `X` (disabled): Whether an item is disabled.
- `I` (invalid): Whether the server configuration is invalid.

**Arguments**

- `service-name` (string): The PPPoE service name. Server accepts clients that send a PADI message with service-names that match this setting, or if the service-name field in the PADI message is not set.
- `interface` (iface_enum { <l2tp>:0xfffffffe }; mandatory): Interface that the clients are connected to.
- `max-mtu` (num): Maximum Transmission Unit. The optimal value is the MTU of the interface the tunnel is working over reduced by 20 (so, for 1500-byte Ethernet link, set the MTU to 1480 to avoid fragmentation of packets).
- `max-mru` (num): Maximum Receive Unit. The optimal value is the MTU of the interface the tunnel is working over reduced by 20 (so, for 1500-byte Ethernet link, set the MTU to 1480 to avoid fragmentation of packets).
- `mrru` (num): Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.
- `authentication` (ubit (pap, chap, mschap1, mschap2)): Authentication methods that the server accepts.
- `keepalive-timeout` (enum: disabled): Defines the time period (in seconds) after which the router starts sending keepalive packets every second. If no traffic and no keepalive responses arrive for twice the `keepalive-timeout`, the non-responding client is disconnected. Set to `disabled` to turn off echo packets.
- `one-session-per-host` (bool): Allow only one session per host (determined by MAC address). If a host tries to establish a new session, the old one is closed.
- `max-sessions` (num): Maximum number of clients that the AC can serve. `0` means no limitation.
- `pado-delay` (num): Delay in milliseconds before sending PADO response.
- `default-profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
- `accept-empty-service` (bool): Accept PADI with empty service name if no matching PPPoE service is available.
- `pppoe-over-vlan-range` (multi { vlan-range: range [1 .. 4094] }): This setting allows a PPPoE server to operate over 802.1Q VLANs. Supports a range of VLAN IDs and individual VLANs specified with comma-separated values, for example: `100-115,120,122,128-130`.

  When you specify the VLAN IDs, the PPPoE server will accept 802.1Q tagged packets from clients, and it will reply using the same VLAN. You then have an option to accept or drop untagged PPPoE clients on the same interface using the `accept-untagged` property.
  You can configure the PPPoE server with `pppoe-over-vlan-range` setting even on VLAN interface enabling the QinQ setups as well. But keep in mind that the inner VLAN tag should be 802.1Q.
- `accept-untagged` (bool): Whether to accept untagged (non-VLAN) PPPoE packets on the interface when `pppoe-over-vlan-range` is specified.
