# /dude/ros/route

> Source: https://manual.mikrotik.com/docs/cli-reference/dude/ros/route

Package: dude; Type: Directory

**Flags**

- `X`: disabled
- `A`: active
- `D`: dynamic
- `C`: connect
- `S`: static
- `r`: rip
- `b`: bgp
- `o`: ospf
- `m`: mme
- `B`: blackhole
- `U`: unreachable
- `P`: prohibit

**Arguments**

- `device` (enum; mandatory)
- `dst-address` (ipPrefix)
- `pref-src` (ipAddr)
- `gateway` (object { gw: alt { interface-address: composite { address: ipAddr , interface: enum } , interface: enum , address: super { addr: ipAddr , [table] [ @enum (main)] } } })
- `check-gateway` (enum: arp | ping)
- `type` (enum: unicast | blackhole | unreachable | prohibit)
- `distance` (num)
- `scope` (num)
- `target-scope` (num)
- `routing-mark` (string)
- `vrf-interface` (enum)
- `bgp-as-path` (string)
- `bgp-local-pref` (num)
- `bgp-prepend` (num)
- `bgp-med` (num)
- `bgp-atomic-aggregate` (bool)
- `bgp-origin` (enum: igp | egp | incomplete)
- `bgp-communities` (multi { community: alt { special: enum (no-export | no-advertise | local-as) { no-export:0xFFFFFF01, no-advertise:0xFFFFFF02, local-as:0xFFFFFF03 } , numbers: super { as: num [ .. 0xffff] , [num] :num [ .. 0xffff] } } })
- `route-tag` (num)

**Read-only arguments**

- `gateway-status` (object { nexthop: super { gw: alt { interface: enum , address: ipAddr } , [table] [ on string] , [state] [ enum (unreachable | reachable | recursive | inactive)] , [via] [ via multi { array-id, ip: ipAddr }] , [device] [ multi { array-id, interface: enum }] } })
- `bgp-weight` (num)
- `bgp-ext-communities` (string)
- `received-from` (enum)
- `ospf-metric` (num)
- `ospf-type` (enum: intra-area | inter-area | external-type-1 | external-type-2 | nssa-external-type-1 | nssa-external-type-2)
