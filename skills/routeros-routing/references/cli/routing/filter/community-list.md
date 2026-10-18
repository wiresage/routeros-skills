# /routing/filter/community-list

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/filter/community-list

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `list` (enum; mandatory): Reference name.
- `communities` (object): List of communities expressed either as a **well-known** name or in the following format: `as:number`, where each section can be integer [0..65535].
  Accepted **well-known** names:
  - `accept-own`
  - `graceful-shutdown`
  - `no-advertise`
  - `no-llgr`
  - `route-filter-6`
  - `accept-own-nh`
  - `internet`
  - `no-export`
  - `no-peer`
  - `route-filter-xlate-4`
  - `blackhole`
  - `llgr-stale`
  - `local-as`
  - `route-filter-4`
  - `route-filter-xlate-6`
- `regexp` (string): Regexp matcher to match communities. The community set with only the regexp parameter cannot be used to append/delete communities.
