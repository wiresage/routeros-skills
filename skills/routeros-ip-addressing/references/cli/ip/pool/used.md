# /ip/pool/used

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/pool/used

Type: Directory

Menu lists all used IP addresses from IP pools.

**Arguments**

- `pool` (enum): Name of the IP pool.
- `address` (ipAddr): IP address that is assigned to a client from the pool.
- `owner` (string): Name of the service which acquired this IP address.
- `info` (string): Additional info, for example, for DHCP - MAC address from the leases menu and for PPP - connections username of a PPP type client.
