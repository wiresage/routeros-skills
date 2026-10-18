# /routing/rip/keys

> Source: https://manual.mikrotik.com/docs/cli-reference/routing/rip/keys

Type: Directory

MD5 authentication key chains.

**Flags**

- `X`: disabled

**Arguments**

- `chain` (enum; mandatory)
- `key-id` (num; mandatory): Key identifier. This number is included in MD5 authenticated RIP messages, and determines which key to use to check authentication for a specific message.
- `key` (string; mandatory): Authentication key. Maximal length 16 characters
- `valid-from` (date): The key is valid from this date and time.
- `valid-till` (date): The key is valid until this date and time.
