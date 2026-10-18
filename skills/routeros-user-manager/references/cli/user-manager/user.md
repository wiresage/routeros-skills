# /user-manager/user

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/user

Package: userman-5; Type: Directory

**Flags**

- `X`: disabled

**Arguments**

- `name` (string; mandatory)
- `password` (string)
- `otp-secret` (string)
- `group` (enum)
- `shared-users` (enum: unlimited)
- `caller-id` (enum: bind)
- `attributes` (object { attribute-value: super { attribute: enum , [value] :string } })

## Commands

### /user-manager/user/add-batch-users

Package: userman-5; Type: Command

**Arguments**

- `username-length` (num)
- `number-of-users` (num)
- `username-prefix` (string)
- `password-length` (enum: empty | same-as-username)
- `username-characters` (ubit (uppercase, lowercase, numbers))
- `password-characters` (ubit (uppercase, lowercase, numbers))
- `profile` (enum)
- `group` (enum)
- `caller-id` (enum: bind)
- `shared-users` (enum (unlimited) { unlimited:0x0 })
- `disabled` (bool)
- `comment` (string)

### /user-manager/user/generate-voucher

Package: userman-5; Type: Command

**Arguments**

- `voucher-template` (enum)

### /user-manager/user/monitor

Package: userman-5; Type: Command

**Read-only arguments**

- `total-uptime` (time)
- `total-download` (num)
- `total-upload` (num)
- `active-sessions` (num)
- `active-sub-sessions` (num)
- `actual-profile` (enum)
- `attributes-details` (object { attribute-value: super { attribute: enum , [value] :string , [value-type] :enum (ip-address | string | uint32 | hex | ip6-prefix | macro) , [raw-value] :0xstring } })
