# /ip/dns/adlist

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dns/adlist

Type: Directory

Ad-blocking lists. The router answers A and AAAA queries for the names in these lists with `0.0.0.0` and `::` (TTL 2 s) instead of asking upstream; other query types, such as MX or HTTPS, go upstream. Only the exact name is blocked, not its subdomains. The names are kept in the DNS cache memory and count against `cache-size` in [`/ip/dns`](../dns.md): each name takes about 75 bytes, so 76 500 names use about 5.6 MiB. When the cache is too small, the import stops with the log messages `adlist read: max cache size reached` and `could not add name, stopping import`, and `name-count` shows how many names were imported; raising `cache-size` afterwards does not complete the list, so remove the adlist and add it again. Disabling an adlist does not free the cache memory its names use: they still count against `cache-size` until the list is removed. The router re-checks the lists every 4 hours. Up to 64 adlists can be added. A static `FWD` entry exempts a name from all adlists; a static A entry alone does not. For examples, see [DNS](../../../guides/network-management/dns.md).

**Flags**

- `X` (disabled): The adlist is disabled and blocks nothing.

**Arguments**

- `file` (file): File on the router with the names to block, as `/file/print` shows it. One name per line, in lower case, in one of these formats:
  - `0.0.0.0 name`, `127.0.0.1 name` or `::1 name` - Hosts file format.
  - `name` - Just the name.

  Lines starting with `#` and comments after a name are ignored. Wildcards such as `*.example.com` and several names on one line are not supported.
- `url` (string): URL of a list in the same format as `file`, for example a public hosts file. The router downloads it and keeps a copy on its storage (not shown in `/file`).
- `ssl-verify` (bool): Whether the router verifies the certificate of the `url` server against the built-in trust store and the certificates in `/certificate`. When the check fails, the router does not import the list and logs `http client error: SSL: ...` in the `dns` topic. For a server with a self-signed certificate, import its CA certificate or set `ssl-verify=no`. Default: yes.

**Read-only arguments**

- `match-count` (num): Number of queries answered from this list.
- `name-count` (num): Number of names imported from this list.

## Commands

### /ip/dns/adlist/pause

Type: Command

Stops blocking by all adlists for the given time, for example `/ip/dns/adlist/pause duration=10m`. Blocking resumes by itself when the time runs out.

**Arguments**

- `duration` (time): How long to stop blocking. `duration=0` ends an active pause.

### /ip/dns/adlist/reload

Type: Command

Checks all adlists for updates now, instead of at the next 4-hour check, and applies only the changes. It does not complete a list whose import stopped because the cache was too small.
