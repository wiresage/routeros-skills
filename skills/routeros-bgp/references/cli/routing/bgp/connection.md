# /routing/bgp/connection

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/connection

Conditions: !smips; Type: Directory

A list of all connection-specific parameters can be seen in the table below.

In addition to connection-specific parameters, template-specific parameters are also directly exposed in this menu, for easier configuration in simple scenarios (when templates are not necessary).

**Flags**

- `D`: dynamic
- `X`: disabled
- `I`: inactive

**Arguments**

- `name` (string; mandatory)
- `instance` (enum; mandatory)
- `remote.address` (address (flags=46i/+:); unset): Remote address used to connect and/or listen to.
- `remote.port` (num; unset)
- `remote.as` (super { as: as , [sub-as] [ /as] }; unset): Remote AS number. If not specified BGP will determine remote AS automatically from the OPEN message.
- `remote.ttl` (num): Acceptable minimum Time To Live, the hop limit for this TCP connection. For example, if 'ttl=255' then only single-hop neighbors will be able to establish the connection. This property only affects EBGP peers.
- `remote.allowed-as` (enum; unset): Name of the num-list containing remote AS numbers that will be allowed to connect. Useful for dynamic peer configuration.
- `local.address` (address (flags=46i:); unset)
- `local.port` (num; unset)
- `local.ttl` (num): Time To Live (hop limit) that will be recorded in sent TCP packets.
- `local.role` (enum: ibgp | ibgp-rr | ebgp | ebgp-provider | ebgp-rs | ebgp-rs-client | ebgp-customer | ebgp-peer; mandatory): BGP role. In most scenarios, set to iBGP or eBGP. For more information on BGP roles and route leak prevention, see [Route Leak Prevention](../../../guides/user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention.md) and the corresponding [RFC 9234](https://tools.ietf.org/html/rfc9234).
- `tcp-md5-key` (string; unset): Key used to authenticate the connection with TCP MD5 signature as described in [RFC 2385](https://tools.ietf.org/html/rfc2385). Leave empty to disable authentication.
- `connect` (bool): Whether to allow the router to initiate the connection.
- `listen` (bool): Enable listening for incoming connections. If `remote.address` is a host address and listening is enabled, close the listening socket after the first successful accept. If `remote.address` is a subnet and listening is enabled, the listening socket remains open after the first successful accept with a hard-coded limit of 256 open connections.
- `routing-table` (enum; unset): Name of the routing table, to install routes in. Overrides the instance parameter.
- `vrf` (enum; unset): Name of the VRF BGP connections operate on. By default uses the "main" routing table.
- `templates` (multi { template: enum }; unset): List of template names that will be used to inherit parameter values from. Useful feature, to easily configure groups with overlapping configuration options.
- `as` (as; unset): A 32-bit BGP autonomous system number. The value accepts AS-Plain or AS-Dot formats. Override the instance ASN and configure BGP confederation using the following format: _`confederation_as/as`_. For example, if your AS is 34 and your confederation AS is 43, set `as=43/34`.
- `nexthop-choice` (enum: default | force-self | propagate; unset): Affect outgoing **NEXT\_HOP** attribute selection. Next-hops set in filters always take precedence and are not changed on route reflection except when set in a filter.   default - select the next-hop as described in [`RFC 4271`](https://tools.ietf.org/html/rfc4271)   force-self - use the local address of the interface that connects to the peer as the next-hop   propagate - propagate received next-hop; if the route has a BGP **NEXT\_HOP** attribute, use it as the next-hop; otherwise, fall back to the default case
- `multihop` (bool; unset): Enable when the remote peer is more than one hop away.This option affects outgoing next-hop selection as described in [`RFC 4271`](https://tools.ietf.org/html/rfc4271) (for eBGP only, excluding iBGP peers local to the confederation). It also affects:Whether to accept connections from peers not in the same network (the remote address of the connection is used for this check)Whether to accept incoming routes with a NEXT\_HOP attribute not in the same network as the address used to establish the connectionThe target scope of routes installed from this peer; routes from multi-hop or iBGP peers resolve their next-hops through IGP routes by default
- `hold-time` (alt { special: enum (infinity) , number: time [3 .. 65535] }; unset): Specifies the BGP Hold Time value to be used when negotiating with peers.According to the BGP specification, if the router does not receive successive **KEEPALIVE** and/or **UPDATE** and/or **NOTIFICATION** messages within the period specified in the Hold Time field of the **OPEN** message, then the BGP connection to the peer will be closed.The minimal `hold-time` value of both peers will be used (note that the special value 0 or 'infinity' is lower than any other value)*   infinity \- never expire the connection and never send keepalive messages.
- `keepalive-time` (time; unset): The interval between keepalive messages, if not set then by default keepalive is 1/3 of the `hold-time`.
- `afi` (ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn); unset): List of address families this peer can exchange routing information. The remote peer must support BGP capabilities optional parameter (they usually do) to negotiate any other address families than IP.
- `cisco-vpls-nlri-len-fmt` (enum: auto-bits | auto-bytes | bits | bytes; unset): VPLS NLRI length format type. Used for compatibility with Cisco VPLS. \[\[Read more>>\]\].
- `output.remove-private-as` (bool; unset): If set, then the BGP **AS-PATH** attribute is removed before sending out route updates if the attribute contains only private AS numbers.The removal process happens before routing filters are applied and before the local, AS number is prepended to the AS path.
- `output.as-override` (bool; unset): If set, then all instances of the remote peer's AS number in the BGP **AS-PATH** attribute are replaced with the local AS number before sending a route update to that peer. Happens before routing filters and prepend.
- `use-bfd` (bool; unset): Whether to use the BFD protocol for faster connection state detection.
- `save-to` (string; unset): Filename to save BGP protocol-specific packet content (Exported PDU) into pcap format. This method allows much simpler peer-specific packet capturing for debugging purposes.
- `output.add-path` (ubit (ip, ipv6); unset): Enable sending of additional paths for specified address families (BGP Addpath).
- `output.affinity` (enum: main | alone | remote-as | instance | afi | vrf | input; unset): Configure output multicore processing. Read more in [Routing Protocol Multi-core Support](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support) article.   **alone** - input and output of each session is processed in its own process, the most likely best option when there are a lot of cores and a lot of peers   **afi, instance, vrf, remote-as** - try to run input/output of new session in process with similar parameters   **main** - run input/output in the main process (could potentially increase performance on single-core even possibly on multicore devices with small amount of cores)   **input** - run output in the same process as input (can be set only for output affinity)
- `output.redistribute` (ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac); unset): Enable redistribution of specified route types.
- `output.filter-select` (enum; unset): Name of the routing select chain to be used for prefix selection. If not specified, then default selection is used.
- `output.filter-chain` (enum; unset): Name of the routing filter chain to be used on the output prefixes. If the chain is not specified, then BGP by default accepts everything.
- `output.network` (enum; unset): Name of the address list used to send local networks. The network is sent only if a matching IGP route exists in the routing table and its **ORIGIN** attribute is set to IGP, other distribution methods have **ORIGIN** attribute set to INCOMPLETE.
- `output.network-blackhole` (bool; unset)
- `output.default-originate` (enum: never | if-installed | always; unset): Specifies default route (0.0.0.0/0) distribution method. 'if-installed' option can be used to distribute default route only if corresponding IGP route present in the routing table.
- `output.default-prepend` (num; unset): How many times to prepend local ASN.
- `output.no-client-to-client-reflection` (bool; unset): Disable client-to-client route reflection in Route Reflector setups.
- `output.no-early-cut` (bool; unset): The early cut is the mechanism, to guess (based on default RFC behavior) what would happen with the sent NLRI when received by the remote peer. If the algorithm determines that the NLRI is going to be dropped, a peer will not even try to send it. However such behavior may not be desired in specific scenarios, then this option should be used to disable the early cut feature. Early cut works with eBGP sessions.
- `output.keep-sent-attributes` (bool; unset): Store in memory sent prefix attributes, required for `dump-saved-advertisements` command to work. By default, sent-out prefixes are not stored to preserve the router's memory. An option should be enabled only for debugging purposes when necessary to see currently advertised prefixes.
- `input.add-path` (ubit (ip, ipv6); unset): Accept received additional paths (BGP Addpath) for specified address families.
- `input.attr-error-handling` (enum: default | revised)
- `input.affinity` (enum: main | alone | remote-as | instance | afi | vrf; unset): Configure input multi-core processing. Read more in [Routing Protocol Multi-core Support](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support) article.
  - **alone** - input and output of each session are processed in its own process, most likely the best option when there are a lot of cores and a lot of peers.
  - **afi, instance, vrf, remote-as** - try to run input/output of new session in process with similar parameters.
  - **main** - run input/output in the main process (could potentially increase performance on single-core even possibly on multi-core devices with a small amount of cores).
- `input.filter` (enum; unset): Name of the routing filter chain to be used on input prefixes. This happens after NLRIs are processed. If the chain is not specified, then BGP by default accepts everything.
- `input.filter-nlri` (enum; unset): Name of the filter chain that will filter incoming IPv4/IPv6 NLRIs directly before they are  stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session restart.
- `input.allow-as` (num; unset): Indicates how many times to allow your own AS number in AS-PATH, before discarding a prefix.
- `input.accept-nlri` (enum; unset): Name of the ipv4/6 address-list. A quick way to filter incoming updates with specific NLRIs. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session restart.
- `input.filter-communities` (enum; unset): A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.
- `input.filter-ext-communities` (enum; unset): A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.
- `input.filter-large-communities` (enum; unset): A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.
- `input.accept-communities` (enum; unset): A quick way to filter incoming updates with specific communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.
- `input.accept-ext-communities` (enum; unset): A quick way to filter incoming updates with specific extended communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.
- `input.accept-large-communities` (enum; unset): A quick way to filter incoming updates with specific large communities. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.
- `input.filter-unknown` (enum; unset): A quick way to filter incoming updates with specific "unknown" attributes. It allows filtering incoming messages directly before they are even parsed and stored in memory, that way significantly reducing memory usage. Regular input filter chain can only reject prefixes which means that it will still eat memory and will be visible in /routing route table as "not active, filtered". Changes to be applied required session refresh.
- `input.limit-process-routes-ipv4` (enum: 10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000; unset): Try to limit the amount of received IPv4 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. [BGP session "clear"](session.md) command must be used to reset the flag if the limit is reached.
- `input.limit-process-routes-ipv6` (enum: 10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000; unset): Try to limit the amount of received IPv6 routes to the specified number. This number does not represent the exact number of routes going to be installed in the routing table by the peer. BGP session "clear" command must be used to reset the flag if the limit is reached.

**Read-only arguments**

- `local.default-address` (address (flags=46i:))
