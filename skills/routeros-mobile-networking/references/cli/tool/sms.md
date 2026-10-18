# /tool/sms

> Source: https://manual.mikrotik.com/docs/cli-reference/tool/sms

Conditions: !smips; Type: Settings Directory

**Arguments**

- `receive-enabled` (bool)
- `port` (alt { serial: enum , interface: iface_enum { none } })
- `channel` (num)
- `secret` (string)
- `allowed-number` (multi { array-id, number: string })
- `sim-pin` (string)
- `sms-storage` (enum: modem | sim): Memory for reading, writing, sending and receiving operations (`<mem1>`, `<mem2>` and `<mem3>` in ETSI TS 127 005), will be used in further +CPMS commands (setting effective when using AT commands only)
- `polling` (bool): Poll new SMS every 5s. It's recommended to enable polling only when there are problems with receiving new SMS otherwise.
- `remove-sent-sms-after-send` (bool): Useful when modem automatically stores sent SMS

**Read-only arguments**

- `status` (enum: off | running)
- `last-ussd` (string)

## Commands

### /tool/sms/send

Conditions: !smips; Type: Command

**Arguments**

- `port` (alt { serial: enum , interface: iface_enum })
- `channel` (num)
- `phone-number` (string)
- `smsc` (string)
- `message` (string)
- `type` (enum: class-1 | class-0 | ussd)
- `status-report-request` (bool)
