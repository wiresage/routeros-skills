# /interface/ethernet/switch/l3hw-settings

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/l3hw-settings

Syscap: rbswitch and crs_prestera; Type: Settings Directory

The L3HW Settings menu allows configuring global parameters for the Layer 3 Hardware Offloading driver.

**Arguments**

- `autorestart` (bool; syscap=!prestera-cpss): Automatically restarts L3HW in case of driver failure. If autorestart is not enabled, then `l3-hw-offloading` gets disabled, and the error code is displayed in the [monitor](l3hw-settings.md). Autorestart does not work for system failures, such as OOM (Out Of Memory).
- `fasttrack-hw` (bool; syscap=!prestera-ac3): Enables or disables FastTrack HW Offloading. Keep it enabled unless HW TCAM memory reservation is required, e.g., for dynamic switch ACL rules creation. Not all switch chips support FastTrack HW Offloading (see [`hw-supports-fasttrack`](#hw-supports-fasttrack)).
- `ipv6-hw` (bool): IPv6 hardware offloading. IPv6 routes occupy a lot of HW memory, enable this option only if IPv6 traffic is significant enough to benefit from hardware routing.
- `icmp-reply-on-error` (bool): Since the hardware cannot send ICMP messages, the packet must be redirected to the CPU to send an ICMP reply in case of an error (e.g., "Time Exceeded", "Fragmentation required", etc.). Enabling helps with network diagnostics but may open potential vulnerabilities for DDoS attacks. Disabling silently drops the packets on the hardware level in case of an error.

**Read-only arguments**

- `hw-supports-fasttrack` (bool): Indicates if the hardware (switch chip) supports FastTrack HW Offloading.

## Commands

### /interface/ethernet/switch/l3hw-settings/monitor

Syscap: rbswitch and crs_prestera; Type: Command

This command allows monitoring switch chip and L3HW related driver stats.

```ros
/interface/ethernet/switch/l3hw-settings/monitor
        ipv4-routes-total: 99363
           ipv4-routes-hw: 61250
          ipv4-routes-cpu: 38112
  ipv4-shortest-hw-prefix: 24
               ipv4-hosts: 87
        ipv6-routes-total: 15
           ipv6-routes-hw: 11
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 7
         route-queue-size: 118
     fasttrack-ipv4-conns: 2031
   fasttrack-hw-min-speed: 0
              nexthop-cap: 8192
            nexthop-usage: 93
    vxlan-mtu-packet-drop: 0
```

**Read-only arguments**

- `state` (enum (ok | stopping | starting | fib-failure | net-failure | switch-failure | fasttrack-failure | out-of-memory) { ok:0, stopping:1, starting:2, fib-failure:3, net-failure:4, switch-failure:5, fasttrack-failure:6, out-of-memory:0xFFFFFFF4 }): Current state of the L3HW driver.
- `ipv4-routes-total` (num): The total number of IPv4 routes handled by the switch driver.
- `ipv4-routes-hw` (num): The number of hardware-offloaded IPv4 routes.
- `ipv4-routes-cpu` (num): The number of IPv4 routes redirected to the CPU.
- `ipv4-shortest-hw-prefix` (num): **Shortest Hardware Prefix (SHWP)** for IPv4. If the entire IPv4 routing table does not fit into the hardware memory, **partial offloading** is applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. `ipv4-shortest-hw-prefix=0` means the entire IPv4 routing table is offloaded to the hardware memory.
- `ipv4-hosts` (num): The number of hardware-offloaded IPv4 hosts (/32 routes).
- `ipv6-routes-total` (num): The total number of IPv6 routes handled by the switch driver.
- `ipv6-routes-hw` (num): The number of hardware-offloaded IPv6 routes (a.k.a. hardware routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).
- `ipv6-routes-cpu` (num): The number of IPv6 routes redirected to the CPU (a.k.a. software routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).
- `ipv6-shortest-hw-prefix` (num): **Shortest Hardware Prefix (SHWP)** for IPv6. If the entire IPv6 routing table does not fit into the hardware memory, **partial offloading** is applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. `ipv6-shortest-hw-prefix=0` means the entire IPv6 routing table is offloaded to the hardware memory. Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).
- `ipv6-hosts` (num): The number of hardware-offloaded IPv6 hosts (/128 routes).
- `route-queue-size` (num; syscap=!prestera-cpss): The number of routes in the queue for processing by the switch chip driver. Under normal working conditions, this field is 0, meaning that all routes are processed by the driver.
- `nexthop-cap` (num): The nexthop capacity.
- `nexthop-usage` (num): The number of currently used nexthops.
- `vxlan-mtu-packet-drop` (num; syscap=prestera-bc2): The number of dropped VXLAN packets due to exceeded interface MTU settings.
- `fasttrack-ipv4-conns` (num; syscap=prestera-bc2): The number of hardware-offloaded FastTrack connections. Parammeter appear only when hardware offloading of FastTrack connections is enabled.
- `fasttrack-hw-min-speed` (num; syscap=prestera-bc2): When the hardware memory for storing FastTrack is full, this field shows the minimum speed (in bytes per second) of a hw-offloaded FastTrack connection. Parammeter appear only when hardware offloading of FastTrack connections is enabled.
