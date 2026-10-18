# /interface/ethernet/switch/qos/priority-flow-control

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/priority-flow-control

Syscap: rbswitch and crs_prestera and !prestera-ac3; Type: Directory

[PFC](../../../../../guides/bridging-and-switching/quality-of-service.md#priority-based-flow-control-pfc) configuration is organized in profiles. Different switch ports can be assigned to different PFC profiles. The maximum number of hardware Tx managers depends on the switch chip model. The builtin profile named "**disabled**" cannot be changed.

**Flags**

- `*`: default
- `X`: disabled
- `I`: inactive
- `H`: hw-offloaded

**Arguments**

- `name` (string; mandatory): The user-defined name of the PFC profile.
- `traffic-class` (multi { array-id, tc: num [ .. 7] }; mandatory): The list of PFC-enabled traffic classes.
- `rx` (bool): Enables receiving of PFC frames. The received PFC frame pauses the specific priority queues on the port that received the PFC frame for the duration specified by the PFC frame. Disabling rx disables queue pausing.
- `tx` (bool): Enables transmission of PFC frames.
- `pause-threshold` (alt { pause-threshold-pct: num [ .. 100] , pause-threshold-byte: num [1536 .. ] }): Transmits a pause frame (XOFF) when the total size of enqueued packets reaches this threshold. Enqueued packets are counted per ingress port. Applies only when **tx=yes**. The value can be given either explicitly in bytes or percent of the respective shared pool size (**shared-poolX-byte-cap**).
- `resume-threshold` (alt { resume-threshold-pct: num [ .. 100] , resume-threshold-byte: num [256 .. ] }): Transmits a resume frame (XON) when the total size of enqueued packets drops down to this threshold. Enqueued packets are counted per ingress port. Applies only when **tx=yes**. The value can be given either explicitly in bytes or percent of the respective shared pool size (**shared-poolX-byte-cap**).

**Read-only arguments**

- `hw-id` (num)
