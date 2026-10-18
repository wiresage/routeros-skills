# /ip/firewall/service-port

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/firewall/service-port

Type: Directory

**Flags**

- `X`: disabled
- `I`: invalid

**Arguments**

- `ports` (multi { port: num [0 .. 65535] }): Port numbers used by the service.
- `sip-direct-media` (bool): Whether SIP direct media is enabled.
- `sip-timeout` (time): SIP timeout value.

**Read-only arguments**

- `name` (string): Name of the service.
