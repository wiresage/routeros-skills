# /system/ntp/server

> Source: https://manual.mikrotik.com/docs/cli-reference/system/ntp/server

Type: Settings Directory

NTP server settings. The server answers time queries from NTP clients on the network; it serves the time the router itself is synchronized to. See the [NTP](../../../guides/system-information-and-utilities/ntp.md) guide.

**Arguments**

- `enabled` (bool): Enable the NTP server. Default: no.
- `broadcast` (bool): Periodically send the time to the addresses in `broadcast-addresses`. Default: no.
- `multicast` (bool): Distribute the time to the local network as multicast. Default: no.
- `manycast` (bool): Take part in manycast discovery, in which clients find servers through multicast queries. Default: no.
- `broadcast-addresses` (multi { broadcast-address: ipAddr }): Broadcast addresses to send the time to when `broadcast` is enabled.
- `vrf` (enum): VRF the server operates in. Default: main.
- `use-local-clock` (bool): Use the router's local clock as a time reference when no better source is available; the daemon then serves and follows its own clock at `local-clock-stratum`. The client's `status` shows `using-local-clock` in this state. The router's clock without external synchronization drifts, so do not use this for precise timekeeping. Default: no.
- `local-clock-stratum` (num): Stratum announced for the local clock when `use-local-clock` is enabled. Default: 5.
- `auth-key` (enum: none): Key from [`/system/ntp/key`](key.md) for symmetric-key authentication of the time exchange. Default: none (no authentication).
