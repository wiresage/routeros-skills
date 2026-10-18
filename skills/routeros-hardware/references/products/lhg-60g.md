# LHG 60G

> Source: https://manual.mikrotik.com/hardware/lhg-60g
>
> Category: 60 GHz products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/lhg-60g-d834c6f77e358b33f6d3fd47663765b4.pdf).

*[Figure]*

The LHG 60G device works in the 60 GHz wireless spectrum, the operating temperature of these devices is from -40°C up to +70°C. Each device has one gigabit Ethernet port and can be powered with PoE.

## Quickstart

- Assemble unit. Please see the (link)
  The device includes a grounding connection (marked ⏚) which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage. Grounding connector included in the package.

Warning! This equipment should be installed and operated with a minimum distance of 95 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.
The IP rating scale for this device is IP54.
*Mounting and configuration of this device should be done by a qualified person.*

## Extension slots and ports

- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- WiGig, 802.11ad.

## Powering

The devices accept powering from the Ethernet port. The Ethernet port accepts PoE input 12-57 V DC (passive and 802.3af/at). A power adapter and a passive PoE injector are included in the box. When using the PoE injector, make sure to use the "Power + Data" connector to connect to the device, and the "Data" connector to your PC, router or switch.
**Connecting to a POE Adapter:**

- Connect the Ethernet cable from the device to the POE+DATA port of the POE adapter.
- Connect an Ethernet cable from your local network (LAN) to the POE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.
  Maximum power consumption 5 W.

## Configuration

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case the IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side.
Please get yourself familiar with additional information on the [W60G interface](https://manual.mikrotik.com/docs/wireless/w60g/).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Buttons and jumpers

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
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

Package includes the following accessories that come with the device:

- K-LHG screw set/fastening set.
- Gigabit POE injector.
- LHG-5G-390 mm Dish (mesh size 0.5 t x1.0 wx1.4 mm ).
- EU/US Switching Power Supply 24 V ⎓, 0.38 A, 9 W, Level VI, cable:1.5 m.
- Hose Clamp SUS304 (Philips type; clamping diameter range 35-70 mm).
- BRAC1_ LHG montage element.
- DynaDish U-Bolt M8 (A2 Stainless Steel).
- QuickMount AIM.

## Specifications

For more information about LHG products, specifications and pictures please visit our web page: <https://mikrotik.com/product/lhg_60g>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point. Scan QR code and choose your preferred OS.

*[Figure]*

*[Figure]*

This device meets the Maximum TX power limit per ETSI regulations. The frequency and the maximum transmitted power in EU are listed below: 57-66GHz: 34.92 dBm. An Operational mode in the 60 GHz band: 58.32 GHz, 60.48 GHz, 62.64 GHz. This device is certified for outdoor use in Point to Multipoint applications. In the following countries this device cannot be used in Fixed Point-to-Point applications:

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/lhg-60g.md](../regulatory/lhg-60g.md).
