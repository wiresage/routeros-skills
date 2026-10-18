# /ip/cloud/back-to-home-user

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/back-to-home-user

Syscap: cloud-vpn; Type: Directory

Back To Home users. Each user is a WireGuard client of the `back-to-home-vpn` interface with its own keys and addresses, and the router adds a dynamic peer for it. The Back To Home app creates a user for each tunnel it sets up: `name` is the model identifier of the phone, for example `iPhone18,1`, and the comment is the tunnel name shown in the app. Several users can have the same name. [`show-client-config`](back-to-home-user.md) prints the client configuration of a user. Users can only be added while Back To Home runs (`vpn-status: running`); otherwise, `add` fails with `back-to-home vpn not enabled`. Revoking Back To Home (`back-to-home-vpn=revoked-and-disabled` in [`/ip/cloud`](../cloud.md)) deletes all users. For an overview, see [Back To Home](../../../guides/network-management/cloud/back-to-home.md).

**Flags**

- `X` (disabled): The user is disabled.
- `A` (active): The user is active.

**Arguments**

- `name` (string): Name of the user. Names do not have to be unique; the Back To Home app uses the phone's model identifier. The client configuration carries the user's comment, or the name when there is no comment, in the `# Name` comment line, which the Back To Home app uses as the tunnel name.
- `expires` (alt { expires: enum (never) { never:0xFFFFFFFF } , interval: time , date-time: date }): When the user stops working: `never` (default), a date and time such as `"2026-10-01 00:00:00"`, or a time interval such as `1d`. The router converts an interval to a date. The value cannot be changed after the user is created: `set` accepts it but keeps the old date. To change it, create the user again.
- `client-dns` (address (flags=46/)): DNS server written into the user's client configuration (`DNS =`). Without it, the configuration has no DNS line and the client keeps its own DNS servers.
- `client-allowed-address` (multi { client-allowed-address: address (flags=46/) }): Addresses the client sends through the tunnel, written into the client configuration as `AllowedIPs` of the router's peer, for example `192.168.88.0/24` for access to the local network only. Default: empty (`0.0.0.0/0, ::/0`, all traffic).
- `allow-lan` (bool): Whether the user can reach the local network. With `no`, the router puts the user's address in the dynamic address list `back-to-home-lan-restricted-peers`, and a dynamic forward rule drops its traffic to the `LAN` interface list, so the user can only use the internet through the router. Default: no.
- `private-key` (string): Private key of the user's client configuration. The router generates it when it is not set.
- `public-key` (string): Public key of the user. The router derives it from the generated key when it is not set.
- `file-access` (enum: disabled | read-only | full): Access of the user to files in `file-access-path` through the File Share service. Adding a user with file access makes the router request the File Share certificate.
  - `disabled` (default) - No file access.
  - `read-only` - Read files.
  - `full` - Read and change files.
- `file-access-path` (string): Directory the user can access with `file-access`, as `/file/print` shows it. Required when `file-access` is not `disabled`; otherwise, adding the user fails with `invalid files path`.

**Read-only arguments**

- `client-address` (multi { address: address (flags=46/) }): IPv4 and IPv6 addresses of the user in the tunnel, the next free addresses from 192.168.216.0/24 and fc00:0:0:216::/64. The router assigns them; they cannot be set.
- `file-access-token` (string): Token the router generates for the user's file access. The client configuration includes it in a `# FilesToken` line when `file-access` is not `disabled`.

## Commands

### /ip/cloud/back-to-home-user/show-client-config

Syscap: cloud-vpn; Type: Command

Prints the WireGuard configuration of a user and the same configuration as a QR code. Import it in a WireGuard app. Give the user by its number or with `[find name=<name>]`; a name alone is a syntax error. The configuration has a second peer with a placeholder key and `AllowedIPs = 0.0.0.0/32`, which carries no traffic; a client connects through the first peer, also when the router uses a relay.

**Read-only arguments**

- `conf` (string): WireGuard configuration of the user.
- `qr` (pic): The configuration as a QR code.
