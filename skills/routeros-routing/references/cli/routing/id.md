# /routing/id

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/id

Type: Directory

Global Router ID election configuration. The Router ID can be configured explicitly or elected from one of the router's IP addresses.

For each VRF table, RouterOS adds a dynamic ID instance that elects the Router ID from one of the IP addresses in that VRF:

```text
[admin@rack1_b33_CCR1036] /routing/id> print
Flags: D - DYNAMIC, I - INACTIVE
Columns: NAME, DYNAMIC-ID, SELECT-DYNAMIC-ID, SELECT-FROM-VRF
#   NAME   DYNAMIC-ID      SELECT-D   SELE
0 D main   111.111.111.2   only-vrf   main

```

**Flags**

- `X`: disabled
- `D`: dynamic
- `I` (inactive): If there was a problem getting a valid ID, then the item can become inactive.

**Arguments**

- `name` (string)
- `id` (ipAddr; unset): Router ID to set explicitly. If the Router ID is not set, RouterOS can elect it from one of the configured IP addresses. See `select-dynamic-id` and `select-from-vrf`.
- `select-dynamic-id` (ubit (any, only-static, only-loopback, only-vrf, only-active, lowest); unset): Select which IP addresses RouterOS uses for Router ID election:
  - `any` - any address found on the router can be elected as the Router ID.
  - `lowest` - select the lowest IP address.
  - `only-static` - pick only statically configured addresses.
  - `only-active` - select an ID only from active IP addresses.
  - `only-loopback` - select an ID only from loopback addresses (loopback address is any non-point-to-point /32 address).
  - `only-vrf` - select an ID only from the selected VRF. Works with `select-from-vrf`.
- `select-from-vrf` (enum; unset): VRF from which to select IP addresses for the ID election.

**Read-only arguments**

- `dynamic-id` (ipAddr): Currently selected ID.
