# hAP ax S

> Source: https://manual.mikrotik.com/hardware/hap-ax-s
>
> Category: Indoor wireless

*[Figure]*

### hAP ax S - E62iUGS-2axD5axT

Our most cost-effective Wi-Fi 6 access point yet. Triple-chain 5 GHz radio (up to 900 Mbit/s throughput), dual-band Wi-Fi 6, 5x Gigabit Ethernet ports, and a 2.5G SFP. Powered by a dual-core ARM CPU, with PoE-in/PoE-out flexibility, a standard DC jack, USB, and a sturdy high-end enclosure that can be mounted on the wall. See the [hAP ax S product page](https://mikrotik.com/product/hap_ax_s) for full specifications and brochures.

## Powering

- Number of DC inputs: 2 (DC jack, PoE-IN).
- PoE-in input Voltage: 18-28 V.
- DC jack input Voltage: 12-28 V.
- PoE-out ports: Ether5.
- Max total out: 0.6 A.
- Total output power: 16.8 W.
- Power adapter nominal voltage 24 V.
- Power adapter nominal current 1.5 A.
- Max power consumption (without attachments) 11 W.
- Max power consumption 34 W.

## Setup

- Ensure your Internet Service Provider (ISP) allows hardware changes and automatically assigns an IP address;
- Connect the ISP cable to the Ethernet1 port;
- Connect the device to the power source;
- Connect to the device through any of the ports, excluding Ethernet1, or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker); **multiple configuration methods are available to ensure accessibility;**
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at <https://mt.lv/winbox> Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Configuration

Full RouterOS documentation is located here: <https://mt.lv/help> The device comes pre‑configured as a router: the WAN port (Ethernet1) is protected by a firewall and runs DHCP, while all other Ethernet ports and the wireless interface are part of the LAN bridge.
To set up the device, connect the ISP cable to the Ethernet1 port and plug the unit into a power source. Then access the device using any Ethernet port except Ethernet1, or join the default Wi‑Fi network named “MikroTik‑…”. The Wi‑Fi password is printed on the sticker attached to the device.
You can connect via the mobile app, WebFig in a web browser, or the WinBox tool (download from <https://mt.lv/winbox>). Configuration with the default IP address 192.168.88.1; if that address is unreachable, open WinBox, go to the “Neighbors” tab, and discover the device.
For recovery, the firmware can be reinstalled over the network using the Reset button.

## Extension slots and ports

| **Parameter** | **Value** |
| --- | --- |
| **Product Code** | E62iUGS-2axD5axT |
| **Architecture** | ARM 32bit |
| **CPU** | EN7562CT, Dual-Core, 950 MHz |
| **CPU Core Count** | 2 |
| **CPU Threads Count** | 2 |
| **Switch Chip Model** | EN7523 |
| **RouterOS License** | Level 4 |
| **Operating System** | RouterOS v7 |
| **Size of RAM** | 512 MB |
| **Storage Size** | 128 MB NAND |
| **Tested Ambient Temperature** | -40 °C to +70 °C |
| **Wireless 2.4 GHz Max Data Rate** | 574 Mbit/s |
| **Wireless 2.4 GHz Number of Chains** | 2 |
| **Wireless 2.4 GHz Standards** | 802.11b/g/n/ax |
| **Antenna Gain (2.4 GHz)** | 5.5 dBi |
| **Wireless 2.4 GHz Chip Model** | MT7916 |
| **Wireless 2.4 GHz Generation** | Wi-Fi 6 |
| **Wireless 5 GHz Max Data Rate** | 2400 Mbit/s |
| **Wireless 5 GHz Number of Chains** | 3 |
| **Wireless 5 GHz Standards** | 802.11a/n/ac/ax |
| **Antenna Gain (5 GHz)** | 6.5 dBi |
| **Wireless 5 GHz Chip Model** | MT7976 |
| **Wireless 5 GHz Generation** | Wi-Fi 6 |
| **Wi-Fi Speed** | AX3000 |
| **10/100/1000 Ethernet Ports (RJ45)** | 5 |
| **1G Ethernet Ports with PoE-Out** | 1 (Ether5) |
| **Fiber (SFP)** | 1 × SFP (2.5G supported) |
| **USB Ports** | 1 × USB Type-A |
| **USB Power Reset** | Yes |
| **Max USB Current (A)** | 1 A |
| **Number of DC Inputs** | 2 (DC jack, PoE-IN) |
| **DC Jack Input Voltage** | 12–28 V |
| **PoE-IN Type** | Passive PoE |
| **PoE-IN Voltage** | 18–28 V |
| **PoE-Out Port** | Ether5 (Passive PoE) |
| **PoE-Out Max Current** | 0.6 A |
| **Total PoE-Out Power** | 16.8 W |
| **Max Power Consumption** | 34 W |
| **Max Power (without attachments)** | 11 W |
| **IP Rating** | IP20 |
| **Other** | CPU temperature monitor |

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until the green LED light starts flashing, release the button to reset RouterOS configuration.
- Keep holding the reset button until the LED turns solid, then release it to enable CAP mode. The device will then start searching for a CAPsMAN server.
- To reinstall RouterOS using the Netinstall utility, enter the device into BOOTP mode. There are two types of booters available: the regular booter and the backup booter.Regular booter - Power on the device, wait 1-2 seconds, then press and hold the Reset button. Wait until the System LED is blinking green, then turns solid "On". When the green LED turns "Off", release the Reset button - the device will enter BOOTP mode.
- Backup booter – Power off the device, press and hold the Reset button, then power it on. Wait until the System LED is blinking green, then solid "On". When the green LED turns "Off", release the Reset button - the device will enter BOOTP mode using the backup booter.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hap-ax-s.md](../regulatory/hap-ax-s.md).
