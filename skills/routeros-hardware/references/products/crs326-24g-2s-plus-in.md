# CRS326-24G-2S+IN

> Source: https://manual.mikrotik.com/hardware/crs326-24g-2s-plus-in
>
> Category: Switches

*[Figure]*

24 Gigabit ports, 2 SFP+ cages and a desktop case – server room power for your home! See the [CRS326-24G-2S+IN product page](https://mikrotik.com/product/crs326_24g_2s_in) for full specifications and brochures.

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

The device is designed to use indoors and it can be placed on the desktop.

The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
Mounting and configuration of this device should be done by a qualified person.

## Powering

The device accepts power in the following ways:

- Ethernet port accepts passive PoE 10-30 V DC ⎓.
- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 10-30 V DC⎓.
  The power consumption under maximum load can reach 24 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

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

| **Product Code** | CRS326‑24G‑2S+IN |
| --- | --- |
| **CPU** | 98DX3236, 800 MHz |
| **CPU Architecture** | ARM 32bit |
| **CPU Core Count** | 2 |
| **Switch Chip Model** | 98DX3236 |
| **RAM** | 512 MB |
| **Storage** | 16 MB Flash |
| **1G Ethernet (RJ45)** | 24 |
| **10G SFP+ Ports** | 2 |
| **Serial Console (RJ45)** | 1 |
| **Operating System** | RouterOS (license level 5) / SwOS (Dual boot) |
| **Operating Temperature** | ‑40 °C to +60 °C |
| **Case Dimensions** | 285 × 144 × 44 mm |

Please visit wiki pages for MikroTik SFP module compatibility table: MikroTik wired interface compatibility

## Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Included Parts

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs326-24g-2s-plus-in.md](../regulatory/crs326-24g-2s-plus-in.md).
