# /routing/ospf/area/range

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/area/range

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive
- `A`: advertise

**Arguments**

- `area` (enum; mandatory): The OSPF area associated with this range.
- `prefix` (address (flags=46/); mandatory): The network prefix of this range.
- `advertise` (bool): Whether to create a summary LSA and advertise it to the adjacent areas.
- `cost` (num; unset): The cost of the summary LSA this range will create. Default - use the largest cost of all routes used (i.e. routes that fall within this range).
