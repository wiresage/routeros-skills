# /interface/ovpn-client

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/ovpn-client

Type: Directory

**Flags**

- `X` (disabled): Whether an item is disabled.
- `R` (running): Whether the interface is running.
- `H` (hw-crypto): Whether hardware encryption is active.
- `Ta` (tls-auth): Whether TLS authentication (tls-auth) is active.
- `Tc` (tls-crypt): Whether tls-crypt authentication is active.

**Arguments**

- `name` (string): Descriptive name of the interface.
- `mac-address` (macAddr): MAC address of the OVPN interface. Automatically generated if not specified.
- `max-mtu` (num): Maximum Transmission Unit. Maximum packet size that the OVPN interface can send without packet fragmentation.
- `connect-to` (address (flags=D46v); mandatory): Remote address of the OVPN server.
- `port` (num): Port to connect to.
- `mode` (enum: ip | ethernet): Layer3 or Layer2 tunnel mode (alternatively tun, tap).
- `protocol` (enum: tcp | udp): Transport protocol to use when connecting to the remote endpoint.
- `user` (string; mandatory): User name used for authentication.
- `password` (string): Password used for authentication. Must not be longer than 1000 characters.
- `profile` (enum): Specifies which PPP profile configuration is used when establishing the tunnel.
- `certificate` (enum: none): Client certificate from the certificate store.
- `verify-server-certificate` (bool): Checks the server certificate's CN or SAN against the connect-to parameter and enables trust-chain validation against the router's certificate store. The IP or hostname must be present in the server's certificate.
- `tls-version` (enum: any | only-1.2): Specifies which TLS versions to allow.
- `auth` (enum: sha1 | md5 | sha256 | sha384 | sha512 | null): Allowed authentication methods.
- `cipher` (enum: blowfish128 | aes128-cbc | aes192-cbc | aes256-cbc | aes128-gcm | aes192-gcm | aes256-gcm | null): Allowed ciphers. To use GCM ciphers, set auth to null, because the GCM cipher also handles authentication.
- `use-peer-dns` (enum: no | yes | exclusively): Whether to add DNS servers provided by the OVPN server to IP/DNS configuration.
- `add-default-route` (bool): Whether to add the OVPN remote address as a default route.
- `route-nopull` (bool): If enabled, the client does not use routes pushed by the server (including def1).
- `disconnect-notify` (bool): Sends explicit disconnect notification in UDP mode.

## Commands

### /interface/ovpn-client/import-ovpn-configuration

Type: Command

**Arguments**

- `file-name` (file): Path to the .ovpn client configuration file to import.
- `skip-cert-import` (bool): Ignore certificate information in the .ovpn file if certificates are added manually.
- `key-passphrase` (string): Passphrase for the certificate private key.
- `ovpn-user` (string): Username for authentication with the OVPN server.
- `ovpn-password` (string): Password for authentication with the OVPN server.

**Read-only arguments**

- `progress` (string): Import progress status.

### /interface/ovpn-client/monitor

Type: Command

**Read-only arguments**

- `status` (string): Current connection status.
- `uptime` (time): Connection uptime.
- `encoding` (string): Encryption encoding used.
- `mtu` (num): Current MTU of the connection.
- `local-address` (ipAddr): Local IP address of the connection.
- `remote-address` (ipAddr): Remote IP address of the connection.
