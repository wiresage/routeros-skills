# /ipv6/dhcp-server/binding

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/dhcp-server/binding

Type: Directory

Bindings of the DHCPv6 servers: the prefixes and addresses given to clients. Dynamic bindings are created from the server's pools; static bindings give a client, identified by its DUID and IAID, a fixed prefix or address. For details, see [DHCPv6 Server](../../../guides/network-management/dhcp/dhcpv6-server.md).

**Flags**

- `I` (invalid): The binding is invalid.
- `X` (disabled): The binding is disabled.
- `R` (radius): The binding was assigned by a RADIUS server.
- `D` (dynamic): The binding is dynamic. Use `make-static` to turn it into a static binding.

**Arguments**

- `address` (alt { prefix: ip6Prefix }): Prefix or address assigned to the client.
- `duid` (string; mandatory): DUID of the client, in hex, for example `0x00030001dc2c6ee7106a`. Together with `iaid`, it identifies the client request the binding answers.
- `iaid` (num; mandatory): Identity association identifier (IAID) of the client request. Together with `duid`, it identifies the binding.
- `ia-type` (enum: na | pd): Type of the binding:
  - `na` - An address binding (IA_NA).
  - `pd` - A prefix delegation binding (IA_PD).
- `server` (enum: all): Name of the DHCPv6 server that can offer this binding, or `all` for every server.
- `life-time` (time): Lifetime of a static binding. Dynamic bindings use the `lease-time` of the server. Default: 1w.
- `prefix-pool` (enum): IPv6 pool the prefix or address of the binding comes from. For addresses, the pool prefix length is 128.
- `dhcp-option` (multi { array-id, option: alt { option: enum , option-set: enum } }): Options (`/ipv6/dhcp-server/option`) to send to this client.
- `rate-limit` (string): Bandwidth limit for the client, in the same format as the `rate-limit` of a DHCP server lease. The server creates a dynamic simple queue for the prefix or address of the binding.
- `allow-dual-stack-queue` (bool): Whether this binding and a DHCP lease of the same client share one dynamic simple queue. Default: yes.
- `address-lists` (multi { array-id, address-list: string }): IPv6 firewall address lists to which the prefix or address of the binding is added. Overrides the `address-lists` setting of the server.
- `insert-queue-before` (enum (first | bottom) { first:0, bottom:0xffffffff }): Where to place the dynamic simple queue created for this binding: `first` (default), `bottom`, or before the named queue.
- `parent-queue` (enum: none): Parent of the dynamic simple queue created for this binding. Default: none.
- `queue-type` (enum): Queue type of the dynamic simple queue created for this binding.

**Read-only arguments**

- `active-server` (enum: none): DHCPv6 server that serves the binding.
- `status` (enum: waiting | offered | bound): State of the binding:
  - `waiting` - A static binding that is not in use, or a dynamic binding that was used before. The server keeps a dynamic binding for 10 minutes so the old client can get it back; after that the prefix can be given to other clients.
  - `offered` - The server answered a Solicit with an Advertise, but has not received the Request. The client has 2 minutes to request the binding.
  - `bound` - The client uses the binding.
- `expires-after` (time): Time until the binding expires.
- `last-seen` (alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe } , time: time }): Time since the server last received a message from the client, or `never`.
- `client-address` (ip6Addr): IPv6 address the client sends from, usually its link-local address. The routes to the binding use it as the gateway.
- `reconfigure-key` (string): Key the server gave the client for authenticating Reconfigure messages (`use-reconfigure`).
- `reconfigure-last-sent` (string): Replay-detection counter of the last Reconfigure message sent to the client. It increases with every Reconfigure message.
- `reconfigure-status` (string)
- `fqdn` (string): FQDN the client sent (option 39).

## Commands

### /ipv6/dhcp-server/binding/make-static

Type: Command

Converts a dynamic binding into a static binding, so the client keeps its prefix or address.

### /ipv6/dhcp-server/binding/send-reconfigure

Type: Command

Sends a Reconfigure message to the client of the binding, which makes the client renew immediately. Requires `use-reconfigure=yes` on the server and a client that accepts Reconfigure messages, for example a RouterOS DHCPv6 client with `allow-reconfigure=yes`.
