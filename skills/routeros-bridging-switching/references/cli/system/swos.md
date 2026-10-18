# /system/swos

> Source: https://manual.mikrotik.com/docs/cli-reference/system/swos

Conditions: !i386, !mmips, !powerpc, !tile, !smips; Syscap: swos; Type: Settings Directory

**Arguments**

- `address-acquisition-mode` (enum: dhcp-with-fallback | static | dhcp-only)
- `static-ip-address` (ipAddr)
- `identity` (string)
- `allow-from` (composite { address: ipAddr , netmask: [ num [ .. 32]] })
- `allow-from-ports` (ubit (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32))
- `allow-from-vlan` (num)

## Commands

### /system/swos/load-config

Conditions: !i386, !mmips, !powerpc, !tile, !smips; Syscap: swos; Type: Command

**Arguments**

- `file` (file)

### /system/swos/password

Conditions: !i386, !mmips, !powerpc, !tile, !smips; Syscap: swos; Type: Command

**Arguments**

- `new-password` (string)
- `confirm-new-password` (string)

### /system/swos/reset-config

Conditions: !i386, !mmips, !powerpc, !tile, !smips; Syscap: swos; Type: Command

### /system/swos/save-config

Conditions: !i386, !mmips, !powerpc, !tile, !smips; Syscap: swos; Type: Command

**Arguments**

- `file` (string)

### /system/swos/upgrade

Conditions: !i386, !mmips, !powerpc, !tile, !smips; Syscap: swos; Type: Command

**Read-only arguments**

- `version` (string)
- `status` (string)
