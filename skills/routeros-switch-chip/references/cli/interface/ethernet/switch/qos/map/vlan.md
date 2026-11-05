# /interface/ethernet/switch/qos/map/vlan

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/qos/map/vlan

Syscap: rbswitch and crs_prestera; Type: Directory

Matches VLAN priorities (802.1p PCP/DEI fields) to QoS profiles. By default, all values are matched to the default QoS profile.

**Flags**

- `*`: default
- `D`: dynamic
- `X`: disabled
- `I`: inactive
- `H`: hw-offloaded

**Arguments**

- `map` (enum): The name of the mapping table.
- `pcp` (multi { pcp-range: range [0 .. 7] }; mandatory): VLAN priority (PCP) value(-s) for the lookup.
- `dei-only` (bool): Maps only packets with DEI (formerly CFI) bit set in the VLAN header.
- `profile` (enum; mandatory): The name of the QoS profile to assign to the matched packets.
