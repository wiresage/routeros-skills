# /ipv6/firewall/raw

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/firewall/raw

Type: Directory

**Arguments**

- `chain` (enum; mandatory): Specifies to which chain the rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.
- `action` (enum: accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | drop | notrack): Action to take if a packet is matched by the rule: `accept` - accept the packet. A packet is not passed to the next firewall rule.  `add-dst-to-address-list` - add the destination address to the address list specified by the `address-list` parameter.  `add-src-to-address-list` - add the source address to the address list specified by the `address-list` parameter.  `drop` - drop the packet.  `jump` - jump to the user-defined chain specified by the value of the `jump-target` parameter.  `log` - add a message to the system log containing the following data: in-interface, out-interface, src-mac, protocol, src-ip:port->dst-ip:port, and length of the packet. After a packet is matched it is passed to the next rule in the list, similar to `passthrough`.  `notrack` - skip connection tracking for the packet.  `passthrough` - if a packet is matched by the rule, increase the counter and go to the next rule (useful for statistics).  `return` - passes control back to the chain from where the jump took place.
- `jump-target` (enum): Name of the target chain to jump to. Applicable only if `action=jump`.
- `tls-host` (super { ! , tls-host: string }): Matches HTTPS traffic based on TLS SNI hostname. Accepts GLOB syntax for wildcard matching. The matcher will not be able to match the hostname if the TLS handshake frame is fragmented into multiple TCP segments.
- `in-interface` (super { ! , interface: iface_enum }): Interface the packet has entered the router.
- `out-interface` (super { ! , interface: iface_enum }): Interface the packet is leaving the router.
- `in-interface-list` (super { ! , interface-list: enum }): Set of interfaces defined in interface list. Works the same as `in-interface`.
- `out-interface-list` (super { ! , interface-list: enum }): Set of interfaces defined in interface list. Works the same as `out-interface`.
- `in-bridge-port` (super { ! , interface: iface_enum }): Actual interface the packet has entered the router if the incoming interface is a bridge. Works only if `use-ip-firewall` is enabled in bridge settings.
- `out-bridge-port` (super { ! , interface: iface_enum }): Actual interface the packet leaves the router if the outgoing interface is a bridge. Works only if `use-ip-firewall` is enabled in bridge settings.
- `in-bridge-port-list` (super { ! , interface-list: enum }): Set of interfaces defined in interface list. Works the same as `in-bridge-port`.
- `out-bridge-port-list` (super { ! , interface-list: enum }): Set of interfaces defined in interface list. Works the same as `out-bridge-port`.
- `packet-mark` (super { ! , mark: enum }): Matches packets marked by the mangle facility with a particular packet mark. If `no-mark` is set, the rule will match any unmarked packet.
- `src-port` (super { ! , port: multi { range: range [ .. 65535] } }): List of source ports and ranges of source ports. Applicable only if the protocol is TCP or UDP.
- `dst-port` (super { ! , port: multi { range: range [ .. 65535] } }): List of destination port numbers or port number ranges.
- `port` (super { ! , port: multi { range: range [ .. 65535] } }): Matches if any (source or destination) port matches the specified list of ports or port ranges. Applicable only if `protocol` is TCP or UDP.
- `icmp-options` (super { ! , type: num [0 .. 255] , [code] [ :range [ .. 255]] }): Matches ICMP type:code fields.
- `src-mac-address` (super { ! , address: macAddr }): Matches the source MAC address of the packet.
- `content` (super { ! , content: string }): Matches packets that contain the specified text.
- `ingress-priority` (super { ! , ingress-priority: num [0 .. 63] }): Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP, or MPLS EXP bit.
- `priority` (super { ! , priority: num [0 .. 63] }): Matches the packet's priority after a new priority has been set. Priority may be derived from VLAN, WMM, DSCP, MPLS EXP bit, or from the priority set by using the set-priority action.
- `dscp` (super { ! , dscp: num [0 .. 63] }): Matches the DSCP IP header field.
- `tos` (super { ! , tos: num [0 .. 255] , [mask] [ /num [0 .. 255]] })
- `limit` (super { ! , count: num [1 .. 32000000000] , [time] [ /time [1 .. ]] , [burst] ,num [ .. 2000000000] , [mode] [ :enum (packet | bit)] }): Matches packets up to a limited rate (packet rate or bit rate). A rule with this matcher will match until this limit is reached. Parameters are written in the following format: `rate[/time],burst:mode`.
  - `rate` - packet or bit count per time interval to match.
  - `time` - specifies the time interval in which the packet or bit rate cannot be exceeded (optional, 1s will be used if not specified).
  - `burst` - initial number of packets or bits to match: this number gets recharged every 10ms so burst should be at least 1/100 of a rate per second.
  -  `mode` - packet or bit mode.
- `dst-limit` (super { count: num , [time] [ /time] , [burst] ,num , [mode] ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) , [expire] [ /time] }): Matches packets until a given rate is exceeded. Rate is defined as packets per time interval. As opposed to the `limit` matcher, every flow has its own limit. Flow is defined by a mode parameter. Parameters are written in the following format: `rate[/time],burst,mode[/expire]`.
  - `rate` - packet count per time interval per-flow to match.
  - `time` - specifies the time interval in which the packet count rate per flow cannot be exceeded (optional, 1s will be used if not specified).
  - `burst` - initial number of packets per flow to match: this number gets recharged by one every time/rate, up to this number.
  - `mode` - specifies what unique fields define flow (src-address, dst-address, src-and-dst-address, dst-address-and-port, addresses-and-dst-port).
  - `expire` - specifies interval after which flow with no packets will be allowed to be deleted (optional).
- `time` (super { ! , start: time [0 .. 86400] , [end] -time [0 .. 86400] , [day] ,ubit (sun, mon, tue, wed, thu, fri, sat) }): Creates a filter based on the packets' arrival time and date or, for locally generated packets, departure time and date. The matcher takes into account the time and timezone configured on the router.
- `random` (super { percent: num [1 .. 99] }): Matches packets randomly with a given probability.
- `nth` (super { ! , every: num [1 .. ] , [packet] [ ,num [1 .. ]] }): Matches every nth packet: `nth=2,1` will match every first packet of 2, hence, 50% of all the traffic matched by the rule.
- `tcp-mss` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] }): Matches the TCP MSS value of an IP packet.
- `per-connection-classifier` (super { ! , values-to-hash: enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) , [denominator] :num [1 .. ] , [remainder] /num [0 .. ] }): PCC matcher allows dividing traffic into equal streams with the ability to keep packets with a specific set of options in one particular stream.
- `packet-size` (super { ! , min: num [ .. 65535] , [max] -num [ .. 65535] }): Matches packets of specified size or size range in bytes.
- `log` (bool): Add a message to the system log containing the following data: in-interface, out-interface, src-mac, protocol, src-ip:port->dst-ip:port, and length of the packet. Allows logging of packets even if the action is not `log`, useful for debugging the firewall.
- `log-prefix` (string): Adds the specified text at the beginning of every log message. Applicable if `action=log` or `log=yes` is configured.
- `ipsec-policy` (super { direction: enum (in | out) , [policy] ,enum (none | ipsec) }): Matches the policy used by IPsec. Value is written in the following format: `direction, policy`.
  - `in` - valid in the PREROUTING, INPUT, and FORWARD chains.
  - `out` - valid in the POSTROUTING, OUTPUT, and FORWARD chains.
  - `ipsec` - matches if the packet is subject to IPsec processing.
  - `none` - matches packets that are not subject to IPsec processing.
- `protocol` (super { ! , protocol: enum (icmpv6) }): Matches the particular IP protocol specified by protocol name or number.
- `src-address` (super { ! , address: ip6Prefix }): Matches packets whose source is equal to the specified IP or falls into the specified IP range.
- `dst-address` (super { ! , address: ip6Prefix }): Matches packets whose destination is equal to the specified IP or falls into the specified IP range.
- `src-address-list` (super { ! , address-list: enum }): Matches the source address of a packet against a user-defined address list. Supports only one list.
- `dst-address-list` (super { ! , address-list: enum }): Matches the destination address of a packet against a user-defined address list. Supports only one list.
- `address-list` (enum): Name of the address list to be used. Applicable if the action is `add-dst-to-address-list` or `add-src-to-address-list`.
- `address-list-timeout` (alt { address-list-timeout: enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff } , address-list-timeout: time [ .. 21474836] }): How long the address stays in `address-list` after the `add-src-to-address-list` or `add-dst-to-address-list` action adds it. With a time, the rule adds a dynamic entry (`D`) that the router removes when the time ends; each new match of the rule resets the time to its full value. The maximum is `35w3d13h13m56s`. An address that is already a static entry in the list stays static.
  - `none-dynamic` (`0s`) - Add a dynamic entry without a timeout. It is not saved in the configuration and a reboot clears it.
  - `none-static` - Add a static entry. It is saved in the configuration and in exports, and stays after a reboot until you remove it.
- `src-address-type` (super { ! , type: ubit (unicast, local, anycast, multicast, unreachable) }): Matches the source address type: `unicast` - an IP address used for point-to-point transmission.  `local` - the address is assigned to one of the router's interfaces.  `anycast` - a packet sent to the nearest node in a group.  `multicast` - a packet is forwarded to a defined group of devices.  `unreachable` - the address is unreachable.
- `dst-address-type` (super { ! , type: ubit (unicast, local, anycast, multicast, unreachable) }): Matches the destination address type: `unicast` - an IP address used for point-to-point transmission.  `local` - the destination address is assigned to one of the router's interfaces.  `anycast` - a packet sent to the nearest node in a group.  `multicast` - a packet is forwarded to a defined group of devices.  `unreachable` - the address is unreachable.
- `headers` (super { ! , type: ubit (hop, dst, route, frag, ah, esp, none, proto) , [mode] [ :enum (exact | contains)] }): Matches IPv6 next-header. Two types of header matching are possible controlled by the `mode` parameter: `contains` - soft matching, matches at least selected headers.  `exact` - matches the exact set of selected headers.
- `tcp-flags` (super { !, , flags: multi { array-id, array-id, flag: super { ! , flag: enum (fin | syn | rst | psh | ack | urg | ece | cwr) } } }): Matches the specified TCP flags: `ack` - acknowledging data.  `cwr` - congestion window reduced.  `ece` - ECN-echo flag (explicit congestion notification).  `fin` - close connection.  `psh` - push function.  `rst` - reset connection.  `syn` - new connection.  `urg` - urgent data.
- `hop-limit` (super { mode: enum (equal | not-equal | less-than | greater-than) , [value] :num [0 .. 255] }): Matches the hop limit field in the IPv6 header.

## Commands

### /ipv6/firewall/raw/reset-counters

Type: Command

### /ipv6/firewall/raw/reset-counters-all

Type: Command
