# /interface/gre6

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/gre6

Type: Directory

[Generic Routing Encapsulation (GRE)](../../guides/virtual-private-networks/gre.md) is a tunneling protocol originally developed by Cisco to encapsulate a wide variety of network layer protocols over an IP network.

**Flags**

- `X`: disabled
- `R`: running

**Arguments**

- `name` (string): Name of the tunnel.
- `mtu` (num): Layer3 maximum transmission unit.
- `local-address` (ip6Addr): IPV6 address used for the local tunnel end.
- `remote-address` (address (flags=6Dvi); mandatory): IPV6 address of the remote tunnel end.
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

- `actual-mtu` (num)
- `current-remote-address` (ip6Addr)
