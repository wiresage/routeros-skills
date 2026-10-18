# RB2011UiAS-2HnD-IN

> Source: https://manual.mikrotik.com/hardware/rb2011uias-2hnd-in
>
> Category: Indoor wireless

*[Figure]*

RouterBOARD 2011UiAS-2HnD has most features and interfaces from all our Wireless routers. It's powered by the new Atheros 600MHz 74K MIPS network processor, has 128MB RAM, five Gigabit LAN ports, five Fast Ethernet LAN ports and SFP cage (SFP module not included!). Also, it features powerful (up to 1W!) dual chain 2.4Ghz 802.11bgn wireless, RJ45 serial port, full-size USB port, and RouterOS L5 license.

## Connecting

Please follow these quick steps to set up your device:

- Choose your powering solution, please see the (link)(link) section for possibilities.
- Connect your internet provider Ethernet cable to the ETH1 port.
- Connect your other local computers to the any of other Ethernet ports.
- Plug the included Switching Power Supply, if you are not using PoE, to start up the device.
- The device will boot up, front led indicator will light in solid blue, and Wireless network will be available for connecting.
- Open network connections on your PC, mobile phone, or other device and search for MikroTik wireless network and connect to it.
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, since there is no password by default (or, for some models, check user and wireless passwords on the sticker)., you will be logged in automatically.
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, to apply country regulation settings, and set up your password on the screen that loads.

## Powering

The device accepts powering from either the power jack or from the LAN1 Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside diameter, female, pin positive plug) accepts 8-30 V DC (overvoltage protection starts at 30 V).
- Eth1 port accepts 8-30 V DC input (at the board; higher voltage needed to compensate for power loss on long cables) from non-standard (passive) Power over Ethernet injectors. The board does not work with IEEE802.3af compliant 48 V power injectors.
  Maximum power consumption 11 W.
  **Connecting to a POE Adapter:**
- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Power output

The device supports PoE out from Ethernet 10 port, you can power MikroTik devices which supports powering through Ethernet. The PoE on Ether10 outputs approximately 2 V below input voltage and supports up to 0.58 A (So provided 24 V PSU will provide 22 V at 0.58 A output to the Ether10 PoE port).

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the front of the unit.
Alternatively, the unit can be mounted on the wall, mounting points are located on the bottom side of the device, screws are not included in the package. Screws with size 4x25 mm fit nicely, depending on your wall structure you can use dowels 6x30 mm and 6 mm drill bit if needed.
Grounding screw is located on the backside of the device case, please connect it accordingly to efficient ground.
When mounting on the wall, please ensure that cable feed is pointing downwards.
We recommend using Cat5/6 shielded cables.
*Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.*

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Extension slots and ports

- Five 10/100/1000 (Gigabit) Ethernet ports (Auto MDI/X).
- Five 10/100 (Fast) Ethernet ports (Auto MDI/X).
- Ether10 supports 500 mA output power, ~2 V below the input voltage. Power out supports auto-detect to protect devices.
- One 8-30 V DC power jack.
- SFP port for SFP module (module not included, works only with Gigabit modules).
- Built-in wireless AP (2GHz, 802.11b/g/n), with external antennas.
- One USB 2.0 type A port.

## Buttons and jumpers

The reset button is located on the back of the device, you will need at least 6mm long tool to reach it properly, a button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers connected to its first Ethernet port (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes a power supply for powering the device:

- EU/US Switching Power Supply 24 V, DC ⎓, 1.2 A, 28.8 W, 86.8%, VI, cable:220 cm RA.
- Two antennas are factory installed on the device.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/RB2011UiAS-2HnD-IN>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

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

Safety warnings and regulatory statements are in [regulatory/rb2011uias-2hnd-in.md](../regulatory/rb2011uias-2hnd-in.md).
