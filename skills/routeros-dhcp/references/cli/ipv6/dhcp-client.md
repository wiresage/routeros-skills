# /ipv6/dhcp-client

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-client

Type: Directory

The DHCPv6 client requests IPv6 addresses, delegated prefixes (DHCPv6-PD) or other settings from a DHCPv6 server. For an overview and configuration examples, see [DHCPv6 Client](../../guides/network-management/dhcp/dhcpv6-client.md). For how DHCPv6 differs from DHCP for IPv4, see [DHCP](../../guides/network-management/dhcp.md).

**Flags**

- `D` (dynamic): The DHCPv6 client was created dynamically.
- `X` (disabled): The DHCPv6 client is disabled.
- `I` (invalid): The DHCPv6 client configuration is invalid.

**Arguments**

- `interface` (iface_enum; mandatory): Interface the client runs on. A received address is added to this interface as a dynamic /128 address.
- `request` (ubit (info, address, prefix); mandatory): What the client requests from the server. One client can request more than one of these:
  - `address` - An IPv6 address (IA_NA), which is added to the client interface as a dynamic /128 address.
  - `prefix` - A delegated prefix (IA_PD), which is added to the IPv6 pool set in `pool-name`.
  - `info` - Only other settings, without an address or prefix (Information-request). The client status is then `idle`.
- `accept-prefix-without-address` (bool): When both an address and a prefix are requested: whether to accept a reply that contains a prefix but no address. With `no`, the client keeps soliciting until a server offers both. Default: yes.
- `add-default-route` (bool): Whether to add a default route (`::/0`) through the DHCPv6 server, or through the relay if the reply came through one. DHCPv6 itself does not provide a default gateway. Default: no.
- `default-route-distance` (num): Distance of the default route the client adds. Default: 1.
- `default-route-tables` (object { table: alt { table-distance: composite { table: alt { table-default: enum (default) { default:0xffffffff } , table: enum } , distance: num [1 .. 255] } , table: alt { table-default: enum (default) { default:0xffffffff } , table: enum } } }): Routing tables to add the default route to, as `table` or `table:distance` entries. `default` is the main routing table, or the VRF routing table when the client interface belongs to a VRF. Default: default.
- `check-gateway` (enum: none | arp | ping | bfd): Gateway check set on the default route the client adds (`none`, `arp`, `ping` or `bfd`), so the route is only used while its gateway responds. Default: none.
- `use-peer-dns` (bool): Whether to accept the DNS servers advertised by the DHCPv6 server. Default: yes.
- `use-interface-duid` (bool): Whether to use a DUID generated from the MAC address of the client interface, instead of the router's DUID that the router's other DHCPv6 clients and its DHCPv6 server use. Default: no.
- `custom-duid` (string): DUID to send instead of the generated one, in hex, for example `0x0003000102aabbccddee`. Overrides `use-interface-duid`.
- `validate-server-duid` (bool): Whether to check that the DUID sent by the DHCPv6 server is correctly formed. With `no`, an incorrectly formed server DUID is accepted, but its minimum length is still checked. Default: yes.
- `rapid-commit` (bool): Whether to ask for the two-message exchange (Solicit and Reply) with the Rapid Commit option. If the server does not use it, or with `no`, the four-message exchange (Solicit, Advertise, Request, Reply) is used. Default: yes.
- `allow-reconfigure` (bool): Whether to accept Reconfigure messages from the DHCPv6 server. When enabled, the client says so in its Solicit, receives a reconfigure key, and renews immediately when the server sends a Reconfigure message. The RouterOS DHCPv6 server sends Reconfigure messages when its settings change and with the `send-reconfigure` command of the binding. Default: no.
- `dhcp-options` (multi { array-id, option: enum }): Options the client sends, selected by name from `/ipv6/dhcp-client/option`. The predefined `fqdn` option sends the router's identity as the client's FQDN (option 39). Default: fqdn.
- `pool-name` (string): Name of the dynamic IPv6 pool the client creates from the received prefix, from which addresses can be assigned to other interfaces. The lifetime of the pool follows the prefix and is extended with each renewal. Applied only when a prefix is requested.
- `pool-prefix-length` (num): Prefix length the pool hands out, for example `64`. It must be equal to or longer than the received prefix. When not set, the length is chosen automatically, for example 64 for a received /56. Applied only when a prefix is requested.
- `prefix-hint` (ip6Prefix): Prefix or prefix length to suggest to the server, for example `::/60` to ask for a /60. The server does not have to follow it. `::/0` sends no hint. Default: ::/0.
- `prefix-address-lists` (multi { array-id, prefix-address-list: string }): IPv6 firewall address lists to which the received prefix is added as a dynamic entry. Applied only when a prefix is requested.
- `script` (alt { script: string }): Script to run when the client gets, renews or loses an address or a prefix. It runs separately for the prefix and for the address, and receives these variables:
  - `pd-valid` - `1` when the prefix was obtained, `0` when it was lost; empty when the run is about the address.
  - `pd-prefix` - The prefix, with its length.
  - `na-valid` - `1` when the address was obtained, `0` when it was lost; empty when the run is about the prefix.
  - `na-address` - The address.
  - `options` - Array of the options received from the server, indexed by option code.
- `custom-iapd-id` (num): Identity association identifier (IAID) to use for the prefix request (IA_PD), instead of the one derived from the client interface.
- `custom-iana-id` (num): Identity association identifier (IAID) to use for the address request (IA_NA), instead of the one derived from the client interface.

**Read-only arguments**

- `status` (enum: stopped | searching... | requesting... | bound | renewing... | rebinding... | stopping... | declining... | error | idle | requesting-info... | confirming...): Current state of the client:
  - `searching...` - Sending Solicit messages and waiting for a server.
  - `requesting...` - Requesting the offered address or prefix.
  - `bound` - The client has its address or prefix.
  - `renewing...` - Renewing with the server that gave the address or prefix.
  - `rebinding...` - The server did not answer the renewal; asking any server.
  - `requesting-info...` - Waiting for the reply to an Information-request (`request=info`).
  - `idle` - The Information-request was answered (`request=info`).
  - `confirming...` - Checking with a server that the address or prefix is still valid for the link.
  - `declining...` - Declining an address.
  - `stopping...` - Sending a Release message.
  - `stopped` - The client is disabled.
  - `error` - The client cannot run.
- `duid` (string): DUID the client sends.
- `dhcp-server-v6` (ip6Addr): Address the server's replies came from, usually the link-local address of the DHCPv6 server.
- `prefix` (composite { prefix: ip6Prefix , expires-after: time }): Received prefix and the time until it expires.
- `address` (composite { address: ip6Addr , expires-after: time }): Received address and the time until it expires.
- `reconfigure-key` (string): Key received from the DHCPv6 server to authenticate its Reconfigure messages. Set only when `allow-reconfigure` is enabled.
- `reconfigure-last-counter` (string): Replay-detection counter of the last Reconfigure message accepted from the DHCPv6 server. It increases with every Reconfigure message.

## Commands

### /ipv6/dhcp-client/release

Type: Command

Releases the current addresses and prefixes. The client sends a Release message to the server, then starts over and solicits again.

### /ipv6/dhcp-client/renew

Type: Command

Renews the current addresses and prefixes immediately, without waiting for the renewal time. If the server does not answer, the client keeps its address and prefix while it retries.
