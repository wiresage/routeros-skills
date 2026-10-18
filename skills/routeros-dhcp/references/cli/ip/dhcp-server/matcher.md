# /ip/dhcp-server/matcher

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/matcher

Type: Directory

Assigns addresses from a specific IP pool to clients whose request contains a matching DHCP option, for example a vendor class identifier or host name. Clients with a static lease keep their static lease even when a matcher matches them. For examples, see [DHCP Server](../../../guides/network-management/dhcp/server.md).

**Flags**

- `X` (disabled): The matcher is disabled.

**Arguments**

- `name` (string; mandatory): Name of the matcher.
- `server` (enum: all; mandatory): DHCP server the matcher applies to, or `all` for every server.
- `address-pool` (enum: static-only): IP pool to give matching clients an address from.
- `option-set` (enum: none): Option set (`/ip/dhcp-server/option/sets`) to send to matching clients.
- `code` (alt { number: num [1 .. 254] , option: enum (vendor-specific) }; mandatory): Code of the DHCP option to match (1-254).
- `value` (string; mandatory): Value to look for in the option, as text or as hex with the `0x` prefix.
- `matching-type` (enum: exact | substring; mandatory): How `value` is compared with the option:
  - `exact` - The option must be equal to `value`.
  - `substring` - `value` can appear anywhere in the option.

  When two substring matchers match the same option, it is random which one applies.
