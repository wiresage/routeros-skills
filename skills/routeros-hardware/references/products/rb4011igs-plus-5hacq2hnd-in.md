# RB4011iGS+5HacQ2HnD-IN

> Source: https://manual.mikrotik.com/hardware/rb4011igs-plus-5hacq2hnd-in
>
> Category: Indoor wireless

*[Figure]*

The device is already configured with basic settings, you can simply plug in your ISP cable and start using the Internet. We recommend you to set up a password to secure your device. See the [RB4011iGS+5HacQ2HnD-IN product page](https://mikrotik.com/product/rb4011igs_5hacq2hnd_in) for full specifications and brochures.

## Setup

- Choose your powering solution, please see the section for possibilities.
- Connect your Internet cable to port Ethernet1.
- Set your computer IP configuration to *automatic* (DHCP).
- Connect to the device through any of the ports, excluding Ethernet1, or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker).
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at <https://mt.lv/winbox>.
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device.
- Proceed to connect using the MAC address. The username is "admin," and there is no password (or, for some models, check user and wireless passwords on the sticker).
- Click the "Check for updates" button and update RouterOS to the latest version.
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu.
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device.
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates.
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings.
- Set up your wireless network password in the left field.
- Set up your router password in the bottom field.

## Powering

The power consumption under maximum load can reach 44 W. The device accepts power from the power jack or from the first Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-57 V DC.
- First Ethernet port accepts Power over Ethernet 18-57 V DC.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mounting

It is possible to attach the device to a wall, using the provided screw holes on the back of the unit. The device should be mounted in a way that the cable openings are pointing downward.
The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat5/6 shielded cables for our devices.
Mounting and configuration of this device should be done by a qualified person.
*The enclosure includes a grounding screw hole with an M4 thread (screw not included). In locations with the risk of ESD discharge, you are encouraged to connect the grounding screw to verified grounding infrastructure.*
This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Extension slots and ports

- The Ethernet ports are connected in two groups of five, each group is connected through a switch chip. The ports can be configured individually and support automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- SFP+ port accepts SFP and SFP+ modules. Refer to the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).
- RJ45 console port for serial console access, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity.
- Integrated QCA9984 Dual-Band 4x4 with 4 SS MIMO, 5 GHz 802.11a/n/ac.
- One MiniPCIe slot, with installed MiniPCIe Card R11e-2HnD, 2.4 GHz 802.11b/g/n. Only Mini PCIe cards supported.

## Buttons and jumpers

The reset button has the following functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers connected to its first Ethernet port (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Accessories

Package includes the following accessories that come with the device:

- Power adapter 24 V DC ⎓ 2.5 A 60 W 80 % VI 121x54x33 cable 2 m plug RA 2.1 mm.
- EU/US power cord, D03+QT3 H05VV-F 3x0.75mm2 1.83m RoHS.
- Mounting kit K-59 fastening set.
  Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## MikroTik mobile app

*[Figure]*

*[Figure]*

*[Figure]*

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

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

Safety warnings and regulatory statements are in [regulatory/rb4011igs-plus-5hacq2hnd-in.md](../regulatory/rb4011igs-plus-5hacq2hnd-in.md).
