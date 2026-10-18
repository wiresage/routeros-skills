# /interface/wifi/datapath

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/datapath

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `bridge` (iface_enum { none }; unset)
- `bridge-cost` (num; unset)
- `bridge-horizon` (num; unset)
- `openflow-switch` (enum; unset; syscap=openflow)
- `client-isolation` (bool; unset)
- `traffic-processing` (enum: on-cap | on-capsman | on-capsman-secure; unset)
- `vlan-id` (num; unset)
- `interface-list` (enum; unset)
