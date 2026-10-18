# /interface/eoip

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/eoip

Type: Directory

[Ethernet over IP (EoIP)](../../guides/virtual-private-networks/eoip.md) Tunneling is a MikroTik RouterOS protocol designed to create an Ethernet tunnel between two routers over an IP network.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `R` (running): Whether the interface is running.

**Arguments**

- `name` (string): Interface name.
- `mtu` (num): Layer3 maximum transmission unit.
- `mac-address` (macAddr): Media Access Control number of an interface. The address numeration authority IANA allows the use of MAC addresses in the range from 00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF freely.
- `local-address` (ipAddr): Source address of the tunnel packets, local to the router.
- `remote-address` (address (flags=4Dv); mandatory): IP address of the remote end of the EoIP tunnel.
- `tunnel-id` (num; mandatory): Unique tunnel identifier, which must match the other side of the tunnel.
- `keepalive` (super { keepalive-interval: time [1 .. ] , [keepalive-retries] [ ,num [1 .. ]] }): The keepalive parameter sets the time interval in which the tunnel running flag remains even if the remote end of the tunnel goes down. If the configured time and retries fail, the interface running flag is removed.
  Parameters are written in the following format: `KeepaliveInterval,KeepaliveRetries`
   where KeepaliveInterval is the time interval and KeepaliveRetries is the number of retry attempts.
  By default keepalive is set to 10 seconds and 10 retries.
- `dscp` (num): DSCP value of the packet. Inherited means the DSCP value is inherited from the packet to be encapsulated.
- `clamp-tcp-mss` (bool): Controls whether to change MSS size for received TCP SYN packets. When enabled, the router changes the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet still contains the original MSS, and only after decapsulation the MSS is changed.
- `dont-fragment` (bool): Whether to include the DF bit in related packets.
  - `no` - fragment if needed.
  - `inherit` - use the DF flag of the original packet.
- `ipsec-secret` (string; syscap=security): When a secret is specified, the router adds a dynamic IPsec peer to remote-address with a pre-shared key and policy (by default phase2 uses sha1/aes128cbc).
- `allow-fast-path` (bool): Whether to allow FastPath processing. Must be disabled if IPsec tunneling is used.
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp): [Address Resolution Protocol](https://manual.mikrotik.com/docs/getting-started/networking-fundamentals/index#arp-and-tying-it-all-together) mode.
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time }): Time interval in which ARP entries time out.
- `arp-accept` (bool): Whether to accept gratuitous ARP replies.
- `loop-protect` (enum: default | off | on): Enables or disables loop protect on the selected interface. `default` works as turned off.
- `loop-protect-send-interval` (time): Sets how often loop protect packets are sent on the selected interface.
- `loop-protect-disable-time` (time): Sets how long the selected interface is disabled when a loop is detected.

**Read-only arguments**

- `actual-mtu` (num): Actual maximum transmission unit of the tunnel.
- `l2mtu` (num): [Layer2 maximum transmission unit](https://manual.mikrotik.com/docs/hardware/mtu-in-routeros). Not configurable for EoIP.
- `current-remote-address` (ipAddr): Current IPv4 address of the remote end.
- `loop-protect-status` (enum: off | on | disabled): Loop protection status:
  - `on` - loop protect is enabled and the interface is sending and listening for loop protect packets
  - `off` - loop protect is disabled
  - `disabled` - loop protect is enabled, the interface has received a loop protect packet and disabled itself to prevent a loop.
