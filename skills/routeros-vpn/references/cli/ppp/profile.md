# /ppp/profile

> Source: https://manual.mikrotik.com/docs/cli-reference/ppp/profile

Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string; mandatory)
- `local-address` (alt { pool: enum , address: ipAddr })
- `remote-address` (alt { pool: enum , address: ipAddr })
- `remote-ipv6-prefix-pool` (enum)
- `remote-ipv6-prefix-reuse` (bool)
- `dhcpv6-pd-pool` (enum)
- `dhcpv6-use-radius` (bool)
- `dhcpv6-lease-time` (time)
- `bridge` (iface_enum)
- `bridge-port-priority` (num)
- `bridge-path-cost` (num)
- `bridge-horizon` (num)
- `bridge-learning` (enum (default | no | yes) { default:0xffffffff, no:0, yes:1 })
- `bridge-port-vid` (num)
- `bridge-port-trusted` (bool)
- `session-timeout` (time)
- `idle-timeout` (time)
- `use-ipv6` (enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 })
- `use-mpls` (enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 })
- `use-compression` (enum (default | no | yes) { default:0xffffffff, no:0, yes:1 })
- `use-encryption` (enum (default | no | yes | required) { default:0xffffffff, no:0, yes:1, required:2 })
- `only-one` (enum (default | no | yes) { default:0xffffffff, no:0, yes:1 })
- `change-tcp-mss` (enum (default | no | yes) { default:0xffffffff, no:0, yes:1 })
- `use-upnp` (enum (default | no | yes) { default:0xffffffff, no:0, yes:1 })
- `rate-limit` (string)
- `insert-queue-before` (enum (bottom | first) { bottom:0xffffffff, first:0 })
- `parent-queue` (enum: none)
- `queue-type` (composite { upload-queue: enum , download-queue: enum })
- `incoming-filter` (enum)
- `outgoing-filter` (enum)
- `address-list` (multi { address-list: enum })
- `interface-list` (enum)
- `dns-server` (multi { address: ipAddr })
- `wins-server` (multi { address: ipAddr })
- `on-up` (alt { script: string })
- `on-down` (alt { script: string })
