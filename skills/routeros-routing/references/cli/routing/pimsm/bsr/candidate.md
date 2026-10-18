# /routing/pimsm/bsr/candidate

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/bsr/candidate

Conditions: !smips; Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `instance` (enum)
- `address` (address (flags=46i))
- `scope4` (address (flags=4/); unset)
- `scope6` (num; unset)
- `priority` (num)
- `hash-mask-length` (num)

**Read-only arguments**

- `state` (enum: candidate | pending | elected)
