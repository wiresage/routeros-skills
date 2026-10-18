# /interface/ethernet/switch/mac-based-vlan

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/mac-based-vlan

Syscap: musicswitch; Type: Directory

MAC Based VLAN table is used to assign a VLAN based on the source MAC.

All CRS1xx/2xx series switches support up to 1024 MAC Based VLAN table entries.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `src-mac-address` (macAddr; mandatory): Matching source MAC address for MAC based VLAN rule.
- `new-service-vid` (num): The new service VLAN ID replaces the original service VLAN ID for matched packets.
- `new-customer-vid` (num): The new customer VLAN ID replaces the original service VLAN ID for matched packets. If set to 4095, then traffic is dropped.
