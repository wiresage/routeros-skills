# /iot/bluetooth/connections

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/connections

Package: iot; Type: Directory

**Read-only arguments**

- `name` (string)
- `direction` (enum (incoming | outgoing) { incoming:0x01, outgoing:0x02 })

## Commands

### /iot/bluetooth/connections/connect

Package: iot; Type: Command

**Arguments**

- `pdev` (enum)

### /iot/bluetooth/connections/disconnect

Package: iot; Type: Command

**Arguments**

- `pdev` (enum)

### /iot/bluetooth/connections/read

Package: iot; Type: Command

**Arguments**

- `uuid` (enum)
- `pdev` (enum)

**Read-only arguments**

- `value` (string)
- `hex` (string)
- `bytes` (multi { array-id, value: num })

### /iot/bluetooth/connections/subscribe

Package: iot; Type: Command

**Arguments**

- `uuid` (enum)
- `type` (enum (notification | indication) { notification:0x01, indication:0x02 })
- `pdev` (enum)

### /iot/bluetooth/connections/unsubscribe

Package: iot; Type: Command

**Arguments**

- `uuid` (enum)
- `type` (enum (notification | indication) { notification:0x01, indication:0x02 })
- `pdev` (enum)

### /iot/bluetooth/connections/write

Package: iot; Type: Command

**Arguments**

- `uuid` (enum)
- `data-hex` (string)
- `data-str` (string)
- `data-bytes` (multi { array-id, value: num })
- `pdev` (enum)

### /iot/bluetooth/connections/write-no-resp

Package: iot; Type: Command

**Arguments**

- `uuid` (enum)
- `data-hex` (string)
- `data-str` (string)
- `data-bytes` (multi { array-id, value: num })
- `pdev` (enum)
