# OmniTIK series

> Source: https://manual.mikrotik.com/hardware/omnitik-series
>
> Category: Wireless systems

> **This article covers**
>
> - **[OmniTIK 5 ac](https://mikrotik.com/product/rbomnitikg_5hacd)** (RBOmniTikG-5HacD)
> - **[OmniTIK 5 PoE ac](https://mikrotik.com/product/rbomnitikpg_5hacd)** (RBOmniTikPG-5HacD)
> - **[OmniTIK 5 PoE](https://mikrotik.com/product/RBOmniTikUPA-5HnDr2)** (RBOmniTikUPA-5HnD)
> - **[OmniTIK 5](https://mikrotik.com/product/RBOmniTikU-5HnDr2)** (RBOmniTikU-5HnD)

This device needs to be upgraded to RouterOS v7.11.2 or the latest version to ensure compliance with local authority regulations.
It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*
*Configuration manual for software with additional information can be found at <https://mt.lv/help>*

*MikroTik devices are for professional use, if you do not have qualifications please seek a consultant <https://mikrotik.com/consultants>*

## First use

First Ethernet is always configured as a WAN port (protected by a firewall, enabled DHCP client, and disabled MAC connection/discovery). Other Ethernet ports and wireless interfaces are added to the local LAN bridge with 192.168.88.1/24 address set and configured DHCP server.

- Open the bottom lid.
- Connect your PC or LAN cables to the Ethernet ports.
- Connect power source as described in the Powering section.
- Set LAN computer IP configuration to automatic (DHCP).
- The Default IP address of the unit is 192.168.88.1, open this address in your web browser to start the configuration. The username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, apply country regulation settings and set up your password on the screen that loads.
  We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest visiting the RouterOS documentation page to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).

## Powering

The device accepts power in the following ways:

- Ethernet port accepts passive PoE 12-57 V DC ⎓. For Omnitik 5 models, 11-30 V.
  The power consumption under maximum load can reach 14 W.
  PoE version accepts 12-57 V DC with a maximum consumption of 18W, with attachments 66 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Power output

*Applies only to OmniTik 5 PoE ac:* This device can supply PoE power to external devices from its Ethernet ports. This is convenient as you don't need any additional PoE injectors to power other devices. The output voltage will be the same as the input voltage. The maximum power output of each Ethernet port in this mode is 1A (the total maximum for all ports is 2A). To reach maximum output power it is recommended to use a high voltage adapter together with the included PoE injector to power the OmniTik unit (48/56V), because 802.3af/at the input is limited to 30W and OmniTik will consume up to 15W by itself. Once Power Output is enabled in RouterOS, the Ethernet LED adds red color to it (green means Ethernet link is made, red means power but no link, red and green both means there is link and power).

## Mounting

On the back of the device, slide the included pole mount adapter with the clip facing forward, until the clip clicks into place.

*[Figure]*

## [OmniTIK 5 PoE ac](https://mikrotik.com/product/rbomnitikpg_5hacd) (RBOmniTikPG-5HacD)

Use the included hose clamp to attach the unit to a pole or mast. Adjustable QuickMount adapters are available separately.

*[Figure]*

The OmniTik has a locking screw that secures the port door, it can be closed with a 5mm hex screwdriver.

## Grounding

The installation infrastructure (towers and masts), must be properly grounded.
Please secure all loose Ethernet cables and antenna cables to the pole or mast approximately 30cm from the device, so that the cable weight is not pulling the ports and connectors.

## Extension slots and ports

- Five Gigabit Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One integrated wireless 5GHz 802.11a/n/ac, 2x2 MIMO with built in grid antenna, max gain 7.5dBi.

## Buttons and jumpers

The reset button has the following functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/omnitik-series.md](../regulatory/omnitik-series.md).
