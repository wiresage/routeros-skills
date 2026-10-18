# hEX PoE

> Source: https://manual.mikrotik.com/hardware/hex-poe
>
> Category: Ethernet routers

### hEX PoE (RB960PGS)

*[Figure]*

hEX PoE is a powerful five-port Gigabit Ethernet router with an SFP port capable of powering other devices.

## First use

- Choose your powering solution, please see the (link) on how to connect.
- The device will boot up and after the short beep, the network will be available for connecting.
- Set your computer IP configuration to automatic (DHCP).
- Once connected to the network, open <https://192.168.88.1> in your web browser to start configuration, since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Set up your password on the screen that loads.

## Mounting

This device is designed for use indoors by placing it on the flat surface or mounting on the wall, mounting points are shown in the picture below, screws are not included in the package. Screws with size 4x25 mm fit nicely, depending on your wall structure you can use dowels 6x30 mm and 6 mm drill bit if needed.

*[Figure]*

When mounting on the wall, please ensure that the cable feed is pointing downwards. We recommend using Cat6 cable for our devices. The IP rating scale for this device is IPX0.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.

## Powering

The device accepts power from the power jack or from the first Ethernet port (Passive PoE):

- Direct input power jack (5.5mm outside and 2mm inside, female, pin positive) accepts 12 - 57 V ⎓DC.
- The first Ethernet port accepts passive Power over Ethernet 12 - 57 V ⎓DC.
- PoE out on 2 - 5 Ethernet port, It also supports passive PoE input and passive or 802.3af/at PoE output. Ethernet ports 2-5 can power other PoE capable devices with the same voltage as applied to the unit. It can power at/af mode B (4,5+)(7,8-) compatible devices, if 48-57 input voltage is used.
  The power consumption of this device under maximum load with attachments is 59 W. Without attachments 6 W.

## Power output

This device can supply PoE power to external devices from its Ethernet ports. This is convenient as you don't need any additional PoE injectors to power other devices. The output voltage will be the same as the input voltage. The maximum power output of each Ethernet port in this mode is 1 A (the total maximum for all ports is 2 A). Once Power Output is enabled in RouterOS, the Ethernet LED adds red color to it (green means Ethernet link is made, red means power but no link, red and green both means there is link and power).

## Booting process

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section Reset button.

## Extension slots and ports

- The device has five individual Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- 1G SFP port.
- USB type-A slot.
  Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Buttons and jumpers

### Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and bridge all interfaces.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Connecting to a POE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Accessories

The package includes the following accessories that come with the device:

*[Figure]*

## Specifications

For more information about this product, specifications, and pictures please visit our web page: <https://mikrotik.com/product/RB960PGS>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hex-poe.md](../regulatory/hex-poe.md).
