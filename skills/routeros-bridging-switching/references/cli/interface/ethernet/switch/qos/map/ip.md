# /interface/ethernet/switch/qos/map/ip

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/map/ip

Syscap: rbswitch and crs_prestera; Type: Directory

Matches DSCP values to QoS profiles.

**Flags**

- `*`: default
- `D`: dynamic
- `X`: disabled
- `I`: inactive
- `H`: hw-offloaded

**Arguments**

- `map` (enum): The name of the mapping table. If not set, the standard (built-in) mapping table gets altered.
- `dscp` (multi { dscp-range: range [0 .. 63] }; mandatory): DSCP value(-s) for the lookup.
- `profile` (enum; mandatory): The name of the QoS profile to assign to the matched packets.
