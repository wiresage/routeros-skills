# IPSEC with Fortinet and Encryption Domain

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/245792775/IPSEC+with+Fortinet+and+Encryption+Domain
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2024-04-22.

A site-to-site VPN using IKEv2 between a Fortinet FortiGate and a Mikrotik.

## Step-by-step guide

### ROS

> **Info**
>
> /ip ipsec profile
> add dh-group=ecp521 dpd-interval=2m dpd-maximum-failures=5 enc-algorithm=aes-256 hash-algorithm=sha512 lifetime=1d name=fortigate \
>     nat-traversal=no proposal-check=obey
>
> /ip ipsec peer
> add address=10.0.0.1/32 disabled=no exchange-mode=ike2 name=fortigate profile=fortigate send-initial-contact=yes
>
> /ip ipsec proposal
> add auth-algorithms="" disabled=no enc-algorithms=aes-256-gcm lifetime=1h name=fortigate pfs-group=ecp521
>
> /ip ipsec identity
> add auth-method=pre-shared-key disabled=no generate-policy=no peer=fortigate secret=<PRESHAREDKEY>
>
> /ip ipsec policy
> add action=encrypt disabled=no dst-address=192.168.111.0/24 dst-port=any ipsec-protocols=esp level=require peer=fortigate proposal=fortigate \
>     protocol=all sa-dst-address=10.0.0.1 sa-src-address=10.0.0.2 src-address=192.168.222.0/24 src-port=any tunnel=yes

### Fortinet

> **Info**
>
> config vpn ipsec phase1-interface
>     edit "vpn-to-mikrotik"
>         set interface "wan2"
>         set ike-version 2
>         set peertype any
>         set net-device disable
>         set proposal aes256-sha512
>         set dhgrp 21
>         set remote-gw 10.0.0.2
>         set psksecret <PRESHAREDKEY>
>     next
> end
> config vpn ipsec phase2-interface
>     edit "vpn-to-mikrotik"
>         set phase1name "vpn-to-mikrotik"
>         set proposal aes256gcm
>         set dhgrp 21
>         set auto-negotiate enable
>         set keylifeseconds 3600
>         set src-subnet 192.168.111.0 255.255.255.0
>         set dst-subnet 192.168.222.0 255.255.255.0
>     next
> end

### Note

It may be needed to add a firewall rule to ROS device:

If the Encryption Domain Address is: 1.2.3.4.
And the server's IP is: 4.3.2.1

Add a rule to firewall ( chain=srcnat with action action=src-nat):
*/ip firewall nat add*
*chain=srcnat*
*src-address=4.3.2.1*
*out-interface=ether1*
*action=src-nat*
*to-addresses=1.2.3.4*
*protocol=all*

## Related articles

- [IPSEC with Fortinet and Encryption Domain](https://help.mikrotik.com/docs/spaces/RKB/pages/245792775/IPSEC+with+Fortinet+and+Encryption+Domain)
