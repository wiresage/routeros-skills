# /iot/bluetooth/scanners/advertisements

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/scanners/advertisements

Package: iot; Type: Directory

**Read-only arguments**

- `device` (enum)
- `pdu-type` (enum: adv-ind | adv-direct-ind | adv-scan-ind | adv-noconn-ind | scan-rsp | unknown)
- `time` (date)
- `epoch` (num): Milliseconds since Unix Epoch
- `address-type` (enum: public | random)
- `address` (macAddr): Advertiser Bluetooth address
- `rssi` (num): Signal strength
- `length` (num): Advertisement data length
- `data` (string): Advertisement data in hex format
- `phy` (enum: 1M | 2M | CODED-S8 | CODED-S2 | NONE): Advertisement primary PHY
- `phy-secondary` (enum: 1M | 2M | CODED-S8 | CODED-S2 | NONE): Advertisement secondary PHY
- `legacy` (bool): Advertisement legacy compatibility
- `filter-comment` (string): Comment of the matching whitelist filter

## Commands

### /iot/bluetooth/scanners/advertisements/clear

Package: iot; Type: Command
