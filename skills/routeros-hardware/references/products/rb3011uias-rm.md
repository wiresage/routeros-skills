# RB3011UiAS-RM

> Source: https://manual.mikrotik.com/hardware/rb3011uias-rm
>
> Category: Ethernet routers

*[Figure]*

## First use

- Connect your Internet cable to port 1, and local network PCs to ports 2-10.
- Choose your powering solution, please see the section for possibilities.
- Set your computer IP configuration to *automatic* (DHCP).
- The default IP address from the local network is 192.168.88.1, open this address in your web browser to start the configuration. The username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. The device needs to have an active Internet connection.
- Set up strong password for the device.

## Powering

The device accepts powering from either the power jack or from the LAN1 Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside diameter, female, pin positive plug) accepts 10-30 V DC ⎓ (overvoltage protection starts at 30 V).
- Eth1 port accepts 10-30 V DC ⎓ input (at the board; higher voltage needed to compensate for power loss on long cables) from non-standard (passive) Power over Ethernet injectors. The board does not support IEEE802.3af compliant 48 V power injectors.
  The power consumption under maximum load can reach 30 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Extension slots and ports

- Ten 10/100/1000 (Gigabit) Ethernet ports (Auto MDI/X).
- USB 3.0 type A.
- LCD panel.
- SFP port for SFP module.
- The Ether10 port supports PoE output, with the auto-detection feature. This means you can connect Laptops and other non-PoE devices without damaging them. The PoE on Ether10 outputs approximately 2 V below input voltage and supports up to 0.7 A (So provided 24 V PSU will provide 22V/0.7 A output to the Ether10 PoE port).

## Mounting

*[Figure]*

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right,
- place the device in rackmount enclosure and align with the holes so that the device fits conveniently,
- tighten screws to secure it in place.
  The IP rating scale for this device is IPX0. The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
  We recommend Cat5/6 cables for our devices.
  *Mounting and configuration of this device should be done by a qualified person.*

Operating humidity can be from 5% to 95% non-condensing.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Reset button

To use the reset button, hold it and then turn on the device, while still holding the button.

- Release the button when the green LED starts flashing, to reset the RouterOS configuration. To not load the backup bootloader, you can start holding the button after power is already applied.
- Release the button after LED is no longer flashing (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network). You can also release the button at the time when the device has appeared on the Netinstall utility device list.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- EU/US Switching Power Supply DC ⎓ 24 V, 1.2 A, 28.8 W, 86.8%, VI, cable:220 cm.
- 1U rackmount bracket black.
- Fastening set for RB2011 rackmount case K-19 v3.
  Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Specifications

For more information about this product, specifications and pictures please visit our web page: <https://mikrotik.com/product/RB3011UiAS-RM>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

*[Figure]*

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb3011uias-rm.md](../regulatory/rb3011uias-rm.md).
