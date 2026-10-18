# hAP lite

> Source: https://manual.mikrotik.com/hardware/hap-lite
>
> Category: Indoor wireless

*[Figure]*

Low cost home wireless AP with dual chain 2.4GHz wireless, powered by USB. See the [hAP lite product page](https://mikrotik.com/product/RB941-2nD) for full specifications and brochures.

## Quickstart

Please follow these quick steps to set up your device:

- Connect your ISP Ethernet cable to the Ethernet port 1.
- Connect the device to the power source (see "").
- Open network connections on your PC, mobile phone or other device and search for MikroTik wireless network and connect to it.
- The configuration has to be done through the wireless network using a web browser or mobile app - (see ""). Alternatively, you can use the WinBox configuration tool <https://mt.lv/winbox>.
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, user name: a*dmin* and there is no password by default (or, for some models, check user and wireless passwords on the sticker)..
- When using a mobile application choose Quick setup and it will guide you through all necessary configuration in six easy steps.
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, to apply country regulation settings and set up your password in the screen that loads.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Powering

The device accepts power in the following ways:

- microUSB accepts 5 V DC⎓.
  The power consumption under maximum load can reach 5 W.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the front of the unit.
Alternatively, unit can be mounted on the wall, mounting points are located on the bottom side of the device, screws are not included in the package. Screws with size 4x25 mm fit nicely, depending on your wall structure you can use dowels 6x30 mm and 6 mm drill bit if needed.

*[Figure]*

When mounting on the wall, please ensure that cable feed is pointing downwards.
The IP rating scale of this device is IPX0. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Extension slots and ports

- Four 10/100 Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- Integrated wireless module 2.4 GHz, 802.11b/g/n, antenna gain 1.5 dBi.

## Reset button

RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU Switching Power Supply 5 V, 1 A, 5 W, Level VI, cable:1.5 m, MicroUSB.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hap-lite.md](../regulatory/hap-lite.md).
