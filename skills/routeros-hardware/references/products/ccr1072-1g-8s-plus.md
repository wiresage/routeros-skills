# CCR1072-1G-8S+

> Source: https://manual.mikrotik.com/hardware/ccr1072-1g-8s-plus
>
> Category: Ethernet routers

*[Figure]*

The CCR1072 is a high-performance multicore router with eight SFP+ cages. Ports are directly connected to a Tilera 72 core CPU and assisted by 16 GB of built-in ECC RAM.

## First use

The Ethernet port 1 (BOOT) has a default IP address for connecting: 192.168.88.1 username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker). Please connect with your web browser to this IP address and choose WebFig to configure it. The device doesn't have any other configuration applied by default, please connect to it, and set up WAN IP addresses, user password, firewall, etc. Please see the (link) section.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right;
- Place the device in rackmount enclosure and align with the holes so that the device fits conveniently;
- Tighten screws to secure it in place.

*[Figure]*

The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment. We recommend Cat6 cables for our devices.
*Mounting and configuration of this device should be done by a qualified person.*

## Powering

The device has dual removable (hot-swap compatible) power supply units AC **⏦** 110-240V (2.5 A) with standard IEC compatible sockets with Maximum power consumption of 125 W.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see a section (link)

## Extension slots and ports

- 2x M.2 slots, which accept 80mm Key-M x4 PCIe 2.0 modules. M.2 slots are located on the PCB board inside the device. In order to access them remove screws on the back of the router for upper cover and while lifting up and pulling towards the cover slides off.
- microSD card slot.
- Smart Card slot for private key storage.
- 1 Gigabit Ethernet port.
- 8 SFP+ ports for 10 Gigabit connectivity.
- USB slot type A.
- microUSB slot type AB.
- Automatic fan speed control.The CCR1072 has PCIe Gen 2.0 x4 connections to the two M.2 slots.Recommended are NVMe M.2 2280mm M key SSD disks with a capacity of up to 1TB.

## Reset button

The reset button has two functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU/US AC **⏦** power cord, D03+QT3 H05VV-F 3x0.75 mm 2 1.83 m RoHS.
- Fastening set for rackmount case K-10 R2.
- Rackmount Case x72 Side Bracket.
  Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/CCR1072-1G-8Splus>

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

*[Figure]*

Safety Notice
Electric shock hazard. This equipment is to be serviced by trained personnel only. This is a class A device, operating it near residential radio equipment could cause radio interference.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ccr1072-1g-8s-plus.md](../regulatory/ccr1072-1g-8s-plus.md).
