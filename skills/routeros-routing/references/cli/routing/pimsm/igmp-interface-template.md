# /routing/pimsm/igmp-interface-template

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/igmp-interface-template

Conditions: !smips; Type: Directory

**Flags**

- `X` (disabled): The template is disabled.

**Arguments**

- `instance` (enum; mandatory): The PIM instance the template belongs to.
- `interfaces` (object { interface: iface_enum }; unset): The interfaces that follow this template and run IGMP/MLD.
- `robustness` (num): The robustness value of the IGMP/MLD querier on the interfaces of this template.
- `query-interval` (time): How often to send out IGMP/MLD General Queries on the interfaces of this template.
- `query-response-interval` (time): The maximum response time advertised in IGMP/MLD General Queries on the interfaces of this template.
- `last-member-query-interval` (time): The response time advertised in IGMP/MLD group-specific queries on the interfaces of this template.
