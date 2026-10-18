# /ip/dhcp-client

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-client

Type: Directory

The DHCP client gets an IPv4 address and network settings for an interface from a DHCP server. For an overview and configuration examples, see [DHCP Client](../../guides/network-management/dhcp/client.md). For how DHCP works, see [DHCP](../../guides/network-management/dhcp.md).

**Flags**

- `X` (disabled): The DHCP client is disabled.
- `I` (invalid): The DHCP client configuration is invalid.
- `D` (dynamic): The DHCP client was created dynamically.

**Arguments**

- `name` (string): Name of the DHCP client. If not set, RouterOS generates a name, for example `client1`.
- `interface` (iface_enum; mandatory): Interface the DHCP client runs on. The received IP address is added to this interface as a dynamic address.
- `add-default-route` (enum: no | yes | special-classless): Which routes received from the DHCP server to add to the routing table.
  - `yes` (default) - Add the classless static routes (option 121) when the server sends them, otherwise a default route through the received gateway (option 3). When option 121 is present, the gateway from option 3 is ignored.
  - `special-classless` - Add both the classless static routes and a default route through the received gateway.
  - `no` - Do not add routes.
- `default-route-distance` (num): Distance of the routes the client adds. Default: 1.
- `default-route-tables` (object { table: alt { table-distance: composite { table: alt { table-default: enum (default) { default:0xffffffff } , table: enum } , distance: num [1 .. 255] } , table: alt { table-default: enum (default) { default:0xffffffff } , table: enum } } }): Routing tables to add the routes to, as `table` or `table:distance` entries. A distance given here overrides `default-route-distance` for that table. `default` is the main routing table, or the VRF routing table when the client interface belongs to a VRF. Default: default.
- `check-gateway` (enum: none | arp | ping | bfd): Gateway check set on the routes the client adds (`none`, `arp`, `ping` or `bfd`), so a route is only used while its gateway responds. See [gateway reachability](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/routing-decision). Default: none.
- `use-peer-dns` (bool): Whether to use the DNS servers received from the DHCP server. They are added to the dynamic servers of the DNS resolver (`/ip/dns`). Default: yes.
- `use-peer-ntp` (bool): Whether to use the NTP servers received from the DHCP server. They are added as dynamic entries to the NTP client servers (`/system/ntp/client/servers`). Default: yes.
- `allow-reconfigure` (bool): Whether to accept Reconfigure (FORCERENEW) messages from the DHCP server. When enabled, the client asks for a reconfigure key when it binds, and the server sends the key in its reply. The key authenticates the server's Reconfigure messages (RFC 6704, HMAC-MD5). On a Reconfigure message, the client renews its lease immediately. The server can only send Reconfigure messages to clients that bound with this setting enabled. Default: no.
- `vlan-priority` (num): Priority Code Point (PCP, 0-7) set in the VLAN header of the packets the client sends. Applies only when the client runs on a VLAN interface.
- `dscp` (num): DSCP value (0-63) set in the IP header of the packets the client sends. When not set, packets are sent with DSCP 0.
- `use-broadcast` (enum: always | never | both): Whether the client sets the broadcast flag in DHCPDISCOVER and DHCPREQUEST messages, which asks the server to broadcast its replies. Renewal requests are sent as unicast and never set the flag.
  - `both` (default) - Set the flag during the first 15 seconds of getting an address, then continue without it.
  - `always` - Always set the flag.
  - `never` - Never set the flag.
- `dhcp-options` (multi { array-id, option: enum }): Options the client sends to the DHCP server, selected by name from `/ip/dhcp-client/option`. The predefined `clientid` and `clientid_duid` options both use code 61: `clientid` identifies the client by the MAC address of its interface, `clientid_duid` by the router's DUID (RFC 4361), the same DUID the DHCPv6 client uses. Default: hostname,clientid.
- `script` (alt { script: string }): Script to run when the client gets a lease and when it loses or releases it. The script receives these variables:
  - `bound` - `1` when a lease was obtained, `0` when it was lost or released.
  - `server-address` - IP address of the DHCP server.
  - `lease-address` - IP address from the lease.
  - `interface` - Name of the client interface.
  - `gateway-address` - Gateway received from the server.
  - `vendor-specific` - Value of the vendor-specific information option (option 43) received from the server.
  - `lease-options` - Array of the options received from the server, indexed by option code. Values of binary options are hex strings.

**Read-only arguments**

- `custom-source-mac-address` (macAddr): Custom source MAC address used by the DHCP client.
- `custom-hostname-suffix` (string): Suffix appended to the hostname sent to the DHCP server.
- `status` (enum: stopped | searching... | requesting... | bound | renewing... | rebinding... | error): Current state of the client:
  - `searching...` - Sending DHCPDISCOVER messages and waiting for an offer.
  - `requesting...` - Requesting an offered address.
  - `bound` - The client has a lease.
  - `renewing...` - Renewing the lease with the server that issued it, from half of the lease time.
  - `rebinding...` - The server did not answer the renewal. Requesting the lease from any server, from 87.5% of the lease time.
  - `stopped` - The client is disabled.
  - `error` - The client cannot run.
- `address` (composite { address: ipAddr , netmask: num [ .. 32] }): IP address and prefix length received from the DHCP server.
- `netmask` (ipAddr): Subnet mask received from the DHCP server.
- `gateway` (ipAddr): Gateway received from the DHCP server (option 3).
- `dhcp-server` (ipAddr): IP address of the DHCP server that issued the lease.
- `primary-dns` (ipAddr): First DNS server received from the DHCP server.
- `secondary-dns` (ipAddr): Second DNS server received from the DHCP server.
- `primary-ntp` (ipAddr): First NTP server received from the DHCP server.
- `secondary-ntp` (ipAddr): Second NTP server received from the DHCP server.
- `cmr-address` (ipAddr)
- `caps-managers` (multi { ip: ipAddr }): CAPsMAN addresses received from the DHCP server (option 138).
- `reconfigure-key` (string): Key received from the DHCP server to authenticate its Reconfigure messages (RFC 6704, HMAC-MD5). Set only when `allow-reconfigure` is enabled.
- `reconfigure-last-counter` (string): Replay-detection counter of the last Reconfigure message accepted from the DHCP server. It starts at 0 when the client binds and increases with every Reconfigure message.
- `expires-after` (time): Time until the lease expires.

## Commands

### /ip/dhcp-client/release

Type: Command

Releases the current lease. The client sends a DHCPRELEASE message to the DHCP server, gives up the address and starts requesting a new lease.

### /ip/dhcp-client/renew

Type: Command

Renews the current lease immediately, without waiting for half of the lease time. If the server does not answer, the client continues with rebinding and keeps its address until the lease expires.
