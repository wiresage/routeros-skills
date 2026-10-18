# /zerotier

> Source: https://manual.mikrotik.com/docs/cli-reference/zerotier

Package: zerotier; Type: Directory

The [ZeroTier](../guides/virtual-private-networks/zerotier.md) network hypervisor is a self-contained network virtualization engine that implements an Ethernet virtualization layer

**Flags**

- `X` (disabled): Whether an item is disabled.
- `R` (online): Whether the instance is online.
- `F` (tcp-fallback): Whether TCP fallback is active.

**Arguments**

- `name` (string): Instance name.
- `disabled` (bool): Whether an item is disabled.
- `port` (num): Port number the instance listens to.
- `identity` (string): Instance 40-bit unique address.
- `interfaces` (multi { array-id, interface: iface_enum }): List of interfaces used to discover ZeroTier peers with ARP and IP type connections.
- `route-distance` (num): Route distance for routes obtained from planet/moon servers.
- `backup-priorities` (multi { array-id, array-id, backup-priority: composite { interface: iface_enum , priority: num } }): Backup interface priorities for failover.

**Read-only arguments**

- `identity.public` (string): Public identity of the instance.
- `state` (string): Current state of the instance.
- `moons` (multi { array-id, moon: string }): List of moons the instance is connected to.
