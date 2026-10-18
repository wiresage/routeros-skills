# Oracle IPsec

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/225312967/Oracle+IPsec
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2023-12-04.

Configuration example for Oracle IPsec, seems common issue. Add local addresses to each IPSEC endpoint and configure the Oracle IPSEC side to have similar endpoints (they were optional).

## Step-by-step guide

Add local addresses to each IPSEC endpoint and configure the Oracle IPSEC side to have similar endpoints:

1. ROS configuration example:

   /interface bridge
   add name=br-oci-ipsec

   /ip address
   ...
   add address=[10.34.2.2/30](http://10.34.2.2/30) comment="oracle OCI ipsec - tunnel1" interface=br-oci-ipsec network=10.34.2.0
   add address=[10.34.2.6/30](http://10.34.2.6/30) comment="oracle OCI ipsec - tunnel2" interface=br-oci-ipsec network=10.34.2.4

   /ip ipsec policy
   set 0 disabled=yes
   add dst-address=[10.34.0.0/16](http://10.34.0.0/16) peer=tunnel-1-vcn-10-34-0-0 src-address=[192.168.0.0/16](http://192.168.0.0/16) tunnel=yes # existing config
   add dst-address=[10.34.0.0/16](http://10.34.0.0/16) peer=tunnel-2-vcn-10-34-0-0 src-address=[192.168.0.0/16](http://192.168.0.0/16) tunnel=yes # existing config
   add dst-address=[10.34.2.0/30](http://10.34.2.0/30) peer=tunnel-1-vcn-10-34-0-0 src-address=[10.34.2.0/30](http://10.34.2.0/30) tunnel=yes # new
   add dst-address=[10.34.2.4/30](http://10.34.2.4/30) peer=tunnel-2-vcn-10-34-0-0 src-address=[10.34.2.4/30](http://10.34.2.4/30) tunnel=yes # new
2. The corresponding Oracle OCI tunnel configuration with IPv4 inside tunnel interface CPE / Oracle addresses configured as [10.34.2.2/30](http://10.34.2.2/30) & [10.34.2.1/30](http://10.34.2.1/30).

   *[Figure]*

> **Info**

## Related articles

- [x86 on USB](https://help.mikrotik.com/docs/spaces/RKB/pages/130220233/x86+on+USB)
- [How to install WinBox](https://help.mikrotik.com/docs/spaces/RKB/pages/6488069/How+to+install+WinBox)
- [IPSEC with Fortinet and Encryption Domain](https://help.mikrotik.com/docs/spaces/RKB/pages/245792775/IPSEC+with+Fortinet+and+Encryption+Domain)
- [Wireguard IPv6](https://help.mikrotik.com/docs/spaces/RKB/pages/242909215/Wireguard+IPv6)
- [Remote access to a LMT Mikrotik router](https://help.mikrotik.com/docs/spaces/RKB/pages/240156678/Remote+access+to+a+LMT+Mikrotik+router)
