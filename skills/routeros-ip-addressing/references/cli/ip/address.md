# /ip/address

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/address

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic
- `S` (slave): Whether address belongs to an interface which is a slave port to some other master interface.

**Arguments**

- `address` (composite { address: ipAddr , netmask: [ num [ .. 32]] }; mandatory)
- `network` (ipAddr): Network address, that is calculated from address parameter using address itself and the netmask.
- `netmask` (ipAddr)
- `broadcast` (ipAddr)
- `interface` (iface_enum; mandatory): Specifies the interface on which the IPv4 address is configured. You can select it from the pool of interfaces available on the router.

**Read-only arguments**

- `actual-interface` (iface_enum): Actual interface on which address is set up. For example, if address was configured on ethernet interface and ethernet interface was added to bridge, then actual interface is bridge not ethernet.
- `vrf` (enum): Indicates which VRF this IP address is associated with.
