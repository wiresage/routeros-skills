# wAP ac

> Source: https://manual.mikrotik.com/hardware/wap-ac
>
> Category: Indoor wireless

*[Figure]* *[Figure]*

The wAP ac is a small dual-band weatherproof wireless access point for mounting on a pole, wall, or the ceiling. The new revision features 2x Gigabit Ethernet ports, enhanced wireless antenna performance, more RAM, and a powerful quad-core CPU. See the [wAP ac product page](https://mikrotik.com/product/wap_ac) for full specifications and brochures.

> **This article covers**
>
> - **wAP ac** (RBwAPG-5HacD2HnD)
> - **wAP ac BE** (RBwAPG-5HacD2HnD-BE)

## Quickstart

- Make sure your Internet service provider is allowing hardware change and will issue an IP address.
- Open the bottom lid.
- Plug the included PoE injector into the ISP outlet and attach an Ethernet cable to it.
- Connect the other end of the Ethernet cable to this router.
- Plug the provided power supply into the PoE injector.
- Connect your computer to the wireless network.
- Open <https://192.168.88.1> in your web browser to start the configuration.
- User name: **admin** and there is no password by default (or, for some models, check user and wireless passwords on the sticker)..
- You will be logged in to the configuration screen.
- Click the "*Check_for_updates*" button on the right side and update your RouterOS software to the latest version. Must have an active Internet connection.
- The device will reboot.
- Connect again and choose your country on the left side of the screen, to apply country regulation settings.
- Set up your wireless network password, the password must be at least eight symbols.
- Set the *Installation* to indoors or outdoors, depending on the usage type.
- Set up your router password in the bottom field to the right and repeat it, it will be used to login next time.

## Mounting

The device can be mounted in several ways: wall, ceiling, pole or it can be placed in specially designed MikroTik holder which comes with the package. The package includes a drill hole template with instructions, to help you with the Ethernet cable installation and attachment to a ceiling or a wall. The package also includes a steel bracket to put on the other side of a dropdown ceiling tile and two screws and wall anchors. The Unit can be attached to the pole using zip ties or steel clamp.
To prevent the bottom lid for opening the different screw can be used. One Torx T20 security screw is included for optional use. Use it with the included L-shaped wrench to fix it into the bottom lid. Detailed instructions of replacing the screw are in the package.

When using and installing this device please pay attention to Maximum Permissible Exposure (MPE) safety distance with a minimum of 31 cm between the radiator and your body.

**Mounting on the mast or pole:**

*[Figure]*

** It's recommended to use electrical tape to increase friction between materials.*

- Mount plastic tie straps to steel brackets guiding them through holes.
- Mount bracket to the device.
- Secure them with a screw.
- Mount and align the device on the pole or mast.
- Guide Ethernet cable through the opening and connect to the Ethernet port.
- Close bottom latch and secure with a screw.
  It's recommended to secure Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.

*[Figure]*

**Mounting unit on the wall:**

- Use included a template to mark spots for drilling holes. And if needed for Ethernet cable. Align accordingly, it will depend on how the device will be mounted finally.
- Insert dowels if needed, depends on wall structure and material.
- Place included a steel bracket on the wall.
- Use screws to secure it in the place.
- Extend your Ethernet cable through the opening and connect to the Ethernet port.
- Mount the device on the steel bracket
- Secure it in place with the screw.
- Close bottom latch.

Avoid mounting the device on the low ground spot, as you won't be able to attach and close the bottom latch. **Mounting on the ceiling:**

*[Figure]*

A Special bracket is included in the package to mount on the drop ceiling. As it consists of two parts, to be attached on both sides of the ceiling tile.

- Use the template to mark spots for holes.
- Place both mounting brackets on the spot.
- Secure them together using screws.
  Continue assembling in the same manner if mounting on the wall.
- Extend your Ethernet cable through the opening and connect to the Ethernet port.
- Mount the device on the steel bracket.
- Secure it in place with the screw.
- Close bottom latch.

## Bottom Lid

- The bottom lid is secured in place with the captive screw.
- Use the Philips PH2 screwdriver to unscrew it, but do not remove the screw completely.

*[Figure]*

- Pull the cover in the opposite direction from the device to remove it.

*[Figure]*

- Reassemble.

## Powering

The device accepts power from the power jack or from the Ethernet port, both provided in the package:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 10-57 V ⎓ DC;
- Ethernet port accepts 802.3af/at PoE 18-57 V ⎓ DC.
  The power consumption under maximum load can reach 10 W. Please attach ground (earth) wire to the screw under the bottom lid.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.
  The grounding screw is located under the bottom lid:

*[Figure]*

## Extension slots and ports

*[Figure]*

- Integrated two Wireless modules operating at 2.4 GHz and 5 GHz, supporting AP/CPE/P2P/repeater modes.
- Two 10/100/1000 Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.

## Configuration

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.

- Internet connection configuration <https://mt.lv/configuration>;
- Upgrade options for the RouterOS software <https://mt.lv/upgrade>;
  RouterOS includes many configuration options in addition to what is described in this document. We suggest visiting the RouterOS documentation page to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).
  It is possible to boot the device from a network, for reinstalling RouterOS for recovery purposes. This can be done from the first Ethernet port. See above how to do this.

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Datasheet for any device is available on the official manufacturer website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).

Please make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

## Accessories

*[Figure]*

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/wap-ac.md](../regulatory/wap-ac.md).
