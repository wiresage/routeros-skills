# /system/ntp/client/servers

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ntp/client/servers

Type: Directory

NTP servers of the client. Static entries are added here or with `servers` in [`/system/ntp/client`](../client.md); entries learned from DHCP (when the DHCP client has `use-peer-ntp=yes`) are dynamic. See the [NTP](../../../../guides/system-information-and-utilities/ntp.md) guide.

**Flags**

- `X` (disabled): The entry is disabled.
- `D` (dynamic): Dynamic entry, learned from DHCP. Dynamic entries cannot be edited.

**Arguments**

- `address` (address (flags=46D); mandatory): IP address or domain name of the NTP server. IPv4 and IPv6 addresses can carry a `@vrf` suffix, and a link-local IPv6 address an `%interface` suffix. Domain names are resolved with `/ip/dns`; the result shows in `resolved-address`.
- `min-poll` (num): Shortest interval between queries to this server, as the power of 2 in seconds (6 means every 64 s). Must be lower than `max-poll`. Range: 3..17. Default: 6.
- `max-poll` (num): Longest interval between queries to this server, as the power of 2 in seconds (10 means every 1024 s). Range: 3..17. Default: 10.
- `iburst` (bool): When enabled, the client sends a burst of about a second interval queries right after the server is added, to get an initial estimate quickly. Default: yes.
- `auth-key` (enum: none): Key from [`/system/ntp/key`](../key.md) used to authenticate replies from this server. Replies that fail authentication are rejected (crypto NAK) and the client does not synchronize. Default: none.

**Read-only arguments**

- `resolved-address` (address (flags=46)): IP address that the domain name in `address` resolved to.
