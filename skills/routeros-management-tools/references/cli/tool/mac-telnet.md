# /tool/mac-telnet

> Source: https://manual.mikrotik.com/docs/cli-reference/tool/mac-telnet

Type: Command

Opens a MAC Telnet session to a device on the same layer-2 segment, by its MAC address. The client asks for a user name and password. When the device does not answer or refuses the connection, the command returns to the prompt without an error message. For examples, see [MAC server](../../guides/management-tools/mac-server.md).

**Arguments**

- `host` (enum): MAC address of the device to connect to.
- `interface` (iface_enum; unset): Interface to send the connection attempts out of. Without it, the client sends them out of every interface.
