# /tool/romon/port

> Source: https://manual.mikrotik.com/docs/cli-reference/tool/romon/port

Type: Directory

Ports that participate in the [RoMON network](../../../guides/management-tools/romon.md#choose-ports).

**Flags**

- `*`: default
- `X`: disabled
- `D`: dynamic

**Arguments**

- `interface` (iface_enum { all }; mandatory): Interface that participates in RoMON; either a single interface or the built-in wildcard `all`. Master interfaces such as bridges are not accepted — name the physical ports. The preconfigured `all` entry cannot be added a second time, removed, enabled or disabled; only its `cost`, `forbid` and `secrets` can be changed.
- `forbid` (bool): Whether the matched interface is allowed or forbidden to participate in the RoMON network.
- `cost` (num): The port's cost. All specific port entries have higher priority than the wildcard entry with `interface=all`.
- `secrets` (multi { array-id, name: string }): List of individual port secrets used for RoMON message hashing.
