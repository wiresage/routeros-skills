# /caps-man/datapath

> Source: https://manual.mikrotik.com/docs/cli-reference/caps-man/datapath

Package: wireless-rep; Type: Directory

**Arguments**

- `name` (string; mandatory)
- `mtu` (num)
- `l2mtu` (num)
- `arp` (enum: disabled | enabled | proxy-arp | reply-only | local-proxy-arp)
- `client-to-client-forwarding` (bool; unset)
- `bridge` (iface_enum; unset)
- `bridge-cost` (num; unset)
- `bridge-horizon` (num; unset)
- `openflow-switch` (enum; unset)
- `local-forwarding` (bool; unset)
- `vlan-mode` (enum: no-tag | use-tag | use-service-tag; unset)
- `vlan-id` (num; unset)
- `interface-list` (enum; unset)
