# /ipv6/route

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/route

Type: Directory

**Flags**

- `D`: dynamic
- `X`: disabled
- `I`: inactive
- `A`: active
- `c`: connect
- `s`: static
- `r`: rip
- `b`: bgp
- `o`: ospf
- `i`: is-is
- `d`: dhcp
- `v`: vpn
- `m`: modem
- `g`: slaac
- `y`: bgp-mpls-vpn
- `H`: hw-offloaded
- `+`: ecmp

**Arguments**

- `dst-address` (address (flags=6/))
- `routing-table` (enum)
- `pref-src` (address (flags=6); unset)
- `gateway` (address (flags=6ivSL); unset)
- `blackhole` (switch)
- `check-gateway` (enum: none | arp | ping | bfd; unset)
- `distance` (num; unset)
- `scope` (num; unset)
- `target-scope` (num; unset)
- `vrf-interface` (iface_enum; unset)
- `suppress-hw-offload` (bool; syscap=crs_prestera)

**Read-only arguments**

- `immediate-gw` (multi { gw: address (flags=6i) })
