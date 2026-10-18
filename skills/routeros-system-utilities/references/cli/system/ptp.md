# /system/ptp

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ptp

Conditions: !smips; Syscap: ptp; Type: Directory

PTP (IEEE 1588-2008, PTPv2) instance configuration. Each entry is one PTP profile instance; ports join it in [`/system/ptp/port`](ptp/port.md). Supported only on specific switch/router hardware (see the [Precision Time Protocol](../../guides/system-information-and-utilities/precision-time-protocol.md) guide).

**Flags**

- `I`: inactive
- `X`: disabled

**Arguments**

- `name` (string): Name of the PTP profile instance
- `priority1` (enum: auto): First value of the grandmaster election; the lower value wins. With `auto`, the value of the chosen profile applies (802.1AS: 246, other profiles: 128)
- `priority2` (enum: auto): Second value of the grandmaster election, used for ties. With `auto`, the value of the chosen profile applies (802.1AS: 248, other profiles: 128)
- `delay-mode` (enum: auto | e2e | p2p): Delay measurement mechanism: `e2e` (request-response) or `p2p` (peer delay). With `auto`, the profile default applies (802.1AS: p2p, other profiles: e2e)
- `transport` (enum: auto | ipv4 | l2-non-forwardable | l2-forwardable): Transport used for PTP messages: `ipv4` (multicast 224.0.1.129 for PTP primary messages and 224.0.0.107 for peer delay messages), `l2-forwardable` (multicast MAC 01-1B-19-00-00-00, forwarded by PTP-unaware bridges) or `l2-non-forwardable` (01-80-C2-00-00-0E, not forwarded by compliant bridges). With `auto`, the profile default applies (802.1AS and G.8275.1 use `l2-non-forwardable`; AES67, SMPTE and the default profile use `ipv4`)
- `profile` (enum: default | 802.1as | g8275.1 | aes67 | smpte-2059): Operating profile: `default` (plain PTPv2), `802.1as` (AVB/TSN, IEEE 802.1AS-2020), `aes67` (audio over IP), `g8275.1` (telecom frequency and phase), `smpte-2059` (professional broadcast). The profile also presets the auto values of domain, priority1/2, transport and delay-mode
- `domain` (enum: auto): PTP domain number separating independent PTP instances on one network. Allowed ranges differ per profile (0-127 for most, 24-43 for G.8275.1). With `auto`, the profile default applies (default profile/AES67: 0, G.8275.1: 24, SMPTE: 127)
- `ptp-mode` (enum: ordinary-clock | transparent-clock): Clock mode of the instance: an ordinary clock (end device; grandmaster or slave) or a transparent clock (measures and forwards residence time without acting as an end device)

## Commands

### /system/ptp/monitor

Conditions: !smips; Syscap: ptp; Type: Command

Show the detailed status and synchronization accuracy of a PTP profile instance, `monitor <number or name>`.

**Read-only arguments**

- `name` (string): Name of the PTP profile instance
- `clock-id` (string): Identifier of the local clock
- `priority1` (num): The local priority1 value in the grandmaster election
- `priority2` (num): The local priority2 value in the grandmaster election
- `i-am-gm` (bool): Whether this device is the grandmaster clock
- `gm-clock-id` (string): Identifier of the grandmaster clock
- `gm-priority1` (num): The priority1 of the grandmaster clock
- `gm-priority2` (num): The priority2 of the grandmaster clock
- `master-clock-id` (string): Identifier of the master clock in the PTP path (the grandmaster clock or a boundary clock)
- `slave-port` (iface_enum): The local port connected towards the master clock
- `freq-drift` (num): Frequency drift between the master and the slave clock, in parts per billion
- `offset` (num): Time difference between the master and the slave clock, in nanoseconds
- `slave-port-delay` (num): Measured delay for packets between the two clocks, in nanoseconds (cable and transceiver lengths matter)
