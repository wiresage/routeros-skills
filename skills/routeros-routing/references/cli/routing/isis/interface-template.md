# /routing/isis/interface-template

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/isis/interface-template

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `instance` (enum)
- `interfaces` (object { interface: iface_enum }; unset)
- `levels` (ubit (l1, l2))
- `ptp` (switch; unset)
- `passive` (switch; unset)
- `ptp.hello-interval` (num; unset)
- `ptp.hello-multiplier` (num; unset)
- `ptp.hello-3way` (switch; unset)
- `ptp.l1.csnp-interval` (num; unset)
- `ptp.l1.psnp-interval` (num; unset)
- `ptp.l1.metric` (num; unset)
- `ptp.l2.csnp-interval` (num; unset)
- `ptp.l2.psnp-interval` (num; unset)
- `ptp.l2.metric` (num; unset)
- `bcast.l1.hello-interval` (num; unset)
- `bcast.l1.hello-interval-dr` (num; unset)
- `bcast.l1.hello-multiplier` (num; unset)
- `bcast.l1.priority` (num; unset)
- `bcast.l1.csnp-interval` (num; unset)
- `bcast.l1.psnp-interval` (num; unset)
- `bcast.l1.metric` (num; unset)
- `bcast.l2.hello-interval` (num; unset)
- `bcast.l2.hello-interval-dr` (num; unset)
- `bcast.l2.hello-multiplier` (num; unset)
- `bcast.l2.priority` (num; unset)
- `bcast.l2.csnp-interval` (num; unset)
- `bcast.l2.psnp-interval` (num; unset)
- `bcast.l2.metric` (num; unset)
