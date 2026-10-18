# /interface/mesh/port

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/mesh/port

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive
- `D`: dynamic

**Arguments**

- `interface` (iface_enum; mandatory)
- `mesh` (iface_enum; mandatory)
- `path-cost` (num)
- `hello-interval` (time)
- `port-type` (enum: auto | WDS | wireless | ethernet)

**Read-only arguments**

- `active-port-type` (enum: wireless | WDS | ethernet-mesh | ethernet-bridge | ethernet-mixed)
- `dr-address` (macAddr)
