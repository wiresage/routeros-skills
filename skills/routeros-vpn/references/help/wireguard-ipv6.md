# Wireguard IPv6

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/242909215/Wireguard+IPv6
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2024-04-03.

## Step-by-step guide

Wireguard server, ROS side:

1. Add an IPv6 address from an unused subnet to the Wireguard interface on the ROS device. Follow Wireguard configuration example for IPv4 [WireGuard](https://help.mikrotik.com/docs/display/ROS/WireGuard#WireGuard-RoadWarriorWireGuardtunnel)
2. Add the IPv6 address for the peer to the "Allowed address" list.
3. Add IPv6 firewall filter rule to allow the client IP address on the forward chain.

Client configuration, make sure all steps are done:

1. Add IPv6 address to the client.
2. Add ::/0 to "Allowed IPs" on the mobile client, make sure the default route is created.
3. Add IPv6 DNS server to the mobile client.
