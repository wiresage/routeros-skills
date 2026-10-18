# CRS304-4XG-IN

> Source: https://manual.mikrotik.com/hardware/crs304-4xg-in
>
> Category: Switches

*[Figure]*

This is a compact and powerful device designed to simplify your 10 Gigabit network setups. It comes equipped with 4x10G Ethernet ports that are ready to use right out of the box. See the [CRS304-4XG-IN product page](https://mikrotik.com/product/crs304_4xg_in) for full specifications and brochures.

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

This indoor switch offers multiple mounting options, including a side DIN rail mount and standard screw points on the back for easy integration. The DIN rail mount can also be repositioned to the back.

*[Figure]*

*[Figure]*

## Powering

The device can be powered through two DC power jacks (for redundancy failover), a 2-pin terminal, or the MGMT/BOOT Ethernet PoE-in port:

- Direct input power jacks DC1, DC2 (5.5 mm outside and 2 mm inside, female, pin positive) accept DC ⎓ 12-57 V DC.
- MGMT/BOOT Ethernet PoE-in port accepts passive or 802.3af/at Power over Ethernet in the range of DC ⎓ 36-57 V.
- 2-pin terminal accepts DC ⎓ 12-57 V DC.
  The power consumption of this device is 21 W at maximum load and 15 W at minimum.
  When powering this device with 802.3af/at, we recommend avoiding grounding for optimal compatibility.

## Connecting to a POE Adapter

- Connect the device to the included PoE injector using an Ethernet cable, attaching it to the data+power or PoE-out port;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector.

## Configuration

Full documentation for RouterOS is available at: <https://mt.lv/help> You can configure the device using WebFig in a web browser or the "WinBox" configuration tool <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility.**
**To start setup, open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RS-232 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the Reset button.

Marvell Prestera switch chip features user manual

## Extension slots and ports

- Four 1G/2.5G/5G/10G Ethernet ports.
- One Gigabit Ethernet port, suggested to be used for management (Supports Auto MDI/X so you can use either straight or cross-over cables for connecting to other network devices). The MGMT/BOOT Ethernet port can also be used for network booting and recovery with Netinstall.

## Reset button

- To reset the configuration, unplug the device from power, press and hold the Reset button, and release it when the USER (USR) LED starts flashing.
- To load the backup bootloader, press and hold the Reset button before applying power, then release it after three seconds.
- To initiate the Netinstall process (booting the device in BOOTP mode to reinstall RouterOS), press and hold the Reset button, power on the device, and wait for the USER (USR) LED to flash, then become stable. When the USR LED turns off, release the Reset button.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs304-4xg-in.md](../regulatory/crs304-4xg-in.md).
