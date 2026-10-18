# CRS328-4C-20S-4S+RM

> Source: https://manual.mikrotik.com/hardware/crs328-4c-20s-4s-plus-rm
>
> Category: Switches

*[Figure]*

Smart Switch, 20 x SFP cages, 4 x SFP+ cages, 4 x Combo ports (Gigabit Ethernet or SFP), 800MHz CPU, 512MB RAM, 1U rackmount case, Dual Power Supplies, RouterOS L5 or SwitchOS (Dual Boot). See the [CRS328-4C-20S-4S+RM product page](https://mikrotik.com/product/crs328_4c_20s_4s_rm) for full specifications and brochures.

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

## Powering

- The device accepts powering from two IEC connectors. AC input range 100-240 V ⏦.
  The power consumption under maximum load can reach 43 W.

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

| **Product Code** | CRS328-4C-20S-4S+RM |
| --- | --- |
| **CPU** | 98DX3236, 800 MHz |
| **CPU Architecture** | ARM 32bit |
| **CPU Core Count** | 2 |
| **Switch Chip Model** | 98DX3236 |
| **RAM** | 512 MB |
| **Storage** | 16 MB Flash |
| **Combo Ethernet/SFP Ports** | 4 |
| **SFP Ports** | 20 |
| **SFP+ Ports** | 4 |
| **Serial Console (RJ45)** | 1 |
| **Operating System** | RouterOS (license level 5) / SwitchOS (Dual boot) |
| **Operating Temperature** | -20 °C to +60 °C |
| **Case Dimensions** | 443 × 194 × 44 mm |

Please visit help pages for MikroTik SFP module compatibility table: MikroTik wired interface compatibility

## Combo ports

The four combo interfaces each have two physical connectors of which only one can be used at the same time. The ports will be automatically represented as combo1-4 in the RouterOS. It is possible to select which physical port will be used in the RouterOS software Ethernet menu. If left to default "auto", and both F/T have cables plugged in, SFP will take priority. For example, if you have plugged an Ethernet cable into the 1T port and an SFP module in the 1F port, you will have to choose in RouterOS which one to use. Double click the respective combo interface in RouterOS GUI to see which socket is used.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if the designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
  *[Figure]*
- Tighten screws to secure it in place.
  The IP rating scale for this device is IPX0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
  *The mounting and configuration of this device should be done by a qualified person.* *We recommend using Cat6 cables for our devices.*

## Buttons and jumpers

### Reset button

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total of 15 seconds). **The first Ethernet port (combo-ether1) is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

### Mode button

The action of the mode button can be configured from RouterOS software to execute any user-supplied RouterOS script. For configuration, use the menu /system routerboard mode-button

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs328-4c-20s-4s-plus-rm.md](../regulatory/crs328-4c-20s-4s-plus-rm.md).
