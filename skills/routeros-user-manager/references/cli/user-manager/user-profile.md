# /user-manager/user-profile

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/user-profile

Package: userman-5; Type: Directory

**Arguments**

- `user` (enum; mandatory)
- `profile` (enum; mandatory)

**Read-only arguments**

- `state` (enum: waiting | running | running-active | used)
- `end-time` (alt { constant: enum (not-yet-running | unlimited) , date: date })

## Commands

### /user-manager/user-profile/activate-user-profile

Package: userman-5; Type: Command
