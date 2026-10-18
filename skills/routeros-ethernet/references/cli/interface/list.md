# /interface/list

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/list

Type: Directory

Interface lists allow defining a set of interfaces for easier interface management in different interface-based configuration sections such as Neighbour Discovery, Firewall, Bridge, and Internet Detect.

There are four predefined lists: `all` (contains all interfaces), `none` (contains no interfaces), `dynamic` (contains dynamic interfaces), and `static` (contains static interfaces). You can also create additional interface lists.

> **Info**
>
> Dynamic interfaces are interfaces that have a "dynamic" flag. Any interface that does not have a dynamic flag will be part of the `static` interface list.

Members are added to an interface list in the following order:

1. Include members are added to the interface list.
2. Exclude members are removed from the list.
3. Statically configured members are added to the list.

**Flags**

- `*` (builtin): Built-in system list.
- `D` (dynamic): Dynamically created list.

**Arguments**

- `name` (string; mandatory): Name of the interface list. Predefined lists include "all", "none", "dynamic", and "static".
- `include` (multi { include-list: enum }): Interface list whose members are included in this list. Multiple lists can be specified, separated by commas.
- `exclude` (multi { exclude-list: enum }): Interface list whose members are excluded from this list. Multiple lists can be specified, separated by commas.

**Read-only arguments**

- `dynamic` (bool): Whether the interface list was created dynamically.
