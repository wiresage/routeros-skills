# /dude/ros/neighbor

> Source: https://manual.mikrotik.com/docs/cli-reference/dude/ros/neighbor

Package: dude; Type: Directory

**Arguments**

- `device` (enum; mandatory)

**Read-only arguments**

- `interface` (enum)
- `address` (alt { address4: ipAddr , address6: ip6Addr })
- `address4` (ipAddr)
- `address6` (ip6Addr)
- `mac-address` (macAddr)
- `identity` (string)
- `platform` (string)
- `version` (string)
- `unpack` (enum (none | simple | uncompress-headers | uncompress-all) { none:0x00, simple:0x01, uncompress-headers:0x03, uncompress-all:0x07 })
- `age` (time)
- `uptime` (time)
- `software-id` (string)
- `board` (string)
- `ipv6` (bool)
- `interface-name` (string)
