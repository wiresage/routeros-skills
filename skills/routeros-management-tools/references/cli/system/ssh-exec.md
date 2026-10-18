# /system/ssh-exec

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ssh-exec

Type: Command

The [`ssh-exec`](../../guides/management-tools/ssh.md#run-remote-commands-from-scripts) command is a non-interactive SSH command, allowing you to execute commands remotely on a device through scripts and scheduler.

**Arguments**

- `address` (alt { ip: ipAddr , ipv6-address: composite { ip6: ip6Addr , interface: [ iface_enum] } }): Remote host IPv4 or IPv6 address.
- `command` (string): Remote command to execute.
- `user` (string): Username for the remote host.
- `password` (string): Password for the remote host. You should use SSH PKI authentication instead of plain text passwords.
- `port` (num): TCP port the SSH server listens on. Default: 22.
- `known-hosts-ignore` (bool): skip host key validation
- `src-address` (alt { ip: ipAddr , ip6: ip6Addr }): Source address to use when connecting. Supports both IPv4 and IPv6.
- `vrf` (enum): VRF to run the command over; the connection is made inside that routing table.
- `output-to-file` (string): Write output to file instead of 'output' variable.

**Read-only arguments**

- `exit-code` (num): Exit code reported by the remote command shell; `0` when the command ran. A connection or authentication failure aborts `ssh-exec` itself instead of returning.
- `output` (string): Returns the output of the remotely executed command.
