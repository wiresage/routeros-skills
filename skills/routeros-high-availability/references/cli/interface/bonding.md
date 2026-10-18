# /interface/bonding

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/bonding

Type: Directory

[Bonding](../../guides/high-availability-solutions/bonding.md) is used in High Availability Solutions.

**Flags**

- `X` (disabled): disabled.
- `R` (running): running.

**Arguments**

- `name` (string): Name of the bonding interface.
- `mtu` (num): Maximum Transmit Unit in bytes. Must be smaller or equal to the smallest L2MTU value of a bonding slave.
- `forced-mac-address` (macAddr): By default, the bonding interface will use the MAC address of the first selected slave interface. This property allows to configure static MAC address for the bond interface (all zeros, broadcast or multicast addresses will not apply). RouterOS will automatically change the MAC address for slave interfaces and it will be visible in [`/interface/ethernet`](https://manual.mikrotik.com/docs/cli-reference/interface/ethernet) configuration export
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp): [Address Resolution Protocol](https://manual.mikrotik.com/docs/getting-started/networking-fundamentals/index#arp-and-tying-it-all-together) mode.
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time }): How long the ARP record is kept in the ARP table after no packets are received from IP. Value auto equals the value of arp-timeout in IP/Settings, default is 30s.
- `slaves` (multi { array-id, slave: iface_enum }): At least two ethernet-like interfaces separated by a comma, which will be used for bonding.
- `mode` (enum: balance-rr | active-backup | balance-xor | broadcast | 802.3ad | balance-tlb | balance-alb): Specifies one of the bonding policies.
  - `802.3ad` - LACP, IEEE 802.3ad dynamic link aggregation. In this mode, the interfaces are aggregated in a group where each slave shares the same speed. It provides fault tolerance and load balancing. Slave selection for outgoing traffic is done according to the `transmit-hash-policy`.
  - `active-backup` - provides link backup, only one slave active at a time.
  - `balance-alb` - adaptive load balancing, both outgoing and incoming traffic balanced. The device driver should have support for changing its MAC address.
  - `balance-rr` - round-robin load balancing. Slaves in a bonding interface will transmit and receive data in sequential order. It provides load balancing and fault tolerance.
  - `balance-tlb` - outgoing traffic distributed according to current load. Incoming traffic is not balanced and is received by the current slave. If receiving slave fails, then another slave takes the MAC address of the failed slave.
  - `balance-xor` - static LAG, transmit based on `transmit-hash-policy`. This mode provides load balancing and fault tolerance.
  - `broadcast` - broadcasts the same data on all interfaces. This provides fault tolerance but slows down traffic throughput on some slow machines.

  MikroTik devices with Marvell Prestera switch and 88E6393X, 88E6191X, 88E6190 switch chips support bridge hardware offloading with bonding interfaces.
  Only `802.3ad` (LACP), `balance-xor` (static LAG) and `active-backup` bonding modes are hardware offloaded, other bonding modes will use the CPU's resources.
- `primary` (iface_enum): Controls the primary interface between active slave ports, works only for `active-backup`, `balance-tlb` and `balance-alb` modes. For `active-backup` mode, it controls which running interface is supposed to send and receive the traffic. For `balance-tlb` mode, it controls which running interface is supposed to receive all the traffic, but for `balance-alb` mode, it controls which interface is supposed to receive the unbalanced traffic (the non-IPv4 traffic). When none of the interfaces are selected as primary, device will automatically select the interface that is configured as the first one.
- `link-monitoring` (enum: none | arp | mii): Method to use for monitoring the link. Some bonding modes require specific link monitoring to work properly.
  - `arp` - uses ARP to determine whether the remote interface is reachable.
  - `mii` - uses Media Independent Interface to determine link status. Link status determination relies on the device driver.
  - `none` - no link monitoring.
- `arp-interval` (time): Time in milliseconds defines how often to monitor ARP requests.
- `arp-ip-targets` (multi { array-id, arp-target: ipAddr }): IP target address which will be monitored if link-monitoring is set to arp. Multiple IP addresses can be specified, separated by a comma.
- `mii-interval` (time): How often to monitor the link for failures (used only if link-monitoring is mii).
- `down-delay` (time): If a link failure has been detected, the bonding interface is disabled for a down-delay time. Only has effect when link-monitoring is set to mii.
- `up-delay` (time): If a link has been brought up, the bonding interface is disabled for up-delay time. Only has effect when link-monitoring is set to mii.
- `lacp-rate` (enum: 30secs | 1sec): LACP rate specifies how often to exchange LACPDUs between bonding peers. `1sec` - short timeout. `30secs` - long timeout.
- `transmit-hash-policy` (enum: layer-2 | layer-3-and-4 | layer-2-and-3 | encap-2-and-3 | encap-3-and-4): Selects the transmit hash policy for slave selection in balance-xor and 802.3ad modes.
  - `layer-2` - Uses XOR of hardware MAC addresses to generate the hash. This algorithm will place all traffic to a particular network peer on the same slave. This algorithm is 802.3ad compliant.
  - `layer-2-and-3` - This policy uses a combination of layer2 and layer3 protocol information to generate the hash. Uses XOR of hardware MAC addresses and IP addresses to generate the hash. This algorithm will place all traffic to a particular network peer on the same slave. For non-IP traffic, the formula is the same as for the layer2 transmit hash policy. This policy is intended to provide a more balanced distribution of traffic than layer2 alone, especially in environments where a layer3 gateway device is required to reach most destinations. This algorithm is 802.3ad compliant.
  - `layer-3-and-4` - This policy uses upper layer protocol information, when available, to generate the hash. This allows for traffic to a particular network peer to span multiple slaves, although a single connection will not span multiple slaves. For fragmented TCP or UDP packets and all other IP protocol traffic, the source and destination port information is omitted. For non-IP traffic, the formula is the same as for the layer2 transmit hash policy. This algorithm is not fully 802.3ad compliant.
  - `encap-2-and-3` - This policy works like the layer-2-and-3 method for distributing traffic, but uses a process to also analyze the encapsulated packet headers. If an encapsulation protocol (like tunneling) is used, it may select the inner headers instead of the outer ones. RouterOS can use this feature when tunnels like 6to4, GRE, GRE6, IPIP, IPIP6, PPPoE, or PPTP are run over a bonding interface.
  - `encap-3-and-4` - This policy works like the layer-3-and-4 method for distributing traffic, but uses a process to also analyze the encapsulated packet headers. If an encapsulation protocol (like tunneling) is used, it may select the inner headers instead of the outer ones. RouterOS can use this feature when tunnels like 6to4, GRE, GRE6, IPIP, IPIP6, PPPoE, or PPTP are run over a bonding interface.
- `min-links` (num): How many active slave links needed for bonding to become active.
- `mlag-id` (num): Changes [MLAG](../../guides/high-availability-solutions/multi-chassis-link-aggregation-group.md) ID for bonding interface. The same MLAG ID should be used on both peer devices to successfully create a single MLAG.  The [`mlag-peer-port`](https://manual.mikrotik.com/docs/cli-reference/interface/bridge#mlag-peer-port) should not be configured with the MLAG ID.
- `lacp-user-key` (num): Specifies the upper 10 bits of the port key. The lower 6 bits are automatically assigned based on individual port link speed and duplex.
- `lacp-mode` (enum: passive | active): Specifies whether ports actively or passively participates in the LACP.
  - `active` - ports actively initiate LACP communication.
  - `passive` - ports only respond to LACP messages.
- `lacp-system-id` (macAddr): Specifies the LACP system ID used for LACP negotiations.
- `lacp-system-priority` (num): Specifies the LACP system priority used for LACP negotiations.

**Read-only arguments**

- `mac-address` (macAddr): MAC address of the bonding interface.

## Commands

### /interface/bonding/monitor

Type: Command

Command is used to monitor the bonding interface and bonding ports.

**Read-only arguments**

- `mode` (enum: balance-rr | active-backup | balance-xor | broadcast | 802.3ad | balance-tlb | balance-alb): Used bonding mode.
- `active-ports` (multi { array-id, port: iface_enum }): Shows the active bonding ports.
- `inactive-ports` (multi { array-id, port: iface_enum }): Shows the inactive bonding ports (e.g. a disabled or backup interface).
- `lacp-system-id` (macAddr): Shows the local LACP system ID.
- `lacp-system-priority` (num): Shows the local LACP priority.
- `lacp-partner-system-id` (macAddr): Shows the partner LACP system ID.

### /interface/bonding/monitor-slaves

Type: Command

Command is used to monitor individual bonding ports.

**Flags**

- `A`: active
- `P`: partner

**Arguments**

- `bond` (iface_enum): Bonding interface to monitor.
- `once` (bool): Show the monitor output once instead of continuously.

**Read-only arguments**

- `port` (iface_enum): Used bonding port.
- `key` (num): Shows the local LACP aggregation key. The lower 6 bits are automatically assigned based on individual port link speed and duplex. The upper 10 bits can be manually specified using the lacp-user-key setting.
- `flags` (string): Shows the local LACP flags.
  - A - activity (link is active).
  - T - timeout (link is using short timeout).
  - G - aggregation (link can be aggregatable).
  - S - synchronization (link is synchronized).
  - C - collecting (link is able to collect incoming frames).
  - D - distributing (link is able to distribute outgoing frames).
  - F - defaulted (link is using defaulted partner information).
  - E - expired (link has expired state).
- `partner-sys-id` (macAddr): Shows the partner LACP system ID.
- `partner-sys-priority` (num): Shows the partner LACP priority.
- `partner-key` (num): Shows the partner LACP aggregation key.
- `partner-flags` (string): Shows the partner LACP flags.
