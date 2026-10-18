# /zerotier/controller

> Source: https://manual.mikrotik.com/docs/cli-reference/zerotier/controller

Package: zerotier; Type: Directory

Zerotier configuration controller.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `I` (inactive): Whether the controller is inactive.

**Arguments**

- `disabled` (bool): Whether an item is disabled.
- `instance` (enum; mandatory): ZeroTier instance name.
- `name` (string; mandatory): Short name for this controller.
- `network` (string): 16-digit network ID.
- `private` (bool): Enables access control.
- `broadcast` (bool): Allows receiving broadcast (FF:FF:FF:FF:FF:FF) packets.
- `mtu` (num): Network MTU.
- `multicast-limit` (num): Maximum recipients for a multicast packet.
- `ip-range` (super { first: address (flags=4) , [last] [ -address (flags=4)] }): IP range, for example, 172.16.16.1-172.16.16.254.
- `ip6-range` (super { first: address (flags=6) , [last] [ -address (flags=6)] }): IPv6 range, for example, `fd00:feed:feed:beef::-fd00:feed:feed:beef:ffff:ffff:ffff:ffff`.
- `ip6-rfc4193` (bool): The rfc4193 mode gives every member a /128 on a /88 network.
- `ip6-6plane` (bool): Gives every member a /80 within a /40 network and uses NDP emulation to route all IPs under that /80 to its owner.
- `routes` (object { route: super { dst: address (flags=46/) , [gw] [ @address (flags=46)] } }): Push routes in the following format: `Routes ::= Route[,Routes] Route ::= Dst[@Gw]`.
