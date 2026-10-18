# hAP ac lite TC

> Source: https://manual.mikrotik.com/hardware/hap-ac-lite-tc
>
> Category: Indoor wireless

*[Figure]*

The hAP ac lite is a simple home wireless access point. It is configured out of the box, you can simply plug in your internet cable and start using wireless internet. We recommend you set up a password to secure your device, follow these steps.

## Quickstart

Make sure that your ISP is allowing hardware change, please follow these quick steps to set up your device:

- Connect your ISP Ethernet cable to the Ethernet port 1.
- Connect the device to the power source (see "").
- Open network connections on your PC, mobile phone, or other device and search for MikroTik wireless network and connect to it.
- The Configuration has to be done through the wireless network using a web browser or mobile app - (see ""). Alternatively, you can use the WinBox configuration tool <https://mt.lv/winbox>.
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, user name: a*dmin* and there is no password by default (or, for some models, check user and wireless passwords on the sticker).
- When using a mobile application choose Quick setup and it will guide you through all necessary configuration in six easy steps.
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, to apply country regulation settings, and set up your password on the screen that loads.

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

The device accepts power from the power jack or from the first Ethernet port (Passive PoE):

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 10-30 V DC.
- First Ethernet port accepts passive Power over Ethernet accepts 12-30 V DC.
  The power consumption under maximum load can reach 5 W.
  The Ether5 port supports PoE output for powering other RouterBOARD devices. The port has an auto-detection feature, so you can connect Laptops and other non-PoE devices without damaging them. The PoE on Ether5 outputs approximately 2 V below input voltage and supports up to 0.58A (So provided 24 V PSU will provide 22V/0.58 A output to the Ether5 PoE port).

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the front of the unit.
Alternatively, the unit can be mounted on the wall, mounting points are located on the bottom side of the device, screws are not included in the package. Screws with size 4x25 mm fit nicely, depending on your wall structure you can use dowels 6x30 mm and 6 mm drill bit if needed.
When mounting on the wall, please ensure that cable feed is pointing downwards.
We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Extension slots and ports

- Five individual 10/100 Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- Integrated Wireless 2.4 GHz and 5 GHz 802.11 a/b/g/n/ac, simultaneous dual-band radio with onboard PIF antennas, max gain 1.5 dBi.

## Buttons and jumpers

The reset button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU Switching Power Supply 24 V.

## Specifications

For more information about this product, specifications, pictures, downloads and test results please visit our web page: <https://mikrotik.com/product/RB952Ui-5ac2nD>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

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

Safety warnings and regulatory statements are in [regulatory/hap-ac-lite-tc.md](../regulatory/hap-ac-lite-tc.md).
