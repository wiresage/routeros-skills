# /interface/ovpn-server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ovpn-server

Type: Directory

An interface is created for each tunnel established to the specified server. There are two types of interfaces in the OVPN server configuration:

- Static interfaces are added administratively when you need to reference a specific interface name (for example, in firewall rules or elsewhere) created for a particular user.
- Dynamic interfaces are added to this list automatically when a user connects and their username does not match any existing static entry, or if the matching static entry is already active, since two separate tunnel interfaces cannot use the same name.

Dynamic interfaces appear when a user connects and disappear when the user disconnects. Therefore, it is not possible to reference the tunnel created for that user in router configuration (for example, in firewall rules). If persistent rules are required for a user, create a static entry. Otherwise, dynamic configuration is sufficient.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `D` (dynamic): Whether the server interface was created dynamically.
- `R` (running): Whether the interface is running.
- `H` (hw-crypto): Whether hardware encryption is active.

**Arguments**

- `name` (string): Interface name.
- `user` (string; mandatory): User name used for authentication.

**Read-only arguments**

- `mtu` (num): Current MTU of the connection.
- `client-address` (string): IP address of the connected client.
- `uptime` (time): Connection uptime.
- `encoding` (string): Encryption encoding used.

## Commands

### /interface/ovpn-server/monitor

Type: Command

**Read-only arguments**

- `status` (string): Current connection status.
- `uptime` (time): Connection uptime.
- `user` (string): Authenticated user name.
- `caller-id` (string): Caller ID of the connected client.
- `encoding` (string): Encryption encoding used.
- `mtu` (num): Current MTU of the connection.
- `local-address` (ipAddr): Local IP address of the connection.
- `remote-address` (ipAddr): Remote IP address of the connection.
