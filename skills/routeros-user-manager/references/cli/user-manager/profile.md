# /user-manager/profile

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/profile

Package: userman-5; Type: Directory

**Arguments**

- `name` (string; mandatory)
- `validity` (alt { validity: enum (unlimited) , validity: time }; mandatory)
- `name-for-users` (string)
- `starts-when` (enum: first-auth | assigned)
- `price` (num)
- `override-shared-users` (enum: off | unlimited)
