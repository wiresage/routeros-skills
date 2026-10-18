# /routing/stats/origin

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/stats/origin

Type: Directory

**Flags**

- `Y`: synthetic
- `Z`: terminal
- `X`: stopping
- `A`: abandoned
- `H`: hold
- `U`: attrs-updated
- `M`: attrs-merge

**Read-only arguments**

- `name` (string)
- `type` (string)
- `instance-id` (num)
- `dealer-id` (num)
- `publisher-idx` (num)
- `route-type` (string)
- `pid` (enum)
- `route-count` (multi { route-count: num })
- `in-policy` (num)
- `update.in-policy` (num)
- `total-route-count` (num)
