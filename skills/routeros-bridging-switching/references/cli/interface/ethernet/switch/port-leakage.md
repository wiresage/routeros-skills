# /interface/ethernet/switch/port-leakage

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/port-leakage

Syscap: musicswitch; Type: Directory

Port leakage allows bypassing egress VLAN filtering on the port. A leaky port is allowed to access other ports for various applications such as security, network control, and management. Note: When both isolation and leakage are applied to the same port, the port is isolated.

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
