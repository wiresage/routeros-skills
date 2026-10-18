# mAP

> Source: https://manual.mikrotik.com/hardware/map
>
> Category: Indoor wireless

*[Figure]*

The mAP 2nD is a small wireless AP device with 2 Ethernet ports, Ether1 supports powering by PoE, Ether2 supports PoE output for powering another device. Depending on software configuration, it can function as a wireless client, an access point or a repeater. See the [mAP product page](https://mikrotik.com/product/RBmAP2nD) for full specifications and brochures.

## Quickstart

- Connect your Internet cable to Ether1, and your PC to Ether2. If using the mAP to power another router using the PoE output feature, connect the router to Ether2, and use the built-in wireless AP to configure the mAP.
- Set computer/router IP configuration to *automatic* (DHCP).
- Wireless AP mode is enabled by default, you can connect to the SSID "MikroTik". Log into your router from your web browser by opening 192.168.88.1 in the address bar user admin and no password (or, for some models, check user and wireless passwords on the sticker)..
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, to apply country regulation settings, and set up your password on the screen that loads.
- The Ether2 port supports PoE output, with the auto-detection feature. This means you can connect Laptops and other non-PoE devices without damaging them. The PoE on Ether2 outputs approximately 2V below input voltage and supports up to 0.5 A (So provided 24V PSU will provide 22 V / 0.5 A output to the Ether2 PoE port).

## Powering

The device accepts power from the power jack or the first Ethernet port (Passive PoE):

- DC power jack (5.5 mm outside and 2 mm inside diameter, female, pin positive plug) accepts 8-57 V DC ⎓.
- The first Ethernet port accepts passive Power over Ethernet 11-57 V DC ⎓.
- The mAP can also be powered with the built-in micro USB port, using the USB 5 V ⎓ power.
  Under maximum load, the power consumption of this device is 4W (when not using PoE output)

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Booting process

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device for reinstallation network, see section Buttons and jumpers

## Extension slots and ports

- Two 10/100 Ethernet ports, supporting automatic cross/straight cable connection (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated Wireless 2.4GHz 802.11b/g/n 2x2 dual chain MIMO, Onboard PIF antennas, max gain 1.2dBi.
- One micro USB 2.0 port.

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the front of the unit.
We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Buttons and jumpers

RouterBOOT reset button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

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

Safety warnings and regulatory statements are in [regulatory/map.md](../regulatory/map.md).
