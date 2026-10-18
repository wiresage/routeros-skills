# /iot/modbus

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/modbus

Package: iot; Type: Settings Directory

**Arguments**

- `disabled` (bool)
- `hardware-port` (enum)
- `tcp-port` (num)
- `timeout` (num)
- `rx-switch-offset` (num)
- `interframe-gap` (num)
- `disable-security-rules` (bool)

## Commands

### /iot/modbus/read-holding-registers

Package: iot; Type: Command

**Arguments**

- `ip` (ipAddr)
- `port` (num)
- `timeout` (num)
- `slave-id` (num)
- `reg-addr` (num)
- `num-regs` (num)

**Read-only arguments**

- `values` (multi { array-id, value: num })

### /iot/modbus/transceive

Package: iot; Type: Command

**Arguments**

- `address` (num)
- `function` (num)
- `data` (string)
- `values` (multi { array-id, value: num })
- `rx-switch-offset` (num)

**Read-only arguments**

- `address` (num)
- `function` (num)
- `data` (string)
- `values` (multi { array-id, value: num })
- `time` (date)
- `status` (enum: ok | error)
- `error` (num)
- `error-description` (string)
