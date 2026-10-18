# RB5009UPr+S+IN

> Source: https://manual.mikrotik.com/hardware/rb5009upr-plus-s-plus-in
>
> Category: Ethernet routers

*[Figure]*

A new version of our popular heavy-duty RB5009 router with PoE-in and PoE-out on all ports. Perfect for small and medium ISPs. 2.5 Gigabit Ethernet & 10 Gigabit SFP+, numerous powering options. See the [RB5009UPr+S+IN product page](https://mikrotik.com/product/rb5009upr_s_in) for full specifications and brochures.

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

The power consumption under maximum load can reach 150 W. The device accepts power from the power jack, 2-pin terminal, or from any Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin-positive plug) accepts 24-57 V DC.
- The **Ethernet ports** accept Power over Ethernet 24-57 V DC, **802.3af/at -**802.3af/at (ether1), Mode B (ether2-ether8).
- 2-pin terminal input Voltage 24-57 V DC.
- PoE-Out ports Ether1 - Ether8, max out per port output (input < 30 V): 640 mA, max out per port output (input > 30 V): 440 mA.
- Max total out 2.59 A.
- Total output power 130 W.
- Total output current 2.28 A.
- 2-pin terminal specifications: Connector Plug P=5.08mm 1x2pin RA TH Tin plated 300V 10A
  Mode B: **Ethernet port 2 - 8**.
  Pins 4 & 5 = DC+
  Pins 7 & 8 = DC-

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mounting

The device is designed to use indoors and it can be mounted on the wall, or it can be placed on the desktop.

*[Figure]*

- Find the designed mounting holes on both sides of the device, as shown in the picture;
- Use provided screws to secure the device to the wall;
- Based on the wall material you can use a drill bit and provided dowels.
  The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
  We recommend Cat6 cables for our devices.
  *The mounting and configuration of this device should be done by a qualified person.*

## Rackmount

If desired placement is rackmount, additional brackets can be purchased separately:

### RB5009 rackmount kit K-79

*[Figure]*

## Extension slots and ports

- Product code RB5009UPr+S+IN.
- CPU 88F7040 1.4 GHz.
- CPU architecture ARM 64bit.
- CPU core count 4.
- Size of RAM 1 GB.
- RAM type DDR4.
- Storage 1 GB, NAND.
- A number of 1G Ethernet ports 7.
- A number of 2.5G Ethernet ports 1.
- A number of 10G SFP+ ports 1.
- USB port 1 (3.0 type A).
- Operating system Only v7 RouterOS.
- Switch chip model 88E6393.
- Dimensions 220 x 125 x 22 mm.
- Operating temperature -40°C to +60°C.

## Buttons and jumpers

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset the RouterOS configuration to defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
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

- ADAPT1_EU/US Switching Power Supply 48V 2A.
- SET1_ K-55 fastening set.
- PAD1_ 4 pcs Pad D=7; H=1.5 mm, black, one side adhesive 3M988T
  See the [MikroTik wired interface compatibility](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb5009upr-plus-s-plus-in.md](../regulatory/rb5009upr-plus-s-plus-in.md).
