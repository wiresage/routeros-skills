# /cmr

> Source: https://manual.mikrotik.com/docs/cli-reference/cmr

Package: cmr; Type: Settings Directory

Settings of the CMR server, the router that controls a fleet of CMR clients. Enable the server with `enabled=yes`; it then distributes software packages, discovers and tracks the devices, and evaluates the alert rules that monitor them. See [CMR](../guides/management-tools/cmr.md) for an overview of the package.

**Arguments**

- `enabled` (enum: yes | no): Whether CMR server is enabled or not. Default: no.
- `local-id` (string; unset): Unique CMR specific device identifier.
- `pairing-requirement` (enum: none | password | confirm; unset): Defines what the remote device must do before this device accepts the pairing:
  - **none** - this device accepts pairing automatically, without additional checks
  - **password** - the remote device may approve pairing by giving the username and password of a RouterOS user on this device; CMR has no separate pairing password
  - **confirm** - pairing must be approved locally by running the `pair` command on this device; approval from the remote side is not possible
- `packages-directory` (file; unset): Directory on the server's file system containing RouterOS packages that the server distributes to the managed devices and serves from when it matches the version an upgrade needs. The value is picked from the router's file list: directory entries are entered with a trailing slash (for example `cmrpkgs/`), plain files without one. Packages are resolved individually: a package already present here for the required version is sent directly without downloading it again, and only the missing packages are downloaded and cached. A value that does not point to an existing directory is kept but cannot be used; the `/cmr` menu then shows `directory does not exist, using memory` and packages are served from memory instead.
- `packages-cache-type` (enum: directory | memory; unset): Where the server stores the package files it downloads: `directory` keeps them on the server's storage, `memory` keeps them in RAM. With `directory`, the server stores them in a `cmrcache` subdirectory of `packages-directory`, which it creates in the router's file list; packages that are already present in `packages-directory` are served from there without being downloaded. When the directory is missing or unusable the server reports `directory does not exist, using memory` in the `/cmr` menu, stores the packages in RAM instead, and switches back to the directory when it becomes available again.
- `packages-cache-limit` (num; unset): Maximum amount of package data held in the cache, in megabytes. A value larger than the available RAM or storage is accepted and the server shows an informational note; the cache then uses all the space that is available and evicts older entries when a file larger than the remaining space must be stored.
- `upgrade-check-interval` (time; unset): How often the CMR server checks the MikroTik update servers for available versions. The minimum value is 1 minute. Default: `10h`.
- `track-topology` (bool; unset): Enables network topology discovery. Fetches the following information from CMR clients: routes, WiFi registration table, ARP table, neighbors, DHCP state, and interface states. This information is required for full CMR functionality, for example, automatic link discovery in the `/cmr/layout` menu. Default: yes.
- `fetch-comments` (bool; unset): Enables fetching of comments for interfaces/ports and the WiFi registration table. Default: yes.
- `controller-addresses` (multi { array-id, address: address (flags=46D) }; unset): CMR server IP addresses that are sent to the devices when the controller address cannot be discovered automatically (MNDP, or DNS: the client resolves `_cmr._tcp.lan` and `_cmr._tcp.` followed by the domain name from DHCP).
- `apptraffic-devices` (object; unset): Select devices using labels for which to collect app traffic data. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used. Default: `gateway`; `all` selects every device.
- `auto-labels` (alt { auto-labels: enum (none | all) { none:0, all:0xffff } , auto-labels: ubit (version, architecture, model, board-name, identity, address) }; unset): Whether to fetch labels information from the connected cmr-client devices. Can be configured to fetch only specific labels. Default: all.

**Read-only arguments**

- `self-client-id` (string; unset): ID that is used by CMR server to connect to itself, for it to be displayed in a device list.

## Commands

### /cmr/push-button

Type: Command

Using this command device pairing can be performed using physical routerboard/reset button on the server device.

**Arguments**

- `interface` (multi { array-id, interface: iface_enum }; unset): Select interface or interface list on which to search for CMR client. Default: all.

**Read-only arguments**

- `state` (string): State of device pairing.
- `error` (string; unset): Error information, in case pairing is unsuccessful.
- `peer` (multi { array-id, mac: macAddr }; unset): Peer address.
- `peer-id` (string; unset): Peer ID.
