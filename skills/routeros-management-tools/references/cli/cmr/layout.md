# /cmr/layout

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/layout

Package: cmr; Type: Directory

Topology configuration; the topology itself can only be displayed in the GUI, not in the CLI.

**Arguments**

- `name` (string): Name of the layout/topology.
- `scale` (num; unset): Background picture scale in percents. Default: 100.
- `file` (string; unset): Background picture selection.

## Commands

### /cmr/layout/add-devices

Package: cmr; Type: Command

This command adds multiple devices to the topology in bulk.

**Arguments**

- `labels` (object; unset): Select devices that should be added to the topology using labels. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used. (default value: **all**)
- `devices` (multi { array-id, device: enum }; unset): Select specific devices that should be added to the topology.

### /cmr/layout/rebuild-links

Package: cmr; Type: Command

If links between nodes in the topology were deleted or not generated initially, this command automatically generates them based on port data.

**Arguments**

- `labels` (object; unset): Select devices using labels for which links should be rebuilt. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used. (default value: **all**)
- `devices` (multi { array-id, device: enum }; unset): Select specific devices for which links should be rebuilt.
