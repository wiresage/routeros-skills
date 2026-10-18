# /ip/dns/cache

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dns/cache

Type: Directory

Answers the router can give from its cache: upstream answers and the static entries. For a complete list, including the PTR records made for static entries, see [`all`](cache/all.md). For an overview, see [DNS](../../../guides/network-management/dns.md).

**Flags**

- `S` (static): The record comes from a static entry in [`/ip/dns/static`](static.md). Static records show a TTL of 0s here.

**Read-only arguments**

- `type` (enum: A | NS | CNAME | MX | TXT | AAAA | SRV): Record type.
- `data` (alt { address: ipAddr , name: string , info: composite { rmail: string , email: string } , mx: composite { preference: num , exchange: string } , srv: composite { port: num , target: string } , soa-mname: string , address6: ip6Addr }): Data of the record, for example the address of an `A` record.
- `name` (string): Domain name of the record.
- `ttl` (time): Remaining time before the record expires from the cache. It counts down, and it is never longer than `cache-max-ttl` in [`/ip/dns`](../dns.md).

## Commands

### /ip/dns/cache/flush

Type: Command

Empties the DNS cache. Static entries from [`/ip/dns/static`](static.md) stay available. For an overview, see [DNS](../../../guides/network-management/dns.md).
