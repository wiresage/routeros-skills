# wAP R ac

> Source: https://manual.mikrotik.com/hardware/wap-r-ac
>
> Category: LTE products

*[Figure]*

## [wAP R ac](https://mikrotik.com/product/wap_r_ac) (RBwAPGR-5HacD2HnD)

The wAP R ac is a small weatherproof device with integrated antennas and miniPCIe slot for your modem. See the [wAP R ac product page](https://mikrotik.com/product/wap_r_ac) for full specifications and brochures.

## Quickstart

- Use a Phillips head screwdriver to loosen the screw, which secures the bottom lid (see (link).
- SIM card slot.
- LED indicating a power state of the device.
- LED - user-defined.
- LED Indicating the activity of the LTE network.
- Plastic doors for SMA cables.
- MiniPCIe slot.
- Integrated Wireless module operating at 2.4 GHz, 802.11b/g/n and 5 GHz, 802.11a/n/ac protocol.

## Configuration

The device is configured as an AP router. Eth1 is blocked by the firewall, you can access router for configuration through the wireless interface.
You should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case the IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side. When using WinBox on login the default configuration settings will be shown.
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

*[Figure]*

## Operating system support

The device supports RouterOS software version v6. The specific factory-installed version number is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/wap-r-ac.md](../regulatory/wap-r-ac.md).
