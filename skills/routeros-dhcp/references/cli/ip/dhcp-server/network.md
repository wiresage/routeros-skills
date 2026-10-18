# /ip/dhcp-server/network

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/network

Type: Directory

Settings sent to DHCP clients. The server sends a client the settings of the network entry that contains the client's address. For details, see [DHCP Server](../../../guides/network-management/dhcp/server.md).

**Flags**

- `D` (dynamic): The network was created dynamically.

**Arguments**

- `address` (composite { address: ipAddr , netmask: num [ .. 32] }): Network this entry applies to, for example `192.168.88.0/24`.
- `gateway` (multi { address: ipAddr }): Default gateway sent to clients (option 3). More than one gateway can be listed.
- `netmask` (num): Subnet mask sent to clients, as a prefix length, when it should differ from the mask of `address`. With `0`, the mask of `address` is used.
- `dns-server` (alt { server: multi { address: ipAddr } }): DNS servers sent to clients (option 6). When not set, the server sends the DNS servers the router itself uses (`/ip/dns`).
- `dns-none` (bool): Whether to send no DNS servers at all, not even those of the router. Default: no.
- `wins-server` (multi { address: ipAddr }): WINS servers sent to clients (option 44).
- `ntp-server` (alt { server: multi { address: ipAddr } }): NTP servers sent to clients (option 42). When not set, the server sends the NTP servers the router itself uses.
- `ntp-none` (bool): Whether to send no NTP servers at all, not even those of the router. Default: no.
- `caps-manager` (multi { address: ipAddr }): CAPsMAN addresses sent to clients (option 138).
- `domain` (string): Domain name sent to clients (option 15).
- `next-server` (ipAddr): Address of the server for the next step of network boot, sent in the `siaddr` field, for example a TFTP server. When not set, the address of the DHCP server is sent.
- `boot-file-name` (string): Name of the boot file for network boot, sent in the `file` field.
- `dhcp-option` (multi { array-id, option: enum }): Options (`/ip/dhcp-server/option`) sent to clients in this network. Options of the server and of the lease take precedence.
- `dhcp-option-set` (enum: none): Option set (`/ip/dhcp-server/option/sets`) sent to clients in this network. Options of the server and of the lease take precedence.
- `cmr-none` (bool): no servers will be sent to client
- `cmr-server` (ipAddr): If unset, IP address of dhcp server will be included if CMR is enabled; if set, the custom IP address will always be included even if CMR is disabled
