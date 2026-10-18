# /routing/pimsm/interface-template

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/interface-template

Conditions: !smips; Type: Directory

The interface template menu defines which interfaces will participate in PIM and what per-interface configuration will be used.

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `instance` (enum; mandatory): Name of the PIM instance this interface template belongs to.
- `interfaces` (object { interface: iface_enum }; unset): List of interfaces that will participate in PIM.
- `hello-period` (time): Periodic interval for Hello messages.
- `hello-delay` (time): Randomized interval for the initial Hello message on interface startup or detecting a new neighbor.
- `priority` (num): The Designated Router (DR) priority. A single Designated Router is elected on each network. The priority is used only if all neighbors have advertised a priority option. The numerically largest priority is preferred. In case of a tie or if priority is not used - the numerically largest IP address is preferred.
- `join-prune-period` (time)
- `propagation-delay` (time): Sets the value for a prune pending timer. It is used by upstream routers to figure out how long they should wait for a Join override message before pruning an interface that has join suppression enabled.
- `override-interval` (time): Sets the maximum time period over which to randomize when scheduling a delayed override Join message on a network that has join suppression enabled.
- `join-tracking-support` (bool): Sets the value of a Tracking (T) bit in the LAN Prune Delay option in the Hello message. When enabled, a router advertises its willingness to disable Join suppression. It is possible for upstream routers to explicitly track the join membership of individual downstream routers if Join suppression is disabled. Unless all PIM routers on a link negotiate this capability, explicit tracking and the disabling of the Join suppression mechanism are not possible.
- `source-addresses` (object { address: address (flags=46) }; unset)
