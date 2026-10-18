# /ip/dhcp-relay

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-relay

Type: Directory

The DHCP relay forwards DHCP requests from clients on its interface to DHCP servers in other networks, and delivers the replies back to the clients. New relays are created disabled; enable them after adding. For an overview and examples, see [DHCP Relay](../../guides/network-management/dhcp/relay.md).

**Flags**

- `X` (disabled): The relay is disabled. New relays are created disabled.
- `I` (invalid): The relay configuration is invalid.

**Arguments**

- `name` (string): Name of the relay.
- `interface` (iface_enum; mandatory): Interface on which the relay listens for DHCP requests from clients.
- `dhcp-server-vrf` (enum): VRF in which the DHCP servers are reached. When it differs from the VRF of `interface`, the replies of the server, which are sent to `local-address`, must be brought into this VRF, for example with a dst-nat rule. Default: main.
- `dhcp-server` (multi { address: ipAddr }; mandatory): DHCP servers to forward requests to. The relay forwards every request to all of them.
- `delay-threshold` (alt { const: enum (none) , time: time }): Minimum value of the seconds-elapsed field (`secs`) a request must have to be forwarded, so the relay forwards only clients that have been trying for that long. With `none`, all requests are forwarded. Default: none.
- `local-address` (ipAddr): Address the relay writes into the gateway address field (`giaddr`) of forwarded requests. The DHCP server sends its replies to this address and selects the server by its `relay` property. With `0.0.0.0`, an address of `interface` is used. Default: 0.0.0.0.
- `add-relay-info` (bool): Whether to add relay agent information (option 82) to forwarded requests. The circuit ID is the MAC address of `interface`, and the remote ID is the MAC address of the client, or `relay-info-remote-id` when it is set. Default: no.
- `relay-info-remote-id` (string): Text to send as the remote ID in option 82 instead of the MAC address of the client. Used only with `add-relay-info=yes`.
- `local-address-as-src-ip` (bool): Whether to send forwarded requests from `local-address` instead of from the address of the interface towards the server. Default: no.

## Commands

### /ip/dhcp-relay/monitor

Type: Command

Shows the counters of a DHCP relay.

**Read-only arguments**

- `requests` (num): Number of client requests the relay forwarded to the servers.
- `responses` (num): Number of server replies the relay delivered to clients.

### /ip/dhcp-relay/reset-counters

Type: Command

Resets the request and response counters of all DHCP relays.
