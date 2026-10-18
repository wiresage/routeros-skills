# /ip/ipsec/policy

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/policy

Type: Directory

> **Info**
>
> Policy order is important. It works similarly to firewall filters where policies are executed from top to bottom (priority parameter is removed).
>
> All packets are IPIP encapsulated in tunnel mode, and their new IP header's src-address and dst-address are set to sa-src-address and sa-dst-address values of this policy. If you do not use tunnel mode (i.e., you use transport mode), then only packets whose source and destination addresses are the same as sa-src-address and sa-dst-address can be processed by this policy. Transport mode can only work with packets that originate at and are destined for IPsec peers (hosts that established security associations). To encrypt traffic between networks (or a network and a host) you have to use tunnel mode.

**Flags**

- `T` (template): Whether the item is a template to assign for dynamic peers.
- `B` (backup): Whether the item is included in the backup.
- `X` (disabled): Whether the item is disabled.
- `D` (dynamic): Whether the item was created dynamically.
- `I` (invalid): Whether this policy is invalid - the possible cause is a duplicate policy with the same src-address and dst-address.
- `A` (active): Whether the item is currently active.
- `*` (default): Whether the item is the default.

**Arguments**

- `peer` (multi { array-id, peer: enum }): Name of the peer on which the policy applies.c
- `tunnel` (bool): Whether to use tunnel mode.
- `group` (enum): Policy group name.
- `src-address` (alt { prefix6: ip6Prefix , prefix4: ipPrefix }): Source address or network to be matched in packets. Applicable when tunnel mode (`tunnel=yes`) or template (`template=yes`) is used.
- `src-port` (num): Source port.
- `dst-address` (alt { prefix6: ip6Prefix , prefix4: ipPrefix }): Destination address or network to be matched in packets. Applicable when tunnel mode (`tunnel=yes`) or template (`template=yes`) is used.
- `dst-port` (num): Destination port.
- `protocol` (enum: all): IP protocol number or name.
- `action` (enum: encrypt | discard | none): Action to take for matching traffic.
  - `none` - pass the packet unchanged.
  - `discard` - drop the packet.
  - `encrypt` - apply transformations specified in this policy and its SA.
- `level` (enum: require | use | unique): Specifies what to do if some of the SAs for this policy cannot be found:
  - `use` - skip this transform, do not drop the packet, and do not acquire SA from IKE daemon;
  - `require` - drop the packet and acquire SA;
  - `unique` - drop the packet and acquire a unique SA that is only used with this particular policy. It is used in setups where multiple clients can sit behind one public IP address (clients behind NAT).
- `ipsec-protocols` (enum: ah | esp): Specifies what combination of Authentication Header and Encapsulating Security Payload protocols you want to apply to matched traffic.
- `sa-src-address` (alt { ipv6: ip6Addr , ip: ipAddr }): endpoint address
- `sa-dst-address` (alt { ipv6: ip6Addr , ip: ipAddr }): endpoint address
- `proposal` (enum): Proposal template name.
- `template` (bool): Whether this policy is a template.

**Read-only arguments**

- `active-interface` (iface_enum): The interface through which the SA is established.
- `ph2-count` (num): Number of phase 2 exchanges.
- `ph2-state` (enum: spawning | starting | ready-to-send | getspi-sent | getspi-done | msg1-sent | ready-to-establish | commiting | adding-sa | established | expired | no-phase2): Current phase 2 state.
