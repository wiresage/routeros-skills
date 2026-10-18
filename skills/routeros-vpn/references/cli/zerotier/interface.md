# /zerotier/interface

> Source: https://manual.mikrotik.com/docs/cli-reference/zerotier/interface

Package: zerotier; Type: Directory

**Flags**

- `D` (dynamic): Whether the interface was created dynamically.
- `X` (disabled): Whether an item is disabled.
- `R` (running): Whether the interface is running.

**Arguments**

- `name` (string): Short name for the interface.
- `arp-timeout` (alt { arp-timeout: enum (auto) , arp-timeout: time }): ARP timeout value.
- `disable-running-check` (bool): Forces the interface into running state.
- `network` (string; mandatory): 16-digit network ID.
- `instance` (enum; mandatory): ZeroTier instance name.
- `allow-managed` (bool): ZeroTier managed IP addresses and routes are assigned.
- `allow-global` (bool): ZeroTier IP addresses and routes can overlap public IP space.
- `allow-default` (bool): The network can override the system default route (force VPN mode).

**Read-only arguments**

- `mac-address` (macAddr): MAC address of the ZeroTier interface.
- `mtu` (num): Maximum transmission unit of the interface.
- `bridge` (bool): Whether the interface acts as a bridge.
- `dhcp` (bool): Whether DHCP is enabled on the interface.
- `network-name` (string): Human-readable network name from the controller.
- `status` (string): Current status of the interface on the network.
- `type` (string): Type of the network interface.
