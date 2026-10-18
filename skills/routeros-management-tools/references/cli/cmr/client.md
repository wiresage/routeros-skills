# /cmr/client

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/client

Conditions: !smips, !powerpc; Type: Settings Directory

For an overview of the CMR-client and its usage, see the [CMR-Client](../../guides/management-tools/cmr/client.md) documentation.

**Arguments**

- `enabled` (enum: yes | no): Whether CMR client is enabled or not. Default: no.
- `peer-id` (string; unset): Unique CMR specific device identifier, of the CMR server.
- `local-id` (string; unset): Unique CMR specific device identifier.
- `pairing-requirement` (enum: none | password; unset): Defines what the remote device must do before this device accepts the pairing:
  - **none** - this device accepts pairing automatically, without additional checks
  - **password** (default) - the remote device may approve pairing by giving the username and password of a RouterOS user on this device; CMR has no separate pairing password
- `controller-addresses` (multi { array-id, address: address (flags=46D) }; unset): Specifies the controller IP addresses to use. This setting is optional when the client can discover the controller automatically through neighbor discovery or DNS (`_cmr._tcp.lan`, or `_cmr._tcp.` followed by the domain name from DHCP), but must be configured when the controller address cannot be determined automatically.

**Read-only arguments**

- `status` (string): Current CMR-client status.
- `controller-identity` (string): CMR server identity.
- `controller-address` (address): CMR server IP address.
- `pairing-status` (multi { array-id, status: string }): Current pairing status.
- `saved-addresses` (multi { array-id, address: address (flags=46) }): List of CMR server's discovered IP addresses.

## Commands

### /cmr/client/forget

Conditions: !smips, !powerpc; Type: Command

Forget device pairing and disconnect device from CMR server.

### /cmr/client/pair

Conditions: !smips, !powerpc; Type: Command

Initiate pairing process to CMR server.

**Arguments**

- `username` (string; unset): CMR server username.
- `password` (string; unset): CMR server password.

**Read-only arguments**

- `address` (address (flags=46)): CMR server IP address.
- `status` (string): Pairing status.

### /cmr/client/push-button

Type: Command

Using this command device pairing can be performed using physical routerboard/reset button on the client device.

**Arguments**

- `interface` (multi { array-id, interface: iface_enum }; unset): Select inteface or interface list on which to search for CMR server. (default value: **all**)

**Read-only arguments**

- `state` (string): State of device pairing.
- `error` (string; unset): Error information, in case pairing is unsuccessfull.
- `peer` (multi { array-id, mac: macAddr }; unset): CMR server address.
- `peer-id` (string; unset): CMR server ID.
