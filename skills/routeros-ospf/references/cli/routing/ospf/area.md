# /routing/ospf/area

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/area

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive
- `D`: dynamic
- `T`: transit-capable

**Arguments**

- `name` (string): The name of the area
- `instance` (enum; mandatory): Name of the OSPF instance this area belongs to.
- `area-id` (ipAddr): OSPF area identifier. If the router has networks in more than one area, then an area with `area-id=0.0.0.0` (the backbone) must always be present. The backbone always contains all area border routers. The backbone is responsible for distributing routing information between non-backbone areas. The backbone must be contiguous, i.e. there must be no disconnected segments. However, area border routers do not need to be physically connected to the backbone - connection to it may be simulated using a virtual link.
- `type` (enum: default | stub | nssa): The area type. Read more on the area types in the [OSPF user guides](../../../guides/user-guides/routing-and-networking-protocols/unicast/ospf/areas-and-virtual-links.md).
- `no-summaries` (switch): Flag parameter, if set then the area will not flood summary LSAs in the stub area.
- `default-cost` (num; unset): Default cost of injected LSAs into the area. If the value is not set, then stub area type-3 default LSA will not be originated.
- `nssa-translator` (enum: candidate | no | yes; unset): The parameter indicates which ABR will be used as a translator from `type-7` to `type-5` LSA. Applicable only if area type is NSSA.
  - yes - the router will be always used as a translator.
  - no - the router will never be used as a translator.
  - candidate - OSPF elects one of the candidate routers to be a translator.

**Read-only arguments**

- `transit-capable` (bool)
