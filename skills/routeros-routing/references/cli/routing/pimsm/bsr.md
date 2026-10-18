# /routing/pimsm/bsr

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/bsr

Conditions: !smips; Type: Directory

**Flags**

- `D`: dynamic

**Read-only arguments**

- `instance` (enum)
- `scope4` (address (flags=4/); unset)
- `scope6` (num; unset)
- `address` (address (flags=46))
- `priority` (num)
- `hash-mask-length` (num)
- `state` (enum: accept-any | accept-preferred | candidate | pending | elected)
