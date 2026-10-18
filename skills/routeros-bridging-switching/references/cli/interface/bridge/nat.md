# /interface/bridge/nat

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/bridge/nat

Type: Directory

**Arguments**

- `all` (switch)
- `static` (switch)
- `dynamic` (switch)
- `chain` (enum; mandatory)
- `action` (enum: accept | passthrough | drop | jump | return | log | mark-packet | set-priority | src-nat | dst-nat | redirect | arp-reply)
- `jump-target` (enum)
- `new-packet-mark` (enum)
- `to-src-mac-address` (macAddr)
- `to-dst-mac-address` (macAddr)
- `to-arp-reply-mac-address` (macAddr)
- `new-priority` (num)
- `passthrough` (bool)
- `in-interface` (super { ! , interface: iface_enum })
- `in-bridge` (super { ! , interface: iface_enum })
- `out-interface` (super { ! , interface: iface_enum })
- `out-bridge` (super { ! , interface: iface_enum })
- `in-interface-list` (super { ! , interface-list: enum })
- `out-interface-list` (super { ! , interface-list: enum })
- `in-bridge-list` (super { ! , interface-list: enum })
- `out-bridge-list` (super { ! , interface-list: enum })
- `src-mac-address` (super { ! , address: macAddr , [mask] /macAddr })
- `dst-mac-address` (super { ! , address: macAddr , [mask] /macAddr })
- `mac-protocol` (super { ! , protocol: alt { protocol-name: enum (length) , protocol-number: num [ .. 65535] } })
- `src-address` (super { ! , address: ipAddr , [netmask] /num [ .. 32] })
- `dst-address` (super { ! , address: ipAddr , [netmask] /num [ .. 32] })
- `src-address6` (super { ! , address: ip6Prefix })
- `dst-address6` (super { ! , address: ip6Prefix })
- `src-port` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `dst-port` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `ip-protocol` (super { ! , protocol: enum () })
- `packet-mark` (super { ! , mark: enum })
- `packet-type` (super { ! , type: enum (host | broadcast | multicast | other-host) })
- `limit` (super { count: num , [time] [ /time] , [burst] ,num })
- `802.3-sap` (super { ! , sap: num [ .. 0xff] })
- `802.3-type` (super { ! , type: num [ .. 0xffff] })
- `arp-opcode` (super { ! , opcode: alt { common-opcode: enum (request | reply | request-reverse | reply-reverse | drarp-request | drarp-reply | drarp-error | inarp-request | inarp-reply | arp-nak) , opcode-number: num [ .. 65535] } })
- `arp-hardware-type` (super { ! , type: num [ .. 0xffff] })
- `arp-packet-type` (super { ! , type: num [ .. 0xffff] })
- `arp-src-address` (super { ! , address: ipAddr , [netmask] /num [ .. 32] })
- `arp-dst-address` (super { ! , address: ipAddr , [netmask] /num [ .. 32] })
- `arp-src-mac-address` (super { ! , address: macAddr , [mask] /macAddr })
- `arp-dst-mac-address` (super { ! , address: macAddr , [mask] /macAddr })
- `arp-gratuitous` (super { gratuitous: bool })
- `vlan-id` (super { ! , type: num [ .. 4095] })
- `vlan-priority` (super { ! , type: num [ .. 7] })
- `vlan-encap` (super { ! , protocol: alt { protocol-name: enum (length) , protocol-number: num [ .. 65535] } })
- `stp-type` (super { ! , type: alt { type-name: enum (config | tcn) { config:0, tcn:0x80 } , type-number: num [ .. 255] } })
- `stp-flags` (super { ! , type: alt { type-name: enum (topology-change | topology-change-ack) { topology-change:1, topology-change-ack:0x80 } , type-number: num [ .. 255] } })
- `stp-root-priority` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `stp-root-address` (super { ! , address: macAddr , [mask] /macAddr })
- `stp-root-cost` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `stp-sender-priority` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `stp-sender-address` (super { ! , address: macAddr , [mask] /macAddr })
- `stp-port` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `stp-msg-age` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `stp-max-age` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `stp-hello-time` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `stp-forward-delay` (super { ! , min: num [0 .. 65535] , [max] -num [0 .. 65535] })
- `ingress-priority` (super { ! , priority: num [0 .. 63] })
- `tls-host` (super { ! , tls-host: string })
- `log` (bool)
- `log-prefix` (string)

## Commands

### /interface/bridge/nat/reset-counters

Type: Command

### /interface/bridge/nat/reset-counters-all

Type: Command
