# /system/ssh

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ssh

Type: Command

[SSH client](../../guides/management-tools/ssh.md#ssh-client) to connect to remote hosts.

**Arguments**

- `address` (alt { ip: ipAddr , ipv6-address: composite { ip6: ip6Addr , interface: [ iface_enum] } }): Remote host IPv4 or IPv6 address.
- `command` (string): Remote command to execute.
- `user` (string): Username for the remote host. Defaults to the currently logged-in user.
- `port` (num): TCP port the SSH server listens on. Default: 22.
- `src-address` (alt { ip: ipAddr , ip6: ip6Addr }): Source address to use when connecting. Supports both IPv4 and IPv6.
- `vrf` (enum): VRF to make the connection in. Matches the remote host only inside that routing table.
- `output-to-file` (string): Write output to file instead of terminal. Does not accept password input, use key authentication.
