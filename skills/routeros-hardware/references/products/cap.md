# cAP

> Source: https://manual.mikrotik.com/hardware/cap
>
> Category: Indoor wireless

*[Figure]*

The cAP is a small AP device with one Ethernet port, it supports powering by PoE and optionally can be managed by the CAPsMAN management server.

## Connecting

- Connect POE to the Ethernet port, please see section for instructions on how to connect POE.
- Set your computer IP configuration to *automatic* (DHCP).
- The device wireless access point mode is enabled by default.
- The device will boot up and Wireless network will be available for connecting.
- Open network connections on your pc, mobile phone, or other device and search for MikroTik wireless network and connect to it.
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, to apply country regulation settings, and set up your password on the screen that loads.

## Powering

The device accepts power from the Ethernet port:

- Ethernet port accepts 12-57 V DC **⎓** (802.3af/at or passive PoE).
  The power consumption under maximum load can reach 4 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your WAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Mounting

It is possible to attach the device to a wall or ceiling, using the provided mounting bracket on the back of the unit.

*[Figure]*

- Attach the mounting bracket to the wall or ceiling with provided three screws.
- Use a 5 mm drill bid if necessary with provided dowels.
- Connect needed cables to the device.
- If needed second mounting bracket can be used for additional support when working on thin ceilings or walls, provided screw length is 20 mm.
- Attach the second mount to the other side of the ceiling and secure with screws through the first mount.
- Attach the device to the mounting bracket and turn clockwise until the device secures in place.
  We recommend using Cat5/6 cable for our devices. The IP rating scale for this device is IPX0.
  *Mounting and configuration of this device should be done by a qualified person.*
  Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- One Integrated Wireless 2.4 GHz 802.11b/g/n.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. The mode button can be configured in RouterOS menu /system routerboard mode-button.

## Accessories

Package includes the following accessories that come with the device:

- K-46 mounting set.
- DC ⎓ EU/US Switching Power Supply 24 V, 0.2 A, 4.8 W, Level VI, cable:1.5 m.
- POE Injector with shielded ethernet cable/connector (RBPOE).
- cAP_2nD mount ceiling attachment.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/RBcAP2nD>

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

Safety warnings and regulatory statements are in [regulatory/cap.md](../regulatory/cap.md).
