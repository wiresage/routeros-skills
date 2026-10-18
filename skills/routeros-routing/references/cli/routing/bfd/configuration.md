# /routing/bfd/configuration

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bfd/configuration

Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive

**Arguments**

- `vrf` (enum; unset): The Virtual Routing and Forwarding instance to which this configuration applies.
- `interfaces` (object { interface: iface_enum }; unset): list of interfaces where BFD configuration should be active.
- `addresses` (object { address: alt { ipv6: ip6Prefix , ip: ipPrefix } }; unset): This config entry will only apply to BFD sessions established with these specific remote neighbors.
- `address-list` (enum; unset): Firewall address list name. BFD configuration will apply if remote IP address is contained within specified list.
- `min-tx` (time; unset): Desired transmit interval that the local router would like to use when sending BFD packets to the neighbor.
- `min-rx` (time; unset): Minimum receive interval that the local router requires between received BFD packets.
- `multiplier` (num; unset): This value is multiplied by the negotiated transmission interval to determine the **Hold Time**; if no packets within the Hold time are received - the neighbor is declared down. `Hold Time = negotiated interval × multiplier`
- `forbid-bfd` (bool; unset): if = **yes**: BFD sessions matching criteria will be prohibited.
- `keyring` (enum; mandatory)
