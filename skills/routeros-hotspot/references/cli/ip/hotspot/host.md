# /ip/hotspot/host

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/hotspot/host

Type: Directory

**Flags**

- `S`: static
- `H`: DHCP
- `D`: dynamic
- `A`: authorized
- `P`: bypassed

**Read-only arguments**

- `mac-address` (macAddr)
- `address` (ipAddr)
- `to-address` (ipAddr)
- `server` (enum)
- `uptime` (time)
- `idle-time` (time)
- `idle-timeout` (time)
- `keepalive-timeout` (time)
- `host-dead-time` (time)
- `bridge-port` (iface_enum)
- `vlan-id` (num)
- `http-proxy` (composite { address: ipAddr , port: num })
- `bytes-in` (num)
- `bytes-out` (num)
- `packets-in` (num)
- `packets-out` (num)
- `found-by` (string)

## Commands

### /ip/hotspot/host/make-binding

Type: Command

**Arguments**

- `comment` (string)
- `type` (enum: regular | bypassed | blocked)
