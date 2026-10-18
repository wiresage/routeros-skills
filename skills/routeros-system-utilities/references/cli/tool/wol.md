# /tool/wol

> Source: https://manual.mikrotik.com/docs/cli-reference/tool/wol

Type: Command

See [Wake on LAN](../../guides/system-information-and-utilities/wake-on-lan.md) for the full documentation.

**Arguments**

- `interface` (iface_enum): Interface to send the magic packet out of, for example the LAN bridge. With an interface, the router sends an Ethernet frame (EtherType `0x0842`) to the broadcast MAC address on it. Without an interface, it sends a UDP packet to `255.255.255.255` port 9 through the default route, which on most routers is the internet connection.
- `mac` (macAddr): MAC address of the computer to wake. The magic packet holds it 16 times.
