# /routing/filter/community-ext-list

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/filter/community-ext-list

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `list` (enum; mandatory): Reference name.
- `communities` (object): List of extended communities expressed as a **raw** integer value or in the typed format: `type:value`, where type can be:
  - `rt` - route-target
  - `soo` -  site of origin.

  The value depends on the type.
- `regexp` (string): Regexp matcher to match communities. The community set with only the regexp parameter cannot be used to append/delete communities.
