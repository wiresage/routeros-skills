# /interface/sstp-server/server

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/sstp-server/server

Type: Settings Directory

**Arguments**

- `enabled` (bool): Enables or disables the SSTP server.
- `port` (num): Listening port for the SSTP server.
- `max-mtu` (num): Maximum Transmission Unit.
- `max-mru` (num): Maximum Receive Unit.
- `mrru` (num): Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it is split into multiple packets, allowing full-size IP or Ethernet packets to be sent over the tunnel.
- `keepalive-timeout` (enum: disabled): Keepalive timeout in seconds.
- `default-profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
- `authentication` (ubit (pap, chap, mschap1, mschap2)): Allowed authentication methods. By default all methods are allowed.
- `certificate` (enum: none): Server certificate from the certificate store.
- `verify-client-certificate` (bool): Verifies the client certificate against the router's certificate store.
- `pfs` (enum: no | yes | required): Specifies which TLS authentication to use. `yes` - TLS uses ECDHE-RSA and DHE-RSA. `required` - uses only ECDHE.
- `tls-version` (enum: any | only-1.2): Specifies which TLS version to allow.
- `ciphers` (ubit (aes256-sha, aes256-gcm-sha384)): Allowed ciphers.
