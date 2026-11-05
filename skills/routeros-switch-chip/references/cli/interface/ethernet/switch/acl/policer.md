# /interface/ethernet/switch/acl/policer

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/acl/policer

Syscap: musicswitch; Type: Directory

**Flags**

- `I`: invalid

**Arguments**

- `name` (string): Name of the Policer used in ACL.
- `yellow-rate` (num; mandatory): Maximum data rate limit for packets with yellow drop precedence.
- `yellow-burst` (num): Maximum data rate which can be transmitted while the burst is allowed for packets with yellow drop precedence.
- `red-rate` (num): Maximum data rate limit for packets with red drop precedence.
- `red-burst` (num): Maximum data rate which can be transmitted while the burst is allowed for packets with red drop precedence.
- `meter-unit` (enum: bit | packet): Measuring units for ACL traffic rate.
- `meter-len` (enum: layer-1 | layer-2 | layer-3): Packet classification which sets the packet byte length for metering.
  - `layer-1` - includes entire layer-2 frame + FCS + inter-packet gap + preamble.
  - `layer-2` - includes layer-2 frame + FCS.
  - `layer-3` - includes only layer-3 + ethernet padding without layer-2 header and FCS.
- `color-awareness` (bool): `yes` - makes the policer take into account pre-colored drop precedence.
  `no` - ignores drop precedence.
- `bucket-coupling` (bool)
- `yellow-action` (enum: drop | forward | remark): Performed action for exceeded traffic with yellow drop precedence.
- `new-dei-for-yellow` (alt { spcial-dei: enum (remap) { remap:0xffffffff } , dei: num [ .. 1] }): New DEI for yellow drop precedence packets.
- `new-pcp-for-yellow` (alt { special-pcp: enum (remap) { remap:0xffffffff } , pcp: num [ .. 7] }): New PCP for yellow drop precedence packets.
- `new-dscp-for-yellow` (alt { special-dscp: enum (remap) { remap:0xffffffff } , dscp: num [ .. 63] }): New DSCP for yellow drop precedence packets.
- `red-action` (enum: drop | forward | remark): Performed action for exceeded traffic with red drop precedence.
- `new-dei-for-red` (alt { spcial-dei: enum (remap) { remap:0xffffffff } , dei: num [ .. 1] }): New DEI for red drop precedence packets.
- `new-pcp-for-red` (alt { special-pcp: enum (remap) { remap:0xffffffff } , pcp: num [ .. 7] }): New PCP for red drop precedence packets.
- `new-dscp-for-red` (alt { special-dscp: enum (remap) { remap:0xffffffff } , dscp: num [ .. 63] }): New DSCP for red drop precedence packets.

**Read-only arguments**

- `green-counter` (num)
- `yellow-counter` (num)
- `red-counter` (num)
