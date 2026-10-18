# /routing/gmp

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/gmp

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `interfaces` (object { interface: iface_enum }): Name of the interface, multiple interfaces and interface lists are supported.
- `groups` (object { group: address (flags=46) }): The multicast group address to be used by the interface, multiple group addresses are supported.
- `exclude` (switch): When `exclude` is set, the interface expects to reject multicast data from the configured `sources`. When this option is not used, the interfaces will emit source specific join for the configured `sources`.
- `sources` (object { source: address (flags=46) }; unset): The source address list used by the interface, multiple source addresses are supported. This setting has an effect when IGMPv3 or MLDv2 protocols are active.
