# /iot/mqtt/brokers

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/mqtt/brokers

Package: iot; Type: Directory

**Flags**

- `W`: Will message enabled

**Arguments**

- `name` (string; mandatory)
- `address` (string; mandatory)
- `port` (num)
- `ssl` (bool)
- `client-id` (string)
- `username` (string)
- `password` (string)
- `will-topic` (string)
- `will-message` (string)
- `will-qos` (num)
- `will-retain` (bool)
- `certificate` (enum: none)
- `auto-connect` (bool)
- `keep-alive` (num)
- `parallel-scripts-limit` (num)

**Read-only arguments**

- `connected` (bool)
