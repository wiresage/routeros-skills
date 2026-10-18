# /zerotier/controller/member

> Source: https://manual.mikrotik.com/docs/cli-reference/zerotier/controller/member

Package: zerotier; Type: Directory

**Flags**

- `X` (disabled): Whether an item is disabled.
- `I` (inactive): Whether the member is inactive.
- `A` (authorized): Whether the member is authorized.
- `B` (bridge): Whether the member acts as a bridge.

**Arguments**

- `disabled` (bool): Whether an item is disabled.
- `name` (string): Name of the member.
- `network` (enum; mandatory): Network the member belongs to.
- `zt-address` (string; mandatory): ZeroTier address of the member.
- `authorized` (bool): Whether the member is authorized to join the network.
- `bridge` (bool): Whether the member acts as a bridge.
- `ip-address` (multi { array-id, addr: address (flags=46) }): IP address assigned to the member.

**Read-only arguments**

- `lost` (bool): Whether the connection to the member is lost.
- `last-seen` (time): Time since the member was last seen.
