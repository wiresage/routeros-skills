# /ipv6/dhcp-server

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-server

Type: Directory

The DHCPv6 server delegates IPv6 prefixes (DHCPv6-PD) and assigns IPv6 addresses to clients. Prefixes and addresses come from IPv6 pools or from static bindings (`/ipv6/dhcp-server/binding`). For an overview and configuration examples, see [DHCPv6 Server](../../guides/network-management/dhcp/dhcpv6-server.md).

**Flags**

- `D` (dynamic): The DHCPv6 server was created dynamically.
- `X` (disabled): The DHCPv6 server is disabled.
- `I` (invalid): The DHCPv6 server configuration is invalid.

**Arguments**

- `name` (string; mandatory): Name of the DHCPv6 server.
- `interface` (iface_enum; mandatory): Interface the DHCPv6 server listens on.
- `prefix-pool` (alt { prefix-pool-static: enum (static-only) { static-only:0xffffffff } , prefix-pool-name: enum }): IPv6 pool from which dynamic prefix bindings get their prefixes. With `static-only`, only static bindings are given out. Default: static-only.
- `address-pool` (alt { address-pool-static: enum (static-only) { static-only:0xffffffff } , address-pool-name: enum }): IPv6 pool from which dynamic address bindings get their addresses. The pool prefix length must be 128. With `static-only`, only static bindings are given out. Default: static-only.
- `lease-time` (time): Lifetime of new and renewed bindings. Clients are told to renew after half of it and to rebind after 80% of it, and the preferred lifetime is 90% of it. Default: 3d.
- `rapid-commit` (bool): Whether to answer a Solicit that asks for Rapid Commit directly with a Reply (two-message exchange). With `no`, the server always answers with an Advertise first. Default: yes.
- `use-radius` (enum: no | yes | accounting): Whether to use a RADIUS server for bindings: `no` (default), `yes` for authentication and accounting, or `accounting` for accounting only.
- `preference` (num): Preference value sent in Advertise messages. Clients prefer the server with the highest value. Default: 255.
- `binding-script` (alt { script: string }): Script to run when a binding is bound and when it ends. It runs separately for each binding, and receives these variables:
  - `bindingBound` - `1` when the binding was bound, otherwise `0`.
  - `bindingServerName` - Name of the DHCPv6 server.
  - `bindingDUID` - DUID of the client.
  - `bindingAddress` - IPv6 address the client sends from, usually its link-local address.
  - `bindingPrefix` - The delegated prefix, or the assigned address for an address binding.
- `dns-none` (bool): Don't add DNS servers to responses
- `dhcp-option` (multi { array-id, option: alt { option: enum , option-set: enum } }): Options (`/ipv6/dhcp-server/option`) to send to clients, for example DNS servers (option 23).
- `insert-queue-before` (enum (first | bottom) { first:0, bottom:0xffffffff }): Where to place the dynamic simple queues created for bindings with a `rate-limit`: `first` (default) at the top of `/queue/simple`, `bottom` at the end, or before the named queue.
- `parent-queue` (enum: none): Parent of the dynamic simple queues created for bindings with a `rate-limit`. Default: none.
- `route-distance` (num): Distance of the routes the server adds to each delegated prefix and assigned address, through the client's link-local address. Default: 1.
- `allow-dual-stack-queue` (bool): Whether a binding and a DHCP lease of the same client share one dynamic simple queue, which then contains both the IPv6 and the IPv4 address. The client is recognized by its MAC address and DUID. The DHCP server must have this setting enabled as well. Default: yes.
- `use-reconfigure` (bool): Whether to send Reconfigure messages. When enabled, clients that accept them get a reconfigure key, and the server sends a Reconfigure message by itself: to all its bindings when `address-pool`, `lease-time` or `dhcp-option` change, and to a binding when the binding's settings change, so the clients renew; and a rebind request when the server or the binding's server is removed. The `send-reconfigure` command of the binding sends one manually. Default: no.
- `address-lists` (multi { array-id, address-list: string }): IPv6 firewall address lists to which the prefix or address of each binding is added. The `address-lists` setting of a binding overrides this.
- `add-dns-entries` (bool): Whether to add a dynamic DNS entry (type AAAA) for each address binding. The entry name is the FQDN the client sends (option 39) followed by `add-dns-entries-suffix`, and its TTL is the lease time. Prefix bindings get no entry. Default: no.
- `add-dns-entries-suffix` (string): Domain appended to the client name in the DNS entries created by `add-dns-entries`, for example `laptop.lan`. Default: lan.
- `ignore-ia-na-bindings` (bool): Whether to ignore address requests (IA_NA) and act as if the client's messages did not contain them, so only prefixes are handed out. Without it, a server with no address pool still answers each address request that no address is available, which can make a client that requests both keep asking. Default: no.

**Read-only arguments**

- `duid` (string): DUID of the server. The router uses the same DUID for its DHCPv6 clients.
