# CRS309-1G-8S+IN

> Source: https://manual.mikrotik.com/hardware/crs309-1g-8s-plus-in
>
> Category: Switches

*[Figure]*

This device is a network switch with eight SFP+ ports and one-gigabit port. It is already configured, with all ports switched together. See the [CRS309-1G-8S+IN product page](https://mikrotik.com/product/crs309_1g_8s_in) for full specifications and brochures.

## Quickstart

- Mount unit or place on the flat surface, please see paragraph for instructions.
- Choose your powering solution, please see the section for possibilities.
- Connect with your PC to any Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Use WebFig in a web browser or the WinBox configuration tool <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Mounting

*[Figure]*

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure.

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right.
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
  The IP rating scale for this device is IPX0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
  We recommend shielded Cat5/6 cables for our devices.
  *Mounting and configuration of this device should be done by a qualified person.*

## Powering

The device accepts 12-57 V DC ⎓ from the direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts. The Ethernet port 1 accepts 802.3af/at and passive PoE power input (18-57 V DC).
The power consumption of this device under maximum load is up to 23 W. It is possible to connect both power inputs at the same time and they will work in fail-over mode (input with higher voltage will work as the main source).
When using 802.3af/at to power this device, we recommend not using grounding for best compatibility.

## Configuration

Full documentation for both RouterOS and SwOS is available at: <https://mt.lv/help> You can configure the device using WebFig in a web browser or the "WinBox" configuration tool <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility.**
**To start setup, open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RS-232 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the Reset button.

Marvell Prestera switch chip features user manual

The device supports booting either RouterOS (for full routing and switching functionality) or SwOS (for switch-only operation). By default, the device boots into RouterOS, but you can switch to the other operating system as follows:

- From SwOS: Go to the System menu and click the Boot RouterOS button at the bottom of the page.
- From RouterOS: Open System → RouterBOARD → Settings and select Boot OS.
  It is also possible to choose the operating system and configure other boot options using the serial console menu.

## Reset button

- To reset the configuration, unplug the device from power, press and hold the Reset button, and release it when the USER (USR) LED starts flashing.
- To load the backup bootloader, press and hold the Reset button before applying power, then release it after three seconds.
- To initiate the Netinstall process (booting the device in BOOTP mode to reinstall RouterOS), press and hold the Reset button, power on the device, and wait for the USER (USR) LED to flash, then become stable. When the USR LED turns off, release the Reset button.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## LED indicators

- The power LED is lit when the router is powered from the DC jack or PoE.
- The user LED can be configured from RouterOS.
- The port LEDs indicate the individual Ethernet and SFP port activity.

## Extension slots and ports

| **Product Code** | CRS309‑1G‑8S+IN |
| --- | --- |
| **CPU** | 98DX8208, 800 MHz |
| **CPU Architecture** | ARM 32bit |
| **CPU Core Count** | 2 |
| **Switch Chip Model** | 98DX8208 |
| **RAM** | 512 MB |
| **Storage** | 16 MB Flash |
| **1G Ethernet (RJ45)** | 1 |
| **10G SFP+ Ports** | 8 |
| **Operating System** | RouterOS / SwOS (Dual boot) |
| **Operating Temperature** | ‑40 °C to +70 °C |
| **Case Dimensions** | 272 × 191 × 44 mm |

## Accessories

Package includes the following accessories that come with the device:

*[Figure]*

See the [MikroTik wired interface compatibility](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## Operating system support

The device supports dual boot with SwOS version 2.9 and later, as well as RouterOS version 7 or later. The specific factory-installed RouterOS version is indicated in the RouterOS menu under `/system resource`. Other operating systems have not been tested and are not officially supported.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs309-1g-8s-plus-in.md](../regulatory/crs309-1g-8s-plus-in.md).
