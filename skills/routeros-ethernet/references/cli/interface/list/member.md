# /interface/list/member

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/list/member

Type: Directory

List of static interface members. Dynamically added interfaces from `include` and `exclude` statements do not appear in this sub-menu.

> **Info**
>
> Care must be taken when working with bridges and lists. Adding a bridge as a member is not the same as adding all its ports. Adding all slave ports as members is not the same as adding the bridge itself. This can impact the functionality of Neighbour Discovery.

**Flags**

- `X` (disabled): Member entry is disabled.
- `D` (dynamic): Dynamically added member.

**Arguments**

- `list` (enum; mandatory): Name of the interface list to which the member belongs.
- `interface` (iface_enum; mandatory): Name of the interface that is a member of the list.

**Read-only arguments**

- `dynamic` (bool): Whether the member was added dynamically.
