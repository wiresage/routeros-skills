# /routing/filter/community-large-list

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/filter/community-large-list

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `list` (enum; mandatory): Reference name.
- `communities` (object): List of large communities expressed in the following format: `admin:value1:value2`, where each section can be an integer [0..4294967295].
- `regexp` (string): Regexp matcher to match communities. The community set with only the regexp parameter cannot be used to append/delete communities.
