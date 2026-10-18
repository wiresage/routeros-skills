# /routing/ospf/lsa

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/lsa

Type: Directory

**Flags**

- `S` (self-originated): Whether the LSA originated from the router itself.
- `F`: flushing
- `W`: wraparound
- `D`: dynamic

**Read-only arguments**

- `instance` (enum)
- `area` (enum): The area this LSA belongs to.
- `link` (address (flags=4i))
- `link-instance-id` (num)
- `type` (string)
- `originator` (ipAddr): An originator of the LSA record.
- `id` (ipAddr): LSA record ID
- `sequence` (num): A number of times the LSA for a link has been updated.
- `age` (num): How long ago (in seconds) the last update occurred.
- `checksum` (num)
- `body` (string)
