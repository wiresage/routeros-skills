# /user-manager/user/group

> Source: https://manual.mikrotik.com/docs/cli-reference/user-manager/user/group

Package: userman-5; Type: Directory

**Flags**

- `*`: default

**Arguments**

- `name` (string; mandatory)
- `outer-auths` (ubit (pap, chap, mschap1, mschap2, eap-tls, eap-ttls, eap-peap, eap-mschap2))
- `inner-auths` (ubit (ttls-pap, ttls-chap, ttls-mschap1, ttls-mschap2, peap-mschap2))
- `attributes` (object { attribute-value: super { attribute: enum , [value] :string } })

**Read-only arguments**

- `default-name` (string)
