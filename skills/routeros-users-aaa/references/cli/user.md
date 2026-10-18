# /user

> Source: https://manual.mikrotik.com/docs/cli-reference/user

Type: Directory

Router administration user accounts. Each user belongs to exactly one [group](user/group.md) that grants the rights (policies) the user has. See [User](../guides/authentication-authorization-accounting/user.md) for the full guide.

**Flags**

- `E` (expired): Password expired with [`/user/expire-password`](user.md). At the next interactive login the user is asked to set a new password; setting a new password clears the flag.
- `X` (disabled): User account is disabled and cannot log in.

**Arguments**

- `name` (string; mandatory): Login user name. Letters, digits and the characters `_` `.` `#` `-` `@` are allowed; the name must end with a letter or a digit and cannot start with `.` or `-`.
- `group` (enum; mandatory): User group that grants the rights (policies) the user has.
- `password` (string; mandatory): Login password. Any characters are accepted, including spaces, symbols and UTF-8. An explicitly empty value (`password=""`) allows logging in with a blank password. The complexity policy from [`/user/settings`](user/settings.md) applies when set.
- `inactivity-timeout` (time): Idle time after which `inactivity-policy` is applied to an interactive console session. Range 00:01:00 to 1d00:00:00. Default: 10m.
- `inactivity-policy` (enum: none | logout | lockscreen): Action taken when `inactivity-timeout` expires:
  - `none` (default) - The idle session keeps running.
  - `logout` - Closes the idle session with the message "`<name>` was logged out due to inactivity".
  - `lockscreen` - Locks the session ("Session is locked (Ctrl-D to Quit)") and asks for the user's password to resume; wrong passwords print "Sorry, try again.".
- `address` (object { address: alt { address: ipPrefix , address: ip6Prefix } }): IP address with mask or IPv6 prefix. When set, the user may log in only from matching source addresses; logins from other addresses are refused.

**Read-only arguments**

- `last-logged-in` (date): Date and time of the user's last login.

## Commands

### /user/expire-password

Type: Command

Expires the selected users' passwords (sets the `E` flag in [`/user`](user.md)). At the next interactive login the user is asked to set a new password; setting a new password with `/user/set` also clears the flag. See [User](../guides/authentication-authorization-accounting/user.md) for the full guide.
