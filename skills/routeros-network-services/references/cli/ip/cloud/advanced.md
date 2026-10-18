# /ip/cloud/advanced

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/advanced

Type: Settings Directory

Advanced DDNS settings. For an overview, see [DDNS](../../../guides/network-management/cloud.md#ddns).

**Arguments**

- `use-local-address` (bool): Whether the DNS name points to the router's local address instead of its public address. With `yes`, `dns-name` resolves to the address the router sends its requests from, for example a private address behind NAT, and `public-address` still shows the public address. Default: no.
