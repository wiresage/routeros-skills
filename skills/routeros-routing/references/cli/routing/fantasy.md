# /routing/fantasy

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/fantasy

Type: Directory

Fantasy menu is a fancy way to generate large amount of routes for testing purposes. Main benefits of this approach compared to a script are the generation speed and simplicity. It is easy to remove all fantasy generated routes just by disabling the fantasy rule.

Fantasy uses a random generator from hashed route sequence number, seed and other parameters.

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `name` (string)
- `dst-address` (address (flags=46it/)): Prefix from which route will be generated.
- `prefix-length` (range): Prefix length for generated route (can be specified as integer range). For example `dst-address=192.168.0.0/16` and `prefix-length=24` will generate /24 routes from `192.168.0.0/16` subnet.
- `gateway` (address (flags=46iv/))
- `scope` (range): Scope to be set; can be set as range.
- `target-scope` (range): Target scope to be set; can be set as range.
- `instance-id` (range)
- `dealer-id` (range)
- `seed` (string): Random generator seed.
- `count` (num)
- `offset` (num): Route sequence number offset.
- `priv-offs` (range)
- `priv-size` (range)
- `use-hold` (bool)
