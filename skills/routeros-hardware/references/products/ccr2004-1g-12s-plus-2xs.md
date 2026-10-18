# CCR2004-1G-12S+2XS

> Source: https://manual.mikrotik.com/hardware/ccr2004-1g-12s-plus-2xs
>
> Category: Ethernet routers

*[Figure]*

The CCR2004 is a high-performance multicore router with twelve 10G SFP+ ports and two 25G SFP28 ports. See the [CCR2004-1G-12S+2XS product page](https://mikrotik.com/product/ccr2004_1g_12s_2xs) for full specifications and brochures.

## Quickstart

- Connect with your computer to the device using Ethernet cable;
- Download the configuration tool <https://mt.lv/winbox> Open the **Neighbors** tab and connect to the device using MAC address;
- The user name: **admin**, by the default there is no password (or, for some models, check user and wireless passwords on the sticker).;
- To update the device to the latest software version download the latest RouterOS software from <https://mikrotik.com/download>;
- Choose ARM64 packages, and save them to your computer;
- Return to the WinBox and upload downloaded packages to the Files menu;
- Restart the device.
- Detailed info on how to upgrade the device <https://mt.lv/upgrade>;
- Set a strong password.

## Powering

The device has dual integrated power supply units AC **⏦** 110-240V (5 A) with standard IEC compatible sockets with Maximum power consumption of 32 W, with attachments 49 W.

## Configuration

The Ethernet port 1 has a default IP address for connecting: 192.168.88.1. The username is admin and there is no password. The device doesn't have any other configuration applied by default, please set up WAN IP addresses, user password, and update the device. RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case the IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side
For recovery purposes, it is possible to boot the device for reinstallation, see a section (link)

## Specifications

Size of RAM notice - RouterOS v6 will support 1792MB ECC / to fully utilize please use RouterOS v7 4GB ECC.

## Reset button

The reset button has two functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

*[Figure]*

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right;
- Place the device in rackmount enclosure and align with the holes so that the device fits conveniently;
- Tighten screws to secure it in place.
  The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment. We recommend Cat6 cables for our devices.

## Included Parts

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

*[Figure]*

Safety Notice
Electric shock hazard. This equipment is to be serviced by trained personnel only.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ccr2004-1g-12s-plus-2xs.md](../regulatory/ccr2004-1g-12s-plus-2xs.md).
