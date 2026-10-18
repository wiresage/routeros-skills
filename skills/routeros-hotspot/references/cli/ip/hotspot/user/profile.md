# /ip/hotspot/user/profile

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/user/profile

Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string)
- `address-pool` (enum: none)
- `session-timeout` (time)
- `idle-timeout` (super { idle-timeout: alt { symbolic-names: enum (none) , time-interval: time } })
- `keepalive-timeout` (super { keepalive-timeout: alt { symbolic-names: enum (none) , time-interval: time } })
- `status-autorefresh` (alt { symbolic-names: enum (none) , time-interval: time })
- `shared-users` (enum: unlimited)
- `add-mac-cookie` (bool)
- `mac-cookie-timeout` (time)
- `rate-limit` (string)
- `insert-queue-before` (super { queue: enum (bottom | first) { bottom:0xffffffff, first:0 } })
- `parent-queue` (super { queue: enum (none) })
- `queue-type` (super { queue: enum })
- `address-list` (multi { address-list: string })
- `incoming-filter` (string)
- `outgoing-filter` (string)
- `incoming-packet-mark` (string)
- `outgoing-packet-mark` (string)
- `on-login` (alt { script: string })
- `on-logout` (alt { script: string })
- `transparent-proxy` (bool)
- `open-status-page` (enum: http-login | always)
- `advertise` (bool)
- `advertise-url` (multi { url: string })
- `advertise-interval` (multi { time-interval: time })
- `advertise-timeout` (alt { symbolic-names: enum (immediately | never) { immediately:0, never:0xffffffff } , time-interval: time })
