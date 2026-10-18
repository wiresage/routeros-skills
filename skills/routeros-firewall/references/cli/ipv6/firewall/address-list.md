# /ipv6/firewall/address-list

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/firewall/address-list

Type: Directory

An IPv6 firewall address list is a named set of IPv6 addresses and prefixes that IPv6 filter, NAT, mangle and raw rules match with `src-address-list` and `dst-address-list`. Entries are added here, by the `add-src-to-address-list` and `add-dst-to-address-list` rule actions, and from DNS names in the list. These actions pass the packet on to the next rule. IPv6 lists are separate from the IPv4 lists in [`/ip/firewall/address-list`](../../ip/firewall/address-list.md), even when a list has the same name. See [Address lists](../../../guides/firewall-and-quality-of-service/firewall/address-lists.md).

**Flags**

- `X` (disabled): Disabled: the entry stays in the list but does not match.
- `D` (dynamic): Dynamic: the entry has a timeout or was added with `dynamic=yes`, by a firewall rule with a time or `none-dynamic`, from a resolved DNS name or by another feature (DNS, DHCP server). Dynamic entries are not saved in the configuration or in exports, and a reboot clears them.

**Arguments**

- `list` (enum; mandatory): Name of the address list. A new name creates the list. Rules match the list with `src-address-list` and `dst-address-list`.
- `address` (alt { address: ip6Prefix , dns-name: string }): An IPv6 address, a prefix or a DNS name. A prefix with host bits is stored as its network, and an address without a prefix length is stored as a /128. Ranges are not accepted (`is not a valid dns name`). For a DNS name, the router adds one dynamic entry for each AAAA record in the answer, with the name as the comment, and resolves the name again when the record expires. An address that is already in the list is refused with `already have such entry`.
- `timeout` (time): Time after which the router removes the entry. An entry with a timeout is dynamic (`D`): it is not saved in the configuration or in exports, and a reboot clears it. The maximum is `35w3d13h13m56s`. Without a timeout, the entry stays until you remove it.
- `dynamic` (bool): With `yes`, the entry is dynamic (`D`) and has no timeout: it is not saved in the configuration and a reboot clears it. Default: no.

**Read-only arguments**

- `creation-time` (date): When the entry was created. A static entry keeps this time after a reboot; an imported entry gets the time of the import.
