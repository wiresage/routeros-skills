# /interface/ethernet/switch/qos/tx-manager

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/tx-manager

Syscap: rbswitch and crs_prestera; Type: Directory

Transmission (Tx) Manager controls packet enqueuing for transmission and packet tx order. Different switch ports can be assigned to different Tx managers. The maximum number of hardware Tx managers depends on the switch chip model.

> **Info**
>
> Port status has no effect on the allocated resources. Running ports receive the same amount of queue buffers as disconnected or disabled ones if all of them are assigned to the same Tx Manager.

**Flags**

- `*`: default
- `X`: disabled
- `I`: inactive
- `H`: hw-offloaded

**Arguments**

- `name` (string; mandatory): Tx Manager name.
- `queue-buffers` (alt { queue-buffers-pct: num [ .. 100] , queue-buffers-byte: num [1536 .. 67108864] }): The total number of hardware Tx buffers allocated to all ports linked to this Tx Manager. Any value but **auto** is NOT scaled by the number of ports. For example, if queue-buffers=30%, and there are 3 ports using this Tx Manager, each respective port receives 10% of the total available resources. Adding two more ports to the Tx Manager drops per-port buffers down to 6% (30/5).

**Read-only arguments**

- `hw-id` (num)
