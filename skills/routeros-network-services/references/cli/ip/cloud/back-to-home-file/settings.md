# /ip/cloud/back-to-home-file/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/back-to-home-file/settings

Syscap: cloud-vpn; Type: Settings Directory

State of the File Share service: its DNS name, certificate and connection to the relay servers. The service starts with the first share in [`/ip/cloud/back-to-home-file`](../back-to-home-file.md) and stops when the last one is removed. For an explanation, see [How File Share works](../../../../guides/network-management/cloud/file-share.md#how-file-share-works).

**Arguments**

- `prefer-relay-code` (string): Code of the relay region to prefer, from `relay-regions`, for example `EUR1`. When it is empty, the router picks a relay by its round-trip time (`relay-rtts`). Default: empty.

**Read-only arguments**

- `enabled` (bool): `yes` while at least one share exists and the service runs. It changes to `no` when you remove the last share.
- `dns-name` (string): Name the shares are served under: `<serial>.routingthecloud.net`, with the serial number in lower case. When the router uses the relay, the name resolves to the relay.
- `status` (string): State of the service, for example:
  - `getting cert status: requesting SSL certificate`, `requesting validation`, `requesting authorization`, `requesting order finalization` - The router is getting the Let's Encrypt certificate.
  - `running` - The service runs.
- `relay-rtts` (multi { code: string }): Round-trip time to each relay region over IPv4 and IPv6, for example `EUR1 (ip4: 1.103ms, ip6: timeout)`.
- `relay-ipv4-status` (string): Connection to the relay over IPv4, for example `connected (region: EUR1 ip: <relay address> rtt: 1.103ms reachable: unknown )`.
- `relay-ipv6-status` (string): Connection to the relay over IPv6, for example `testing rtt` while the router measures the round-trip time.
- `relay-regions` (multi { code: string }): Relay regions the router can use, for example `EUR1` and `USA1`. Use a code from this list in `prefer-relay-code`.
- `relay-addresses` (multi { address: ipAddr }): IPv4 addresses of the relay servers, one per region.
- `relay-addresses-ipv6` (multi { address: ip6Addr }): IPv6 addresses of the relay servers, one per region.
- `certificate` (enum: none): Certificate the shares use, `fileshare-<serial>.routingthecloud.net` in `/certificate`. `none` after `remove-certificate`.

## Commands

### /ip/cloud/back-to-home-file/settings/remove-certificate

Syscap: cloud-vpn; Type: Command

Deletes the File Share certificate from `/certificate`. It works only when no share exists; otherwise, it fails with `cannot remove certificate while file shares active`. The next share requests a new certificate. See [Stop File Share](../../../../guides/network-management/cloud/file-share.md#stop-file-share).
