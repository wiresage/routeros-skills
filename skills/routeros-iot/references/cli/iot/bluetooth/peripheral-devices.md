# /iot/bluetooth/peripheral-devices

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/peripheral-devices

Package: iot; Type: Directory

**Arguments**

- `address-type` (enum: public | random; mandatory)
- `address` (macAddr; mandatory)
- `name` (string)
- `persist` (bool)
- `mtik-key` (string)

**Read-only arguments**

- `rssi` (num)
- `last-data` (string): Advertisement data in hex format
- `last-seen` (date)
- `beacon-types` (multi { array-id, beacon-types: enum (unknown | mikrotik | ibeacon | eddystone-uid | eddystone-url | eddystone-tlm | eddystone-eid) })
- `mtik-version` (num)
- `mtik-encrypted` (bool)
- `mtik-acc-x` (num)
- `mtik-acc-y` (num)
- `mtik-acc-z` (num)
- `mtik-temperature` (num)
- `mtik-battery` (num)
- `mtik-uptime` (num)
- `mtik-flags` (multi { array-id, flags: enum (reed-switch | tilt | free-fall | impact-x | impact-y | impact-z) })
- `ibeacon-uuid` (string)
- `ibeacon-major` (num)
- `ibeacon-minor` (num)
- `ibeacon-rssi-at-1m` (num)
- `eddy-rssi-at-1m` (num)
- `eddy-namespace` (string)
- `eddy-instance` (string)
- `eddy-version` (num)
- `eddy-battery-voltage` (num)
- `eddy-temperature` (num)
- `eddy-packet-count` (num)
- `eddy-uptime` (num)
- `eddy-tx-power` (num)
- `eddy-eid` (string)
