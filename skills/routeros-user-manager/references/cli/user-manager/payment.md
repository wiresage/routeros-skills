# /user-manager/payment

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/payment

Package: userman-5; Type: Directory

**Arguments**

- `user` (enum)
- `profile` (enum)
- `price` (num)
- `currency` (string)
- `trans-start` (date)
- `trans-end` (alt { constant: enum (not-finished) , date: date })
- `trans-status` (enum: started | pending | approved | declined | error | timeout | aborted | user-approved)
- `method` (enum: paypal | authorize-net)
- `user-message` (string)
