# /queue/simple

> Source: https://manual.mikrotik.com/docs/cli-reference/queue/simple

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic

**Arguments**

- `name` (string)
- `target` (object { target: alt { target-interface: iface_enum , target-address: alt { ip-address: ipPrefix , ipv6-address: ip6Prefix } } }; mandatory)
- `dst` (alt { ip-address: ipPrefix , ipv6-address: ip6Prefix , interface: iface_enum })
- `parent` (enum: none)
- `packet-marks` (multi { array-id, packet-mark: enum })
- `priority` (composite { upload-priority: num [1 .. 8] , download-priority: num [1 .. 8] })
- `queue` (composite { upload-queue: enum , download-queue: enum })
- `limit-at` (composite { upload-limit-at: num , download-limit-at: num })
- `max-limit` (composite { upload-max-limit: num , download-max-limit: num })
- `burst-limit` (composite { upload-burst-limit: num , download-burst-limit: num })
- `burst-threshold` (composite { upload-threshold: num , download-threshold: num })
- `burst-time` (composite { upload-burst-time: time , download-burst-time: time })
- `bucket-size` (composite { upload-bucket-size: num [ .. 10000] , download-bucket-size: num [ .. 10000] })
- `total-priority` (num)
- `total-queue` (enum)
- `total-limit-at` (num)
- `total-max-limit` (num)
- `total-burst-limit` (num)
- `total-burst-threshold` (num)
- `total-burst-time` (time)
- `total-bucket-size` (num)
- `time` (super { ! , start: time , [end] -time , [day] ,ubit (sun, mon, tue, wed, thu, fri, sat) })

**Read-only arguments**

- `bytes` (composite { upload: num , download: num })
- `total-bytes` (num)
- `packets` (composite { upload: num , download: num })
- `total-packets` (num)
- `dropped` (composite { upload: num , download: num })
- `total-dropped` (num)
- `rate` (composite { upload: num , download: num })
- `total-rate` (num)
- `packet-rate` (composite { upload: num , download: num })
- `total-packet-rate` (num)
- `queued-packets` (composite { upload: num , download: num })
- `total-queued-packets` (num)
- `queued-bytes` (composite { upload: num , download: num })
- `total-queued-bytes` (num)
- `pcq-queues` (composite { upload: num , download: num })
- `total-pcq-queues` (num)

## Commands

### /queue/simple/reset-counters

Type: Command

### /queue/simple/reset-counters-all

Type: Command
