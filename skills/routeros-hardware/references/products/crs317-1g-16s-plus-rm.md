# CRS317-1G-16S+RM

> Source: https://manual.mikrotik.com/hardware/crs317-1g-16s-plus-rm
>
> Category: Switches

*[Figure]*

Smart Switch, 1 x Gigabit LAN, 16 x SFP+ cages, Dual Core 800MHz CPU, 1GB RAM, 1U rackmount passive cooling case, Dual Power Supplies. See the [CRS317-1G-16S+RM product page](https://mikrotik.com/product/crs317_1g_16s_rm) for full specifications and brochures.

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
- Place the device in the rackmount enclosure and align with the holes so that the device fits conveniently.
  *[Figure]*
- Tighten screws to secure it in place.

The IP rating scale for this device is IP0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
The mounting and configuration of this device should be done by a qualified person.

## Powering

The device accepts powering through two IEC C14 standard connectors and supports both AC 110/240 V ⏦. Only one PSU is active at the time, the second one is used for redundancy.
The PoE injector is not included. The power consumption of this device under maximum load is up to 44W.

The device is fitted with passive cooling heatsinks and under normal load will operate silently, but in emergencies, two redundant fans will automatically switch on to keep the device cool, if ambient temperatures are above normal. The device has been tested to operate in ambient temperatures from -20 ℃ to +60 ℃.

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

| **Product Code** | CRS317‑1G‑16S+RM |
| --- | --- |
| **CPU** | 98DX8216, 800 MHz |
| **CPU Architecture** | ARM 32bit |
| **CPU Core Count** | 2 |
| **Switch Chip Model** | 98DX8216 |
| **RAM** | 1 GB |
| **Storage** | 16 MB Flash |
| **1G Ethernet (RJ45)** | 1 |
| **10G SFP+ Ports** | 16 |
| **Serial Console (RJ45)** | 1 |
| **Operating System** | RouterOS (license level 6) / SwitchOS (dual boot) |
| **Operating Temperature** | ‑20 °C to +60 °C |
| **Case Dimensions** | 443 × 224 × 44 mm |

## Reset button

- To reset the configuration, unplug the device from power, press and hold the Reset button, and release it when the USER (USR) LED starts flashing.
- To load the backup bootloader, press and hold the Reset button before applying power, then release it after three seconds.
- To initiate the Netinstall process (booting the device in BOOTP mode to reinstall RouterOS), press and hold the Reset button, power on the device, and wait for the USER (USR) LED to flash, then become stable. When the USR LED turns off, release the Reset button.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## SwOS Reset and Reinstall

CRS317-1G-16S+ has built-in backup SwOS firmware which can be loaded in case standard firmware breaks or upgrade fails:

- Holding the Reset button for few seconds while CRS317-1G-16S+ is booting resets configuration and loads backup firmware SwOS 2.3p.
- After loading back up firmware SwOS 2.3p it is possible to connect to 192.168.88.1 using a web browser and install new SwOS firmware.

## Accessories

Package includes the following accessories that come with the device:

*[Figure]*

Please visit the wiki pages for the MikroTik SFP module compatibility table: MikroTik wired interface compatibility.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs317-1g-16s-plus-rm.md](../regulatory/crs317-1g-16s-plus-rm.md).
