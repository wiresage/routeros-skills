# /iot/wiliot

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/wiliot

Package: iot; Type: Settings Directory

**Arguments**

- `spoof-gps` (bool)
- `lat` (num)
- `long` (num)
- `server` (enum: none): Used MQTT server
- `scanner` (enum: none)
- `advertiser` (enum: none)
- `wi-fi` (iface_enum { none })
- `features` (ubit (gateway, bridge)): supported Wiliot features

**Read-only arguments**

- `status` (string)
- `gateway-id` (string)
- `type` (string)
- `owner` (string)

## Commands

### /iot/wiliot/clear

Package: iot; Type: Command

### /iot/wiliot/disable

Package: iot; Type: Command

**Read-only arguments**

- `status` (string)

### /iot/wiliot/enable

Package: iot; Type: Command

**Read-only arguments**

- `status` (string)
