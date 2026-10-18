# /dude/ros/address

> Source: https://manual.mikrotik.com/docs/cli-reference/dude/ros/address

Package: dude; Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid
- `D`: dynamic

**Arguments**

- `device` (enum; mandatory)
- `address` (composite { address: ipAddr , netmask: [ num [ .. 32]] }; mandatory)
- `network` (ipAddr)
- `netmask` (ipAddr)
- `broadcast` (ipAddr)
- `interface` (enum; mandatory)

**Read-only arguments**

- `actual-interface` (enum)
