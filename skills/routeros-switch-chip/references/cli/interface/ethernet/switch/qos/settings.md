# /interface/ethernet/switch/qos/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/settings

Syscap: rbswitch and crs_prestera; Type: Settings Directory

**Arguments**

- `multicast-buffers` (num): Maximum amount of packet buffers for multicast traffic (% of total buffer memory).
- `mirror-buffers` (num; syscap=!prestera-cpss): Maximum number of packet buffers for [mirrored](../../../../../guides/bridging-and-switching/marvell-prestera-switch-chip-features.md#mirroring) traffic (% of the total buffer memory).
- `mirror-profile` (enum): The name of the [QoS profile](profile.md) to assign to the [mirrored](../../../../../guides/bridging-and-switching/marvell-prestera-switch-chip-features.md#mirroring) packets.
- `shared-buffers` (num): Maximum number of packet buffers that are shared between ports (% of the total buffer memory). Setting it to 0 disables buffer sharing. The remaining buffer memory is split between the ports.
  All buffers are treated as shared on new generation switch chips that use **Dynamic Buffers**. The switch chip automatically adjusts port and queue buffer limits based on the current congestion level. Using the auto value allows the device to utilize 100% of the available buffer memory, which is the recommended setting for most scenarios. In specific use cases where latency is more important than avoiding packet drops, the buffer limit can be manually reduced.
- `lossless-buffers` (num; syscap=!prestera-ac3): If the device supports multiple shared buffer pools, this setting allows adjusting the size of the lossless pool (% of the shared buffer memory, where 100% means all shared buffers allocated by the `shared-buffers` setting). For example, if shared-buffers=50 and lossless-buffers=80, the lossless pool receives 40% of the total buffer memory (80% of 50% or "0.8 * 0.5 = 0.4"), and the lossy pool receives the remaining 10% of shared buffers.
- `lossless-traffic-class` (multi { array-id, tc: num [ .. 7] }; syscap=!prestera-ac3): The list of lossless traffic classes.
- `wred-threshold` (enum: low | medium | high; syscap=!prestera-ac3): A relative number of packets above a shared queue cap (`queueX-shared-packet-cap` or `queueX-shared-byte-cap`) where random drops take place. This threshold is applied only to queues with enabled [Weighted Random Early Detection](../../../../../guides/bridging-and-switching/quality-of-service.md#weighted-random-early-detection-wred) (`wred=yes`) that use shared buffers (`use-shared-buffers=yes`). The higher the queue buffer fill level, the higher the packet drop chance. The `low` threshold means the random tail drop starts later; the `high` - sooner.
