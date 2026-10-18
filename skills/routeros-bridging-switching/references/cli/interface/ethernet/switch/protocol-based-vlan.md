# /interface/ethernet/switch/protocol-based-vlan

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/protocol-based-vlan

Syscap: musicswitch; Type: Directory

The Protocol Based VLAN table is used to assign VID and QoS attributes to related protocol packets per port.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `frame-type` (enum: ethernet | rfc-1042 | llc): Encapsulation type of the matching frames.
- `protocol` (alt { protocol: enum () , protocol-number: num [ .. 65535] }): Matching protocol for Protocol-based VLAN rule.
- `ports` (multi { array-id }; mandatory): Matching switch ports for Protocol-based VLAN rule.
- `set-service-vid-for` (enum: none | untagged-or-priority-tagged | tagged | all): Service VLAN ID assignment command for different packet types.
- `new-service-vid` (num): The new service VLAN ID replaces the original service VLAN ID for the specified protocol.
- `set-customer-vid-for` (enum: none | untagged-or-priority-tagged | tagged | all): Customer VLAN ID assignment command for different packet types.
- `new-customer-vid` (num): The new customer VLAN ID replaces the original customer VLAN ID for the specified protocol. If set to 4095, then traffic is dropped.
- `set-qos-for` (enum: none | untagged-or-priority-tagged | tagged | all): Frame type for which QoS assignment command applies.
- `qos-group` (enum (none) { none:0xffffffff }): Defined QoS group from the QoS group menu.
