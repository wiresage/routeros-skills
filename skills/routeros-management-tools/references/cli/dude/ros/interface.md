# /dude/ros/interface

> Source: https://manual.mikrotik.com/docs/cli-reference/dude/ros/interface

Package: dude; Type: Directory

**Flags**

- `D`: dynamic
- `X`: disabled
- `R`: running
- `S`: slave

**Arguments**

- `device` (enum; mandatory)
- `name` (string)
- `mtu` (num)
- `l2mtu` (num)

**Read-only arguments**

- `default-name` (string)
- `type` (string)
- `actual-mtu` (num)
- `max-l2mtu` (num)
- `mac-address` (macAddr)
- `fast-path` (bool)
- `last-link-down-time` (date)
- `last-link-up-time` (date)
- `link-downs` (num)
- `rx-byte` (num)
- `tx-byte` (num)
- `rx-packet` (num)
- `tx-packet` (num)
- `rx-drop` (num)
- `tx-drop` (num)
- `rx-error` (num)
- `tx-error` (num)
- `fp-rx-byte` (num)
- `fp-tx-byte` (num)
- `fp-rx-packet` (num)
- `fp-tx-packet` (num)
