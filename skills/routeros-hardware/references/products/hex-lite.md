# hEX lite

> Source: https://manual.mikrotik.com/hardware/hex-lite
>
> Category: Ethernet routers

5x Ethernet, Small plastic case, 850MHz CPU, 64MB RAM, Most affordable MPLS router, RouterOS L4. See the [hEX lite product page](https://mikrotik.com/product/RB750r2) for full specifications and brochures.

### hEX lite (RB750r2)

*[Figure]*

## First use

- Choose your powering solution, please see the section for possibilities.
- Connect your Internet cable to port 1 (labeled "Internet"), and local network computers to ports 2-5.
- Connect your direct input power jack if not using POE, to start up the device.
- The device will boot up and after the short beep, the network will be available for connecting.
- Set your computer IP configuration to automatic (DHCP).
- Once connected to the network, open <https://192.168.88.1> in your web browser to start configuration, since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Set up your password on the screen that loads.

## Mounting

This device is designed for use indoors by placing it on the flat surface or mounting on the wall, mounting points are shown on the picture below, screws are not included in the package. Screws with size 4x25 mm fit nicely, depending on your wall structure you can use dowels 6x30 mm and 6 mm drill bit if needed.

*[Figure]*

When mounting on the wall, please ensure that the cable feed is pointing downwards. We recommend using Cat5/6 cable for our devices. The IP rating scale for this device is IPX0.

## Powering

The board accepts power from the power jack or from the first Ethernet port (Passive PoE):

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 6-30 V DC;
- First Ethernet port accepts passive Power over Ethernet accepts 6-30 V DC.
  Normally the power consumption of this device is 2 W.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- Five individual Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices. The Ethernet port accepts 6-30 V DC power from a passive PoE injector, 12 V or more is recommended to compensate for the loss in cables.

## Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and bridge all interfaces.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Specifications

For more information about this product, specifications and pictures please visit our web page: <https://mikrotik.com/product/RB750r2>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hex-lite.md](../regulatory/hex-lite.md).
