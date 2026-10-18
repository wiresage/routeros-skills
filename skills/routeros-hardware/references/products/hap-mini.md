# hAP mini

> Source: https://manual.mikrotik.com/hardware/hap-mini
>
> Category: Indoor wireless

### hAP mini RB931-2nD

*[Figure]*

The hAP is a simple home wireless access point. It is already configured, you can simply plug in your ISP cable and start using wireless internet. We recommend you set up a password to secure your device. See the [hAP mini product page](https://mikrotik.com/product/RB931-2nD) for full specifications and brochures.

## Setup

- Choose your powering solution, please see the section for possibilities.
- Connect your internet cable to the first port, and, if you have wired devices, connect them to the other ports
- Set your computer IP configuration to automatic (DHCP).
- From your PC or smartphone, connect to the wireless network name which starts with "MikroTik".
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, user name: a*dmin* and there is no password by default (or, for some models, check user and wireless passwords on the sticker)..
- When using a mobile application choose Quick setup and it will guide you through all necessary configuration in six easy steps.
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, to apply country regulation settings and set up your password on the screen that loads.

## Powering

The device accepts powering from the microUSB port. The port itself doesn't function as a standard microUSB port for data, it is only used for power. You can use any standard 0.5 - 2A USB adapter that usually comes with smartphones. One 5V 0.7A USB charger is included in the box.
The power consumption under maximum load can reach 3.5W.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Extension slots and ports

- The Ethernet ports are connected through a switch chip, can be configured individually and support automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- The Integrated wireless module which supports AP/CPE/P2P/Repeater modes.

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the back of the unit.
The IPX rating scale of this device is IPX0. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Buttons and jumpers

RouterBOOT reset button has the following functions:

- Hold the button before powering on the device, and at power-up, the button will force load the backup boot loader. Continue holding the button for the other two functions of this button.
- Release the button when green LED starts flashing, to reset RouterOS configuration. To not load the backup boot loader, you can start holding the button after power is already applied.
- Release the button after LED is no longer flashing (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number v6 at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Datasheet for any device is available on the official manufacturer website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).

Please make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hap-mini.md](../regulatory/hap-mini.md).
