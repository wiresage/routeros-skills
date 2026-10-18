# /user-manager/limitation

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/limitation

Package: userman-5; Type: Directory

**Arguments**

- `name` (string; mandatory)
- `download-limit` (num)
- `upload-limit` (num)
- `transfer-limit` (num)
- `uptime-limit` (time)
- `reset-counters-start-time` (date)
- `reset-counters-interval` (alt { constant: enum (disabled | hourly | daily | weekly | monthly) , reset-counters-interval: time })
- `rate-limit-rx` (num)
- `rate-limit-tx` (num)
- `rate-limit-burst-rx` (num)
- `rate-limit-burst-tx` (num)
- `rate-limit-burst-threshold-rx` (num)
- `rate-limit-burst-threshold-tx` (num)
- `rate-limit-burst-time-rx` (time)
- `rate-limit-burst-time-tx` (time)
- `rate-limit-min-rx` (num)
- `rate-limit-min-tx` (num)
- `rate-limit-priority` (num)
