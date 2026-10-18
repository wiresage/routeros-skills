# /interface/ethernet/switch/port-isolation

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/port-isolation

## /interface/ethernet/switch/port-isolation

Syscap: musicswitch; Type: Directory

The CRS switches support flexible multi-level isolation features, which can be used for user access control, traffic engineering and advanced security and network management. The isolation features provide an organized fabric structure allowing the user to easily program and control the access by port, MAC address, VLAN, protocol, flow, and frame type. The following isolation and leakage features are supported:

- Port-level isolation
- MAC-level isolation
- VLAN-level isolation
- Protocol-level isolation
- Flow-level isolation
- Free combination of the above

Port-level isolation supports different control schemes on the source port and destination port. Each entry can be programmed with access control for either the source port or the destination port.

- When the entry is programmed with source port access control, the entry is.

applied to the ingress packets.

- When the entry is programmed with destination port access control, the entry

is applied to the egress packets.

**Flags**

- `X`: disabled
- `D`: dynamic
- `I`: invalid

**Arguments**

- `ports` (multi { array-id }): Isolated/leaked ports.
- `type` (enum: src | dst): Lookup type of the isolation/leakage entry:
  - src - Entry applies to ingress packets of the ports.
  - dst - Entry applies to egress packets of the ports.
- `forwarding-type` (ubit (bridged, routed)): Matching traffic forwarding type on Cloud Router Switch.
- `traffic-type` (ubit (unicast, multicast, broadcast)): Matching traffic type.
- `registration-status` (ubit (known, unknown)): Registration status for matching packets. Known ones are present in UFDB and MFDB, and unknown ones are not.
- `protocol-type` (ubit (arp, nd, dhcpv4, dhcpv6, ripv1)): Included protocols for isolation/leakage.
- `flow-id` (num)
- `mac-profile` (enum: promiscuous | isolated | community1 | community2): Matching MAC isolation/leakage profile.
- `port-profile` (num): Matching Port isolation/leakage profile.
- `vlan-profile` (enum: promiscuous | isolated | community1 | community2): Matching VLAN isolation/leakage profile.

## /interface/ethernet/switch/port-isolation

Syscap: rbswitch; Type: Directory

**Flags**

- `I`: invalid

**Arguments**

- `forwarding-override` (multi { array-id, port: alt { port: enum , interface-list: enum } })

**Read-only arguments**

- `name` (string)
- `switch` (enum)
- `current-forwarding-override` (multi { array-id, port: enum })
