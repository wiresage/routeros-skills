# /queue/tree

> Source: https://manual.mikrotik.com/docs/cli-reference/queue/tree

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `name` (string)
- `parent` (enum (global) { global:0xfffff4 }; mandatory)
- `packet-mark` (multi { array-id, packet-mark: enum })
- `limit-at` (num)
- `queue` (enum)
- `priority` (num)
- `max-limit` (num)
- `burst-limit` (num)
- `burst-threshold` (num)
- `burst-time` (time)
- `bucket-size` (num)

**Read-only arguments**

- `bytes` (num)
- `packets` (num)
- `dropped` (num)
- `rate` (num)
- `packet-rate` (num)
- `queued-packets` (num)
- `queued-bytes` (num)
- `pcq-queues` (num)

## Commands

### /queue/tree/reset-counters

Type: Command

### /queue/tree/reset-counters-all

Type: Command
