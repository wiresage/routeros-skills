# /routing/pimsm/instance

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/instance

Conditions: !smips; Type: Directory

The instance menu defines the main PIM-SM settings. The instance is then used for all other PIM-related configurations like interface-template, static RP, and Bootstrap Router.

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `vrf` (enum): Name of the VRF for control connections.
- `name` (string): Name of the instance.
- `afi` (enum: ip | ipv6): Specifies address family for PIM.
- `switch-to-spt` (bool): Whether to switch to Shortest Path Tree (SPT) if multicast data bandwidth threshold is reached. The router will not proceed from protocol phase one (register encapsulation) to native multicast traffic flow if this option is disabled. It is recommended to enable this option.
- `switch-to-spt-interval` (time): Time interval in which to account for multicast data bandwidth, used in conjunction with `switch-to-spt-bytes` to determine if the switching threshold is reached.
- `switch-to-spt-bytes` (num): Multicast data bandwidth threshold. Switching to Shortest Path Tree (SPT) happens if this threshold is reached in the specified time interval. If a value of 0 is configured, switching will happen immediately.
- `crp-advertise-contained` (bool): Currently not implemented.
- `bsm-forward-back` (bool): Currently not implemented.
- `rp-hash-mask-length` (num): The hash mask allows changing how many groups to map to one of the matching RPs.
- `rp-static-override` (bool): Changes the selection priority for static RP. When disabled, the bootstrap RP set has a higher priority. When enabled, static RP has a higher priority.
- `ssm-range` (address (flags=46/)): Currently not implemented.
