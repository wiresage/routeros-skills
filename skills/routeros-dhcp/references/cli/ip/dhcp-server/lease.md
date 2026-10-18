# /ip/dhcp-server/lease

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/lease

Type: Directory

Leases of the DHCP servers. Dynamic leases are created when clients get an address from a pool; static leases give a specific client a fixed address, a pool, or its own settings. For details, see [DHCP Server](../../../guides/network-management/dhcp/server.md).

**Flags**

- `X` (disabled): The lease is disabled.
- `R` (radius): The lease was assigned by a RADIUS server.
- `D` (dynamic): The lease is dynamic: it was created when a client got an address from the pool. Use `make-static` to turn it into a static lease.
- `B` (blocked): The client is blocked (`block-access=yes`) and gets no reply from the server.

**Arguments**

- `address` (alt { ip-address: ipAddr , pool: enum }): IP address of a static lease, or the name of an IP pool to give the client an address from. With `0.0.0.0`, the address pool of the server is used.
- `mac-address` (macAddr): MAC address of the client the static lease is for.
- `use-src-mac` (bool): Whether to identify the client by the source MAC address of its packets instead of the client hardware address field (`chaddr`) of the DHCP message.
- `client-id` (string): Client identifier (option 61) of the client the static lease is for, in the format shown in `active-client-id`, for example `1:4e:97:a1:4c:d1:38`.
- `rate-limit` (string): Bandwidth limit for the client, as `rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]]`. Rates are in bits per second, with an optional `k` or `M` suffix, and missing tx values are taken from the rx values. Only static leases can have a rate limit.

  The server creates a dynamic simple queue named `dhcp-ds<hostname/MAC>` for the address of the lease, with this limit as `limit-at` and `max-limit`.
- `routes` (object { route: composite { dst-address: address (flags=4/) , gateway: [ composite { gateway: address (flags=46ivL) , distance: [ num [1 .. 255]] }] } }): Routes the server adds while the lease is bound, as `dst-address/mask gateway distance` entries separated by commas, for example `10.77.0.0/24 172.31.255.105 5`.
- `insert-queue-before` (enum (bottom | first) { bottom:0xffffffff, first:0 }): Where to place the dynamic simple queue created for this lease: `first` (default) at the top of `/queue/simple`, `bottom` at the end, or before the named queue.
- `parent-queue` (enum: none): Parent of the dynamic simple queue created for this lease. Default: none.
- `queue-type` (enum): Queue type of the dynamic simple queue created for this lease.
- `address-lists` (multi { array-id, address-list: string }): Firewall address lists to which the address of the lease is added while the lease is bound.
- `server` (enum: all): DHCP server the lease belongs to. With `all`, the static lease is valid on every server.
- `block-access` (bool): Whether to block the client: the server does not answer it, and the lease gets the `B` flag. Default: no.
- `allow-dual-stack-queue` (bool): Whether this lease and a DHCPv6 binding of the same client share one dynamic simple queue, which then contains both the IPv4 and the IPv6 address. Default: yes.
- `lease-time` (time): Lease time for this client. When not set, or set to `0s`, the `lease-time` of the server is used.
- `always-broadcast` (bool): Whether to broadcast replies to this client even when it has not set the broadcast flag. Default: no.
- `dhcp-option` (multi { array-id, option: enum }): Options (`/ip/dhcp-server/option`) to send to this client. They take precedence over the options of the server and of the network.
- `dhcp-option-set` (enum: none): Option set (`/ip/dhcp-server/option/sets`) to send to this client. It takes precedence over the options of the server and of the network.
- `agent-circuit-id` (string): When set, the lease matches requests whose relay agent information (option 82) contains this circuit ID, even if the MAC address or client ID differ.
- `agent-remote-id` (string): When set, the lease matches requests whose relay agent information (option 82) contains this remote ID, even if the MAC address or client ID differ.

**Read-only arguments**

- `status` (enum: waiting | testing | declined | offered | bound | authorizing | conflict): State of the lease:
  - `waiting` - A static lease that is not in use.
  - `testing` - The server is checking the address for conflicts (`conflict-detection`).
  - `offered` - The server offered the address and waits for the client's request.
  - `bound` - The client uses the address.
  - `authorizing` - The server waits for the reply from the RADIUS server.
  - `conflict` - Another host already uses the address. The lease keeps the address out of use for the lease time; `check-status` frees it when the other host no longer answers.
  - `declined` - The client declined the address with a DHCPDECLINE message.
- `expires-after` (time): Time until the lease expires.
- `last-seen` (alt { symbolic-names: enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe } , time: time }): Time since the server last received a request from the client, or `never`.
- `age` (time): Time since the lease was created.
- `active-address` (ipAddr): IP address the client uses.
- `active-mac-address` (macAddr): MAC address of the client that uses the lease.
- `active-client-id` (string): Client identifier (option 61) of the client that uses the lease.
- `active-server` (enum): DHCP server that serves the client.
- `active-agent-circuit-id` (string): Circuit ID from the relay agent information (option 82) of the client's request, in hex.
- `active-agent-remote-id` (string): Remote ID from the relay agent information (option 82) of the client's request, in hex.
- `active-agent-circuit-id-ascii` (string): Circuit ID from the relay agent information (option 82) of the client's request, as text.
- `active-agent-remote-id-ascii` (string): Remote ID from the relay agent information (option 82) of the client's request, as text.
- `host-name` (string): Host name the client sent (option 12).
- `class-id` (string): DHCP option 60 from last received DHCP request
- `src-mac-address` (macAddr): Source MAC address of the client's last request.
- `reconfigure-key` (string): Key the server gave the client, in its reply when the client bound, for authenticating Reconfigure messages (RFC 6704, HMAC-MD5). Requires `use-reconfigure` on the server.
- `reconfigure-last-sent` (string): Replay-detection counter of the last Reconfigure message sent to the client. It increases with every Reconfigure message.
- `reconfigure-status` (string)

## Commands

### /ip/dhcp-server/lease/check-status

Type: Command

Checks a lease that is in the `conflict` or `declined` status again, and frees the address when no other host answers for it any more.

### /ip/dhcp-server/lease/make-static

Type: Command

Converts a dynamic lease into a static lease, so the client keeps its address.

### /ip/dhcp-server/lease/send-reconfigure

Type: Command

Sends a Reconfigure (FORCERENEW) message to the client of the lease, which makes the client renew its lease immediately. It works only for clients that got a reconfigure key, which requires `use-reconfigure=yes` on the server and a client that asks for the key, for example a RouterOS DHCP client with `allow-reconfigure=yes`.
