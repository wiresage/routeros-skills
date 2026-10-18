# CCR2004-16G-2S+

> Source: https://manual.mikrotik.com/hardware/ccr2004-16g-2s-plus
>
> Category: Ethernet routers

*[Figure]*

This powerful and affordable router crushes all previous CCR models in single-core performance. 16x Gigabit Ethernet ports, USB, 2x10G SFP+ cages, active cooling and the best single-core performance per watt & best overall performance per watt among all the CCR devices. See the [CCR2004-16G-2S+ product page](https://mikrotik.com/product/ccr2004_16g_2splus) for full specifications and brochures.

## Quickstart

- Connect your PC to the MGMT/BOOT port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Configuration should be made using WebFig in a web browser or the WinBox configuration tool <https://mt.lv/winbox> Open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Powering

*[Figure]*

The device has dual integrated power supply units AC **⏦** 100-240V with standard IEC compatible sockets with Maximum power consumption of 48 W.

## Specifications

- Product code CCR2004-16G-2S+
- CPU AL32400 1.7 GHz
- CPU architecture ARM 64bit
- CPU core count 4
- Size of RAM 4 GB
- RAM type DDR4
- Storage 128 MB, NAND
- Number of 1G Ethernet ports 16
- Number of 10G SFP+ ports 2
- Operating system RouterOS (License level 6)
- Switch chip model 88E6191X, 88E619X
- Dimensions 443 x 210 x 44 mm
- Operating temperature -20°C to +60°C

## Reset button

The reset button has two functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset the RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

*[Figure]*

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right;
- Place the device in rackmount enclosure and align with the holes so that the device fits conveniently;
- Tighten screws to secure it in place.
  The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment. We recommend Cat6 cables for our devices.

## Included Parts

*[Figure]*

- PLUG1-2_ EU/US power cord, JL3-JL38C (D03+QT3) H05VV-F 3x0.75mm2 1.83m
- SET1_ Fastening set K-57
- CASE3-4_ 1U rackmount bracket white

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ccr2004-16g-2s-plus.md](../regulatory/ccr2004-16g-2s-plus.md).
