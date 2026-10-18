# /routing/route

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/route

Type: Directory

A read-only table that lists routes from all the address families as well as all filtered routes with all possible route attributes.

Default example output of the table with various route types:

```ros
[admin@MikroTik] /routing/route> print
Flags: A - ACTIVE; c, s, a, l, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
    DST-ADDRESS                 GATEWAY           AFI    D  SCOPE  TA  IMMEDIATE-GW
 lH 10.0.0.0/8                                    ip     0
;;; defconf
As  10.0.0.0/8                  10.155.130.1      ip     1     30  10  10.155.130.1%ether1
 lH 10.155.130.0/25                               ip     0
Ac  10.155.130.0/25             ether1            ip     0     10      ether1
 aH 10.155.130.12/32                              ip     0
 lH 111.13.0.0/24                                 ip     0
Ac  111.13.0.0/24               ether2            ip     0     10      ether2
 aH 111.13.0.1/32                                 ip     0
Ac  111.111.111.2/32            loopback@vrfTest  ip     0     10      loopback
Ac  2111:4::/64                 ether2            ipv6   0     10      ether2
Ac  fe80::%ether1/64            ether1            ipv6   0     10      ether1
Ac  fe80::%ether2/64            ether2            ipv6   0     10      ether2
Ac  fe80::%ether3/64            ether3            ipv6   0     10      ether3
Ac  fe80::%ether4/64            ether4            ipv6   0     10      ether4
Ac  3333::2/128                 loopback@vrfTest  ipv6   0     10      loopback
Ac  fe80::%loopback/64          loopback@vrfTest  ipv6   0     10      loopback
Ay  111.111.111.2/32&65530:100  loopback@vrfTest  vpnv4  0     10   5  loopback
Ay  3333::2/128&65530:100       loopback@vrfTest  vpnv6  0     10   5  loopback
A H ether1                                        link   0
A H ether2                                        link   0
A H ether3                                        link   0
A H ether4                                        link   0
A H loopback                                      link   0
```

Detailed example output with some BGP, OSPF, and other routes:

```ros
[admin@MikroTik] /routing/route> print detail
Flags: X - disabled, F - filtered, U - unreachable, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - ldp-mapping, y - copy; H - hw-offloaded;
+ - ecmp, B - blackhole
  o   afi=ip4 contribution=best-candidate dst-address=0.0.0.0/0 routing-table=main gateway=10.155.101.1%ether1 immediate-gw=10.155.101.1%ether1
       distance=110 scope=20 target-scope=10 belongs-to="OSPF route"
       ospf.metric=2 .tag=111 .type=ext-type-1
       debug.fwp-ptr=0x203425A0

 Ad + afi=ip4 contribution=active dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1
       distance=1 scope=30 target-scope=10 vrf-interface=ether1 belongs-to="DHCP route"
       debug.fwp-ptr=0x20342060

 As + afi=ip4 contribution=active dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1
       distance=1 scope=30 target-scope=10 belongs-to="Static route"
       debug.fwp-ptr=0x20342060

 Fb   afi=ip4 contribution=filtered dst-address=1.0.0.0/24 routing-table=main gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1 distance=20
       scope=40 target-scope=10 belongs-to="BGP IP routes from 10.155.101.217" rpki=valid
       bgp.peer-cache-id=*B000002 .aggregator="13335:172.68.180.1" .as-path="65530,100,9002,13335" .atomic-aggregate=yes .origin=igp
       debug.fwp-ptr=0x20342960

```

**Flags**

- `X`: disabled
- `F` (filtered): A flag indicates whether the route was filtered by routing filters and excluded from being used as the best route.
- `U` (unreachable): A flag indicates whether the route next-hop is unreachable.
- `A` (active): A flag indicates whether the route is elected as Active and eligible to be added to the FIB.
- `c`: connect
- `s`: static
- `r`: rip
- `b` (bgp): A flag indicates whether this route was added by the [BGP](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/unicast/bgp/index) protocol.
- `n`: bgp-net
- `o`: ospf
- `i`: isis
- `d` (dhcp): A flag indicates whether the route was added by the DHCP service.
- `v` (vpn): A flag indicates whether the route was added by one of the VPN protocols (PPPoE, L2TP, SSTP, etc.)
- `m` (modem): A flag indicates whether the route is added by the LTE or 3g modems.
- `a` (ldp-address): A flag indicates whether the route entry is an LDP address.
- `l` (ldp-mapping): A flag indicates whether the route entry is the LDP mapping.
- `g`: slaac
- `y` (bgp-mpls-vpn): A flag indicates a copy of the route to be redistributed as the L3VPN route. VPNv4/6 related attributes are attached to this route.
- `e`: evpn
- `H` (hw-offloaded): Indicates whether the route is eligible to be hardware offloaded on supported hardware.
- `+` (ecmp): A flag indicates whether the route is added as an [Equal-Cost Multi-Path](../../guides/user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) route in the FIB
- `B` (blackhole): A flag indicates whether it is a blackhole route.

**Read-only arguments**

- `afi` (enum: bad | ip | ipv6 | l2vpn | vpnv4 | vpnv6 | l2vpn-cisco | mip4 | mip6 | link | l2vpn-link | evpn; unset): Address family this route belongs to.
- `contribution` (enum: filtered | unreachable | candidate | best-candidate | active): Shows the route status contributing to the election process, e.g "filtered, active, candidate"
- `dst-address` (address (flags=46i/SR))
- `routing-table` (enum): Routing table this route belongs to.
- `ve-id` (num)
- `ve-block-offset` (num)
- `ve-block-size` (num)
- `label` (num)
- `pref-src` (address (flags=46); unset)
- `gateway` (address (flags=46ivL)): Configured gateway, for the actually resolved gateway, see `immediate-gw` parameter.
- `nexthop-id` (num; unset)
- `immediate-gw` (multi { gw: address (flags=46i) }): Shows actual (resolved) gateway and interface that will be used for packet forwarding. Displayed in format `[ip%interface]`.
- `check-gateway` (enum: none | arp | ping | bfd; unset): Currently used check-gateway option.
- `distance` (num; unset)
- `scope` (num; unset): Scope used in the next-hop lookup process. [Read more>>](../../guides/user-guides/routing-and-networking-protocols/routing-decision.md#nexthop-lookup)
- `target-scope` (num; unset): Target scope used in next-hop lookup process. [Read more>>](../../guides/user-guides/routing-and-networking-protocols/routing-decision.md#nexthop-lookup).
- `vrf-interface` (iface_enum; unset): Internal use only parameter which allows identifying to which VRF route should be added. Used by services that add routes dynamically, for example, DHCP client. Shown for debugging purposes.
- `belongs-to` (string): Descriptive info showing from where the route was received.
- `local-address` (address (flags=46iv)): Local IP address of the connected network.
- `route-cost` (num)
- `total-cost` (num)
- `rpki` (enum: unknown | valid | invalid; unset): Current status of the prefix from the [RPKI](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/unicast/rpki) validation process.
- `bgp.session` (enum): [BGP](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/unicast/bgp/index) session that installed the route. See `/routing/bgp/session` menu.
- `bgp.aggregator` (string)
- `bgp.as-path` (string): Value of the **`AS_PATH`** BGP attribute.
- `bgp.cluster-list` (string)
- `bgp.communities` (multi { value: string }): Value of the **`COMMUNITIES`** BGP attribute.
- `bgp.ext-communities` (multi { value: string }): Value of the **`EXTENDED_COMMUNITIES`** BGP attribute.
- `bgp.large-communities` (multi { value: string }): Value of the **`LARGE_COMMUNITIES`** BGP attribute.
- `bgp.unknown` (multi { value: string }): Hex blob of unknown [BGP](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/unicast/bgp/index) attributes.
- `bgp.originator-id` (address (flags=4))
- `bgp.nexthop` (multi { gw: address (flags=4) })
- `bgp.out-nexthop` (multi { gw: address (flags=4iv) })
- `bgp.weight` (num)
- `bgp.local-pref` (num): Value of the **`LOCAL_PREF`** BGP attribute.
- `bgp.igp-metric` (num): Value of the **`IGP_METRIC`** BGP attribute
- `bgp.pmsi` (string)
- `bgp.med` (num): Value of the **`MED`** BGP attribute.
- `bgp.atomic-aggregate` (bool)
- `bgp.origin` (enum: igp | egp | incomplete)
- `bgp.esi` (string)
- `bgp.otc` (num)
- `route-distinguisher` (string)
- `rip.tag` (num)
- `rip.metric` (num)
- `ospf.metric` (num)
- `ospf.tag` (num)
- `ospf.type` (enum: intra | inter | ext-type-1 | ext-type-2 | nssa-type-1 | nssa-type-2)
- `isis.type` (enum: l1 | l2 | l1-inter | l1-ext | l2-ext | l1-inter-ext)
- `isis.metric` (num)
- `mpls.labels` (multi { label: num })
- `mpls.in-label` (num): Mapped MPLS ingress label.
- `mpls.out-label` (num): Mapped MPLS egress label.
- `ldp.peer-id` (num)
- `ldp.label` (num): LDP mapped MPLS label.
- `mtu` (num)
- `hoplimit` (num)
- `debug.fwp-ptr` (num)
- `debug.route-ptr` (num)
- `debug.input.refs` (num)
- `debug.input.size` (num)
- `debug.input.ptr` (num)
- `debug.input.raw` (string)
- `debug.merge.refs` (num)
- `debug.merge.size` (num)
- `debug.merge.ptr` (num)
- `debug.merge.raw` (string)
