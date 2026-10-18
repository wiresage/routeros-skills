# /iot/lora/channels

> Source: https://manual.mikrotik.com/docs/cli-reference/iot/lora/channels

Package: iot; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `radio` (enum: radio0 | radio1 | radio2 | radio3)
- `freq-off` (num)
- `bandwidth` (enum: 7.8_kHz | 15.6_kHz | 31.2_kHz | 62.5_kHz | 125_kHz | 250_kHz | 500_kHz | 200_kHz | 400_kHz | 800_kHz | 1600_kHz)
- `spread-factor` (enum: SF7 | SF8 | SF9 | SF10 | SF11 | SF12 | SF5 | SF6)
- `datarate` (num)

**Read-only arguments**

- `name` (string)
- `type` (enum: MSF | LoRa | FSK)
- `freq` (num)
