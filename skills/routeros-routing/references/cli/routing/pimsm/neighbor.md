# /routing/pimsm/neighbor

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/neighbor

Conditions: !smips; Type: Directory

The neighbor menu shows all detected neighbors that are running PIM and their statuses. This menu contains dynamic and read-only entries.

**Flags**

- `R` (designated-router): The neighbor is the elected Designated Router (DR) on the network segment.
- `J` (join-tracking): The neighbor supports join tracking. It sets the Tracking (T) bit in the LAN Prune Delay option of its Hello messages.

**Read-only arguments**

- `instance` (enum): Name of the PIM instance this neighbor is detected on.
- `address` (address (flags=46i)): Shows the neighbor's IP address and local interface the neighbor is detected on.
- `priority` (num): Indicates the neighbor's priority value.
- `timeout` (time): Shows the remaining time after the neighbor is removed from the list if no new Hello message is received. The hold time equals neighbor's `hello-period * 3.5`.
- `propagation-delay` (time): Indicates the neighbor's value of the propagation delay in the LAN Prune Delay option in the Hello message.
- `override-interval` (time): Indicates the neighbor's value of the override interval in the LAN Prune Delay option in the Hello message.
