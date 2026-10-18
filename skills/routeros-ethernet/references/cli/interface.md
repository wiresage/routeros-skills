# /interface

> Source: https://manual.mikrotik.com/docs/cli-reference/interface

Type: Directory

Interface list with counters and state. Each interface row counts its own packets and bytes; values beginning with `fp` show the Fast Path share of that traffic (streamlined CPU forwarding; HW-offloaded traffic shows in neither), and `tx-queue-drop` counts the packets dropped by the interface queue.

**Flags**

- `D` (dynamic): dynamic (created automatically)
- `X`: disabled
- `I`: inactive
- `R`: running
- `S` (slave): slave (member of a bridge or bond)
- `P`: passthrough
- `w` (power-limited): power-limited (on PoE-out boards the power budget is in effect)

**Arguments**

- `name` (string): Name of the interface
- `mtu` (num): Configured MTU
- `l2mtu` (num): Configured layer-2 MTU

**Read-only arguments**

- `default-name` (string): The factory-set name of the interface
- `type` (string): Interface type
- `actual-mtu` (num): MTU in effect (hardware/driver negotiated)
- `max-l2mtu` (num): Maximum layer-2 MTU the hardware/driver supports
- `vrf` (enum): VRF the interface is bound to (blank for the main routing table)
- `mac-address` (macAddr): MAC address of the interface
- `last-link-down-time` (date): Time the link last went down
- `last-link-up-time` (date): Time the link last came up
- `link-downs` (num): How many times the link has gone down
- `rx-byte` (num): Bytes received
- `tx-byte` (num): Bytes transmitted
- `rx-packet` (num): Packets received
- `tx-packet` (num): Packets transmitted
- `rx-drop` (num): Packets received and dropped
- `tx-drop` (num): Packets dropped during transmission
- `tx-queue-drop` (num): Packets dropped by the interface queue (congestion signal)
- `rx-error` (num): Corrupted receive frames
- `tx-error` (num): Transmission errors
- `fp-rx-byte` (num): Bytes received over Fast Path
- `fp-tx-byte` (num): Bytes transmitted over Fast Path
- `fp-rx-packet` (num): Packets received over Fast Path
- `fp-tx-packet` (num): Packets transmitted over Fast Path
- `fp-rps-drop` (num): Packets dropped in the receive-packet-steering path

## Commands

### /interface/blink

Type: Command

### /interface/reset-counters

Type: Command
