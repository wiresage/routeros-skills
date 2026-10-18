# /interface/ethernet/switch/qos

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos

Syscap: rbswitch and crs_prestera; Type: Directory

The entire QoS hardware configuration is located under `/in/eth/sw/qos`. This centralized approach allows you to store all QoS-related configuration items in one place, making it easy to monitor and export settings using `/in/eth/sw/qos/export`.

QoS entries have two major flag indicators:

- **H** - Hardware-offloaded entry.
- **I** - Inactive entry.

## Commands

### /interface/ethernet/switch/qos/monitor

Syscap: rbswitch and crs_prestera; Type: Command

Monitors hardware QoS resources.

```ros
[admin@crs312] /interface/ethernet/switch/qos> monitor once
           total-packet-cap: 11 480
           total-packet-use: 0
             total-byte-cap: 2648.0KiB
             total-byte-use: 0
       multicast-packet-cap: 1 148
       multicast-packet-use: 0
         multicast-byte-cap: 264.8KiB
         multicast-byte-use: 0
  mirror-ingress-packet-cap: 1 148
  mirror-ingress-packet-use: 0
    mirror-ingress-byte-cap: 264.8KiB
    mirror-ingress-byte-use: 0
   mirror-egress-packet-cap: 1 148
   mirror-egress-packet-use: 0
     mirror-egress-byte-cap: 264.8KiB
     mirror-egress-byte-use: 0
      lossy-pool-packet-cap: 2 301
      lossy-pool-packet-use: 0
   lossless-pool-packet-cap: 2 301
   lossless-pool-packet-use: 0
        lossy-pool-byte-cap: 530.0KiB
        lossy-pool-byte-use: 0
     lossless-pool-byte-cap: 530.0KiB
     lossless-pool-byte-use: 0
```

**Read-only arguments**

- `total-packet-cap` (num; syscap=!prestera-cpss): Total packet capacity. The maximum number of hardware packet descriptors that the device can store in all queues.
- `total-packet-use` (num; syscap=!prestera-cpss): Total packet usage. The current number of packet descriptors residing in the hardware memory.
- `total-byte-cap` (num): Total tx memory capacity.
- `total-byte-use` (num): Total tx memory usage. The current number of bytes occupied by the packets in all tx queues.
- `multicast-packet-cap` (num; syscap=!prestera-cpss): Multicast packet capacity. The maximum number of hardware packet descriptors that can be used by multicast/broadcast traffic. Depends on the `multicast-buffers` setting.
- `multicast-packet-use` (num; syscap=!prestera-cpss): Multicast packet usage. The hardware makes a copy of the packet descriptor for each multicast destination.
- `multicast-byte-cap` (num; syscap=!prestera-ac3): Multicast byte capacity.
- `multicast-byte-use` (num; syscap=prestera-bc2): Multicast byte usage.
- `mirror-ingress-packet-cap` (num; syscap=!prestera-cpss): Ingress mirror packet capacity. The maximum number of hardware packet descriptors that can be used by ingress mirrored traffic. Depends on the `mirror-buffers` setting.
- `mirror-ingress-packet-use` (num; syscap=!prestera-cpss): Ingress mirror packet usage.
- `mirror-ingress-byte-cap` (num; syscap=prestera-bc2): Ingress mirror byte capacity. Depends on the `mirror-buffers` setting.
- `mirror-ingress-byte-use` (num; syscap=prestera-bc2): Ingress mirror byte usage.
- `mirror-egress-packet-cap` (num; syscap=!prestera-cpss): Egress mirror packet capacity. The maximum number of hardware packet descriptors that can be used by egress mirrored traffic. Depends on the `mirror-buffers` setting.
- `mirror-egress-packet-use` (num; syscap=!prestera-cpss): Egress mirror packet usage.
- `mirror-egress-byte-cap` (num; syscap=prestera-bc2): Egress mirror byte capacity. Depends on the `mirror-buffers` setting.
- `mirror-egress-byte-use` (num; syscap=prestera-bc2): Egress mirror byte usage.
- `shared-packet-cap` (num; syscap=prestera-ac3): Shared packet capacity. The maximum number of hardware packet descriptors that can be shared between ports and tx queues. Depends on the `shared-buffers` setting.
- `shared-packet-use` (num; syscap=prestera-ac3): Shared packet usage. The current number of shared packet descriptors used by all tx queues.
- `shared-byte-cap` (num; syscap=prestera-ac3): Shared tx memory capacity. Depends on the `shared-buffers` setting.
- `shared-byte-use` (num; syscap=prestera-ac3): Shared tx memory usage. The current number of shared buffers occupied by the packets in all tx queues.
- `lossy-pool-packet-cap` (num; syscap=prestera-bc2): Shared packet capacity of the lossy pool.
- `lossy-pool-packet-use` (num; syscap=prestera-bc2): Shared packet usage of the lossy pool.
- `lossless-pool-packet-cap` (num; syscap=!prestera-ac3): Shared packet capacity of the lossless pool.
- `lossless-pool-packet-use` (num; syscap=!prestera-ac3): Shared packet usage of the lossless pool.
- `lossy-pool-byte-cap` (num; syscap=!prestera-ac3): Lossy pool byte capacity.
- `lossy-pool-byte-use` (num; syscap=!prestera-ac3): Lossy pool byte usage.
- `lossless-pool-byte-cap` (num; syscap=!prestera-ac3): Lossless pool byte capacity.
- `lossless-pool-byte-use` (num; syscap=!prestera-ac3): Lossless pool byte usage.
- `wred-packet-cap` (num; syscap=prestera-bc2): The maximum packet count that a queue can use above the shared cap to trigger a random tail drop (`queueX-shared-packet-cap` in `/in/eth/sw/qos/port/print` usage) . For example, if `queue1-shared-packet-cap=3072` and `wred-packet-cap=512`, WRED triggers when `queue1-packet-use` exceeds 3072, reaching 100% drop rate at 3072+512=3584 packets.
- `wred-byte-cap` (num; syscap=prestera-bc2): The maximum byte count that a queue can use above the shared cap to trigger a random tail drop (`queueX-shared-byte-cap`). For example, if `queue1-shared-byte-cap=768KiB` and `wred-byte-cap=128KiB`, WRED triggers when `queue1-packet-use` exceeds 768KiB, reaching 100% drop rate at 768+128=896KiB.
