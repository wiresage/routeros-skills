# /system/package/local-update/update-package-source

> Source: https://manual.mikrotik.com/docs/cli-reference/system/package/local-update/update-package-source

Type: Directory

The server from which to get the package is defined in this list.

**Arguments**

- `address` (alt { ipv6: ip6Addr , ip: ipAddr }; mandatory): IP address of the local package server.
- `user` (string; mandatory): Username for accessing the local package server.
- `password` (string; mandatory): Password for accessing the local package server.
