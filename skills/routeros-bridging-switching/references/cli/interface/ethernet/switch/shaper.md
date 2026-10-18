# /interface/ethernet/switch/shaper

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/shaper

Syscap: musicswitch; Type: Directory

Traffic shaping restricts the rate and burst size of the flow which is transmitted out from the interface. The shaper is implemented by a token bucket. If the packet exceeds the maximum rate or the burst size, which means not enough tokens for the packet, the packet is stored in the buffer until there are enough tokens to transmit it.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `port` (enum; mandatory): Physical port for traffic shaper.
- `target` (enum: queue0 | queue1 | queue2 | queue3 | queue4 | queue5 | queue6 | queue7 | wrr-group0 | wrr-group1 | port): Three levels of shapers are supported on each port (including CPU port).
  - `port` - entry applies to the port of the switch-chip.
  - `wrr-group0` or `wrr-group1` - entry applies to one of the 2 Weighted Round Robin queue groups on the port.
  - `queue0`-`queue7` - entry applies to one of the 8 queues on the port.
- `meter-unit` (enum: bit | packet): Measuring units for traffic shaper rate.
- `rate` (num): Maximum data rate limit.
- `burst` (num): Maximum data rate which can be transmitted while the burst is allowed.
