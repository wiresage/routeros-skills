# /interface/dot1x/client

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/dot1x/client

Conditions: !smips; Type: Directory

**Flags**

- `I`: inactive
- `X`: disabled

**Arguments**

- `interface` (iface_enum; mandatory)
- `eap-methods` (multi { method: enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2) }; mandatory)
- `identity` (string; mandatory)
- `password` (string)
- `anon-identity` (string)
- `certificate` (enum: none)

**Read-only arguments**

- `status` (string)
