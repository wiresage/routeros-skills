# /ipv6/address

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/address

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic
- `G`: global
- `L`: link-local
- `S` (slave): Whether address belongs to an interface which is a slave port to some other master interface.
- `d`: deprecated

**Arguments**

- `address` (composite { address: ip6Addr , netmask: [ num [ .. 128]] }): IPv6 address.  Address can also be constructed from the pool if `from-pool` parameter is specified.
  For example if address is set to `::1/64` then address will be constructed as follows `<prefix_from_pool>::1/64`
- `from-pool` (enum): Name of the pool from which prefix will be taken to construct IPv6 address taking last part of the address from address property.
- `from-pool-policy` (enum: recommended | strict | without-acquire): Specify how to acquire prefix from pool, if `from-pool` parameter is set.

  - `recommended` option will use `address` as a postfix and **subnet-id**, if subnet-id is provided.
  - `strict` will use **address** as a strict postfix.
  - `without-acquire` will not allocate a prefix from a pool and will allow other services to use the exact same prefix. The `without-acquire` option should be mainly used to create SLAAC address on a router which at the same time will be a DHCPv6 server providing addresses to client from the same subnet.
- `interface` (iface_enum; mandatory): Specifies the interface on which the IPv6 address is configured. You can select it from the pool of interfaces available on the router.
- `eui-64` (bool): Whether to calculate EUI-64 address and use it as last 64 bits of the IPv6 address.
- `advertise` (bool): Whether to enable stateless address configuration. The prefix of that address is automatically advertised three times to hosts using ICMPv6 protocol. The option is set by default for addresses with prefix length 64. If address is removed or changed, then old prefix will be deprecated by automatically advertising the old prefix with lifetime set to `0s` three times to hosts using ICMPv6 protocol.
- `no-dad` (bool): If enabled (yes) - disables Duplicate Address Detection (DAD) for IPv6 addresses on an interface. This can be useful in scenarios where you want to assign static IPv6 addresses to devices and avoid the delay caused by DAD.
- `auto-link-local` (bool): If you want to manually add a link‑local address to an interface, this setting lets you override the automatically generated IPv6 link‑local address.

**Read-only arguments**

- `actual-interface` (iface_enum): Actual interface on which address is set up. For example, if address was configured on ethernet interface and ethernet interface was added to bridge, then actual interface is bridge not ethernet.
- `vrf` (enum): Indicates which VRF this IP address is associated with.
- `valid` (alt { valid: enum (forever) , valid: time })
- `preferred` (alt { preferred: enum (forever) , preferred: time })
