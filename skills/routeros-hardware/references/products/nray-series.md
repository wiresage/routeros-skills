# nRAY series

> Source: https://manual.mikrotik.com/hardware/nray-series
>
> Category: 60 GHz products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/nray-series-8b1c8f47fdd8ce1e1b232581c0108acf.pdf).

### [Wireless Wire nRAY](https://mikrotik.com/product/wireless_wire_nray) (nRAYG-60adpair)

*[Figure]*

## Quickstart

Please follow these quick steps to set up your device:

- Unscrew the cover to reach the Ethernet port;
- Guide Ethernet cable through the opening;
- Plug into the Ethernet port and screw clockwise tightly, to ensure water protection;
- Connect the PoE injector into the computer;
- Connect the power adapter to the PoE injector;
- Download WinBox configuration tool <https://mt.lv/winbox>, or use Web browser;
- Default IP: `192.168.88.2` and `192.168.88.3`, user name: **admin**, and please find the password on the sticker;
- By default devices are configured as W60G Bridge;
- Once connected, configure the device, so it has an active Internet connection <https://mt.lv/configuration>, or proceed to the next step to upgrade software manually;
- Upgrade the RouterOS software to the latest version <https://mt.lv/upgrade>;
- Connect again and choose your Region, this can be done in the Wireless menu W60G tab;
- Double click on the W60G interface, go to the Wireless tab and choose your Region;

## Powering

The device accepts power 802.3af/at PoE in 12 – 57 V DC ⎓.
The power consumption under maximum load can reach 6 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Mounting

The device is designed to be used outdoors and mounted on the pole.
When mounting, please ensure that the drain hole is pointing downwards.
The IP rating scale of this device is IP54. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 60 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.
*The mounting and configuration of this device should be done by a qualified person.*

- Assemble the device with a mounting bracket.
  *[Figure]*
- Use M5 screws to fix the mounting bracket, tighten it with the HEX3 tool - not provided in the package.
- Insert U bolt. In the sequence as it is shown in the picture.
  *[Figure]*
- Attach the assembly to the pole.
  *[Figure]*
- Add mount bracket and use two 13 mm nuts to secure the device.
  *[Figure]*

## Aim tool usage

*[Figure]*

The device has led arrows on the back of the unit. Aim using the to reach precise alignment.

*[Figure]*

The arrows will light up and show the direction where to turn the unit. The goal is to reach the 0.4 - 0.8 degree range, where the signal is at its peak.

## Grounding

The installation infrastructure (towers and masts), must be properly grounded.
Please secure all loose Ethernet cables and antenna cables to the pole or mast approximately 30cm from the device, so that the cable weight is not pulling the ports and connectors.

## Configuration

We recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. Please make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). Seek additional help from your local trainers or become a trainer of yourself. <https://mikrotik.com/training/about>
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Notes

This device meets the Maximum TX power limit per ETSI regulations. An Operational mode in the 60 GHz band: 58.32 GHz, 60.48 GHz, 62.64 GHz, 64.80 GHz. This device is certified for outdoor use in Point to Multipoint applications. In the following countries this device cannot be used in Fixed Point-to-Point applications:

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/nray-series.md](../regulatory/nray-series.md).
