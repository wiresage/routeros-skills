# /interface/sstp-server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/sstp-server

Type: Directory

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

### /interface/sstp-server/monitor

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
- `local-ipv6-address` (ip6Addr): Local IPv6 address of the connection.
- `remote-ipv6-address` (ip6Addr): Remote IPv6 address of the connection.
