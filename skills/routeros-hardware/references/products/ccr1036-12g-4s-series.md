# CCR1036-12G-4S-series

> Source: https://manual.mikrotik.com/hardware/ccr1036-12g-4s-series
>
> Category: Ethernet routers

*[Figure]* *[Figure]*

> **This article covers**
>
> - **CCR1036-12G-4S-EM**
> - **CCR1036-12G-4S**

## First use

The device comes preinstalled with RouterOS and is ready to use. The ETH1 port has a default IP address for connecting: 192.168.88.1. The username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker). Please connect with your web browser to this IP address and choose WebFig to configure it. In case the IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device.
The device doesn't have any other configuration or firewall rules applied by default, please connect to it, and set up IP addresses, users, passwords, firewall, etc. Please ensure you have prevented unauthorized access from public networks by use of the firewall filters and restrictions available in the IP services menu in RouterOS. Detailed info on how to upgrade the device <https://mt.lv/upgrade>;
See this page for connection and configuration guides: +<https://mt.lv/help##> Powering
The device accepts powering from two redundant power supplies, each accepts 100-240 V AC power. You can use either, or both at the same time. Up to 60 W power consumption.

## Extension slots and ports

- 12x 10/100/1000 Ethernet ports.
- 4x SFP cage
- USB 2.0 type A
- One M.2 slot, type PCIe x4
- RJ45 console port***Etherboot / Netinstall is available on port ETH12.***

Recommended are M.2 PCIe NVMe 2280mm M key SSD disks with a capacity of up to 1TB.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

*[Figure]*

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
  *The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.* *We recommend shielded Cat5/6 cables for our devices.* *Mounting and configuration of this device should be done by a qualified person.*

## Buttons and jumpers

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.
  The Mode button is not functional by default but can be assigned any script in the menu /system routerboard mode-button

## LEDs

The device has four LED lights. PWR1/2 indicates which power supply is being used. FAULT indicates a problem with the cooling fans. USER can be configured in software.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

*[Figure]*

Safety Notice
Electric shock hazard. This equipment is to be serviced by trained personnel only. This is a class A device, operating it near residential radio equipment could cause radio interference.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ccr1036-12g-4s-series.md](../regulatory/ccr1036-12g-4s-series.md).
