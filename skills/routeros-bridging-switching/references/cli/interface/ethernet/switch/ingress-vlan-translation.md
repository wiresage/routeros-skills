# /interface/ethernet/switch/ingress-vlan-translation

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/ingress-vlan-translation

Syscap: musicswitch; Type: Directory

The Ingress VLAN Translation table allows for up to 15 entries for each port. One or multiple fields can be selected from the packet header for lookup in the Ingress VLAN Translation table. The S-VLAN or C-VLAN or both configured in the first matched entry are assigned to the packet.

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic

**Arguments**

- `protocol` (alt { protocol-name: enum (length | llc-bpdu) { length:1, llc-bpdu:0x4242 } , protocol-number: num [ .. 65535] }): Matching Ethernet protocol. (only for Ingress VLAN Translation)
- `sa-learning` (bool): Enables or disables source MAC learning after VLAN translation. (only for Ingress VLAN Translation)
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
- `new-customer-vid` (alt { special-vid: enum (service-vid) , vid: num [ .. 4095] }): The new customer VLAN ID replaces the matching customer VLAN ID. If set to 4095 and ingress VLAN translation is used, then traffic is dropped.
- `pcp-propagation` (bool): Enables or disables PCP propagation.
  - If the port type is Edge, the customer PCP is copied from the service PCP.
  - If the port type is Network, the service PCP is copied from the customer PCP.
- `swap-vids` (enum: no | assign-cvid-to-svid)
Below is a table of traffic that triggers a rule that has a certain VLAN format set; note that traffic that is tagged with VLAN ID 0 is a special case that is also taken into account.

| Property | Description |
| :-- | :-- |
| **any** | Accepts:Untagged trafficTagged trafficTagged traffic with priority setVLAN 0 trafficVLAN 0 traffic with priority set |
| **priority-tagged-or-tagged** | Accepts:Tagged trafficTagged traffic with priority setVLAN 0 trafficVLAN 0 traffic with priority set |
| **tagged** | Accepts:Tagged trafficTagged traffic with priority set |
| **untagged-or-tagged** | Accepts:Untagged trafficTagged trafficTagged traffic with priority set |

> **Danger**
>
> If `VLAN-format` is set to `any`, then `customer-vid``/``service-vid` set to `0` will trigger the switch rule with VLAN 0 traffic. In this case, the switch rule will be looking for untagged traffic or traffic with a VLAN 0 tag, and only `untagged-or-tagged` will filter out VLAN 0 traffic.
