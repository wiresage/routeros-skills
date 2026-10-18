# /user/settings

> Source: https://manual.mikrotik.com/docs/cli-reference/user/settings

Type: Settings Directory

Password complexity policy enforced when adding a user in [`/user`](../user.md) or changing a password with `/password`. See [User](../../guides/authentication-authorization-accounting/user.md) for the full guide.

**Arguments**

- `minimum-password-length` (num): Shortest accepted password length, in characters. A shorter password is rejected with "password is too short - must be at least N characters". Range 0 to 4294967295. Default: 0.
- `minimum-categories` (num): Number of character categories a password must use, out of four: digits, lowercase letters, uppercase letters and symbols. A weaker password is rejected with "password is too weak - it must contain characters from at least N categories (digits, lower and upper case letters, symbols)". Range 0 to 4. Default: 0.
