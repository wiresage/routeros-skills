# /mpls/ldp/interface

> Source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp/interface

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `interface` (enum; mandatory): Name of the interface or interface list where LDP will be listening.
- `hello-interval` (time; unset): The interval between hello packets that the router sends out on the specified interface/s. The default value is 5s.
- `hold-time` (time; unset): Specifies the interval after which a neighbor discovered on the interface is declared as not reachable. The default value is 15s.
- `transport-addresses` (multi { array-id, transport-address: address (flags=46) }; unset): Used transport addresses if they differ from LDP Instance settings.
- `accept-dynamic-neighbors` (bool; unset): Defines whether to discover neighbors dynamically or use only statically configured in LDP neighbors menu.
- `afi` (ubit (ip, ipv6); unset): Determines interface address family. Only AFIs that are configured as supported by the instance are taken into account. If the value is not explicitly specified then it is considered to be equal to the instance-supported AFIs.
