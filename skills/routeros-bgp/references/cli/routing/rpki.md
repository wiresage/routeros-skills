# /routing/rpki

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/rpki

Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `group` (enum): Group assigned to the database.
- `address` (address (flags=46)): RTR server address.
- `port` (num): RTR server port.
- `vrf` (enum; unset): VRF table used to bind the connection.
- `preference` (num; unset): When multiple RTR sources exist, a higher number indicates higher preference. If preference is not configured, RouterOS prefers the lowest remote IP within the group. If remote IPs are equal, RouterOS prefers the lowest remote port.
- `refresh-interval` (num; unset): Interval in seconds to poll the validator for the newest data.
- `retry-interval` (num; unset): Interval in seconds to retry after a failed data poll from the validator.
- `expire-interval` (num; unset): Interval in seconds for which polled data remains valid when no valid update is received from the validator.

## Commands

### /routing/rpki/rpki-check

Type: Command

**Arguments**

- `prefix` (address (flags=46/))
- `group` (enum)
- `origin-as` (num)

**Read-only arguments**

- `result` (string)

### /routing/rpki/rpki-query

Type: Command

**Arguments**

- `group` (enum)
- `prefix` (address (flags=46/))
- `exact` (switch)

**Read-only arguments**

- `results` (string)
