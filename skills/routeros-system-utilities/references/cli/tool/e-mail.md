# /tool/e-mail

> Source: https://manual.mikrotik.com/docs/cli-reference/tool/e-mail

Type: Settings Directory

Settings of the SMTP server the router sends email through: the server and port, the TLS mode, certificate verification, the sender and the login. `/tool/e-mail/send` uses them for every message unless the command overrides them. See [Email](../../guides/system-information-and-utilities/e-mail.md).

**Arguments**

- `server` (alt { ipv6: ip6Addr , ip: ipAddr , fqdn: string }): SMTP server IP address, IPv6 address, or FQDN. With a name, `last-address` shows the address the router connected to. Default: 0.0.0.0.
- `port` (num): SMTP server port. Default: 25.
- `tls` (enum: no | yes | starttls): TLS encryption mode:
  - `no` (default) - No TLS. The router does not send STARTTLS, also when the server offers it.
  - `yes` - TLS from the start of the connection (implicit TLS, usually port 465).
  - `starttls` - Upgrade the connection with STARTTLS (usually port 587). When the server does not offer STARTTLS, the send fails with `TLS not supported by server`; there is no fallback to an unencrypted connection.
- `vrf` (enum): VRF on which the service creates outgoing connections. Default: main.
- `from` (string): Name or email address that will be shown as the sender. When it is empty, the router sends the message with an empty sender (`<>`), which many servers refuse. Default: <>.
- `user` (string): Username used for authenticating to an SMTP server. The router logs in with AUTH PLAIN; without TLS, the user name and password cross the network unencrypted. Default: "".
- `password` (string): Password used for authenticating to an SMTP server. Default: "".
- `certificate-verification` (enum: no | yes | yes-without-crl): TLS certificate validation:
  - `no` (default) - The router encrypts the connection but does not check the server's certificate.
  - `yes` - Validates the certificate chain against the local certificate store, including the server name. The built-in trust store covers email by default.
  - `yes-without-crl` - Validates the certificate without performing a CRL check.

**Read-only arguments**

- `last-status` (enum: none | resolving-dns | in-progress | failed | succeeded): Status of the last email send attempt: `succeeded` or `failed` when it has ended.
- `last-address` (alt { ip: ipAddr , ipv6: ip6Addr }): IP address of the last used SMTP server.

## Commands

### /tool/e-mail/send

Type: Command

Sends one email message through the SMTP server in [`/tool/e-mail`](e-mail.md). Parameters given to the command override the server settings for this message. The result shows in `last-status` of `/tool/e-mail`. See [Email](../../guides/system-information-and-utilities/e-mail.md).

**Arguments**

- `server` (alt { ipv6: ip6Addr , ip: ipAddr , fqdn: string }): SMTP server IP address, IPv6 address, or FQDN. If not specified, the value from the server configuration is used.
- `port` (num): SMTP server port. If not specified, the value from the server configuration is used.
- `to` (multi { array-id, to: string }): Destination email address. Several addresses are allowed, separated by commas; the router sends one message to all of them.
- `cc` (multi { array-id, cc: string }): Send a copy to listed recipients. Multiple addresses allowed, separated by commas.
- `from` (string): Name or email address that will appear as the sender. If not specified, the value from the server configuration is used; when that is empty too, the sender is `<>`, which many servers refuse.
- `subject` (string): The subject of the message.
- `body` (string): The body text of the email message. `\n` starts a new line.
- `file` (multi { array-id, file: file }): List of file names to attach to the email, separated by commas. Each file is attached as `application/octet-stream`. A file that does not exist is refused before sending (`input does not match any value of file`).
- `user` (string): Username used to authenticate to an SMTP server (AUTH PLAIN; unencrypted without TLS). If not specified, the value from the server configuration is used.
- `password` (string): Password used to authenticate to an SMTP server. If not specified, the value from the server configuration is used.
- `tls` (enum: no | yes | starttls): TLS encryption mode. If not specified, the value from the server configuration is used:
  - `no` - No TLS. The router does not send STARTTLS, also when the server offers it.
  - `yes` - TLS from the start of the connection (implicit TLS, usually port 465).
  - `starttls` - Upgrade the connection with STARTTLS (usually port 587). When the server does not offer STARTTLS, the send fails with `TLS not supported by server`; there is no fallback to an unencrypted connection.
- `certificate-verification` (enum: no | yes | yes-without-crl): TLS certificate validation. If not specified, the value from the server configuration is used:
  - `no` - The router encrypts the connection but does not check the server's certificate.
  - `yes` - Validates the certificate chain against the local certificate store, including the server name. The built-in trust store covers email by default.
  - `yes-without-crl` - Validates the certificate without performing a CRL check.
