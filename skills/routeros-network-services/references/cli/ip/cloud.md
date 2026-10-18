# /ip/cloud

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud

Type: Settings Directory

Settings of the MikroTik cloud services: the DDNS name, the time update at startup and Back To Home. The router sends its requests to `cloud2.mikrotik.com` on UDP port 15252. For an overview and examples, see [Cloud](../../guides/network-management/cloud.md) and [Back To Home](../../guides/network-management/cloud/back-to-home.md).

**Arguments**

- `ddns-enabled` (enum: auto | yes): Whether the router registers a DNS name (`dns-name`) with the cloud server and keeps it pointing to the router's public address.
  - `auto` (default) - DDNS is on only while Back To Home is enabled (`back-to-home-vpn=enabled`). When DDNS turns off, the router asks the cloud server to delete the name, and the name stops resolving within a few minutes.
  - `yes` - DDNS is always on. Behind NAT, the router sends an update every minute.
- `ddns-update-interval` (alt { ddns-update-interval: enum (none) , ddns-update-interval: time [1m .. ] }): Interval at which the router sends DDNS updates to the cloud server, in addition to the updates it decides to send by itself. With `none`, the router only sends its own updates; behind NAT, that is one every minute. Minimum: 1 minute. Default: none.
- `update-time` (bool): Whether the router sets its clock from the cloud server when it starts. It does so only while the NTP client (`/system/ntp/client`) is disabled, also with `ddns-enabled=auto`, and logs `cloud change time <old> => <new>`. DDNS updates and `force-update` do not set the clock. The time zone is set separately by `time-zone-autodetect` in `/system/clock`. Default: yes.
- `back-to-home-vpn` (enum: revoked-and-disabled | enabled; syscap=cloud-vpn): Whether Back To Home runs.
  - `revoked-and-disabled` (default) - Back To Home is off. Setting it removes the `back-to-home-vpn` interface with its peers, addresses and dynamic firewall rules, and all users in [`back-to-home-user`](cloud/back-to-home-user.md), and asks the cloud server to delete `vpn-dns-name`. Enabling Back To Home again creates new keys and a new port, so every client needs a new configuration.
  - `enabled` - Create the WireGuard interface `back-to-home-vpn` with the addresses 192.168.216.1/24 and fc00:0:0:216::1/64, add dynamic firewall and NAT rules, register `vpn-dns-name`, and connect to a relay when the router cannot be reached directly. With `ddns-enabled=auto`, DDNS turns on too.
- `vpn-prefer-relay-code` (string; syscap=cloud-vpn): Code of the relay region to use, from `vpn-relay-regions`, for example `EUR1`. When it is empty, the router uses the relay with the lowest round-trip time (`vpn-relay-rtts`). Default: empty.

**Read-only arguments**

- `public-address` (ipAddr): Public IPv4 address of the router as the cloud server sees it, that is, the source address of the router's requests. Behind NAT, this is the address of the NAT device. Shown after the first reply from the cloud server, also when only the time update runs.
- `public-address-ipv6` (ip6Addr): Public IPv6 address of the router as the cloud server sees it. Shown when the router reaches the cloud server over IPv6.
- `dns-name` (string): DNS name of the router: its serial number in lower case followed by `.sn.mynetname.net`. Shown after the name is registered. It resolves to `public-address`, or to the router's local address with `use-local-address=yes` in [`advanced`](cloud/advanced.md), with a time to live of 60 seconds.
- `status` (string): State of the last request to the cloud server, for example:
  - `updating...` - The router sent a request and is waiting for the reply. Without a reply, it keeps retrying with growing intervals.
  - `updated` - The cloud server confirmed the last request.
  - `failed to connect` - The cloud server did not answer.
- `vpn-dns-name` (string; syscap=cloud-vpn): DNS name of the Back To Home endpoint: the serial number in lower case followed by `.vpn.mynetname.net`. It resolves to the router's public address, or to the relay the router uses when it cannot be reached directly. Client configurations use it as the endpoint.
- `vpn-port` (num; syscap=cloud-vpn): UDP port of the `back-to-home-vpn` WireGuard interface. The router picks it when Back To Home is enabled.
- `vpn-status` (string; syscap=cloud-vpn): State of Back To Home, for example `running`.
- `vpn-relay-rtts` (multi { code: string }; syscap=cloud-vpn): Round-trip time to each relay region over IPv4 and IPv6, for example `EUR1(ip4: 0.976ms, ip6: timeout)`.
- `vpn-relay-ipv4-status` (string; syscap=cloud-vpn): How clients reach the router over IPv4: `reachable directly (region: EUR1 ip: <relay address> rtt: 0.761ms)` when they can connect to the router's public address, or `reachable via relay (region: EUR1 ...)` when they connect through the relay.
- `vpn-relay-ipv6-status` (string; syscap=cloud-vpn): How clients reach the router over IPv6, in the same format as `vpn-relay-ipv4-status`, for example `connecting (...)` while the router has no IPv6 internet access.
- `vpn-relay-regions` (multi { code: string }; syscap=cloud-vpn): Relay regions the router can use, for example `EUR1` and `USA1`. Use a code from this list in `vpn-prefer-relay-code`.
- `vpn-relay-addresses` (multi { address: ipAddr }; syscap=cloud-vpn): IPv4 addresses of the relay servers, one per region.
- `vpn-relay-addresses-ipv6` (multi { address: ip6Addr }; syscap=cloud-vpn): IPv6 addresses of the relay servers, one per region.
- `vpn-private-key` (string; syscap=cloud-vpn): Private key of the `back-to-home-vpn` WireGuard interface.
- `vpn-public-key` (string; syscap=cloud-vpn): Public key of the `back-to-home-vpn` WireGuard interface. Client configurations use it as the key of the router's peer.
- `vpn-peer-private-key` (string; syscap=cloud-vpn): Private key of the built-in client configuration in `vpn-wireguard-client-config`.
- `vpn-peer-public-key` (string; syscap=cloud-vpn): Public key of the built-in client configuration. The router has a dynamic peer with this key on `back-to-home-vpn`.
- `vpn-interface` (iface_enum; syscap=cloud-vpn): WireGuard interface of Back To Home, `back-to-home-vpn`.
- `vpn-wireguard-client-config` (string; syscap=cloud-vpn): WireGuard configuration of the built-in client, with the addresses 192.168.216.2 and fc00:0:0:216::2 and the DNS server the router uses. Import it in a WireGuard app on one device. For more devices, add users in [`back-to-home-user`](cloud/back-to-home-user.md).
- `vpn-wireguard-client-config-qrcode` (pic; syscap=cloud-vpn): `vpn-wireguard-client-config` as a QR code, for a WireGuard app on a phone.
- `warning` (string): Warning about the router's setup, for example `Router is behind a NAT. Remote connection might not work.` Shown only when there is a warning.

## Commands

### /ip/cloud/force-update

Type: Command

Sends a DDNS update to the cloud server right away, for example after the internet connection changed. It does nothing while DDNS is off (`ddns-enabled=auto` without Back To Home), and it does not set the clock.
