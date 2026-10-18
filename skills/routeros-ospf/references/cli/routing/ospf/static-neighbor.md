# /routing/ospf/static-neighbor

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/static-neighbor

Type: Directory

Static configuration of the OSPF neighbors. Required for non-broadcast multi-access networks.

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `area` (enum; mandatory): Name of the area the neighbor belongs to.
- `address` (address (flags=46i); mandatory): The unicast IP address and an interface that can be used to reach the IP of the neighbor. For example, `address=1.2.3.4%ether1` indicates that a neighbor with IP `1.2.3.4` is reachable on the `ether1` interface.
- `instance-id` (num)
- `poll-interval` (time): How often to send hello messages to the neighbors that are in a `down` state (i.e., there is no traffic from them).
