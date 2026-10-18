# CRS326-4C+20G+2Q+RM

> Source: https://manual.mikrotik.com/hardware/crs326-4c-plus-20g-plus-2q-plus-rm
>
> Category: Switches

*[Figure]*

The CRS326-4C+20G+2Q+RM is a network switch with twenty 2.5G Ethernet ports, four 2.5/10G SFP+ ports and one 100M and two 40G QSFP+ ports. The device is ready to use as a switch. See the [CRS326-4C+20G+2Q+RM product page](https://mikrotik.com/product/crs326_4c_20g_2q_rm) for full specifications and brochures.

## Quickstart

- Connect with your PC to any Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Use WebFig in a web browser or the "WinBox" configuration tool <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
  *[Figure]*

The IP rating scale for this device is IP20. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
Mounting and configuration of this device should be done by a qualified person.

## Powering

The device accepts powering from two inputs of 100 – 240 V AC ⏦.
The power consumption without attachments is 51 W. With attachments up to 70 W.

## Configuration

Full documentation for both RouterOS and SwOS is available at: <https://mt.lv/help> You can configure the device using WebFig in a web browser or the "WinBox" configuration tool <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility.**
**To start setup, open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RJ45 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the Reset button.

Marvell Prestera switch chip features user manual

The device supports booting either RouterOS (for full routing and switching functionality) or SwOS (for switch-only operation). By default, the device boots into RouterOS, but you can switch to the other operating system as follows:

- From SwOS: Go to the System menu and click the Boot RouterOS button at the bottom of the page.
- From RouterOS: Open System → RouterBOARD → Settings and select Boot OS.
  It is also possible to choose the operating system and configure other boot options using the serial console menu.

## Extension slots and ports

| **Product Code** | CRS326‑4C+20G+2Q+RM |
| --- | --- |
| **CPU** | QCA9531, 650 MHz |
| **CPU Architecture** | MIPSBE |
| **CPU Core Count** | 1 |
| **Switch Chip Model** | 98DX8332 |
| **RAM** | 128 MB |
| **Storage** | 32 MB Flash |
| **100 Mbps Ethernet (RJ45)** | 1 |
| **2.5G Ethernet (RJ45)** | 20 |
| **Combo 10G (2.5G ETH / SFP+) Ports** | 4 |
| **40G QSFP+ Ports** | 2 |
| **Serial Console (RJ45)** | 1 |
| **Operating System** | RouterOS v7 (License 6) |
| **Operating Temperature** | ‑20 °C to +60 °C |
| **Case Dimensions** | 443 × 258 × 44 mm |

Please visit help pages for MikroTik SFP module compatibility table: MikroTik wired interface compatibility

## Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Hold the Reset button and power on your device (wait until the "USR" led is blinking then stable "On", and when the "USR" led is "Off" - release the Reset button) - the device is booting in bootp mode to reinstall RouterOS using Netinstall. **The MGMT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs326-4c-plus-20g-plus-2q-plus-rm.md](../regulatory/crs326-4c-plus-20g-plus-2q-plus-rm.md).
