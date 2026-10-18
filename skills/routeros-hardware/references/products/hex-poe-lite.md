# hEX PoE lite

> Source: https://manual.mikrotik.com/hardware/hex-poe-lite
>
> Category: Ethernet routers

### hEX PoE lite (RB750UPr2)

*[Figure]*

The hEX PoE lite is a router with five Ethernet ports. It has one USB 2.0 port and supports PoE power output to ports 2-5 (500 mA maximum per port). See the [hEX PoE lite product page](https://mikrotik.com/product/RB750UPr2) for full specifications and brochures.

## First use

- Connect your WAN cable to port 1, and LAN computers to ports 2-5.
- Set LAN computer IP configuration to automatic (DHCP).
- The default IP address from LAN is 192.168.88.1.
- User name admin and no password, (or, for some models, check user and wireless passwords on the sticker)

## Powering

The board accepts power from the power jack or from the first Ethernet port (Passive PoE):

- direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 8-28 V DC,
- The first Ethernet port accepts passive Power over Ethernet accepts 8-28 V DC.
  Normally the power consumption of this device is 2.4 W, under maximum load 3.6 W.

## Power output

This device can supply PoE powering to external devices from its Ethernet ports. This is convenient as you don't need any additional PoE injectors to power other devices. This feature is indicated by the letter "P" in the device model name. The output voltage will be the same as input Voltage, and this feature will have to be enabled on the specific ports in RouterOS software. By default it is disabled. The maximum power output of each Ethernet port in this mode is 500mA. Once Power Output is enabled in RouterOS, the Ethernet LED light turns from Green to Red. Red LED means the port is currently providing PoE power.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- Five individual Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices. The Ethernet port accepts 8-28 V DC powering from a passive PoE injector, 12 V or more is recommended to compensate for the loss in cables.
- One USB type A.

## Reset button

The reset button has three functions:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hex-poe-lite.md](../regulatory/hex-poe-lite.md).
