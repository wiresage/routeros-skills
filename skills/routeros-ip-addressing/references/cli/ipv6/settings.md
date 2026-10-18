# /ipv6/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/settings

Type: Settings Directory

This menu allows you to configure various IPv6-related kernel and system-wide network parameters. These settings control how the operating system handles IP traffic and network communications.

> **Note**
>
> Changing IPv6 settings does not dynamically remove an existing SLAAC configuration, a router reboot is required.
>

**Arguments**

- `disable-ipv6` (bool): Disable or enable IPv6 system-wide. When disabled, prevents link-local address generation.
- `forward` (bool): Enable or disable packet forwarding between interfaces.
- `multipath-hash-policy` (enum: l3 | l4 | l3-inner): Specify the IPv6 hash policy for [ECMP](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/routing-decision#multipath-ecmp-routes) routing:
  - l3 - Layer-3 hashing of source IP, destination IP, flow label, and IP protocol.
  - l3-inner - Layer-3 hashing or inner layer-3 hashing if available.
  - l4 - Layer-4 hashing of source IP, destination IP, IP protocol, source port, and destination port.
- `accept-redirects` (bool): Accept or reject ICMP redirect messages. Enable on hosts and disable on routers.
- `accept-router-advertisements` (enum: no | yes-if-forwarding-disabled | yes): Control acceptance of router advertisement (RA) messages. When enabled, the router obtains addresses using [stateless address configuration](https://manual.mikrotik.com/docs/system-information-and-utilities/neighbor-discovery).
- `accept-router-advertisements-on` (enum): Specify which interfaces to listen for incoming router advertisements (RAs).
- `disable-link-local-address` (bool): Disable automatic link-local address generation for non-VPN interfaces. Use this when you need manually configured link-local addresses.
- `stale-neighbor-detect-interval` (num): Set the interval at which the system checks stale IPv6 neighbor entries and probes them to verify reachability.
- `stale-neighbor-timeout` (num): Timeout duration after which stale IPv6 neighbor entries are purged.
- `min-neighbor-entries` (num): Set the minimum number of IPv6 neighbor entries for which the device must allocate memory.
- `soft-max-neighbor-entries` (num): Set the expected maximum number of IPv6 neighbor entries the system should handle.
- `max-neighbor-entries` (num): Set the maximum number of IPv6 neighbor entries. As of RouterOS version 7.1, the default value depends on installed RAM:
  - 1024 for 64 MiB
  - 2048 for 128 MiB
  - 4096 for 256 MiB
  - 8192 for 512 MiB
  - 16384 for 1024 MiB or higher

  Setting a value higher than the default increases the risk of out-of-memory conditions.
- `allow-fast-path` (bool): Enable [Fast Path](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fast-path) for IPv6 traffic.
Fasttrack and fastpath values are cumulative since the feature was last enabled or since the system restarted.

**Read-only arguments**

- `ipv6-fast-path-active` (bool): Indicates whether the IPv6 fast path feature is currently active.
- `ipv6-fast-path-packets` (num): Total number of packets that have been processed through the IPv6 fast path.
- `ipv6-fast-path-bytes` (num): Total number of bytes that have been processed through the IPv6 fast path.
- `ipv6-fasttrack-active` (bool): Indicates whether the IPv6 fasttrack feature is currently active.
- `ipv6-fasttrack-packets` (num): Total number of packets that have been processed through IPv6 fasttrack.
- `ipv6-fasttrack-bytes` (num): Total number of bytes that have been processed through IPv6 fasttrack.
