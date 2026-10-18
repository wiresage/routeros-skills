# /ip/ipsec/mode-config

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/mode-config

Type: Directory

ISAKMP and IKEv2 configuration attributes are configured in this menu.

> **Note**
>
> Not all IKE implementations support multiple split networks provided by the `split-include` option.

> **Note**
>
> If the RouterOS client is the initiator, it always sends the CISCO UNITY extension, and RouterOS supports only split-include from this extension.

> **Note**
>
> Both attributes Cisco Unity Split DNS (attribute type 28675) and RFC8598 (attribute type 25) are supported, ROS responds to these attributes but only as a responder.

> **Note**
>
> You cannot use `system-dns` and `static-dns` at the same time; ROS can use only one DNS.

**Flags**

- `*` (default): Whether the item is the default.
- `R` (responder): Whether the item acts as a responder.

**Arguments**

- `name` (string; mandatory): Mode config entry name.
- `responder` (bool): Specifies whether the configuration will work as an initiator (client) or responder (server). The initiator will request mode-config parameters from the responder.
- `system-dns` (bool): When this option is enabled, DNS addresses will be taken from /ip/dns.
- `static-dns` (object { address: alt { address4: ipAddr } }): Manually specified DNS server IP addresses to be sent to the client.
- `address` (ipAddr): Address to assign to the peer.
- `address-pool` (enum: none): issue one address for peer from this pool
- `address-prefix-length` (num): issued address netmask
- `split-include` (object { subnet: alt { subnet4: ipPrefix } }): List of subnets in CIDR format, which will be tunneled. Subnets will be sent to the peer using the CISCO UNITY extension. A remote peer will create specific dynamic policies.
- `split-dns` (multi { array-id, dns: string }): List of DNS names that will be resolved using a system-dns=yes or static-dns= setting.
- `src-address-list` (enum): Specifying an address list will generate dynamic source NAT rules. This parameter is only available with responder=no. A roadWarrior client with NAT
- `connection-mark` (enum): conection-mark to be added to srcnat chain for initiator
- `use-responder-dns` (enum: no | yes | exclusively): if the dns servers sent should be used by the initiator
