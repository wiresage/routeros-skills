# /ipv6/nd/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/ipv6/nd/settings

Type: Settings Directory

The IPv6 ND menu has a sub-menu "Settings" which allows changing global neighbor discovery settings.

**Arguments**

- `router-advertisement-route-distance` (num): Specify the distance that must be used when installing SLAAC default route.
- `router-advertisement-ignored-options` (ubit (dns, mtu)): Lets you ignore specific received ND options such as DNS and MTU. If RA will contain such options, they simply will be ignored if selected on this list.
