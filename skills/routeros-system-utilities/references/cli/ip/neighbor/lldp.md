# /ip/neighbor/lldp

> Source: https://manual.mikrotik.com/docs/cli-reference/ip/neighbor/lldp

Type: Directory

This menu shows detailed LLDP type-length-values (TLVs) received from neighboring devices.

> **Note**
>
> The `lldpRemTable` SNMP table reports only neighbors discovered through LLDP. Entries discovered exclusively by CDP or MNDP are excluded from the SNMP LLDP-MIB.

Example output:

```ros
[admin@Switch] > /ip/neighbor/lldp/print
Columns: INTERFACE, ADDRESS4, ADDRESS6, MAC-ADDRESS, LLDP-CHASSIS-ID, LLDP-PORT-ID, LLDP-PORT-DESCRIPTION, LLDP-SYSTEM-NAME, LLDP-SYSTEM-DESCRIPTION
#  INTERFACE  ADDRESS4        ADDRESS6                   MAC-ADDRESS        LLDP-CHASSIS-ID    LLDP-PORT-ID  LLDP-PORT-DESCRIPTION  LLDP-SYSTEM-NAME  LLDP-SYSTEM-DESCRIPTION
0  ether2     192.168.88.128  fe80::f61e:57ff:fe13:d794  F4:1E:57:13:D7:94  F4:1E:57:13:D7:94  ether1        ether1                 Tested_CRS812     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS812-8DS-2DQ-2DDQ
   bridge1
1  ether3     192.168.88.127  fe80::f61e:57ff:fe47:9255  F4:1E:57:47:92:55  F4:1E:57:47:92:55  ether1        ether1                 Tested_CRS520     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS520-4XS-16XQ
   bridge1
2  ether4     192.168.88.9    fe80::1afd:74ff:fe81:9a    18:FD:74:81:00:9A  18:FD:74:81:00:86  ether1        ether1                 Tester6           MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CCR2216-1G-12XS-2XQ
   bridge1
3  ether5     192.168.88.132  fe80::d601:c3ff:fe43:c035  D4:01:C3:43:C0:35  D4:01:C3:43:C0:35  ether1        ether1                 Tested_L009       MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 L009UiGS
   bridge1
4  ether8     192.168.88.129  fe80::f61e:57ff:fec2:8a3d  F4:1E:57:C2:8A:3D  F4:1E:57:C2:8A:2B  ether17       ether17                Tested_CRS418     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS418-8P-8G-2S+
   bridge1
```

**Read-only arguments**

- `interface` (multi { interface: iface_enum }): Interface on which the LLDP neighbor was discovered.
- `address` (alt { address4: ipAddr , address6: ip6Addr }): IPv4 or IPv6 address of the LLDP neighbor.
- `address4` (ipAddr): IPv4 address of the LLDP neighbor.
- `address6` (ip6Addr): IPv6 address of the LLDP neighbor.
- `mac-address` (macAddr): MAC address of the LLDP neighbor.
- `lldp-chassis-id-subtype` (enum: chassis-component | interface-alias | port-component | mac-address | network-address | interface-name | local): Subtype of the LLDP chassis ID.
- `lldp-chassis-id` (string): LLDP chassis ID of the neighbor.
- `lldp-port-id-subtype` (enum: interface-alias | port-component | mac-address | network-address | interface-name | agent-circuit-id | local): Subtype of the LLDP port ID.
- `lldp-port-id` (string): LLDP port ID of the neighbor.
- `lldp-port-description` (string): LLDP port description of the neighbor.
- `lldp-system-name` (string): LLDP system name of the neighbor (system identity).
- `lldp-system-description` (string): LLDP system description of the neighbor.
- `lldp-ttl` (time): LLDP time-to-live value for the neighbor entry.
- `lldp-system-caps` (ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)): LLDP system capabilities of the neighbor.
- `lldp-system-caps-enabled` (ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)): LLDP enabled system capabilities of the neighbor.
