# LtAP mini kit-series

> Source: https://manual.mikrotik.com/hardware/ltap-mini-kit-series
>
> Category: LTE products

> **This article covers**
>
> - **[LtAP mini LTE kit](https://mikrotik.com/product/ltap_mini_lte_kit_2024)** (RB912R-2nD-LTm&R11e-LTE)
> - **LtAP mini LTE kit-US** (RB912R-2nD-LTm&R11e-LTE-US)
> - **LtAP mini 4G kit** (RB912R-2nD-LTm&R11e-4G)

The LtAP mini LTE kit is a wireless access point with two SIM card slots. The LtAP mini LTE, 4G kit comes with a factory-installed card.

## Connecting

- Connect your Internet cable to the Ethernet port (this is optional if using LTE as the primary connection);
- Install your modem using miniPCIe slot (optional);
- Insert the SIM card into the SIM slot;
- Connect the GPS antenna (see "", optional);
- Choose your powering solution (see "");
- Navigate to the network connections section on your computer and locate the wireless network named "*MikroTik-....*". Proceed to connect to it;
- Configuration should be made via a wireless network using a web browser or mobile application. Alternatively, you can use the WinBox configuration tool <https://mt.lv/winbox> Open the <https://192.168.88.1> in your web browser;
- User name: **admin**, and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Select the "Check for updates" button and update RouterOS to the latest version. The device requires an active internet connection;
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the **WinBox** **Files** menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the **QuickSet** menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Mounting

*[Figure]*

- It is possible to attach the device to a wall, using the provided screw holes on the sides of the unit. The device should be mounted in a way that the cable openings are pointing downward as shown in the picture.
- The ports are protected with a small door, that is held in place with one screw. Use the Philips PH2 screwdriver to access the ports.
- The door has cut-out places for all available ports, but only break out the openings that you will use. The device can be used both indoors and outdoors. The IP rating scale for this device is IP54.
- The device enclosure has places where you can drill openings for external LTE and GPS antennas. Use a drill to make holes that are appropriate for the antenna cable used.
  Alternatively, you can obtain a "DINrail Pro" - mounting bracket, designed to fit standard 35 mm x 7.5 mm DIN rails. <https://mikrotik.com/product/dinrail_pro>

When mounting outdoors, ensure that any cable openings are directed downwards. Use a PoE injector and proper grounding. Recommended using Cat6 cable.
*Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.*
*Mounting and configuration of this device should be done by a qualified person.*

## Powering

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin-positive plug) accepts 8-30 V DC.
- micro USB port accepts 5 V powering.
- Ethernet port accepts passive and 802.3af/at Power over Ethernet 8-57 V DC (compensate for the loss on cable, so more than 12 V recommended).
  The power consumption under maximum load with attachments can reach 9 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Extension slots and ports

*[Figure]*

- Built-in 2 GHz wireless access point module, AP/station/bridge/p2p modes are supported. Onboard PIF antennas built-in. Antenna gain1.5 dBi.
- miniPCIe slot and two SIM slots (can't be used without a modem installed, can't be used both at the same time) to be used with a 3G/4G/LTE modem. Onboard antennas are available, but openings for external antennas are provided on the case.
- Built-in GPS module - uFL connector provided for an external antenna. To enable, set the port to serial0 (this disables the DB9 port on the unit). Supports (GPS, GLONASS, BeiDou, Galileo).
- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices. The Ethernet port accepts 12-57 V DC powering from a passive PoE injector.
- One DB9 RS232 serial port for serial console access. Configured as 115200 bit/s, 8 data bits, 1 stop bit, no parity. Can't be used if built-in GPS is enabled on serial0.
- One micro USB 2.0 port for powering only.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).
For recovery purposes, it is possible to boot the device from the network, see section .

## miniPCIe slot usage

The device is equipped with a miniPCIe slot and a factory-installed LTE modem. Two SIM slots are provided for use together with a miniPCIe modem. The SIM slot is not used separately.

In this case, an internal antenna is connected to the modem. Replacing a miniPCIe module should be done by a qualified person, follow safety precautions when handling electrical equipment:- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.

- Open the front cover by unscrewing one screw with the Philips PH2 screwdriver.
- Remove four screws on the bottom of the case and lift off the top part of the case. You will see the antenna attached to it.
- Locate the miniPCIe card on the PCB and remove two screws.
- Attach provided a thick thermal pad to the card, and install the card into miniPCIe slot so that the thermal pad is between PCB and card.
- The secure card in place using previously removed two screws.
- Attach the grey uFL connector to the MAIN antenna connector of the modem, and attach the black cable to the secondary (or AUX) connector.
- To use external antennas (not included), attach antenna connectors and use a 6.5 mm drill bit to drill holes on the side of the unit. (see "") description 4.
- see the picture below on how to place rubber seals for the best water protection.

*[Figure]*

- Attach antenna connectors to the installed card and GPS connector on the PCB, as additional rubber silicone can be used to secure connectors in place on the card and PCB board.

*[Figure]*

Attach a thinner thermal pad to the top of the card.

- Reassembly.
  After you have reinserted the device into the case and secured it with the screws that were removed earlier, slide in the SIM cards from your mobile operator into the SIM slots, with the chips facing as shown on the port label. The slot accepts miniSIM (2FF). Close the black latch for SIM cards, to secure them in the slots.

## GPS usage

In order to use GPS, an external antenna is needed to connect.
Use the "ACGPSA" - can be obtained separately. ACGPSA is a standalone active GPS antenna, that works in the 1575.4 MHz spectrum. Antenna size is 46.5 mm x 26.5 mm x 12.5 mm with an IP67 rating and includes an internal magnet and double-sided tape, so it can easily be attached to various surfaces. It has a long 5m cable with an SMA connector, to be connected to LtAP mini via the ACSMAUFL pigtail (not included, product code ACSMAUFL)
<https://mikrotik.com/product/acgpsa>
<https://mikrotik.com/product/acsmaufl>
To connect a GPS antenna, see "miniPCIe slot usage" step 10.
**Supports - GPS, GLONASS, BeiDou, Galileo).**

Configuration information: [GPS basic examples](https://manual.mikrotik.com/docs/mobile-networking/gps#basic-examples).

The GPS uses an active antenna, connect only when power is turned off.

## Buttons and jumpers

### Reset button

- Hold this button during boot time until the LED light starts flashing, and release the button to reset the RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, the LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or keep holding the button for 5 more seconds until the LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

### Mode button

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. The mode button can be configured in RouterOS menu /system routerboard mode-button

## Accessories

Package includes the following accessories that come with the device:

- DC ⎓ Switching Power Supply 24 V, 1.2 A, 28.8 W, 86.8 %, VI, cable:220 cm RA DC.
- Cable DC ⎓ plug RA 5.5x2.1x10.5 to Striped 2*24 AWG Tin 8 mm, length 0.35 m.
- PoE Injector with shielded Ethernet cable/connector (RBPoE).
- DC ⎓ 24 V 1.2 A power adapter.
- Mounting kit K-55 VMS.
- Elastic thermal pad, 25x40x3.5 mm.

## Specifications

For more information about this product, specification, and pictures visit our web page: {+}<https://mikrotik.com/product/ltap_mini_lte_kit>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Select Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ltap-mini-kit-series.md](../regulatory/ltap-mini-kit-series.md).
