# /routing/bfd/authentication

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/bfd/authentication

Conditions: BFD_AUTHENTICATION; Type: Directory

**Flags**

- `X`: disabled
- `I`: inactive
- `T`: transmit

**Arguments**

- `keyring` (enum; mandatory)
- `key-id` (num; mandatory)
- `type` (enum: none | simple-password | keyed-md5 | meticulous-keyed-md5 | keyed-sha1 | meticulous-keyed-sha1; mandatory)
- `key` (string)
- `transmit-after` (date)
- `accept-before` (date)
