# /routing/nexthop

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/nexthop

Type: Directory

**Flags**

- `I`: unresolved
- `R`: reachable

**Read-only arguments**

- `afi` (enum: bad | ip | ipv6 | l2vpn | vpnv4 | vpnv6 | l2vpn-cisco | mip4 | mip6 | link; unset)
- `address` (address (flags=46iv))
- `gw-state` (enum: unreachable | reachable | recursive | inactive)
- `prev-reachable` (bool)
- `scope` (num)
- `target-scope` (num)
- `check-gateway` (enum: none | arp | ping)
- `gw-check-ok` (bool)
- `interface-ok` (bool)
- `bgp-vpn` (bool)
- `hops` (num)
- `routes` (num)
- `immediate-gw.address` (object { address: address (flags=64iv) })
- `immediate-gw.weight` (object { weight: num })
- `immediate-gw.flap-count` (object { flap-count: num })
- `immediate-gw.interface-idx` (object { interface-idx: num })
- `immediate-gw.mpls-peer-id` (object { mpls-peer-id: num })
- `immediate-gw.mpls-label` (object { mpls-label: num })
- `immediate-gw.blackhole` (object { type: bool })
- `links` (object { link-type: enum (output | input) , address: address (flags=46iv/) , route-id: num , fwp-id: num , ok: switch , cost: switch , reach: switch })

## Commands

### /routing/nexthop/dump-dot

Type: Command
