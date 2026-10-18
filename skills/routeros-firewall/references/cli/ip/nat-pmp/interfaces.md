# /ip/nat-pmp/interfaces

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/nat-pmp/interfaces

Type: Directory

Interface assignments for the NAT-PMP service: the interface that connects to the Internet (`external`) and the interfaces the NAT-PMP clients are connected to (`internal`). The list accepts only one external interface (`only one external interface can be added to the list`). See the [NAT-PMP guide page](../../../guides/firewall-and-quality-of-service/nat-pmp.md).

**Flags**

- `X` (disabled): disabled. The interface is not used by NAT-PMP. New entries are created enabled.
- `D`: dynamic

**Arguments**

- `interface` (iface_enum; mandatory): Name of the interface. On an `internal` interface, the service listens for client requests and sends external address announcements on the multicast group 224.0.0.1, UDP port 5350.
- `type` (enum: external | internal; mandatory): NAT-PMP interface role:
  - `external` - the interface facing the Internet. Only one external interface is allowed.
  - `internal` - the local interface the NAT-PMP clients are connected to.
- `forced-ip` (super { forced-ip: ipAddr }): Report this address to clients as the router's external address instead of the interface address, for example when the external interface has several addresses.
