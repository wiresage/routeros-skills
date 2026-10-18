# /interface/ethernet/switch/l3hw-settings/advanced

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/l3hw-settings/advanced

Syscap: rbswitch and crs_prestera; Type: Settings Directory

This menu allows tweaking l3hw settings for specific use cases.

It is NOT recommended to change the advanced L3HW settings unless instructed by MikroTik Support or a MikroTik Certified Routing Engineer. Applying incorrect settings may break the L3HW operation.

**Arguments**

- `route-queue-limit-high` (num; syscap=!prestera-cpss): The switch driver stops route indexing when [`route-queue-size`](../l3hw-settings.md#route-queue-size) exceeds this value. Lowering this value leads to faster route processing but increases the lag between a route's appearance in RouterOS and hardware memory. Setting **0** disables route indexing when there are any routes in the processing queue - the most efficient CPU usage but the longest delay before hardware offloading. Useful when there are static routes only. Not recommended together with routing protocols (such as BGP or OSPF) when there are frequent routing table changes.
- `route-queue-limit-low` (num; syscap=!prestera-cpss): Re-enable route indexing when [`route-queue-size`](../l3hw-settings.md#route-queue-size) drops down to this value. Must not exceed the high limit. Setting **0** tells the switch driver to process all pending routes before the next hw-offloading attempt. While this is the desired behavior, it may completely block the hw-offloading under a constant BGP feed.
- `shwp-reset-counter` (num): Reset the Shortest HW Prefix (SHWP) and try the full route table offloading after this number of changes in the routing table.
  At a partial offload, when the entire routing table does not fit into the hardware memory and shorter prefixes are redirected to the CPU, there is no need to try offloading route prefixes shorter than SHWP since those will get redirected to the CPU anyway, theoretically. However, significant changes to the routing table may lead to a different index layout and, therefore, a different number of routes that can be hw-offloaded. That's why it is recommended to do the full table re-indexing occasionally.
  Lowering this value may allow more routes to be hw-offloaded but increases CPU usage and vice-versa. Setting `shwp-reset-counter=0` always does full re-indexing after each routing table change.
  This setting is used only during Partial Offloading and has no effect when [`ipv4-shortest-hw-prefix`](advanced.md#ipv4-shortest-hw-prefix)=0 (and ipv6, respectively).
- `partial-offload-chunk` (num; syscap=prestera-bc2): The minimum number of routes for incremental adding in Partial Offloading.
  Depending on the switch chip model, routes are offloaded either as-is (each routing entry in RouterOS corresponds to an entry in the hardware memory) or get indexed, and the index entries are the ones that are written into the hardware memory. This setting is used only for the latter during Partial Offloading.
  Depending on index fragmentation, a single IPv4 route addition can occupy from -3 to +6 LPM blocks of HW memory (some route additions may lower the amount of required HW memory thanks to index defragmentation). Hence, it is impossible to predict the exact number of routes that may fit in the hardware memory. The switch driver uses a binary split algorithm to find the maximum number of routes that fit in the hardware.
  Let's imagine 128k routes, all of them not fitting into the hardware memory. The algorithm halves the number and tries offloading 64k routes. Let's say offloading succeeded. In the next iteration, the algorithm picks 96k, let's say it fails; then 80k - fails again, 72k - succeeds, 76k, etc. until the difference between succeeded and failed numbers drops below the partial-offload-chunk value.
  Lowering the partial-offload-chunk value increases the number of hw-offloaded routes but also raises CPU usage and vice-versa.
- `route-index-delay-min` (time; syscap=!prestera-cpss): The minimum delay between route processing and its offloading. The delay allows processing more routes together and offloading them at once, saving CPU usage.
  It also makes offloading the entire routing table faster by reducing the per-route processing work. On the other hand, it slows down the offloading of an individual route.
  If an additional route is received during the delay, the latter resets to the `route-index-delay-min` value. Adding more and more routes within the delay keeps resetting the timer until the `route-index-delay-max` is reached.
- `route-index-delay-max` (time): The maximum delay between route processing and its offloading. When the maximum delay is reached, the processed routes get offloaded despite more routes pending. However, `route-queue-limit-high` has higher priority than this, meaning that the indexing/offloading gets paused anyway when a certain queue size is reached.
- `neigh-keepalive-interval` (time; syscap=!prestera-cpss): Neighbor (host) keepalive interval. When a host gets hw-offloaded, all traffic from/to it is routed by the switch chip, and RouterOS may think the neighbor is inactive and delete it. To prevent that, the switch driver must keep the offloaded neighbors alive by sending periodic refreshes to RouterOS.
- `neigh-discovery-interval` (time; syscap=!prestera-cpss): The interval between sending ARP (IPv4) or Neighbor Discovery (IPv6) requests to check if the offloaded host is still active.
  Unfortunately, switch chips do not provide per-neighbor stats. Hence, the only way to check if the offloaded host is still active is by sending occasional ARP (IPv4) / Neighbor Discovery (IPv6) requests to the connected network.
  Neighbor discovery is triggered within the neighbor keepalive work. Hence, the discovery time is rounded up to the next keepalive session. Choose a value for `neigh-discovery-interval` not divisible by `neigh-keepalive-interval` to send ARP/ND requests in various sessions, preventing broadcast bursts.
- `neigh-discovery-burst-limit` (num; syscap=!prestera-cpss): The maximum number of ARP/ND requests that can be sent at once.
- `neigh-discovery-burst-delay` (time; syscap=!prestera-cpss): The delay between ARP/ND subsequent bursts if the number of requests exceeds `neigh-discovery-burst-limit`.
- `neigh-dump-retries` (num; syscap=!prestera-cpss): The maximum retry count to offload a neighbor table in case of failure.

## Commands

### /interface/ethernet/switch/l3hw-settings/advanced/monitor

Syscap: rbswitch and crs_prestera; Type: Command

An enhanced version of [Monitor](../l3hw-settings.md) with extra telemetry data for advanced users. Advanced Monitor contains all data from the basic monitor as well.

```ros
/interface/ethernet/switch/l3hw-settings/advanced> monitor once
        ipv4-routes-total: 29968
           ipv4-routes-hw: 29957
          ipv4-routes-cpu: 11
  ipv4-shortest-hw-prefix: 0
               ipv4-hosts: 3
        ipv6-routes-total: 4
           ipv6-routes-hw: 0
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 0
         route-queue-size: 0
         route-queue-rate: 0
       route-process-rate: 0
     fasttrack-ipv4-conns: 0
     fasttrack-queue-size: 0
     fasttrack-queue-rate: 0
   fasttrack-process-rate: 0
   fasttrack-hw-min-speed: 0
   fasttrack-hw-offloaded: 0
    fasttrack-hw-unloaded: 0
                  lpm-cap: 54560
                lpm-usage: 31931
             lpm-bank-cap: 2728
           lpm-bank-usage: 46,0,0,0,2589,2591,1983,0,2728,2728,2728,2728,2728,2728,2728,2728,2728,170,0,0
                  pbr-cap: 8192
                pbr-usage: 0
             pbr-lpm-bank: 3
                nat-usage: 0
              nexthop-cap: 8192
            nexthop-usage: 85
```

**Read-only arguments**

- `error-code` (num): Error code when L3HW driver is in a failure state.
- `state` (enum (ok | stopping | starting | fib-failure | net-failure | switch-failure | fasttrack-failure | out-of-memory) { ok:0, stopping:1, starting:2, fib-failure:3, net-failure:4, switch-failure:5, fasttrack-failure:6, out-of-memory:0xFFFFFFF4 }): Current state of the L3HW driver.
- `ipv4-routes-total` (num): The total number of IPv4 routes handled by the switch driver.
- `ipv4-routes-hw` (num): The number of hardware-offloaded IPv4 routes (a.k.a. hardware routes).
- `ipv4-routes-cpu` (num): The number of IPv4 routes redirected to the CPU (a.k.a. software routes).
- `ipv4-shortest-hw-prefix` (num): **Shortest Hardware Prefix (SHWP)** for IPv4. If the entire IPv4 routing table does not fit into the hardware memory, **partial offloading** is applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. `ipv4-shortest-hw-prefix=0` means the entire IPv4 routing table is offloaded to the hardware memory.
- `ipv4-hosts` (num): The number of hardware-offloaded IPv4 hosts (/32 routes).
- `ipv6-routes-total` (num): The total number of IPv6 routes handled by the switch driver.
- `ipv6-routes-hw` (num): The number of hardware-offloaded IPv6 routes (a.k.a. hardware routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).
- `ipv6-routes-cpu` (num): The number of IPv6 routes redirected to the CPU (a.k.a. software routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).
- `ipv6-shortest-hw-prefix` (num): **Shortest Hardware Prefix (SHWP)** for IPv6. If the entire IPv6 routing table does not fit into the hardware memory, **partial offloading** is applied, where the longest prefixes are hw-offloaded while the shorter ones are redirected to the CPU. This field shows the shortest route prefix (/x) that is offloaded to the hardware memory. All prefixes shorter than this are processed by the CPU. `ipv6-shortest-hw-prefix=0` means the entire IPv6 routing table is offloaded to the hardware memory. Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).
- `ipv6-hosts` (num): The number of hardware-offloaded IPv6 hosts (/128 routes). Shown only when IPv6 hardware routing is enabled (`ipv6-hw=yes`).
- `route-queue-size` (num; syscap=!prestera-cpss): The number of routes in the queue for processing by the switch chip driver. Under normal working conditions, this field is 0, meaning that all routes are processed by the driver.
- `route-queue-rate` (num; syscap=!prestera-cpss): The rate at which routes are added to the queue for processing by the switch driver (growth rate of `route-queue-size` routes per second).
- `route-process-rate` (num; syscap=!prestera-cpss): The rate at which previously queued routes are processed by the switch driver (shrink rate of `route-queue-size` routes per second)..
- `nexthop-cap` (num): The nexthop capacity.
- `nexthop-usage` (num): The number of currently used nexthops.
- `vxlan-mtu-packet-drop` (num; syscap=prestera-bc2): The number of dropped VXLAN packets due to exceeded interface MTU settings.
- `fasttrack-ipv4-conns` (num; syscap=prestera-bc2): The number of hardware-offloaded FastTrack connections. Parammeter appear only when hardware offloading of FastTrack connections is enabled.
- `fasttrack-queue-size` (num; syscap=prestera-bc2): The number of FastTrack connections in the queue for processing by the switch chip driver.
- `fasttrack-queue-rate` (num; syscap=prestera-bc2): The rate at which FastTrack connections are added to the queue for processing by the switch driver (growth rate of `fasttrack-queue-size` connections per second).
- `fasttrack-process-rate` (num; syscap=prestera-bc2): The rate at which previously queued FastTrack connections are processed by the switch driver (shrink rate of `fasttrack-queue-size` connections per second).
- `fasttrack-hw-min-speed` (num; syscap=prestera-bc2): When the hardware memory for storing FastTrack is full, this field shows the minimum speed (in bytes per second) of a hw-offloaded FastTrack connection. Parammeter appear only when hardware offloading of FastTrack connections is enabled.
- `fasttrack-hw-offloaded` (num; syscap=prestera-bc2): The number of FastTrack connections offloaded to the hardware. The counter resets every second.
- `fasttrack-hw-unloaded` (num; syscap=prestera-bc2): The number of FastTrack connections unloaded from the hardware (redirected to software routing). The counter resets every second.
- `lpm-cap` (num; syscap=!prestera-ac3): The size of the LPM hardware table (LPM = Longest Prefix Match). LPM stores route indexes for hardware routing. Not every switch chip model uses LPM. Others use TCAM.
- `lpm-usage` (num; syscap=!prestera-ac3): The number of used LPM blocks.
- `lpm-bank-cap` (num; syscap=!prestera-ac3): LPM memory is organized in banks. This value shows the size of a single bank (in LPM blocks). The bank size depends on the switch chip model. lpm-cap / lpm-bank-cap = the number of banks.
- `lpm-bank-usage` (multi { array-id, lpm-bank: num }; syscap=!prestera-ac3): Per-bank LPM usage (in LPM blocks).
- `pbr-cap` (num; syscap=prestera-bc2): The size of the Policy-Based Routing (PBR) hardware table. PBR is used for NAT offloading of FastTrack connections.
- `pbr-usage` (num; syscap=prestera-bc2): The number of used PBR entries.
- `pbr-lpm-bank` (num; syscap=prestera-bc2): PBR shares LPM memory banks with routing tables. This value shows the LPM bank index shared with PBR (0 = the first bank).
- `nat-usage` (num; syscap=prestera-bc2): The number of used NAT hardware entries (for FastTrack connections).
