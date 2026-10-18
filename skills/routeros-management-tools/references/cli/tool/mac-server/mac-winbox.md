# /tool/mac-server/mac-winbox

> Source: https://manual.mikrotik.com/docs/cli-reference/tool/mac-server/mac-winbox

Type: Settings Directory

MAC WinBox server settings: on which interfaces WinBox can connect to the router by its MAC address. MAC Telnet has its own setting in [`/tool/mac-server`](../mac-server.md). For examples, see [MAC server](../../../guides/management-tools/mac-server.md).

**Arguments**

- `allowed-interface-list` (enum): Interface list on which the router accepts MAC WinBox connections, set the same way as for MAC Telnet in [`/tool/mac-server`](../mac-server.md): put the bridge in the list, not its ports. `none` turns MAC WinBox off. The default configuration sets `LAN`. Default: all.
