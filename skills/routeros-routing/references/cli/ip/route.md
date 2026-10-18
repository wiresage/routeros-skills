# /ip/route

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/route

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
- `y`: bgp-mpls-vpn
- `H`: hw-offloaded
- `+`: ecmp

**Arguments**

- `dst-address` (address (flags=4/))
- `routing-table` (enum)
- `pref-src` (address (flags=4); unset)
- `gateway` (address (flags=46ivL); unset)
- `blackhole` (switch)
- `check-gateway` (enum: none | arp | ping | bfd; unset)
- `distance` (num; unset)
- `scope` (num; unset)
- `target-scope` (num; unset)
- `vrf-interface` (iface_enum; unset)
- `suppress-hw-offload` (bool; syscap=crs_prestera)

**Read-only arguments**

- `immediate-gw` (multi { gw: address (flags=46i) })
- `local-address` (address (flags=4iv))

## Commands

### /ip/route/check

Type: Command

**Arguments**

- `src-ip` (ipAddr)
- `dst-ip` (ipAddr)

**Read-only arguments**

- `status` (string)
- `interface` (iface_enum)
- `nexthop` (ipAddr)
