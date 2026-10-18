# wAP-series

> Source: https://manual.mikrotik.com/hardware/wap-series
>
> Category: Indoor wireless

> **This article covers**
>
> - **wAP**
> - **wAP BE**

*[Figure]*

## Quickstart

- Use a Phillips head screwdriver to loosen the screw, which secures the bottom lid;
- Choose your powering solution, please see the section for possibilities;
- Plug the included PoE injector into the ISP outlet and attach an Ethernet cable to it. Connect the other end of the Ethernet cable to this MikroTik router. Plug the provided power supply into the PoE injector;
- Wireless AP mode is enabled by default, you can connect from your computer to the SSID that begins with "MikroTik". The configuration interface is available via a web browser. The address is <https://192.168.88.1>;
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start the configuration;
- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen (or, for some models, check user and wireless passwords on the sticker).;
- We recommend clicking the "Check for updates" button on the right side and updating your RouterOS software to the latest version to ensure the best performance and stability;
- To personalize your wireless network, SSID can be changed in the fields "Network Name";
- Choose your country on the left side of the screen in the field "Country", to apply country regulation settings;
- Set the *Installation* to indoors or outdoors, depending on the usage type;
- Set up your wireless network password in the field "WiFi Password" the password must be at least eight symbols;
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to login next time;
- Click on the "Apply Configuration" to save changes.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Mounting

The device can be mounted in several ways: wall, ceiling, pole or it can be placed in specially designed MikroTik holder which comes with the package. The package includes a drill hole template with instructions, to help you with the Ethernet cable installation and attachment to a ceiling or a wall. The package also includes a steel bracket to put on the other side of a dropdown ceiling tile and two screws and wall anchors. The Unit can be attached to the pole using zip ties or steel clamp.
To prevent the bottom lid for opening the different screw can be used. One Torx T20 security screw is included for optional use. Use it with the included L-shaped wrench to fix it into the bottom lid. Detailed instructions of replacing the screw are in the package.
The IP rating scale for this device is IP54.
When mounting outdoors, please ensure that any cable openings are directed downwards. Use POE injector and proper grounding. Recommended using Cat5/6 cable.
When using and installing this device please pay attention to Maximum Permissible Exposure (MPE) safety distance with a minimum of 35 cm between the radiator and your body.

**Mounting on the mast or pole:**

*[Figure]*

** It's recommended to use electrical tape to increase friction between materials.*

- Mount plastic tie straps to steel bracket guiding them through holes.
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
  Avoid mounting the device on the low ground spot, as you won't be able to attach and close the bottom latch.

**Mounting on the ceiling:**

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

## Powering

The device accepts power from the power jack or from the Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 11-57 V ⎓ DC;
- Ethernet port accepts 802.3af/at PoE 11-57 V ⎓ DC.
  The power consumption under maximum load can reach 4 W. Please attach ground (earth) wire to the screw under the bottom lid.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Extension slots and ports

- Wireless module 2.4 GHz 802.11b/g/n.
- One 10/100 Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.

## Configuration

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest visiting the RouterOS documentation page to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).
It is possible to boot the device from a network, for reinstalling RouterOS for recovery purposes. This can be done from the first Ethernet port. See above how to do this.

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/wap-series.md](../regulatory/wap-series.md).
