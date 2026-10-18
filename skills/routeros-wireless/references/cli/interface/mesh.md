# /interface/mesh

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/mesh

Type: Directory

**Flags**

- `X`: disabled
- `R`: running

**Arguments**

- `name` (string)
- `mtu` (num)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time })
- `auto-mac` (bool)
- `admin-mac` (macAddr)
- `mesh-portal` (bool)
- `hwmp-default-hoplimit` (num)
- `hwmp-preq-waiting-time` (time)
- `hwmp-preq-retries` (num)
- `hwmp-preq-destination-only` (bool)
- `hwmp-preq-reply-and-forward` (bool)
- `hwmp-prep-lifetime` (time)
- `hwmp-rann-interval` (time)
- `hwmp-rann-propagation-delay` (num)
- `hwmp-rann-lifetime` (time)
- `reoptimize-paths` (bool)

**Read-only arguments**

- `mac-address` (macAddr)

## Commands

### /interface/mesh/traceroute

Type: Command

**Arguments**

- `mesh` (iface_enum)
- `address` (macAddr)
- `hoplimit` (num)

**Read-only arguments**

- `address` (macAddr)
- `time` (num)
- `status` (enum: success | ttl-exceeded | no-route | timeout)
