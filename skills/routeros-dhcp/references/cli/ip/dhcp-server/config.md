# /ip/dhcp-server/config

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/config

Type: Settings Directory

Settings shared by all DHCP servers: how often leases are saved, and RADIUS accounting. For details, see [DHCP Server](../../../guides/network-management/dhcp/server.md).

**Arguments**

- `store-leases-disk` (alt { symbolic-names: enum (immediately | never) { immediately:0, never:0xffffffff } , time-interval: time }): How often leases are saved to disk: a time interval, `immediately`, or `never`. Saving less often reduces writes to the flash storage. Default: 5m.
- `accounting` (bool): Whether to send RADIUS accounting for the leases of servers that use RADIUS (`use-radius`). Default: yes.
- `interim-update` (time): Interval of RADIUS interim accounting updates. Default: 0s.
- `radius-password` (alt { user: enum (empty | same-as-user) , password: string }): Password sent in RADIUS Access-Request messages: `empty`, `same-as-user` (the user name, which is the MAC address of the client), or a fixed password. Default: empty.
