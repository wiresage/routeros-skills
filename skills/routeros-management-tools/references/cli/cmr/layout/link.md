# /cmr/layout/link

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr/layout/link

Package: cmr; Type: Directory

Configuration for a specific link in a topology.

**Arguments**

- `layout` (enum; mandatory): Name of the layout where the link will be displayed.
- `node1` (enum; mandatory): Name of the first node in a link.
- `node2` (enum; mandatory): Name of the second node in a link.

**Read-only arguments**

- `links` (multi { array-id, array-id, link: super { port1: object , [port2] --object } }): Detailed information about the link state, such as PoE status, interface names, and traffic information. A `*` before a port name marks a direct, physical link. Example: `ether1(,tx=85.9KiB,rx=10.8KiB)--ether23(poe=powered-on,tx=10.9KiB,rx=86.8KiB)`
