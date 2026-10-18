# /interface/ethernet/switch/ingress-port-policer

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/ingress-port-policer

Syscap: musicswitch; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `port` (enum; mandatory): Physical port or trunk for the ingress port policer entry.
- `rate` (num; mandatory): Maximum data rate limit.
- `burst` (num): Maximum data rate which can be transmitted while the burst is allowed.
- `meter-unit` (enum: bit | packet): Measuring units for traffic ingress port policer rate.
- `meter-len` (enum: layer-1 | layer-2 | layer-3): Packet classification which sets the packet byte length for metering.
  - `layer-1` - includes the entire layer-2 frame + FCS + inter-packet gap + preamble.
  - `layer-2` - includes the layer-2 frame + FCS.
  - `layer-3` - includes only the layer-3 + ethernet padding without the layer-2 header and FCS.
- `yellow-action` (enum: drop | forward | remark): Performed action for exceeded traffic.
- `new-dei-for-yellow` (alt { spcial-dei: enum (remap) { remap:0xffffffff } , dei: num [ .. 1] }): Remarked DEI for exceeded traffic if yellow-action is remark.
- `new-pcp-for-yellow` (alt { special-pcp: enum (remap) { remap:0xffffffff } , pcp: num [ .. 7] }): Remarked PCP for exceeded traffic if yellow-action is remark.
- `new-dscp-for-yellow` (alt { special-dscp: enum (remap) { remap:0xffffffff } , dscp: num [ .. 63] }): Remarked DSCP for exceeded traffic if yellow-action is remark.
- `packet-types` (ubit (arp-or-nd, tcp-control, broadcast, unregistered-multicast, registered-multicast, unknown-unicast, known-unicast)): Matching packet types for which the ingress port policer entry is valid.
