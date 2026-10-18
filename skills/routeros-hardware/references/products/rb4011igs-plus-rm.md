# RB4011iGS+RM

> Source: https://manual.mikrotik.com/hardware/rb4011igs-plus-rm
>
> Category: Ethernet routers

*[Figure]*

The device is already configured with basic settings, you can simply plug in your ISP cable and start using the Internet. We recommend you set up a password to secure your device. See the [RB4011iGS+RM product page](https://mikrotik.com/product/rb4011igs_rm) for full specifications and brochures.

## Setup

- Connect your Internet cable to the first port, and local network PCs to the other ports.
- Choose your powering solution, please see the section for possibilities.
- Set your computer IP configuration to automatic (DHCP).
- The default IP address from the local network is 192.168.88.1, open this address in your web browser to start the configuration. The username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. The device needs to have an active Internet connection.
- Set up a strong password for the device.

## Powering

The power consumption under maximum load can reach 33 W. The device accepts power from the power jack or from the first Ethernet port:

- Direct-input power jack (5.5 mm outside and 2.1 mm inside, female, pin positive plug) accepts 12-57 V DC.
- The First Ethernet port accepts Power over Ethernet 18-57 V DC.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

*[Figure]*

- Attach rack ears to both sides of the device and tighten four screws to secure them in place;
- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently;
- Tighten screws to secure it in place.
  The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
  We recommend Cat6 cables for our devices.
  *Mounting and configuration of this device should be done by a qualified person.*

Operating humidity can be from 5% to 95% non-condensing.

## Extension slots and ports

- The Ethernet ports are connected in two groups of five, each group is connected through a switch chip. The ports can be configured individually and support automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- SFP+ port accepts SFP and SFP+ modules. Refer to the [MikroTik wired interface compatibility](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility) table.
- RJ45 console port for serial console access, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity.

## Buttons and jumpers

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and bridge all interfaces.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Accessories

Package includes the following accessories that come with the device:

- EU/US Switching Power Supply DC ⎓ 24 V 1.5 A 36 W 87.4% VI 150 cm RA DC plug.
- K-60 fastening set. DIN965, M3x6.
- Mounting kit 4011 rm bracket.
  See the [MikroTik wired interface compatibility](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb4011igs-plus-rm.md](../regulatory/rb4011igs-plus-rm.md).
