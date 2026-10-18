# /iot/bluetooth

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth

Package: iot; Type: Directory

**Flags**

- `X`: offline

**Arguments**

- `name` (string)
- `random-static-address` (macAddr)
- `antenna` (enum: internal | external)

**Read-only arguments**

- `public-address` (macAddr)
- `rx-bytes` (num)
- `tx-bytes` (num)
- `rx-errors` (num)
- `tx-errors` (num)
- `rx-evt` (num)
- `tx-cmd` (num)
- `rx-acl` (num)
- `tx-acl` (num)

## Commands

### /iot/bluetooth/decode-ad

Package: iot; Type: Command

**Arguments**

- `data` (string)
- `key` (string)

**Read-only arguments**

- `type` (enum: unknown | mikrotik | ibeacon | eddystone-uid | eddystone-url | eddystone-tlm | eddystone-eid)
- `version` (num)
- `encrypted` (bool)
- `acc-x` (num)
- `acc-y` (num)
- `acc-z` (num)
- `temperature` (num)
- `uptime` (num)
- `flags` (multi { array-id, flags: enum (reed-switch | tilt | free-fall | impact-x | impact-y | impact-z) })
- `battery` (num)
- `uuid` (string)
- `major` (num)
- `minor` (num)
- `rssi-at-1m` (num)
- `namespace` (string)
- `instance` (string)
- `battery-voltage` (num)
- `packet-count` (num)
- `tx-power` (num)
- `eid` (string)

### /iot/bluetooth/reset-counters

Package: iot; Type: Command
