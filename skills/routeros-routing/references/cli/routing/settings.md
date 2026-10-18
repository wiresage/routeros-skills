# /routing/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/settings

Type: Settings Directory

**Arguments**

- `single-process` (bool): When enabled, all routing-related processes combine into a single routing process to reduce RAM usage. When disabled, routing-related processes run separately and can improve performance and stability in some setups.  By default, single-process is enabled only for devices with 64 MB of RAM or less.  Reboot is required for this change to take effect.
- `dynamic-in-chain` (enum; unset): Name of the chain used to process all dynamically added routes.
- `connected-in-chain` (enum; unset): Name of the chain used to process `connected` routes.
- `check-gateway-ping-interval` (time)
- `check-gateway-ping-timeout` (time)
- `check-gateway-ping-count` (num)
- `policy-rules` (object { chain: enum }): Defines the order of routing decision rules. By default, `user` is the chain where user-defined `/routing/rule` entries are added. You can add custom chains anywhere in the list.
