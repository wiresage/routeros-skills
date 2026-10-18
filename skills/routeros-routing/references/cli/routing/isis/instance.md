# /routing/isis/instance

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/isis/instance

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `name` (string)
- `vrf` (enum)
- `afi` (ubit (ip, ipv6))
- `system-id` (string)
- `areas` (multi { area: string })
- `areas-max` (num)
- `in-filter-chain` (enum; unset)
- `metric-type` (enum: old | wide | both; unset)
- `l1.redistribute` (ubit (connected, static, rip, ospf, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac); unset)
- `l1.out-filter-select` (enum; unset)
- `l1.out-filter-chain` (enum; unset)
- `l1.originate-default` (enum: never | always | if-installed; unset)
- `l1.lsp-max-size` (num; unset)
- `l1.lsp-max-age` (num; unset)
- `l1.lsp-update-interval` (num; unset)
- `l1.lsp-refresh-interval` (num; unset)
- `l2.redistribute` (ubit (connected, static, rip, ospf, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac); unset)
- `l2.out-filter-select` (enum; unset)
- `l2.out-filter-chain` (enum; unset)
- `l2.originate-default` (enum: never | always | if-installed; unset)
- `l2.lsp-max-size` (num; unset)
- `l2.lsp-max-age` (num; unset)
- `l2.lsp-update-interval` (num; unset)
- `l2.lsp-refresh-interval` (num; unset)
