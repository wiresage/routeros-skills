# /routing/pimsm/static-rp

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/static-rp

Conditions: !smips; Type: Directory

The static-rp menu allows manually defining the multicast group to RP mappings. Such a mechanism is not robust to failures but does at least provide a basic interoperability mechanism.

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `instance` (enum; mandatory): The name of the PIM instance this static RP belongs to.
- `group` (address (flags=46/)): The multicast group that belongs to a specific RP.
- `address` (address (flags=46)): The IP address of the static RP.
