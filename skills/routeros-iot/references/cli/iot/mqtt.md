# /iot/mqtt

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/mqtt

Package: iot; Type: Settings Directory

## Commands

### /iot/mqtt/connect

Package: iot; Type: Command

**Arguments**

- `broker` (enum)

### /iot/mqtt/disconnect

Package: iot; Type: Command

**Arguments**

- `broker` (enum)

### /iot/mqtt/publish

Package: iot; Type: Command

**Arguments**

- `broker` (enum)
- `topic` (string)
- `message` (string)
- `qos` (num)
- `retain` (bool)
- `disconnect-after` (bool)
- `force` (bool)

### /iot/mqtt/subscribe

Package: iot; Type: Command

**Arguments**

- `broker` (enum)
- `topic` (string)
- `qos` (num)
- `force` (bool)

### /iot/mqtt/unsubscribe

Package: iot; Type: Command

**Arguments**

- `broker` (enum)
- `topic` (enum)
