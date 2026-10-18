# /routing/rule

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/rule

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive
- `*`: default

**Arguments**

- `src-address` (address (flags=64iv/); unset): Source address to match.
- `dst-address` (address (flags=64iv/); unset): Destination address to match.
- `routing-mark` (enum; unset): Match a specific routing mark.
- `interface` (iface_enum; unset): Incoming interface to match.
- `action` (enum: lookup | lookup-only-in-table | unreachable | drop | mangle): Action to take on the matching packet:
  - drop - silently drop the packet.
  - lookup - perform a lookup in routing tables.
  - lookup-only-in-table - perform lookup only in the specified routing table (see the `table` parameter).
  - unreachable - generate an ICMP unreachable message and send it to the source.
  - mangle - perform actions by firewall mangle rules.
- `table` (enum: local): Name of the routing table to use for lookup.
- `min-prefix` (num; unset): Hide routes from the routing table with the specified prefix length from packets processed by this routing rule. This is equivalent to the Linux IP rule `suppress_prefixlength`. For example, set the value to 0 to suppress the default route in the routing decision.
- `vrf` (switch)
- `realm` (num; unset)
- `chain` (enum; unset): Name of the chain used by routing decision rules. By default, `user` is used when the chain is not specified. If the chain name matches a built-in routing decision name, user-created rules are added after that decision. For example, if `chain=mangle`, user-created rules in this chain are located immediately after the `mangle` decision.
