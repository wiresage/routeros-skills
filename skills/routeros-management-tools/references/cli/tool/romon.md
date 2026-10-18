# /tool/romon

> Source: https://manual.mikrotik.com/docs/cli-reference/tool/romon

Type: Settings Directory

Settings of the RoMON (Router Management Overlay Network) service. See the [RoMON](../../guides/management-tools/romon.md) guide.

**Arguments**

- `enabled` (bool): Disable or enable the RoMON feature.
- `id` (macAddr): MAC address to use as the ID of this router.
- `secrets` (multi { array-id, name: string }): A list of global secrets used for RoMON message hashing.

**Read-only arguments**

- `current-id` (macAddr): The RoMON ID currently in use, automatically selected from the port MAC address when `id` is not set.

## Commands

### /tool/romon/discover

Type: Command

Discover the routers reachable through the [RoMON](../../guides/management-tools/romon.md) overlay network. The table refreshes continuously (stop with `q`); `duration` stops after the given time.

**Flags**

- `A`: active

**Read-only arguments**

- `address` (macAddr): RoMON ID (MAC address) of the discovered router
- `cost` (num): Accumulated cost of the RoMON path to the router (sum of the port costs configured with `/tool/romon/port`)
- `hops` (num): Number of RoMON hops between this router and the discovered router
- `path` (multi { array-id, path-hop: macAddr }): Path of RoMON IDs (MAC addresses) through which the discovery reply passed
- `l2mtu` (num): The smallest L2 MTU on the RoMON path
- `identity` (string): The RouterOS system identity of the discovered router
- `version` (string): The RouterOS version of the discovered router
- `board` (string): The board name of the discovered router
- `uptime` (time): The uptime of the discovered router

### /tool/romon/ping

Type: Command

Ping a router over the [RoMON](../../guides/management-tools/romon.md) overlay by its RoMON ID, without any IP connectivity.

**Arguments**

- `id` (macAddr): RoMON ID (MAC address) of the router to ping
- `size` (num): Size of the ping packet payload (default value: **32**)
- `interval` (time): Interval between pings (default value: **1s**)
- `count` (num): Number of pings to send (default value: **100**)

**Read-only arguments**

- `seq` (num): Ping sequence number
- `host` (macAddr): RoMON ID (MAC address) of the router that answered
- `time` (time): Round-trip time of the reply
- `size` (num): Size of the reply
- `status` (string): Failure reason (for example `timeout`); empty on success
- `sent` (num): Pings sent
- `received` (num): Replies received
- `packet-loss` (num): Percentage of lost pings
- `min-rtt` (time): Smallest round-trip time
- `avg-rtt` (time): Average round-trip time
- `max-rtt` (time): Largest round-trip time

### /tool/romon/ssh

Syscap: security; Type: Command

Open an SSH session to a router over the [RoMON](../../guides/management-tools/romon.md) overlay, without any IP connectivity.

**Arguments**

- `address` (macAddr): RoMON ID (MAC address) of the router to connect to
- `command` (string): A command to run on the remote router instead of an interactive session
- `user` (string): The user account on the remote router to log in with
- `output-to-file` (string): Save the output of `command` to a file on the local router
