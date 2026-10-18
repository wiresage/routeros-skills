# /interface/pppoe-server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/pppoe-server

Type: Directory

There are two types of interface (tunnel) items in PPPoE server configuration - static users and dynamic connections. An interface is created for each tunnel established to the given server. Static interfaces are added administratively if there is a need to reference the particular interface name (in firewall rules or elsewhere) created for the particular user. Dynamic interfaces are added to this list automatically whenever a user is connected and the user's username does not match any existing static entry (or in case the entry is active already, as there can not be two separate tunnel interfaces referenced by the same name - set the *one-session-per-host* value if this is a problem). Dynamic interfaces appear when a user connects and disappear once the user disconnects, so it is impossible to reference the tunnel created for that user in the router configuration (for example, in firewall), so if you need a persistent rule for that user, create a static entry for him/her. Otherwise, it is safe to use a dynamic configuration.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `D` (dynamic): Whether the server interface was created dynamically.
- `R` (running): Whether the interface is running.

**Arguments**

- `name` (string): Interface name.
- `user` (string; mandatory): Username used for authentication.
- `service` (string; mandatory): PPPoE service name.

**Read-only arguments**

- `mtu` (num): Current MTU of the connection.
- `mru` (num): Current MRU of the connection.
- `remote-address` (string): Remote IP address of the connection.
- `encoding` (string): Encryption encoding used.
- `uptime` (time): Connection uptime.
- `interface` (iface_enum): Interface the client is connected through.
- `vid` (num): VLAN ID of the connection.

## Commands

### /interface/pppoe-server/monitor

Type: Command

**Read-only arguments**

- `status` (string): Current connection status.
- `uptime` (time): Connection uptime.
- `user` (string): Authenticated user name.
- `caller-id` (string): Caller ID of the connected client.
- `encoding` (string): Encryption encoding used.
- `service` (string): PPPoE service name.
- `interface` (iface_enum): Interface the client is connected through.
- `mtu` (num): Current MTU of the connection.
- `mru` (num): Current MRU of the connection.
- `local-address` (ipAddr): Local IP address of the connection.
- `remote-address` (ipAddr): Remote IP address of the connection.
- `local-ipv6-address` (ip6Addr): Local IPv6 address of the connection.
- `remote-ipv6-address` (ip6Addr): Remote IPv6 address of the connection.
