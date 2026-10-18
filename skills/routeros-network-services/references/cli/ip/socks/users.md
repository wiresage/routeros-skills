# /ip/socks/users

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/socks/users

Type: Directory

Users for SOCKS5 username/password authentication, used when [`/ip/socks`](../socks.md) has `auth-method=password`. New users are created enabled. For more information, see [SOCKS](../../../guides/network-management/socks.md).

**Flags**

- `X` (disabled): disabled. The user cannot authenticate. New users are created enabled.

**Arguments**

- `name` (string; mandatory): Username for SOCKS5 authentication.
- `password` (string; mandatory): Password for SOCKS5 authentication. Not shown in `print` output.
- `only-one` (bool)
- `rate-limit` (string): Rate limit applied to the user's proxied connections, in bits per second, for example `64000`.
