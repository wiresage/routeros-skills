# ROS v7 differences in IP/Route

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/127369252/ROS+v7+differences+in+IP+Route
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2022-05-20.

IP routes no longer contain the Rules, VRF, and Nexthop tab under the IP Routes menu.

## Step-by-step guide

Rules in v7:

1. First, add table in /routing table menu
2. Then you can add routing rules in /routing rule menu and routes in specific table
3. /ip route add dst-address=x.x.x.x@table gateway=y.y.y.y@main

 VRF in v7:

1. First, add interfaces to a list,
2. Add the list to a vrf.

 Nexthop:

1. Nexthop is available at routing/nexthop/print

> **Info**

## Related articles

[Moving from ROSv6 to v7 with examples](https://help.mikrotik.com/docs/pages/viewpage.action?pageId=30474256)

- [x86 on USB](https://help.mikrotik.com/docs/spaces/RKB/pages/130220233/x86+on+USB)
- [How to install WinBox](https://help.mikrotik.com/docs/spaces/RKB/pages/6488069/How+to+install+WinBox)
- [IPSEC with Fortinet and Encryption Domain](https://help.mikrotik.com/docs/spaces/RKB/pages/245792775/IPSEC+with+Fortinet+and+Encryption+Domain)
- [Wireguard IPv6](https://help.mikrotik.com/docs/spaces/RKB/pages/242909215/Wireguard+IPv6)
- [Remote access to a LMT Mikrotik router](https://help.mikrotik.com/docs/spaces/RKB/pages/240156678/Remote+access+to+a+LMT+Mikrotik+router)
