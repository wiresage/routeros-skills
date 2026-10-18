# RB5009UPr+S+OUT

> Source: https://manual.mikrotik.com/hardware/rb5009upr-plus-s-plus-out
>
> Category: Ethernet routers

*[Figure]*

An outdoor version of our best-selling heavy-duty PoE router. Extensive power redundancy for the best price! 7x Gigabit Ethernet ports, 1x 2.5 Gigabit Ethernet, 10G SFP+, 1GB of RAM, 1GB NAND, modern quad-core CPU, 9 (!) powering options, durable IP66 waterproof enclosure. See the [RB5009UPr+S+OUT product page](https://mikrotik.com/product/rb5009_out) for full specifications and brochures.

## Setup

- Make sure your ISP is allowing hardware change and will automatically issue an IP address.
- Connect your ISP cable to the first Ethernet port.
- Connect your PC to any of the Ethernet ports.
- Connect the device to the power source.
- Use a Web browser or WinBox to connect to the default IP address of 192.168.88.1 from any port, with the username **admin** and no password (or, for some models, check user and wireless passwords on the sticker).
- If IP is not available, download WinBox from our webpage and use it to connect through MAC address.
- Update RouterOS software to the latest version, and make sure that the device has an internet connection.
- If the device does not have an internet connection update software by downloading the latest version from our webpage <https://mikrotik.com/download>
- Find the latest software and choose your packages.
- To get the architecture type of your device model, open WinBox, WebFig go to (System/Resources).
- Download packages to the PC and upload them to the WinBox, WebFig, (Files) menu, and reboot the device.
- Set up your password to secure the device.

## Powering

- PoE-in 802.3af/at
- PoE-Out 802.3af/at the Same voltage as supplied via 2-pin terminal - Passive PoE or
- 802.3af/at Compatible (if 44–57V PSU used)
- PoE-Out ports Ether1 - Ether8, max out per port output (input < 30 V): 620 mA, max out per port output (input > 30 V): 420 mA
- Smart PoE Controller
- Max total out 2.59 A
- Total output power 130 W
- Total output current 2.28 A
- Number of DC inputs 2
- Supported input voltage 24-57 V (PoE in) 24-57 (2-pin terminal)
- Max power consumption (without attachments) 15 W
- Max power consumption 150 W
- 2-pin terminal specifications: Connector Plug P=5.08mm 1x2pin RA TH Tin plated 300V 10A

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mounting

250
We recommend Cat6 cables for our devices.
*The mounting and configuration of this device should be done by a qualified person, to comply **IP66** class please observe the strict procedures for mounting instructions.

## Extension slots and ports

- 4RB5009UPr+S+OUT
- Product code RB5009UPr+S+OUT
- CPU Quad-Core 88F7040 1.4 GHz
- CPU architecture ARM 64bit
- Size of RAM 1 GB
- RAM type DDR4
- Storage 1 GB, NAND
- Number of 1G Ethernet ports 7
- Number of 2.5G Ethernet ports 1
- Number of 10G SFP+ ports 1
- USB 1 USB 3 type A
- Operating system RouterOS v7, License level 5
- Switch chip model 88E6393
- Dimensions 222 x 239 x 57 mm
- Operating temperature -40°C to +70°C

## Buttons and jumpers

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset the RouterOS configuration to defaults.
- Release the button after the LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## LED

- Hidden Green LED behind the Reset button is a USER LED
- Blue LED 1 is the DC1 Power LED
- Blue LED 2 is the DC2 Power LED
- Green SFP+ LED is an SFP+ port link and activity LED
- Ethernet RJ45 Green LEDs are Ethernet port link and activity LEDs
- Ethernet RJ45 Port 1 Orange LED is PoE-in status LED
- Ethernet RJ45 Port 2-8 Orange LEDs are unused on this model

## Accessories

The package includes the following accessories that come with the device:

*[Figure]*

See the [MikroTik wired interface compatibility](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb5009upr-plus-s-plus-out.md](../regulatory/rb5009upr-plus-s-plus-out.md).
