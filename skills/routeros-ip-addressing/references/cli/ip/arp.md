# /ip/arp

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/arp

Type: Directory

Even though IP packets are addressed using IP addresses, hardware addresses must be used to transport data from one host to another. Address Resolution Protocol is used to map OSI level 3 IP addresses to OSI level 2 MAC addresses. A router has a table of currently used ARP entries. Normally the table is built dynamically, but to increase network security, it can be partially or completely built statically by adding static entries. To know more on how ARP works, read [networking fundamentals](https://manual.mikrotik.com/docs/getting-started/networking-fundamentals/index#arp-and-tying-it-all-together).

> **Info**
>
> The default maximum number of ARP entries depends on the installed amount of RAM. It can be adjusted with the command "`/ip/settings/set max-neighbor-entries=`x", see more details on [IPv4 Settings](settings.md).

**Flags**

- `X` (disabled): Whether the ARP entry is disabled.
- `I` (invalid): Whether the entry is not valid.
- `H` (dhcp): Whether the ARP entry is added by DHCP server.
- `D` (dynamic): Whether the entry is dynamically created.
- `P`: published
- `C` (complete): Complete flag is included in ARP entries when the ARP `status` is permanent, reachable, stale, probe, or delay.

**Arguments**

- `address` (ipAddr): IP address to be mapped.
- `mac-address` (macAddr): MAC address to be mapped to.
- `interface` (iface_enum; mandatory): Interface name the IP address is assigned to.
- `published` (bool): Static proxy-arp entry for individual IP addresses. When an ARP query is received for the specific IP address, the device will respond with its own MAC address. No need to set proxy-arp on the interface itself for all the MAC addresses to be proxied. The interface will respond to an ARP request only when the device has an active route towards the destination.

**Read-only arguments**

- `status` (string): Shows the ARP entry state.
  - `delay` - neighbor entry validation is currently delayed.
  - `failed` - ARP resolution has failed.
  - `incomplete` - system does not have the MAC address information for the IP address.
  - `permanent` - ARP entry is considered permanent and will not be removed.
  - `probe` - neighbor is being probed.
  - `reachable` - ARP resolution is successful, the MAC address is known.
  - `stale` - entry is still valid but aged.
- `vrf` (enum): Indicates which VRF this ARP entry is associated with.
