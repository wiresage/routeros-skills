# /ip/dhcp-server/alert

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/alert

Type: Directory

Detects unknown (rogue) DHCP servers on an interface. The alert sends its own DHCPDISCOVER about once a minute, and checks the source of every DHCP reply it sees against `valid-server`. An unknown server is logged with the `dhcp,critical` topics, listed in `unknown-server`, and triggers `on-alert`. Because the alert sends DHCP requests itself, do not use it on an interface where the router runs a DHCP client. For details, see [DHCP Server](../../../guides/network-management/dhcp/server.md).

**Flags**

- `X` (disabled): The alert is disabled. New alerts are created disabled.
- `I` (invalid): The alert configuration is invalid.

**Arguments**

- `interface` (iface_enum; mandatory): Interface to watch for DHCP servers.
- `valid-server` (multi { mac-address: macAddr }): MAC addresses of the DHCP servers that are allowed on the interface. Replies from other servers raise an alert.
- `on-alert` (alt { script: string }): Script to run when an unknown DHCP server is detected.
- `alert-timeout` (alt { symbolic-names: enum (none) , time-interval: time }): Time after which a detected server is forgotten. If the server is still present afterwards, a new alert is raised. With `none`, detected servers are never forgotten. Default: 1h.

**Read-only arguments**

- `unknown-server` (multi { mac-address: macAddr }): MAC addresses of the unknown DHCP servers that were detected.

## Commands

### /ip/dhcp-server/alert/reset-alert

Type: Command

Clears the unknown servers detected by an alert, so they are reported again when they reply.
