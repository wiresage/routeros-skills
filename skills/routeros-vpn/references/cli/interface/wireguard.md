# /interface/wireguard

> Source: https://manual.mikrotik.com/docs/cli-reference/interface/wireguard

Type: Directory

[WireGuard](../../guides/virtual-private-networks/wireguard.md) creates encrypted IP tunnels between peers identified by public keys.

**Flags**

- `X` (disabled): Whether an item is disabled.
- `R` (running): Whether the interface is running.

**Arguments**

- `name` (string): Name of the tunnel.
- `mtu` (num): Layer3 maximum transmission unit.
- `listen-port` (num): Port for the WireGuard service to listen on for incoming sessions.
- `private-key` (string): A base64 private key. If not specified, it is automatically generated upon interface creation. Each network interface has a private key and a list of peers.
- `vrf` (enum): Specifies which VRF the WireGuard UDP socket uses to determine how encrypted packets are sent or received.

**Read-only arguments**

- `public-key` (string): A base64 public key calculated from the private key. Public keys are used by peers to authenticate each other.

## Commands

### /interface/wireguard/wg-export

Type: Command

Export the selected WireGuard interface and its peers in standard WireGuard configuration format. Select the interface with `[find name=...]`. The export does not include interface IP addresses, routes or firewall rules. For an executable RouterOS script, use the regular `/interface/wireguard/export` command. See [WireGuard](../../guides/virtual-private-networks/wireguard.md).

**Arguments**

- `file` (file): Name of the file to export the selected WireGuard interface and its peers to. The file contains `[Interface]` and `[Peer]` sections and the private key; store it securely.

### /interface/wireguard/wg-import

Type: Command

**Arguments**

- `config-file` (file): Path to the file containing the WireGuard configuration to import.
- `config-string` (string): WireGuard configuration string to import directly. Available from RouterOS version 7.19.
