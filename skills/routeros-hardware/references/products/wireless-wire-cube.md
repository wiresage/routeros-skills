# Wireless Wire Cube

> Source: https://manual.mikrotik.com/hardware/wireless-wire-cube
>
> Category: 60 GHz products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/wireless-wire-cube-341547731816889727201641e27bbc3a.pdf).

*[Figure]*

### [Wireless Wire Cube](https://mikrotik.com/product/wireless_wire_cube) (CubeG-5ac60adpair)

It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

## Quickstart

- Connect the device to the included PoE injector with Ethernet cable;
- Connect the PoE injector into the PC or to the network switch;
- Connect the power adapter to the PoE injector;
- Download WinBox configuration tool <https://mt.lv/winbox> Open WinBox and connect to the device;
- Default IP: `192.168.88.2`/`192.168.88.3`, user name: **admin**, please find the password on the sticker;
- Download the latest RouterOS software from <https://mikrotik.com/download>;
- Choose ARM packages, and save them to your PC;
- Open WinBox and upload downloaded packages, drag and drop into any windows;
- Restart the device;
- Connect again and select your Region in the Wireless menu, W60G tab, and in **QuickSet** menu set your Country, to apply country regulation settings.
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

The device can be mounted on the vertical or horizontal pole as shown in pictures A and B. Please note that a device needs to be mounted with the bottom latch facing down. The maximum pole diameter is 51 mm.

Mounting and configuration of this device should be done by a certified person.

Choose your desired position, the device will require precise adjustment for best performance.

- Attach provided mount to the back of the device with provided screws using a ph0 screwdriver.
- Mount on pole with U bolt bracket using 8 mm ratchet.
- Place a bolt in one of the three positions, they will allow for fine adjustment, when placed in the middle you can adjust in a 23-degree range if an adjustment needs to go further replace the screw in a different position.

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
- Integrated 5 GHz 802.11a/n/ac interface with built-in antenna.
- WiGig chipset QCA6335.

## Reset button

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24V DC ⎓, 0.8 A, 9 W, Level VI, cable:1.5 m.
- POE Injector with shielded ethernet cable/connector (RBPOE).
- Cube mount.
- K-70 Fastening set for Cube mount.

## Operating system support

The device supports RouterOS software version *v6.47.2.* The specific factory-installed version number is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

## Notes

This device meets the Maximum TX power limit per ETSI regulations. The frequency and the maximum transmitted power in the EU are listed below: 57-66GHz: 34.92 dBm. An Operational mode in the 60 GHz band: 58.32 GHz, 60.48 GHz, 62.64 GHz. This device is certified for outdoor use in Point to Multipoint applications. In the following countries this device cannot be used in Fixed Point-to-Point applications:

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/wireless-wire-cube.md](../regulatory/wireless-wire-cube.md).
