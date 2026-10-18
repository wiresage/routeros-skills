# /interface/ipipv6

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ipipv6

Type: Directory

[IPIP](../../guides/virtual-private-networks/ipip.md) (IP-in-IP) is a simple tunneling protocol defined in RFC 2003 that encapsulates IP packets within another IP header to transport traffic between two endpoints.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `R` (running): Whether the interface is running.

**Arguments**

- `name` (string): Interface name.
- `mtu` (num): Layer3 maximum transmission unit.
- `local-address` (ip6Addr): IP address on the router used by the IPIP tunnel.
- `remote-address` (address (flags=6Dvi); mandatory): IP address of the remote end of the IPIP tunnel.
- `keepalive` (super { keepalive-interval: time [1 .. ] , [keepalive-retries] [ ,num [1 .. ]] }): The keepalive parameter sets the time interval in which the tunnel running flag remains even if the remote end of the tunnel goes down. If the configured time and retries fail, the interface running flag is removed.
  Parameters are written in the following format: `KeepaliveInterval,KeepaliveRetries`
   where KeepaliveInterval is the time interval and KeepaliveRetries is the number of retry attempts.
  By default keepalive is set to 10 seconds and 10 retries.
- `dscp` (num): DSCP value of the packet. Inherited means the DSCP value is inherited from the tunneled traffic.
- `clamp-tcp-mss` (bool): Controls whether to change the MSS size for received TCP SYN packets. When enabled, the router changes the MSS size for received TCP SYN packets if the current MSS size exceeds the tunnel interface MTU (taking into account the TCP/IP overhead). The received encapsulated packet still contains the original MSS, and only after decapsulation the MSS is changed.
- `dont-fragment` (bool): Whether to include the DF bit in related packets.
  - `no` - fragment if needed.
  - `inherit` - use the DF flag of the original packet.
- `ipsec-secret` (string; syscap=security): When a secret is specified, the router adds a dynamic IPsec peer to remote-address with a pre-shared key and policy (by default phase2 uses sha1/aes128cbc).

**Read-only arguments**

- `actual-mtu` (num): Actual maximum transmission unit of the tunnel.
- `current-remote-address` (ip6Addr): Current IP address of the remote end.
