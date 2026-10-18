# Cube Lite60

> Source: https://manual.mikrotik.com/hardware/cube-lite60
>
> Category: 60 GHz products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/cube-lite60-4d7ed9c7f2202d7a7a4f5a01d2a625ea.pdf).

The Cube Lite60 is an outdoor wireless router with a built-in directional antenna that works in the 60 GHz spectrum.
This device needs to be upgraded to RouterOS v6.46 or the latest version to ensure compliance with local
authority regulations.

It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

## Quickstart

- Open the Ethernet door to connect an Ethernet cable to the Ethernet port, connect the other end of the Ethernet cable to the included PoE injector;
- Plug the PoE injector into your network switch or computer;
- Plug the included power supply into the PoE injector to start up the device;
- Set LAN computer IP configuration to automatic (DHCP);
- The default IP address of the unit is `192.168.88.1`, open this address in your web browser to start the configuration;
- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen (or, for some models, check user and wireless passwords on the sticker);
- We recommend clicking the "Check for updates" button on the right side and updating your RouterOS software to the latest version to ensure the best performance and stability;
- To personalize your wireless network, SSID can be changed in the fields "Network Name";
- Choose your country on the left side of the screen in the field "Country", to apply country regulation settings;
- Set up your wireless network password in the field "WiFi Password" the password must be at least eight symbols;
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to login next time;
- Click on the "Apply Configuration" to save changes.
  *If device RX blocking condition has happened device will restore its signal after a few seconds.*

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

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network (see ).
If the device loses connection, wait for few seconds and then the device will recover connection automatically.

## Assembly and mounting

The device can be mounted on the vertical or horizontal pole as shown in picture A and B. Please note that a device needs to be mounted with bottom latch facing down. The maximum pole diameter is 51 mm.

Mounting and configuration of this device should be done by a certified person.

Choose your desired position, the device will require precise adjustment for best performance.

- Attach provided mount to the back of the device with provided screws using a ph0 screwdriver.
- Mount on pole with U bolt bracket using 8 mm ratchet.
- Place a bolt in one of the three positions, they will allow for fine adjustment, when placed in the middle you can adjust in 23-degree range if an adjustment needs to go further replace the screw in a different position.

*[Figure]*

The IP rating scale for this device is IP54. When mounting outdoors, please ensure that any cable openings are directed downwards. We recommend using the POE injector and proper grounding with Cat6 shielded cable. When using and installing this device please pay attention to Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

Alternatively, the device can be mounted on one of the three mounting slots on the backside of the device.

*[Figure]*

*[Figure]*

- You can use a metal ring for example.
- Use a Phillips screwdriver to loosen the metal ring.
- Slide one end of it through the most convenient of the three mounting slots.
- Position the device on the pole where it will be mounted.
- Slide the loose end of the mounting ring back to its closing latch and use the screwdriver to tighten it.

It's recommended to secure Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.

As an additional option, you can use "quickMOUNT-X" – mounting bracket for an easy adjustment that can be obtained separately. Product web page: <https://mikrotik.com/product/qm_x>

*[Figure]*

Specially designed enables vertical and horizontal adjustment on the pole.

## Grounding

The device includes a grounding connection (marked ⏚) which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage.

## Powering

The Cube Lite60 accepts DC ⎓ power from Passive PoE injectors (one power supply and PoE injector are included) accepts 12-28 V DC ⎓ consuming at maximum load 4 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Extension slots and ports

- 10/100 Ethernet port.
- Integrated w60g interface with built-in antenna.

## Reset button

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24V DC ⎓, 0.38 A, 9 W, Level VI, cable:1.5 m.
- POE Injector with shielded ethernet cable/connector (RBPOE).
- SXT_SQ_Mountv1.
- K-70 Fastening set.

## Specifications

For more information about SQ series products, specifications, pictures, downloads, and test results please visit our web pages: <https://mikrotik.com/product/cube_lite60>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

This device meets the Maximum TX power limit per ETSI regulations. The frequency and the maximum transmitted power in EU are listed below: 57-66GHz: 34.92 dBm. An Operational mode in the 60 GHz band: 58.32 GHz, 60.48 GHz, 62.64 GHz, 64.80 GHz. This device is certified for outdoor use in Point to Multipoint applications. In the following countries this device cannot be used in Fixed Point-to-Point applications:

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/cube-lite60.md](../regulatory/cube-lite60.md).
