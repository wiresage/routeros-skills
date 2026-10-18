# /routing/bgp/session

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/session

Conditions: !smips; Type: Directory

List of BGP already established, not yet connected or disconnected sessions.

**Flags**

- `E`: established

**Read-only arguments**

- `name` (string)
- `instance` (enum)
- `remote.address` (address (flags=46iv+:))
- `remote.port` (num)
- `remote.as` (super { as: as , [sub-as] [ /as] })
- `remote.id` (ipAddr)
- `remote.refused-cap-opt` (bool)
- `remote.capabilities` (ubit (mp, rr, orf, enhe, em, sec, ml, role, gr, as4, dyn, ms, ap, err, llgr, fqdn)): Remote peer's advertised/supported capabilities.
- `remote.afi` (ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)): Remote peer's advertised/supported address families.
- `remote.hold-time` (alt { special: enum (infinity) , number: time [3 .. 65535] })
- `remote.messages` (num): Number of BGP messages received from remote peer.
- `remote.bytes` (num): Total number of bytes received from remote peer.
- `remote.gr-restart` (bool)
- `remote.gr-time` (num)
- `remote.gr-afi` (ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6))
- `remote.gr-afi-fwp` (ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6))
- `remote.eor` (ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)): List of address families that received end-of-rib from remote peer.
- `remote.role` (enum: provider | route-server | route-server-client | customer | peer): Role received from the remote peer. See [Route Leak Prevention](../../../guides/user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention.md).
- `local.role` (enum: ibgp | ibgp-rr | ebgp | ebgp-provider | ebgp-rs | ebgp-rs-client | ebgp-customer | ebgp-peer): Locally configured role. See [Route Leak Prevention](../../../guides/user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention.md).
- `local.address` (address (flags=46iv:))
- `local.port` (num)
- `local.as` (super { as: as , [sub-as] [ /as] })
- `local.id` (ipAddr)
- `local.cluster-id` (ipAddr)
- `local.capabilities` (ubit (mp, rr, enhe, role, gr, as4, ap))
- `local.afi` (ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn))
- `local.messages` (num)
- `local.bytes` (num)
- `local.eor` (ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4))
- `output.affinity` (enum: main | alone | remote-as | instance | afi | vrf | input)
- `output.procid` (num)
- `output.filter-select` (enum)
- `output.filter-chain` (enum)
- `output.network` (enum)
- `output.add-path` (ubit (ip, ipv6))
- `output.remove-private-as` (bool)
- `output.default-originate` (enum: never | if-installed | always)
- `output.default-prepend` (num)
- `output.no-client-to-client-reflection` (bool)
- `output.no-early-cut` (bool)
- `output.keep-sent-attributes` (bool)
- `output.last-notification` (string): Content of last sent notification message.
- `input.affinity` (enum: main | alone | remote-as | instance | afi | vrf)
- `input.procid` (num): Shows which routing process the session is tied to.
- `input.filter` (enum)
- `input.allow-as` (num)
- `input.as-override` (bool)
- `input.ignore-as-path-len` (bool)
- `input.limit-process-routes` (num)
- `input.add-path` (ubit (ip, ipv6))
- `input.last-notification` (string): Content of last received notification message.
- `vrf` (enum)
- `ibgp` (switch): Indicates if the session is iBGP.
- `ebgp` (switch): Indicates if the session is eBGP.
- `limit-exceeded` (switch): Indicates if received prefix count exceeds configured prefix limit by `input.limit-process-routes-ipv4` and/or `input.limit-process-routes-ipv6`.
- `stopped` (switch): Indicates whether session is administratively stopped.
- `routing-table` (enum)
- `nexthop-choice` (enum: default | force-self | propagate)
- `cisco-vpls-nlri-len-fmt` (enum: auto-bits | auto-bytes | bits | bytes)
- `multihop` (bool)
- `hold-time` (alt { special: enum (infinity) , number: time [3 .. 65535] })
- `keepalive-time` (time)
- `use-bfd` (bool)
- `uptime` (time): Uptime of established session.
- `last-started` (date)
- `last-stopped` (date)
- `save-to` (string)
- `prefix-count` (num)
- `keepalive-timer` (time)
- `restart-timer` (time)

## Commands

### /routing/bgp/session/clear

Conditions: !smips; Type: Command

Clear the session flags. For example, to be able to re-establish a session after the prefix limit is reached "limit-exceeded" flag must be cleared. It can be done by specifying `flag` parameter, which is able to take the following values:

* input-last-notification
* limit-exceeded
* output-last-notification
* refused-cap-opt
* stopped

**Arguments**

- `flag` (enum: refused-cap-opt | stopped | limit-exceeded | input-last-notification | output-last-notification): A flag to be cleared from BGP session.

### /routing/bgp/session/dump-saved-advertisements

Conditions: !smips; Type: Command

 Dump saved advertisements from specified BGP session in the \*.pcap file.

**Arguments**

- `save-to` (string): The filename where to store the PCAP data.

### /routing/bgp/session/refresh

Conditions: !smips; Type: Command

Send route refresh to a specified BGP session. Is used to trigger re-sending all the routes from the remote peer.

**Arguments**

- `afi` (enum: ip | ipv6 | l2vpn | vpnv4): Specifies for which address family to send route refresh.

### /routing/bgp/session/resend

Conditions: !smips; Type: Command

Resend prefixes to a specified BGP session. The command takes two arguments:

**Arguments**

- `afi` (enum: ip | ipv6 | l2vpn | vpnv4): Specifies for which address families to resend prefixes.

### /routing/bgp/session/stop

Conditions: !smips; Type: Command
