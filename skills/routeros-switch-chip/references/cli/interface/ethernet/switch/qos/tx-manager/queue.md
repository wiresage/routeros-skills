# /interface/ethernet/switch/qos/tx-manager/queue

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/tx-manager/queue

Syscap: rbswitch and crs_prestera; Type: Directory

Each port has eight Tx queues. The assigned Tx Manager controls packet enqueuing and schedules transmission orders. Each queue can have either strict priority (where packets with the highest traffic class are always transmitted first) or be grouped together for a weighted round-robin tx schedule.

Creating a Tx Manager automatically creates all eight respective queue schedulers.

> **Danger**
>
> Changing any properties of Tx manager or queues completely halts traffic enqueueing and transmission during the offload process. Temporary packet loss is expected while the device is forwarding traffic.

> **Danger**
>
> On some device models, due to hardware limitations, enabling ECN on one queue turns on CE marking of ECN-capable packets on all queues. In such cases, `ecn-actual=yes` despite `ecn=no`.

**Flags**

- `*`: default
- `I`: inactive
- `H`: hw-offloaded

**Arguments**

- `schedule` (enum: strict-priority | low-priority-group | high-priority-group): Schedule tx either by strict priority of the traffic class or round-robin within the group.
  - strict-priority - packets in the respective queue are always scheduled before moving to lower traffic classes. Packets with lower traffic classes are not transmitted until the current queue is empty.
  - high-priority-group - all queues in the group are scheduled together by using a weighted round-robin principle. For example, if TC5 has weight 4, TC4 - 3, and TC3 - 2, then the scheduler transmits 4 packets from queue5, 3 packets from Q4, and 2 packets from Q3 in a single round. To achieve lower latency, each round is "sliced" between all queues in the group. In other words, the packet order in each round of the above example is "Q5, Q4, Q3, Q5, Q4, Q3, Q5, Q4, Q5".
  - low-priority-group - similar logic to the high-priority-group, but the low-priority-group is scheduled only when all queues in the high-priority-group are empty.
- `weight` (num): The weight value for the traffic class if it is a member of a schedule group. The field is not used in the case of a strict priority schedule.
- `queue-buffers` (alt { queue-buffers-pct: num [ .. 100] , queue-buffers-byte: num [1536 .. 67108864] }; syscap=!prestera-cpss): The number of hardware Tx buffers allocated to this queue. Any value but **auto** is NOT scaled by the number of ports, i.e., the value gets split on ports linked to the Tx Manager. When given in percent, it means percentage of the tx-manager's queue-buffers value.
- `use-shared-buffers` (bool; syscap=!prestera-cpss): Allow the queue to use the shared buffer pool when **queue-buffers**are full. If the queue is full and the shared buffers are disabled, the packet gets dropped. If the shared buffers are enabled, the queue may use up to **shared-packet-cap** or **shared-poolX-packet-cap** (see [QoS Settings](../settings.md) for details) packets from the shared pool.
- `wred` (bool; syscap=!prestera-ac3): Enables/disables [Weighted Random Early Detection](../../../../../../guides/bridging-and-switching/quality-of-service.md#weighted-random-early-detection-wred) for the given queue.
- `ecn` (bool; syscap=!prestera-ac3): Enables/disables ECN marking of the transmitted packets.

**Read-only arguments**

- `tx-manager` (enum): The linked Tx Manager
- `traffic-class` (num): The traffic class (tc0..tc7) and the respective port queue (queue0..queue7) that the scheduler controls.
- `wred-actual` (bool; syscap=!prestera-ac3): Actual WRED value
- `ecn-actual` (bool; syscap=!prestera-ac3): Actual ECN value
