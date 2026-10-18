# /ip/dns/cache/all

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/dns/cache/all

Type: Directory

All records in the DNS cache, including the PTR records the router creates for static entries and records the resolver keeps internally. For an overview, see [DNS](../../../../guides/network-management/dns.md).

**Flags**

- `S` (static): The record comes from a static entry in [`/ip/dns/static`](../static.md), for example the PTR record made for a static `A` or `AAAA` entry.
- `N` (negative): A cached negative answer: the name or the record type does not exist.

**Read-only arguments**

- `name` (string): Domain name of the record.
- `type` (enum: A | NS | MD | MF | CNAME | SOA | MB | MG | MR | NULL | WKS | PTR | HINFO | MINFO | MX | TXT | AAAA | SRV): Record type.
- `data` (alt { address: ipAddr , name: string , info: composite { rmail: string , email: string } , mx: composite { preference: num , exchange: string } , srv: composite { port: num , target: string } , soa-mname: string , address6: ip6Addr }): Data of the record, for example the address of an `A` record or the target name of a `PTR` record.
- `ttl` (time): Remaining time before the record expires from the cache.
- `responsible` (string): Email address of the zone administrator, from an `SOA` record.
- `serial` (num): Serial number of the zone, from an `SOA` record.
- `refresh` (num): Refresh interval of the zone, in seconds, from an `SOA` record.
- `retry` (num): Retry interval of the zone, in seconds, from an `SOA` record.
- `expire` (num): Expire time of the zone, in seconds, from an `SOA` record.
- `minimum` (num): Minimum TTL of the zone, in seconds, from an `SOA` record.
