# Wireless Wire Dish

> Source: https://manual.mikrotik.com/hardware/wireless-wire-dish
>
> Category: 60 GHz products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/wireless-wire-dish-0b7f9054624012522cbc79e78af307a1.pdf).

*[Figure]*

The Wireless Wire Dish is a set of two LHG 60G devices that work in the 60 GHz wireless spectrum. Factory configured in pairs for an easy first start.

## Quickstart

- Assemble unit;
- Open the Ethernet door to connect an Ethernet cable to the Ethernet port, connect the other end of the Ethernet cable to the included PoE injector;
- Plug the PoE injector into your network switch;
- Plug the included power supply into the PoE injector to start up the device;
- Mount the devices on the mast or pole;
- Align both units;
- Download WinBox configuration tool <https://mt.lv/winbox> Default IP for the master unit: `192.168.88.2`, slave unit: `192.168.88.3`, user name: **admin** and password is printed on the label, that can be found inside the device cover;
- In case the IP connection is not available, please use the Neighbors tab and connect through MAC address;
- For LHG 60G models, the default IP: `192.168.88.1`, and there is no password;
- Once connected configure the device, so it has an active Internet connection <https://mt.lv/configuration>;
- Upgrade the RouterOS software to the latest version <https://mt.lv/upgrade>;
- Choose your country, to apply country regulation settings.

## Assembly

- Attach the two legs to the LHG case.
- Snap the assembled LHG unit to the grid in the appropriate locations.
- Fix the legs in place with two self thread screws (Use Phillips screwdriver PH2).

*[Figure]*

## Mounting

*[Figure]*

- Attach the mounting assembly to the back of the device with four provided screws.
- Mount the assembled unit to the pole using the provided U bolt clamp. The clamping diameter with the provided steel clamp is 35 – 70 mm.

*[Figure]*

- Use the Aim tool to adjust your device. Please see the section (link)

*[Figure]*

The device includes a grounding connection (marked ⏚) which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage. Grounding connector included in the package.

Warning! This equipment should be installed and operated with a minimum distance of 95 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.
The IP rating scale for this device is IP54.
*Mounting and configuration of this device should be done by a qualified person.*

## Extension slots and ports

- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- WiGig, 802.11ad.

## Powering

The devices accept powering from the Ethernet port. The Ethernet port accepts PoE input 12-57 V DC (passive and 802.3af/at). A power adapter and a passive PoE injector are included in the box. When using the PoE injector, make sure to use the "Power + Data" connector to connect to the device, and the "Data" connector to your PC, router, or switch.
**Connecting to a POE Adapter:**

- Connect the Ethernet cable from the device to the POE+DATA port of the POE adapter.
- Connect an Ethernet cable from your local network (LAN) to the POE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.
  Maximum power consumption 5 W.

## Configuration

Full RouterOS documentation is located here: <https://mt.lv/help> Devices included in the Wireless Wire dish kit have been preconfigured with 60GHz and Ethernet interfaces in bridge mode. Another configuration has to be applied according to the documentation manual linked above.
Connect each of the Wireless Wire dish devices to your network using an Ethernet cable. To be able to communicate between these networks, devices have to be pointed at each other and be in direct line of sight. Once connected the devices will automatically bridge both networks.
Please get yourself familiar with additional information on the [W60G interface](https://manual.mikrotik.com/docs/wireless/w60g/).
Access devices by Ethernet cable, using the MikroTik WinBox utility. WinBox should be used to connect to the default IP address of 192.168.88.2 for the master device and 192.168.88.3 for the slave device. Username for login is admin and password is printed on the label that can be found inside the device cover.
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Buttons and jumpers

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, resets to password-protected state (~5 seconds)
- Release the button when the LED turns solid green to clear all configuration (~10 seconds)
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## LED status

The device includes precise alignment guides using LEDs. The lights indicate with arrows direction to turn the dish if looking from behind the dish to the other end of the link. When alignment LEDs turn off, leaving only the "link established" LED, it means alignment is complete. The LED lights are:

*[Figure]*

- Tilt-up.
- Tilt down.
- Rotate to right.
- Rotate to left.
- LED on when the link established.
- LED on when Ethernet connected.
- User-configurable LED.
- Power state on.

## Accessories

The package includes the following accessories that come with the device:

- K-LHG screw set/fastening set.
- Gigabit POE injector.
- LHG-5G-390 mm Dish (mesh size 0.5 t x1.0 wx1.4 mm ).
- EU/US Switching Power Supply 24 V ⎓, 0.38 A, 9 W, Level VI, cable:1.5 m.
- Hose Clamp SUS304 (Philips type; clamping diameter range 35-70 mm).
- BRAC1_ LHG montage element.
- DynaDish U-Bolt M8 (A2 Stainless Steel).
- QuickMount AIM.

## Specifications

For more information about LHG products, specifications and pictures please visit our web page: <https://mikrotik.com/product/wireless_wire_dish>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point. Scan QR code and choose your preferred OS.

*[Figure]*

*[Figure]*

This device meets the Maximum TX power limit per ETSI regulations. An Operational mode in the 60 GHz band:58.32 GHz, 60.48 GHz, 62.64 GHz. This device is certified for outdoor use in Point-to-multipoint applications. In the following countries, fixed service is allowed only in part of the band:

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/wireless-wire-dish.md](../regulatory/wireless-wire-dish.md).
