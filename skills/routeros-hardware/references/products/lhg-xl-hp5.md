# LHG XL HP5

> Source: https://manual.mikrotik.com/hardware/lhg-xl-hp5
>
> Category: Wireless systems

*[Figure]*

## [LHG XL HP5](https://mikrotik.com/product/RBLHG-5HPnD-XL) (RBLHG-5HPnD-XL)

Dual chain eXtra Large High Power 27dBi 5GHz CPE/Point-to-Point Integrated Antenna. See the [LHG XL HP5 product page](https://mikrotik.com/product/RBLHG-5HPnD-XL) for full specifications and brochures.

## Assembly

Attach the two legs to the LHG case, then snap the assembled LHG unit to the grid in the appropriate locations. Fix the legs in place with two
self thread screws (Included, use Phillips screwdriver PH2). Attach the L shaped mount to the dish using the included screws. Use the U bolt, to
fix the unit to a pole/mast.

## Quickstart

- Open the Ethernet door to connect your PC or LAN cable to the Ethernet port, connect the other end of the Ethernet cable to a PoE injector;
- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Access **WebFig** by opening <https://192.168.88.1>, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and click on the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the "Quick Set" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Powering

The device accepts powering only from Passive PoE injectors.

## Extension slots and ports

- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One integrated wireless device with a built-in grid antenna.

## Buttons and jumpers

The reset button has three functions:
• Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
• Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode (total 10 seconds).
• Or keep holding the button for 5 more seconds until LED turns off, then release it to make the RBLHG-5HPnD-XL look for Netinstall servers (total 15 seconds).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource.

Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/lhg-xl-hp5.md](../regulatory/lhg-xl-hp5.md).
