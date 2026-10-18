# /ip/nat-pmp

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/nat-pmp

Type: Settings Directory

NAT Port Mapping Protocol (NAT-PMP, [RFC 6886](https://www.rfc-editor.org/rfc/rfc6886)) service settings. While enabled, the service waits for mapping requests from the internal interfaces on UDP port 5351, shown as a dynamic `natpmp` entry in `/ip/service`. Configuration examples are on the [NAT-PMP guide page](../../guides/firewall-and-quality-of-service/nat-pmp.md).

**Arguments**

- `enabled` (bool): Enable the NAT-PMP service. Default: no.
