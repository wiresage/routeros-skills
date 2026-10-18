# /routing/igmp-proxy/mfc

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/igmp-proxy/mfc

Type: Directory

Multicast forwarding cache (MFC) status.

RouterOS supports static multicast forwarding rules for IGMP proxy. If a static rule is added, all dynamic rules for that group will be ignored. These rules will take effect only if IGMP-proxy interfaces are configured (upstream and downstream interfaces should be set) otherwise these rules won't be active.

**Flags**

- `X`: disabled
- `A`: active
- `D`: dynamic

**Arguments**

- `group` (ipAddr; mandatory): The multicast group address this rule applies to.
- `source` (ipAddr; mandatory): The multicast data originator address.
- `upstream-interface` (iface_enum; mandatory): The interface that is receiving stream data.
- `downstream-interfaces` (multi { interface: iface_enum }): The received stream will be sent out to the listed interfaces only.

**Read-only arguments**

- `active-downstream-interfaces` (multi { interface: iface_enum }): The packet stream is going out of the router through this interface.
- `bytes` (num): The total amount of received multicast traffic.
- `packets` (num): The total amount of received multicast packets.
- `wrong-packets` (num): The total amount of received multicast packets that arrived on a wrong interface, for example, a multicast stream that is received on a downstream interface instead of an upstream interface.
