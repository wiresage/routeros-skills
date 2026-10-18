# /ip/firewall/connection

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/firewall/connection

Type: Directory

**Flags**

- `E`: expected
- `S`: seen-reply
- `A`: assured
- `C`: confirmed
- `D`: dying
- `F`: fasttrack
- `H`: hw-offload
- `s`: srcnat
- `d`: dstnat
- `h`: uses-helper

**Read-only arguments**

- `protocol` (enum): Connection protocol.
- `src-address` (ipAddr): Source IP address of the connection.
- `src-port` (num): Source port of the connection.
- `dst-address` (ipAddr): Destination IP address of the connection.
- `dst-port` (num): Destination port of the connection.
- `reply-src-address` (ipAddr): Reply source IP address.
- `reply-src-port` (num): Reply source port.
- `reply-dst-address` (ipAddr): Reply destination IP address.
- `reply-dst-port` (num): Reply destination port.
- `tcp-state` (enum: none | syn-sent | syn-recv | established | fin-wait | close-wait | last-ack | time-wait | close | listen): TCP connection state.
- `icmp-type` (num): ICMP type.
- `icmp-code` (num): ICMP code.
- `icmp-id` (num): ICMP ID.
- `gre-protocol` (num): GRE protocol.
- `gre-version` (num): GRE version.
- `gre-key` (num): GRE key.
- `connection-type` (string): Connection type.
- `timeout` (time): Connection timeout.
- `connection-mark` (string): Connection mark.
- `orig-packets` (num): Number of original direction packets.
- `orig-bytes` (num): Number of original direction bytes.
- `orig-fasttrack-packets` (num): Number of original direction fasttrack packets.
- `orig-fasttrack-bytes` (num): Number of original direction fasttrack bytes.
- `repl-packets` (num): Number of reply direction packets.
- `repl-bytes` (num): Number of reply direction bytes.
- `repl-fasttrack-packets` (num): Number of reply direction fasttrack packets.
- `repl-fasttrack-bytes` (num): Number of reply direction fasttrack bytes.
- `orig-rate` (num): Original direction rate.
- `repl-rate` (num): Reply direction rate.
