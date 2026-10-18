# wAP kit-series

> Source: https://manual.mikrotik.com/hardware/wap-kit-series
>
> Category: LTE products

> **This article covers**
>
> - **[wAP LTE kit](https://mikrotik.com/product/wap_lte_kit_2024)**
> - **wAP LTE kit US**
> - **wAP 4G kit**

This device needs to be upgraded to RouterOS v6.44.6 or the latest version to ensure compliance with local authority regulations.

It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

*[Figure]*

## Quickstart

- Use a Phillips head screwdriver to loosen the screw, which secures the bottom lid (see ).
- Insert the SIM card.
- Choose your powering solution, see the section for possibilities.
- Connect the Ethernet cable to the PoE and connect the other end of the Ethernet cable to this MikroTik router. Plug the provided power supply into the PoE injector.
- Wireless AP mode is enabled by default, you can connect from your computer to the SSID that begins with "MikroTik". The configuration interface is available via a web browser. The address is <https://192.168.88.1>.
- Connect to the wireless network, open <https://192.168.88.1> in your web browser to start the configuration.
- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen (or, for some models, check user and wireless passwords on the sticker).
- Select the "Check for updates" button on the right side and update your RouterOS software to the latest version to ensure the best performance and stability. Must have a valid SIM card inserted.
- To personalize your wireless network, SSID can be changed in the fields "Network Name";
- Choose your country on the left side of the screen in the field "Country", to apply country regulation settings.
- Set up your wireless network password in the field "WiFi Password" the password must be at least eight symbols.
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to login next time.
- Select the "Apply Configuration" to save changes.
- To manually update the device if no Internet connection is available.
- Download the latest RouterOS software from <https://mikrotik.com/download>.
- Choose MIPSBE packages, and save them to your PC.
- Connect again and in **Files** menu upload downloaded packages.
- Restart the device.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Select Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Powering

**PoE Input**

The ethernet port accepts 9-30 V passive PoE power. The box contains a 24 V adapter and a PoE injector. Plug the
included PoE injector into the first or internet port of the router that you will use in your LAN (or directly into your
laptop) and attach an ethernet cable to the PoE injector. Connect the other end of this ethernet cable to the wAP
LTE device. Plug the power supply into the PoE injector

**Power jack**

The DC jack (5.5 mm outside and 2 mm inside diameter, female, pin positive plug) supports 9-30 V power, the
the device comes with a 24 V 1.2 A power adapter

**Automotive connector**

The automotive connector can be used to power the device from regular 12/24 V connections in automobiles and
buses. The plug has four pins: bottom left (black) is the ground, bottom right is power in (red). The upper two are
reserved for future use.
Maximum power consumption at 24 V is 6 W without miniPCIe, and 8 W with a full load on the miniPCIe card.

## Mounting

The device can be mounted in several ways: pole, wall, ceiling or it can be placed in specially designed MikroTik holder which comes with the package. The package also includes a drill hole template with detailed mounting instructions, to help you with the Ethernet cable installation and attachment to a ceiling or a wall. Steel bracket to put on the other side of a dropdown ceiling tile and two screws and wall anchors. Zip ties or steel clamps for mounting on the pole.
The IP rating scale for this device is IP54. When mounting outdoors, ensure that any cable openings are directed downwards. You should use the POE injector and proper grounding with Cat6 shielded cable. When using and installing this device pay attention to Maximum Permissible Exposure (MPE) safety distance with a minimum of 35 cm between the radiator and your body. **Mounting on the mast or pole:**

*[Figure]*

** It's recommended to use electrical tape to increase friction between materials.*

- Mount plastic tie straps to steel brackets guiding them through holes.
- Mount bracket to the device.
- Secure them with a screw.
- Mount and align the device on the pole or mast.
- Guide Ethernet cable through the opening and connect to the Ethernet port.
- Close bottom latch and secure with a screw.

It's recommended to secure Ethernet cable to the pole using zip ties. With the distance from the device approximately 38 cm.

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
  150

## Bottom Lid

- The bottom lid is secured in place with the captive screw.
- Use the Philips PH2 screwdriver to unscrew it, but do not remove the screw completely.

*[Figure]*

- Pull the cover in the opposite direction from the device to remove it.

*[Figure]*

- Reassemble.

## Extension slots and ports

- Built-in 2 GHz wireless access point module, AP/station/bridge/p2p modes are supported.
- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straightor crossover cable can be used for connecting to other network devices. The ethernet port accepts 9-30 VDC powering from a passive PoE injector.
- miniPCIe slot and SIM slot (can’t be used separately) to be used with a 3G/4G/LTE modem (some kitsinclude it).

## MiniPCIe slot usage

The device is equipped with a miniPCIe slot (a kit with preinstalled modem also available) to be used with a
3G/4G/LTE modem. A SIM slot is provided for use together with a miniPCIe modem. SIM slot is not used
separately.
To install the miniPCIe module, remove both screws below the power jack and slide out the wAP PCB board. Insert
the miniPCIe modem, and secure it with two Philips screws which are already in place.
Attach the grey uFL connector to the MAIN antenna connector of the modem, attach the black cable to the other (or
AUX) connector. It is possible to use external antennas for the modem, two SMA mounting holes are provided next
to the reset button, or if you prefer to attach antennas to the case directly, SMA antennas can be mounted on the
bottom of the case if you remove the two plastic hole covers first.
After you have reinserted the wAP board into the case and secured it with the screws that were removed earlier,
slide in the SIM card from your mobile operator into the SIM slot, with the chip facing up. The slot accepts miniSIM
(2FF). The SIM slot protects the SIM card from falling out with a plastic latch. You can press the latch and then pull
the SIM out using tweezers or a similar tool.

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Configuration

You should select the "Check for updates" button and update your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest visiting the RouterOS documentation page to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).
It is possible to boot the device from a network, for reinstalling RouterOS for recovery purposes. This can be done from the first Ethernet port. See above how to do this.

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

make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/wap-kit-series.md](../regulatory/wap-kit-series.md).
