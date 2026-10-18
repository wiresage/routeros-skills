# /interface/ethernet/switch/egress-vlan-translation

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/egress-vlan-translation

Syscap: musicswitch; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic

**Arguments**

- `ports` (multi { array-id }; mandatory): Matching switch ports for VLAN translation rule.
- `service-vlan-format` (enum: untagged-or-tagged | priority-tagged-or-tagged | tagged | any): Type of frames with service tag for which VLAN translation rule is valid.
- `service-vid` (num): Matching VLAN ID of the service tag.
- `service-pcp` (num): Matching PCP of the service tag.
- `service-dei` (num): Matching DEI of the service tag.
- `customer-vlan-format` (enum: untagged-or-tagged | priority-tagged-or-tagged | tagged | any): Type of frames with customer tag for which VLAN translation rule is valid.
- `customer-vid` (num): Matching the VLAN ID of the customer tag.
- `customer-pcp` (num): Matching PCP of the customer tag.
- `customer-dei` (num): Matching DEI of the customer tag.
- `new-service-vid` (alt { special-vid: enum (customer-vid) , vid: num [ .. 4095] }): The new service VLAN ID replaces the matching service VLAN ID.
- `new-customer-vid` (alt { special-vid: enum (service-vid) , vid: num [ .. 4095] }): The new customer VLAN ID replaces the matching customer VLAN ID.
- `pcp-propagation` (bool): Enables or disables PCP propagation.
  - If the port type is Edge, the customer PCP is copied from the service PCP.
  - If the port type is Network, the service PCP is copied from the customer PCP.
- `swap-vids` (enum: no | assign-cvid-to-svid)
