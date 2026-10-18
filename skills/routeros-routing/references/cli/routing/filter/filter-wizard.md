# /routing/filter/filter-wizard

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/filter/filter-wizard

Type: Command

**Arguments**

- `chain` (enum)
- `dst` (super { ! , dst: alt { dst-list: enum , dst: address (flags=46/+) } }; unset)
- `dst-len` (super { ! , dst-len: range [ .. 128] }; unset)
- `gateway` (super { ! , dst: alt { dst-list: enum , dst: address (flags=46/+) } }; unset)
- `match-chain` (super { ! , chain: enum }; unset): returns true if provided chain did not reject
- `routing-table` (super { ! , table: enum }; unset): name of the routing table the route was imported from
- `afi` (super { ! , afi: ubit (ip, ipv6, l2vpn, vpnv4, vpnv6, l2vpn-cisco) }; unset): address family of the route
- `protocol` (super { ! , protocol: ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac, bgp-mpls-vpn) }; unset): protocol type from which the route was imported
- `bgp-atomic-aggregate` (bool)
- `bgp-local-origin` (bool): returns true if prefix is locally originated, e.g BGP network
- `suppress-hw-offload` (bool; syscap=crs_prestera)
- `use-te-nexthop` (bool)
- `blackhole` (bool): matches blackhole routes
- `ospf-type` (super { ! , ospf-type: enum (intra | inter | ext1 | ext2 | nssa1 | nssa2) }; unset)
- `rpki` (super { ! , rpki-type: enum (unknown | valid | invalid) }; unset): RPKI validation status of the prefix
- `bgp-origin` (super { ! , bgp-origin: ubit (igp, egp, incomplete) }; unset): matches BGP Origin attribute
- `bgp-as-path` (string): regexp that matches BGP AS-Path attribute, see documentation for more details
- `bgp-communities-match` (super { ! , match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list) }; unset)
- `bgp-communities` (object; unset)
- `bgp-communities-list-name` (enum; unset)
- `bgp-ext-communities-match` (super { ! , match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list) }; unset)
- `bgp-ext-communities` (object; unset)
- `bgp-ext-communities-list-name` (enum; unset)
- `bgp-large-communities-match` (super { ! , match: enum (any | any-list | equal | equal-list | includes | includes-list | subset | subset-list) }; unset)
- `bgp-large-communities` (object; unset)
- `bgp-large-communities-list-name` (enum; unset)
- `distance` (super { ! , value: alt { num-list: enum , range: range [ .. 255] } }; unset)
- `scope` (super { ! , value: alt { num-list: enum , range: range [ .. 255] } }; unset)
- `scope-target` (super { ! , value: alt { num-list: enum , range: range [ .. 255] } }; unset)
- `bgp-weight` (super { ! , value: alt { num-list: enum , range: range [ .. 65535] } }; unset)
- `bgp-local-pref` (super { ! , value: alt { num-list: enum , range: range } }; unset)
- `bgp-med` (super { ! , value: alt { num-list: enum , range: range } }; unset)
- `bgp-out-med` (super { ! , value: alt { num-list: enum , range: range } }; unset)
- `bgp-as-path-length` (super { ! , value: alt { num-list: enum , range: range } }; unset)
- `ospf-metric` (super { ! , value: alt { num-list: enum , range: range } }; unset)
- `set-distance` (alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , val: num [1 .. 255] , value: composite { inc: [ enum (| add | sub)] , val: num [1 .. 255] } }; unset)
- `set-scope` (alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , val: num [1 .. 255] , value: composite { inc: enum (| add | sub) , val: num [1 .. 255] } })
- `set-scope-target` (alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , val: num [1 .. 255] , value: composite { inc: enum (| add | sub) , val: num [1 .. 255] } })
- `set-bgp-weight` (alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , val: num [ .. 65535] , value: composite { inc: enum (| add | sub) , val: num [ .. 65535] } })
- `set-bgp-local-pref` (alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , val: num , value: composite { inc: enum (| add | sub) , val: num } }): set a value of the BGP Local-Pref attribute
- `set-bgp-med` (alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , val: num , value: composite { inc: enum (| add | sub) , val: num } })
- `set-bgp-out-med` (alt { num-props: enum (distance | scope | target-scope | dst-len | bgp-weight | bgp-med | bgp-out-med | bgp-local-pref | bgp-path-len | bgp-path-prepend | bgp-path-peer-prepend | bgp-input-local-as | bgp-input-remote-as | bgp-output-local-as | bgp-output-remote-as | ospf-metric | ospf-tag | ospf-ext-metric | ospf-ext-tag | rip-metric | rip-tag | rip-ext-metric | rip-ext-tag) , val: num , value: composite { inc: enum (| add | sub) , val: num } })
- `set-suppress-hw-offload` (bool; syscap=crs_prestera)
- `set-use-te-nexthop` (bool)
- `set-blackhole` (bool)
- `set-gw-check` (enum: none | arp | ping | bfd): set gateway check
- `set-gateway` (address (flags=46))
- `set-comment` (string)
- `set-bgp-communities` (object): set a value of the BGP Communities attribute
- `set-bgp-communities-list` (enum; unset)
- `set-bgp-ext-communities` (object)
- `set-bgp-large-communities` (object)
- `action` (enum: accept | reject | jump | return; unset)
- `jump-target-chain` (enum; unset)
- `rpki-verify` (enum; unset): Enable RPKI verification in the current chain from specified RPKI group

**Read-only arguments**

- `result` (string)
