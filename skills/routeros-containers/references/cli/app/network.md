# /app/network

> Source: https://manual.mikrotik.com/docs/cli-reference/app/network

Syscap: app; Package: container; Type: Directory

**Flags**

- `e`: external
- `I`: invalid

**Arguments**

- `name` (string)
- `allow-outgoing-access` (bool)

**Read-only arguments**

- `network` (ipAddr)
- `ip` (ipAddr)
- `status` (string)
- `used-ips` (multi { array-id, array-id, ip-and-name: composite { ip: ipAddr , name: string } })
- `bridge-interface` (iface_enum { none })
- `cmds` (multi { cmd: string })
