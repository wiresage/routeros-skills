# /interface/l2tp-server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/l2tp-server

Type: Directory

An interface is created for each tunnel that is established to the given server. There are two types of interfaces in the L2TP server's configuration:
- Static interfaces are added administratively if there is a need to reference the particular interface name (in firewall rules or elsewhere) created for the particular user.
- Dynamic interfaces are added to this list automatically whenever a user is connected and its username does not match any existing static entry (or in case the entry is active already, as there cannot be two separate tunnel interfaces referenced by the same name).

Dynamic interfaces appear when a user connects and disappear once the user disconnects, so it is impossible to reference the tunnel created for that user in the router configuration (for example, in the firewall), so if you need persistent rules for that user, create a static entry for him/her. Otherwise, it is safe to use a dynamic configuration.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `D` (dynamic): Whether the server interface was created dynamically.
- `R` (running): Whether the interface is running.

**Arguments**

- `name` (string): Interface name.
- `user` (string; mandatory): User name used for authentication.

**Read-only arguments**

- `mtu` (num): Current MTU of the connection.
- `mru` (num): Current MRU of the connection.
- `client-address` (string): IP address of the connected client.
- `uptime` (time): Connection uptime.
- `encoding` (string): Encryption encoding used.

## Commands

### /interface/l2tp-server/monitor

Type: Command

**Read-only arguments**

- `status` (string): Current connection status.
- `uptime` (time): Connection uptime.
- `user` (string): Authenticated user name.
- `caller-id` (string): Caller ID of the connected client.
- `encoding` (string): Encryption encoding used.
- `mtu` (num): Current MTU of the connection.
- `mru` (num): Current MRU of the connection.
- `local-address` (ipAddr): Local IP address of the connection.
- `remote-address` (ipAddr): Remote IP address of the connection.
- `local-ipv6-address` (ip6Addr): Local IPv6 address of the connection.
- `remote-ipv6-address` (ip6Addr): Remote IPv6 address of the connection.
