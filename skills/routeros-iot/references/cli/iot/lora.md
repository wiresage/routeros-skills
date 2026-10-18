# /iot/lora

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/lora

Package: iot; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `gateway-id` (string)
- `name` (string)
- `servers` (multi { server: enum })
- `tx-immediate-delay-us` (num)
- `channel-plan` (enum: custom | eu-868 | as-923 | kr-920 | in-865 | il-917 | us-915-1 | us-915-2 | us-915-3 | us-915-4 | us-915-5 | us-915-6 | us-915-7 | us-915-8 | au-915-1 | au-915-2 | ru-864 | ru-864-mid | 2.4-ghz)
- `antenna-gain` (num)
- `forward` (ubit (crc-validation, dev-addr-validation, proprietary-traffic))
- `network` (enum: public | private)
- `lbt-enabled` (bool)
- `listen-time` (num)
- `rssi-threshold` (num)
- `spoof-gps` (bool)
- `lat` (num)
- `long` (num)
- `alt` (num)
- `antenna` (enum: internal-antenna | external-antenna)

**Read-only arguments**

- `status` (string)
- `firmware-id` (string)
- `version` (string)
- `rx-packets` (num)
- `tx-packets` (num)
- `tx-toa` (num)
- `band` (enum: unknown | 863-870 | 902-928 | 2.4-ghz)

## Commands

### /iot/lora/reset-devices

Package: iot; Type: Command

### /iot/lora/send

Package: iot; Type: Command

**Arguments**

- `device-id` (num): device id
- `payload` (string): TX packet payload
- `power` (num): RF power in dBm
- `frequency` (num): Radio TX frequency in MHz (e.g.868500000)
- `bandwidth` (enum: 125kHz | 250kHz | 500kHz): LoRa bandwidth in khz [125, 250, 500]
- `spread-factor` (enum (SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | MULTI) { SF7:0x02, SF8:0x04, SF9:0x08, SF10:0x10, SF11:0x21, SF12:0x40, MULTI:0x7E }): Spread Factor
- `modulation` (enum (MOD_CW | MOD_LORA | MOD_FSK) { MOD_CW:0x08, MOD_LORA:0x10, MOD_FSK:0x20 }): modulation type
- `preamble` (num): preamble length
- `inverted` (bool): invert polarity
