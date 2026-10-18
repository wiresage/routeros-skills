# /ip/neighbor/discovery-settings

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/neighbor/discovery-settings

Type: Settings Directory

**Arguments**

- `discover-interface-list` (super { ! , discover-interface-list: enum }): Interface list whose members the discovery protocol will run on. Default: static.
- `discover-interval` (time): Frequency at which neighbor discovery packets are transmitted. Also adjusts the TTL TLV value for CDP and LLDP packets using the formula: (discover-interval * 4) + 1. Range: 5s..9h6m8s. Default: 30s.
- `lldp-med` (bool): Whether to advertise the LLDP-MED Media Capabilities TLV. Must be enabled when lldp-med-net-policy-vlan is used. Default: yes.
- `lldp-med-net-policy-vlan` (alt { constant: enum (disabled) , vlan-id: num [ .. 4094] }): Advertised VLAN ID for LLDP-MED Network Policy TLV. Allows assigning a VLAN ID for LLDP-MED-capable devices such as VoIP phones. The TLV is only added to interfaces where LLDP-MED-capable devices are discovered and lldp-med is enabled. Other TLV values (Application Type, VLAN Type, L2 Priority, DSCP Priority) are predefined. CDP should be excluded using the protocol setting to avoid LLDP-MED misconfiguration. Default: disabled.
- `lldp-mac-phy-config` (bool): Whether to send MAC/PHY Configuration/Status TLV in LLDP, indicating interface capabilities, duplex status, bit rate, and auto-negotiation. Only applies to Ethernet interfaces. Automatically included when sending LLDP-MED. Default: no.
- `lldp-max-frame-size` (bool): Whether to send Maximum Frame Size TLV in LLDP, indicating the maximum frame size capability of the interface in bytes (l2mtu + 18). Only applies to Ethernet interfaces. Default: no.
- `lldp-vlan-info` (bool): Whether to send IEEE 802.1 Organizationally Specific TLVs in LLDP related to VLANs. When enabled, three TLVs are advertised: Port VLAN ID (bridge port pvid), Port And Protocol VLAN ID (not supported), and VLAN Name (up to 10 active VLANs from the bridge VLAN table). Relevant to interfaces on a vlan-filtering bridge. Default: no.
- `lldp-poe-power` (bool; syscap=poe): Whether to transmit the IEEE 802.3 Organizationally Specific Power Via MDI TLV in LLDP messages. Replaces the PoE-out port poe-lldp-enabled setting. Relevant only for Ethernet interfaces with PoE-Out support. Default: yes.
- `lldp-poe-in-power` (bool; syscap=poe-in): Whether to transmit PoE input power TLVs in LLDP messages.
- `lldp-dcbx` (bool; syscap=crs_prestera): Whether to send Data Center Bridging Capabilities Exchange Protocol (DCBX) TLVs, communicating switch QoS settings and capabilities with neighboring devices using LLDP. Only applies to devices with a Marvell Prestera switch (e.g. CRS3xx). Includes ETS Configuration, Priority Assignment, Bandwidth Allocation, and TSA tables. Default: no.
- `protocol` (ubit (cdp, lldp, mndp)): List of discovery protocols to use. Default: cdp,lldp,mndp.
- `mode` (enum: tx-and-rx | tx-only | rx-only): Neighbor discovery packet sending and receiving mode. Default: tx-and-rx.
- `dying-gasp` (bool): Whether to send a neighbor discovery packet with TTL=0 before a graceful reboot, shutdown, or upgrade. Not sent in case of power loss or kernel panic. On the receiving side, a TTL=0 packet immediately removes the corresponding neighbor entry. Default: no.
- `add-dns-entries` (bool): Whether to create dynamic DNS entries for discovered neighbors, using their identity as the domain name.
- `add-dns-entries-suffix` (string): Suffix added to dynamic DNS entries created for each neighbor.
