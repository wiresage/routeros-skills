# /openflow

> Source: https://manual.mikrotik.com/docs/cli-reference/openflow

Package: openflow; Type: Directory

This menu lists the configuration of OpenFlow clients.

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory): Reference name of the entry
- `datapath-id` (super { number: num [0 .. 65535] , [mac-address] /macAddr }): Datapath ID consisting of two parts (integer number [0..65535] and MAC address) separated by a slash.
- `version` (enum: default | 1 | 1.3): Version of the OpenFlow standard to be used.
- `passive-port` (num): The port on which the OpenFlow agent listens for connections from the controller.
- `controllers` (object { contr: super { controler-protocol: enum (tcp | tls) , [controller-address] /ip6Addr , [controller-port] /num [1 .. 65535] } }): Configuration of the connection to the controller. Supported protocols are **tcp** and **tls**. Example: `tcp/1.2.3.4/6654`.
- `certificate` (enum: none; unset): [Certificate from certificate store](https://manual.mikrotik.com/docs/authentication-authorization-accounting/certificates). Used together with the `verify-peer` parameter.
- `verify-peer` (enum: required | none | if-cert-present; unset): Verify peer's identity against the router's [certificate store](https://manual.mikrotik.com/docs/authentication-authorization-accounting/certificates).
- `isolate-controllers` (bool; unset): Whether to isolate the configured controllers from each other.

**Read-only arguments**

- `openflow-fast-path-packets` (num): Number of packets sent to fast path.
- `openflow-fast-path-bytes` (num): Number of bytes set to fast path.
