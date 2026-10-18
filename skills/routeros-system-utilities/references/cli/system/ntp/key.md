# /system/ntp/key

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ntp/key

Type: Directory

Symmetric keys for NTP authentication, selected by their key ID in [`/system/ntp/client/servers`](client/servers.md) and [`/system/ntp/server`](server.md). The key value is sensitive: it is not shown in `print` or saved in `export` output. See the [NTP](../../../guides/system-information-and-utilities/ntp.md) guide.

**Arguments**

- `key-id` (num; mandatory): Key identifier, referenced by `auth-key` in the client and server configuration.
- `key-val` (string; mandatory): The shared secret. Not included in `export` output.
