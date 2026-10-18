# /user/active

> Source: https://manual.mikrotik.com/docs/cli-reference/user/active

Type: Directory

Currently logged-in management sessions. All properties are read-only. Terminate a session with `/user/active/remove`. See [User](../../guides/authentication-authorization-accounting/user.md) for the full guide.

**Flags**

- `R` (radius): User authenticated through RADIUS (see [`/user/aaa`](aaa.md)).
- `M` (by-romon): Session came through RoMON; `by-romon` holds the MAC address of the RoMON agent.

**Read-only arguments**

- `when` (date): Date and time the session logged in.
- `name` (string): Name of the logged-in user from [`/user`](../user.md).
- `address` (alt { ip: ipAddr , ip6: ip6Addr , address: macAddr }): Source address of the session: IP, IPv6 or MAC address.
- `by-romon` (macAddr): MAC address of the RoMON agent the session came through; set only for RoMON sessions (flag `M`).
- `via` (enum: unknown | winbox | console | telnet | ftp | web | ssh | mac-telnet | bandwidth-test | api | romon | rest-api): Management service the session connected through: `unknown`, `winbox`, `console`, `telnet`, `ftp`, `web`, `ssh`, `mac-telnet`, `bandwidth-test`, `api`, `romon` or `rest-api`.
- `group` (enum): Group of the logged-in user, which grants the session's rights.
