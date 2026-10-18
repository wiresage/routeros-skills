# /interface/veth

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/veth

Conditions: !smips; Syscap: container; Type: Directory

Virtual Ethernet interfaces that connect containers to RouterOS. One end of a veth is this RouterOS interface; the other end is the network interface of the container that uses it, with the veth's name and `container-mac-address`. The address, gateway and DHCP settings are applied inside the container. A veth runs only while a container that uses it runs. See [VETH](../../guides/containers/veth.md).

**Flags**

- `X` (disabled): Disabled: the veth is not used.
- `R` (running): Running: a container that uses the veth is running. Without it, the MAC addresses show as `00:00:00:00:00:00` and a router address on the veth is invalid.

**Arguments**

- `name` (string): Name of the veth. Inside the container, the interface has the same name.
- `mac-address` (macAddr): MAC address of the router's end of the veth. A DHCP server sees this address for a veth with `dhcp=yes`, so a static lease for the container uses it. Set automatically when the container starts if empty.
- `container-mac-address` (macAddr): MAC address of the container's end of the veth, the address of the interface inside the container. Set automatically when the container starts if empty.
- `address` (multi { address: address (flags=46/) }): IPv4 and IPv6 addresses of the container's interface, several separated by commas, for example `172.17.0.2/24,2001:db8:17::2/64`. The router needs its own address in the same subnet on the veth (or on the bridge the veth is a port of) to reach the container.
- `gateway` (address (flags=4)): IPv4 default gateway inside the container, usually the router's address on the veth.
- `gateway6` (address (flags=6)): IPv6 default gateway inside the container.
- `dhcp` (bool): With `yes`, RouterOS runs a DHCP client for the container on the veth and applies the lease inside the container (address and default route). The DHCP server sees the veth's `mac-address` and the host name `<identity>-<veth name>`. The container's DNS server comes from the container settings, not from DHCP. Default: no.

**Read-only arguments**

- `dhcp-address` (address (flags=46/)): The address the DHCP client leased for the container, when `dhcp=yes`.
