# mAP lite

> Source: https://manual.mikrotik.com/hardware/map-lite
>
> Category: Indoor wireless

*[Figure]*

Tiny size 2.4GHz Dual Chain access point with a 650MHz CPU, 64MB RAM and one Ethernet. See the [mAP lite product page](https://mikrotik.com/product/RBmAPL-2nD) for full specifications and brochures.

## Quick Setup Guide

The mAP is a small wireless access point with one ethernet port, the ethernet port supports powering by PoE. Depending on software configuration, it can function as a wireless client, an access point or a repeater.

## First use

- Connect the device to the included power adapter;
- Connect your computer to the wireless network;
- Open 192.168.88.1 in your web browser to start the configuration;
- User name: **admin** and there is no password by default (or, for some models, check user and wireless passwords on the sticker).;

## Powering

The device accepts power from the USB port or from the Ethernet port.

- Micro USB power jack accepts 5 V DC, a USB 5 V adapter is included with the product.
- The Ethernet port accepts passive Power over Ethernet 11-57 V DC.
- The Ethernet port also accepts PoE power from an 802.3af switch over the pins +4,5/-7,8 or +3,6/-1,2.
  Under maximum load, the power consumption of this device is 4 W.

## Booting process

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).
For recovery purposes, it is possible to boot the device from the network, see section Buttons and jumpers

## Extension slots and ports

- One 10/100 Ethernet port, supporting automatic cross/straight cable connection (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated Wireless 2.4GHz 802.11b/g/n 2x2 MIMO, Onboard PIF antennas, max gain 2dBi.
- One microUSB 2.0 port for powering only.

## Buttons and jumpers

RouterBOOT reset button has the following functions:

- Hold the button before powering on the device, and at power-up, the button will force load the backup boot loader. Continue holding the button for the other two functions of this button.
- Release the button when green LED starts flashing, to reset RouterOS configuration. To not load the backup boot loader, you can start holding the button after power is already applied.
- Release the button after LED is no longer flashing (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/map-lite.md](../regulatory/map-lite.md).
