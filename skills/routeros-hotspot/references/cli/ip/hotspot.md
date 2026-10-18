# /ip/hotspot

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `S`: HTTPS

**Arguments**

- `name` (string)
- `interface` (alt { interface: iface_enum , interface: iface_enum }; mandatory)
- `address-pool` (enum: none)
- `profile` (enum)
- `idle-timeout` (alt { symbolic-names: enum (none) , time-interval: time })
- `keepalive-timeout` (alt { symbolic-names: enum (none) , time-interval: time })
- `login-timeout` (alt { symbolic-names: enum (none) , time-interval: time })
- `addresses-per-mac` (enum: unlimited)

**Read-only arguments**

- `ip-of-dns-name` (ipAddr)
- `proxy-status` (string)

## Commands

### /ip/hotspot/reset-html

Type: Command

### /ip/hotspot/setup

Type: Command

**Read-only arguments**

- `interface` (alt { interface1: iface_enum , interface2: iface_enum })
- `address` (composite { address: ipAddr , netmask: num })
- `masq` (bool)
- `pool` (multi { range: composite { min: ipAddr , max: ipAddr } })
- `ssl-cert` (enum (import-other-certificate | none) { import-other-certificate:0, none:0xffffffff })
- `passphrase` (string)
- `smtp-server` (ipAddr)
- `use-dnscache` (bool)
- `dns-server` (multi { address: ipAddr })
- `dns-name` (string)
- `username` (string)
- `password` (string)
