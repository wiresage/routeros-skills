# /ip/ipsec/identity

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/identity

Type: Directory

Identities are configuration parameters that are specific to the remote peer. The main purpose of identity is to handle authentication and verify the peer's integrity.

**Flags**

- `D` (dynamic): Whether the item was created dynamically.
- `X` (disabled): Whether an item is disabled.

**Arguments**

- `peer` (enum; mandatory): Peer name.
- `auth-method` (enum: pre-shared-key | digital-signature | eap | eap-radius | pre-shared-key-xauth | rsa-key | rsa-signature-hybrid): Authentication method:
  - digital-signature - authenticate using a pair of RSA certificates;
  - eap - IKEv2 EAP authentication for the initiator (peer with a netmask of /32). Must be used together with eap-methods;
  - eap-radius - IKEv2 EAP RADIUS passthrough authentication for the responder (RFC 3579). A server certificate in this case is required. If a server certificate is not specified then only clients supporting EAP-only (RFC 5998) will be able to connect. Note that the EAP method should be compatible with EAP-only;
  - pre-shared-key - authenticate by a password (pre-shared secret) string shared between the peers (not recommended since an offline attack on the pre-shared key is possible);
  - rsa-key - authenticate using an RSA key imported in the keys menu. Only supported in IKEv1;
  - pre-shared-key-xauth - authenticate by a password (pre-shared secret) string shared between the peers + XAuth username and password. Only supported in IKEv1;
  - rsa-signature-hybrid - responder certificate authentication with initiator XAuth. Only supported in IKEv1.
- `eap-methods` (multi { array-id, method: enum (eap-tls | eap-ttls | eap-peap | eap-mschapv2) }): All EAP methods require a whole certificate chain including intermediate and root CA certificates to be present in System/Certificates menu. Also, the username and password (if required by the authentication server) must be specified. Multiple EAP methods can be specified and are used in the specified order.

  Supported EAP methods:
  - eap-mschapv2;
  - eap-peap - also known as PEAPv0/EAP-MSCHAPv2;
  - eap-tls - requires additional client certificate specified under certificate parameter;
  - eap-ttls.
- `mode-config` (enum: none): Name of the configuration parameters from mode-config menu. When the parameter is set mode-config is enabled.
- `notrack-chain` (string): Adds IP/Firewall/Raw rules matching IPsec policy to a specified chain. Use together with generate-policy.
- `my-id` (alt { string: composite { type: enum (fqdn | user-fqdn | key-id) , data: string } , address: composite { type: enum (address) , data: alt { ipv6: ip6Addr , ip: ipAddr } } , other: enum (auto | dn) }): On the initiator, this controls what ID_i is sent to the responder. On the responder, this controls what ID_r is sent to the initiator. In IKEv2, the responder also expects this ID in received ID_r from the initiator.
  - auto - tries to use correct ID automatically: IP for pre-shared key, SAN (DN if not present) for certificate based connections;
  - address - IP address is used as ID;
  - dn - the binary Distinguished Encoding Rules (DER) encoding of an ASN.1 X.500 Distinguished Name;
  - fqdn - fully qualified domain name;
  - key-id - use the specified key ID for the identity;
  - user fqdn - specifies a fully-qualified username string, for example, "user@domain.com".
- `remote-id` (alt { string: composite { type: enum (fqdn | user-fqdn | key-id) , data: string } , address: composite { type: enum (address) , data: alt { ipv6: ip6Addr , ip: ipAddr } } , auto: enum (auto | ignore | dn) }): This parameter controls what ID value to expect from the remote peer. Note that all types except for ignore will verify remote peer's ID with a received certificate. In case the peer sends the certificate name as its ID, it is checked against the certificate, else the ID is checked against Subject Alt. Name.
  - auto - accept all IDs;
  - address - IP address is used as ID;
  - dn - the binary Distinguished Encoding Rules (DER) encoding of an ASN.1 X.500 Distinguished Name;
  - fqdn - fully qualified domain name. Only supported in IKEv2;
  - user fqdn - a fully-qualified username string, for example, "user@domain.com". Only supported in IKEv2;
  - key-id - specific key ID for the identity. Only supported in IKEv2;
  - ignore - do not verify received ID with certificate (dangerous).

  \* Wildcard key ID matching is not supported, for example, `remote-id="key-id:CN=*.domain.com"`
- `match-by` (enum: remote-id | certificate): Defines the logic used for peer's identity validation.
  - remote-id - verifies the peer's ID according to remote-id setting.
  - certificate verifies the peer's certificate with what is specified under remote-certificate setting.
- `key` (enum): Name of the private key from the keys menu. Applicable if RSA key authentication method (auth-method=rsa-key) is used.
- `remote-key` (enum): Name of the public key from the keys menu. Applicable if RSA key authentication method (auth-method=rsa-key) is used.
- `secret` (string): Secret string. If it starts with '0x', it is parsed as a hexadecimal value. Applicable if pre-shared key authentication method (`auth-method=pre-shared-key` or `auth-method=pre-shared-key-xauth`) is used.
- `certificate` (multi { array-id, certificate: enum }): Local certificate. Applicable if digital signature authentication method (`auth-method=digital-signature`) or EAP (`auth-method=eap`) is used.
- `remote-certificate` (enum: none): Certificate for authenticating the remote side (validating packets; no private key required). If a remote-certificate is not specified then the received certificate from a remote peer is used and checked against the CA in the certificate menu. A proper CA must be imported in a certificate store. If remote-certificate and match-by=certificate are specified, only the specific client certificate will be matched. Applicable if digital signature authentication method (`auth-method=digital-signature`) is used.
- `username` (string): EAP or XAuth username.
- `password` (string): EAP or XAuth password.
- `generate-policy` (enum: no | port-override | port-strict): Allow this peer to establish SA for non-existing policies. Such policies are created dynamically for the lifetime of SA. Automatic policies allow, for example, to create IPsec secured L2TP tunnels, or any other setup where remote peer's IP address is not known at the configuration time.
  - no - do not generate policies;
  - port-override - generate policies and force policy to use any port (old behavior);
  - port-strict - use ports from peer's proposal, which should match peer's policy.
- `policy-template-group` (enum): Policy template group to use for generated policies. If none of the templates match, Phase 2 SA will not be established.
