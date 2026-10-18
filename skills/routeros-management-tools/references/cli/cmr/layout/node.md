# /cmr/layout/node

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/layout/node

Package: cmr; Type: Directory

Configuration for a specific node in a topology.

**Arguments**

- `name` (string): Name of the node.
- `layout` (enum; mandatory): Name of the layout where the node will be displayed.
- `device` (enum; unset): Name of the device that the node will represent in the topology. Mutually exclusive with `target-layout` parameter.
- `target-layout` (enum; unset): Name of the layout that the node will represent in the topology. Mutually exclusive with `device` parameter.
- `x` (num; unset): X coordinate of the node in a topology. Default X value is incremented by 200 each time a new node is added, to prevent overlapping when no coordinates are specified. (default value: **0+200*n**)
- `y` (num; unset): Y coordinate of the node in a topology. (default value: **0**)
