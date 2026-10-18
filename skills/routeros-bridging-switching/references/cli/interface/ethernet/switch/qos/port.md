# /interface/ethernet/switch/qos/port

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/port

Syscap: rbswitch and crs_prestera; Type: Directory

This sub-menu configures QoS settings for individual switch ports. It allows you to assign a QoS profile to ingress packets arriving on a specific port. If the port is configured as trusted, the assigned profile can be overridden by match rules based on packet header values.

By default, all ports are untrusted and receive the default QoS profile (Best-Effort, PCP=0, DSCP=0). In this default state, priority fields are cleared from egress packets.

**Flags**

- `I`: invalid
- `R`: running

**Arguments**

- `profile` (enum; syscap=crs_prestera): QoS profile to assign to ingress packets by default.
- `map` (enum; syscap=crs_prestera): QoS Packet-to-Profile mapping.
- `trust-l2` (enum: ignore | trust | keep; syscap=crs_prestera): Trust Layer 2 header (PCP) for QoS mapping.
- `trust-l3` (enum: ignore | trust | keep; syscap=crs_prestera): Trust Layer 3 header (DSCP) for QoS mapping.
- `tx-manager` (enum; syscap=crs_prestera): QoS Tx Manager for egress traffic on this port.
- `pfc` (enum; syscap=!prestera-ac3): Priority Flow Control profile for ingress traffic on this port.
- `egress-rate-queue0` (num; syscap=switch-rate): Egress rate limit for queue 0.
- `egress-rate-queue1` (num; syscap=switch-rate): Egress rate limit for queue 1.
- `egress-rate-queue2` (num; syscap=switch-rate): Egress rate limit for queue 2.
- `egress-rate-queue3` (num; syscap=switch-rate): Egress rate limit for queue 3.
- `egress-rate-queue4` (num; syscap=switch-rate): Egress rate limit for queue 4.
- `egress-rate-queue5` (num; syscap=switch-rate): Egress rate limit for queue 5.
- `egress-rate-queue6` (num; syscap=switch-rate): Egress rate limit for queue 6.
- `egress-rate-queue7` (num; syscap=switch-rate): Egress rate limit for queue 7.
**Port Stats**

```ros
[admin@Mikrotik] /interface/ethernet/switch/qos/port> print stats where name=ether2
                  name:     ether2
             tx-packet:      2 887
               tx-byte:  3 938 897
           drop-packet:      1 799
             drop-byte:  2 526 144
      tx-queue0-packet:         50
      tx-queue1-packet:      1 871
      tx-queue3-packet:        774
      tx-queue5-packet:        192
        tx-queue0-byte:      3 924
        tx-queue1-byte:  2 468 585
        tx-queue3-byte:  1 174 932
        tx-queue5-byte:    291 456
    drop-queue1-packet:      1 799
      drop-queue1-byte:  2 526 144
```

**Port Resources/Usage**

> **Danger**
>
> Due to hardware limitations, some switch chip models may break traffic flow while accessing QoS port `usage` data. Use port `usage` for diagnostics/troubleshooting only. For monitoring, use QoS `monitor` or Port `stats` instead.

```ros
[admin@crs326] /interface/ethernet/switch/qos/port> print usage where name=ether2
                 name:  ether2
           packet-cap:     136
           packet-use:       5
             byte-cap:  35 840
             byte-use:   9 472
    queue0-packet-cap:     130
    queue0-packet-use:       1
    queue1-packet-cap:       5
    queue1-packet-use:       4
    queue3-packet-cap:      65
    queue3-packet-use:       2
      queue0-byte-cap:  24 576
      queue0-byte-use:     256
      queue1-byte-cap:   7 680
      queue1-byte-use:   6 144
      queue3-byte-cap:  14 080
      queue3-byte-use:   3 072
```

**Port PFC Stats (Previous Generations)**
```ros
[admin@crs317] /interface/ethernet/switch/qos/port> print pfc interval=1 where running
                 name:  sfp-sfpplus1 sfp-sfpplus2   ether1
                  pfc:          roce     disabled disabled
               pfc-tx:            46
        pfc-paused-tc:             3
 pfc3-pause-threshold:     1 048 576
pfc3-resume-threshold:        10 240
             pfc3-use:     1 075 200
```

**Port PFC Stats (New Generations)**
```routeros
[admin@crs812] /interface/ethernet/switch/qos/port> print pfc interval=1 where pfc=roce
                 name:       sfp56-5
                  pfc:          roce
             rx-pause:           287
             tx-pause:            46
             pfc3-use:     2 184 200
```

**Read-only arguments**

- `name` (string): Port name.
- `switch` (enum): Switch chip name.
- `tx-packet` (multi { counter: num }): The total number of packets transmitted via this port.
- `tx-bytes` (multi { counter: num }): The total number of bytes transmitted via this port.
- `packet-use` (num; syscap=!prestera-cpss): Port's packet usage. The number of packets currently enqueued in all port's queues.
- `byte-use` (num): Port's byte usage. The size of hardware buffers (in bytes) that are currently allocated for the enqueued packets. Since the buffers are allocated by blocks (usually - 256B each), the allocated buffer size can be bigger than the actual payload.
- `queue0-shared-packet-cap` (num; syscap=prestera-bc2): Shared queue capacity (individual queue capacity + shared buffers) for queue 0.
- `queue1-shared-packet-cap` (num; syscap=prestera-bc2): Shared queue capacity (individual queue capacity + shared buffers) for queue 1.
- `queue2-shared-packet-cap` (num; syscap=prestera-bc2): Shared queue capacity (individual queue capacity + shared buffers) for queue 2.
- `queue3-shared-packet-cap` (num; syscap=prestera-bc2): Shared queue capacity (individual queue capacity + shared buffers) for queue 3.
- `queue4-shared-packet-cap` (num; syscap=prestera-bc2): Shared queue capacity (individual queue capacity + shared buffers) for queue 4.
- `queue5-shared-packet-cap` (num; syscap=prestera-bc2): Shared queue capacity (individual queue capacity + shared buffers) for queue 5.
- `queue6-shared-packet-cap` (num; syscap=prestera-bc2): Shared queue capacity (individual queue capacity + shared buffers) for queue 6.
- `queue7-shared-packet-cap` (num; syscap=prestera-bc2): Shared queue capacity (individual queue capacity + shared buffers) for queue 7.
- `queue0-shared-byte-cap` (num; syscap=!prestera-ac3): Shared queue capacity (individual queue capacity + shared buffers) for queue 0.
- `queue1-shared-byte-cap` (num; syscap=!prestera-ac3): Shared queue capacity (individual queue capacity + shared buffers) for queue 1.
- `queue2-shared-byte-cap` (num; syscap=!prestera-ac3): Shared queue capacity (individual queue capacity + shared buffers) for queue 2.
- `queue3-shared-byte-cap` (num; syscap=!prestera-ac3): Shared queue capacity (individual queue capacity + shared buffers) for queue 3.
- `queue4-shared-byte-cap` (num; syscap=!prestera-ac3): Shared queue capacity (individual queue capacity + shared buffers) for queue 4.
- `queue5-shared-byte-cap` (num; syscap=!prestera-ac3): Shared queue capacity (individual queue capacity + shared buffers) for queue 5.
- `queue6-shared-byte-cap` (num; syscap=!prestera-ac3): Shared queue capacity (individual queue capacity + shared buffers) for queue 6.
- `queue7-shared-byte-cap` (num; syscap=!prestera-ac3): Shared queue capacity (individual queue capacity + shared buffers) for queue 7.
- `queue0-packet-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of packets that can be enqueued in queue 0.
- `queue1-packet-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of packets that can be enqueued in queue 1.
- `queue2-packet-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of packets that can be enqueued in queue 2.
- `queue3-packet-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of packets that can be enqueued in queue 3.
- `queue4-packet-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of packets that can be enqueued in queue 4.
- `queue5-packet-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of packets that can be enqueued in queue 5.
- `queue6-packet-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of packets that can be enqueued in queue 6.
- `queue7-packet-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of packets that can be enqueued in queue 7.
- `queue0-byte-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of bytes that can be enqueued in queue 0.
- `queue1-byte-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of bytes that can be enqueued in queue 1.
- `queue2-byte-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of bytes that can be enqueued in queue 2.
- `queue3-byte-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of bytes that can be enqueued in queue 3.
- `queue4-byte-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of bytes that can be enqueued in queue 4.
- `queue5-byte-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of bytes that can be enqueued in queue 5.
- `queue6-byte-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of bytes that can be enqueued in queue 6.
- `queue7-byte-cap` (num; syscap=!prestera-cpss): Individual queue capacity. The maximum number of bytes that can be enqueued in queue 7.
- `queue0-packet-use` (num; syscap=!prestera-cpss): Queue packet usage. The number of enqueued packets in queue 0.
- `queue1-packet-use` (num; syscap=!prestera-cpss): Queue packet usage. The number of enqueued packets in queue 1.
- `queue2-packet-use` (num; syscap=!prestera-cpss): Queue packet usage. The number of enqueued packets in queue 2.
- `queue3-packet-use` (num; syscap=!prestera-cpss): Queue packet usage. The number of enqueued packets in queue 3.
- `queue4-packet-use` (num; syscap=!prestera-cpss): Queue packet usage. The number of enqueued packets in queue 4.
- `queue5-packet-use` (num; syscap=!prestera-cpss): Queue packet usage. The number of enqueued packets in queue 5.
- `queue6-packet-use` (num; syscap=!prestera-cpss): Queue packet usage. The number of enqueued packets in queue 6.
- `queue7-packet-use` (num; syscap=!prestera-cpss): Queue packet usage. The number of enqueued packets in queue 7.
- `queue0-byte-use` (num): Queue buffer usage (in bytes) for queue 0.
- `queue1-byte-use` (num): Queue buffer usage (in bytes) for queue 1.
- `queue2-byte-use` (num): Queue buffer usage (in bytes) for queue 2.
- `queue3-byte-use` (num): Queue buffer usage (in bytes) for queue 3.
- `queue4-byte-use` (num): Queue buffer usage (in bytes) for queue 4.
- `queue5-byte-use` (num): Queue buffer usage (in bytes) for queue 5.
- `queue6-byte-use` (num): Queue buffer usage (in bytes) for queue 6.
- `queue7-byte-use` (num): Queue buffer usage (in bytes) for queue 7.
- `byte-max` (num; syscap=prestera-bc2): Maximum port buffer fill level (in bytes). Use the reset-counters command to reset values.
- `queue0-byte-max` (num; syscap=!prestera-ac3): Maximum queue buffer fill level (in bytes) for queue 0.
- `queue1-byte-max` (num; syscap=!prestera-ac3): Maximum queue buffer fill level (in bytes) for queue 1.
- `queue2-byte-max` (num; syscap=!prestera-ac3): Maximum queue buffer fill level (in bytes) for queue 2.
- `queue3-byte-max` (num; syscap=!prestera-ac3): Maximum queue buffer fill level (in bytes) for queue 3.
- `queue4-byte-max` (num; syscap=!prestera-ac3): Maximum queue buffer fill level (in bytes) for queue 4.
- `queue5-byte-max` (num; syscap=!prestera-ac3): Maximum queue buffer fill level (in bytes) for queue 5.
- `queue6-byte-max` (num; syscap=!prestera-ac3): Maximum queue buffer fill level (in bytes) for queue 6.
- `queue7-byte-max` (num; syscap=!prestera-ac3): Maximum queue buffer fill level (in bytes) for queue 7.
- `pfc0-pause-threshold` (num; syscap=prestera-bc2): Pause threshold of traffic class 0.
- `pfc1-pause-threshold` (num; syscap=prestera-bc2): Pause threshold of traffic class 1.
- `pfc2-pause-threshold` (num; syscap=prestera-bc2): Pause threshold of traffic class 2.
- `pfc3-pause-threshold` (num; syscap=prestera-bc2): Pause threshold of traffic class 3.
- `pfc4-pause-threshold` (num; syscap=prestera-bc2): Pause threshold of traffic class 4.
- `pfc5-pause-threshold` (num; syscap=prestera-bc2): Pause threshold of traffic class 5.
- `pfc6-pause-threshold` (num; syscap=prestera-bc2): Pause threshold of traffic class 6.
- `pfc7-pause-threshold` (num; syscap=prestera-bc2): Pause threshold of traffic class 7.
- `pfc0-resume-threshold` (num; syscap=prestera-bc2): Resume threshold of traffic class 0.
- `pfc1-resume-threshold` (num; syscap=prestera-bc2): Resume threshold of traffic class 1.
- `pfc2-resume-threshold` (num; syscap=prestera-bc2): Resume threshold of traffic class 2.
- `pfc3-resume-threshold` (num; syscap=prestera-bc2): Resume threshold of traffic class 3.
- `pfc4-resume-threshold` (num; syscap=prestera-bc2): Resume threshold of traffic class 4.
- `pfc5-resume-threshold` (num; syscap=prestera-bc2): Resume threshold of traffic class 5.
- `pfc6-resume-threshold` (num; syscap=prestera-bc2): Resume threshold of traffic class 6.
- `pfc7-resume-threshold` (num; syscap=prestera-bc2): Resume threshold of traffic class 7.
- `pfc0-use` (num; syscap=!prestera-ac3): Current buffer usage of traffic class 0 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
- `pfc1-use` (num; syscap=!prestera-ac3): Current buffer usage of traffic class 1 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
- `pfc2-use` (num; syscap=!prestera-ac3): Current buffer usage of traffic class 2 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
- `pfc3-use` (num; syscap=!prestera-ac3): Current buffer usage of traffic class 3 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
- `pfc4-use` (num; syscap=!prestera-ac3): Current buffer usage of traffic class 4 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
- `pfc5-use` (num; syscap=!prestera-ac3): Current buffer usage of traffic class 5 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
- `pfc6-use` (num; syscap=!prestera-ac3): Current buffer usage of traffic class 6 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
- `pfc7-use` (num; syscap=!prestera-ac3): Current buffer usage of traffic class 7 (in bytes). In other words, it is the total size of all queued packets on all ports that were received from this port. Only PFC-enabled traffic classes are displayed.
- `pfc-paused-tc` (multi { array-id, tc: num }; syscap=prestera-bc2): The list of traffic classes that should be paused. PFC pause frames (XOFF) are periodically sent with the listed timers set from this port.
- `pfc-unknown` (multi { counter: num }; syscap=prestera-bc2): Unknown PFC frame count.
- `pfc-rx` (multi { counter: num }; syscap=prestera-bc2): Received PFC frame count.
- `pfc-tx` (num; syscap=prestera-bc2): Transmitted PFC frame count.
- `rx-pause` (multi { counter: num }; syscap=prestera-cpss): Received pause frame count.
- `tx-pause` (multi { counter: num }; syscap=prestera-cpss): Transmitted pause frame count.
- `tx-queue0-packet` (multi { counter: num }): The number of packets transmitted via this port from queue 0.
- `tx-queue0-byte` (multi { counter: num }): The number of bytes transmitted via this port from queue 0.
- `tx-queue1-packet` (multi { counter: num }): The number of packets transmitted via this port from queue 1.
- `tx-queue1-byte` (multi { counter: num }): The number of bytes transmitted via this port from queue 1.
- `tx-queue2-packet` (multi { counter: num }): The number of packets transmitted via this port from queue 2.
- `tx-queue2-byte` (multi { counter: num }): The number of bytes transmitted via this port from queue 2.
- `tx-queue3-packet` (multi { counter: num }): The number of packets transmitted via this port from queue 3.
- `tx-queue3-byte` (multi { counter: num }): The number of bytes transmitted via this port from queue 3.
- `tx-queue4-packet` (multi { counter: num }): The number of packets transmitted via this port from queue 4.
- `tx-queue4-byte` (multi { counter: num }): The number of bytes transmitted via this port from queue 4.
- `tx-queue5-packet` (multi { counter: num }): The number of packets transmitted via this port from queue 5.
- `tx-queue5-byte` (multi { counter: num }): The number of bytes transmitted via this port from queue 5.
- `tx-queue6-packet` (multi { counter: num }): The number of packets transmitted via this port from queue 6.
- `tx-queue6-byte` (multi { counter: num }): The number of bytes transmitted via this port from queue 6.
- `tx-queue7-packet` (multi { counter: num }): The number of packets transmitted via this port from queue 7.
- `tx-queue7-byte` (multi { counter: num }): The number of bytes transmitted via this port from queue 7.
- `tx-drop-packet` (multi { counter: num }): Total transmitted packets dropped.
- `tx-drop-byte` (multi { counter: num }): Total transmitted bytes dropped.
- `tx-drop-queue0-packet` (multi { counter: num }): The number of packets dropped from queue 0.
- `tx-drop-queue0-byte` (multi { counter: num }): The number of bytes dropped from queue 0.
- `tx-drop-queue1-packet` (multi { counter: num }): The number of packets dropped from queue 1.
- `tx-drop-queue1-byte` (multi { counter: num }): The number of bytes dropped from queue 1.
- `tx-drop-queue2-packet` (multi { counter: num }): The number of packets dropped from queue 2.
- `tx-drop-queue2-byte` (multi { counter: num }): The number of bytes dropped from queue 2.
- `tx-drop-queue3-packet` (multi { counter: num }): The number of packets dropped from queue 3.
- `tx-drop-queue3-byte` (multi { counter: num }): The number of bytes dropped from queue 3.
- `tx-drop-queue4-packet` (multi { counter: num }): The number of packets dropped from queue 4.
- `tx-drop-queue4-byte` (multi { counter: num }): The number of bytes dropped from queue 4.
- `tx-drop-queue5-packet` (multi { counter: num }): The number of packets dropped from queue 5.
- `tx-drop-queue5-byte` (multi { counter: num }): The number of bytes dropped from queue 5.
- `tx-drop-queue6-packet` (multi { counter: num }): The number of packets dropped from queue 6.
- `tx-drop-queue6-byte` (multi { counter: num }): The number of bytes dropped from queue 6.
- `tx-drop-queue7-packet` (multi { counter: num }): The number of packets dropped from queue 7.
- `tx-drop-queue7-byte` (multi { counter: num }): The number of bytes dropped from queue 7.

## Commands

### /interface/ethernet/switch/qos/port/reset-counters

Syscap: rbswitch and crs_prestera; Type: Command
