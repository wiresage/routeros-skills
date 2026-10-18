# CRS112-8G-4S-IN

> Source: https://manual.mikrotik.com/hardware/crs112-8g-4s-in
>
> Category: Switches

*[Figure]*

This device is a network switch with eight gigabit Ethernet ports and four SFP ports. It is already configured, with all ports switched together. This unit is compatible with 1.25G SFP modules.

## Quickstart

The Default configuration, Switch mode all interfaces are switched; LAN Configuration.
All ports are bridged with IP 192.168.88.1/24 set on the bridge.

- Place on the flat surface (see “Mounting”).
- Connect your PC to any Ethernet port.
- Connect the power adapter to the DC jack.
- Set IP for your PC to 192.168.88.2
- The Initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility or Webbrowser.
- Use WinBox or Web browser to connect to the default IP address of 192.168.88.1 from any port, with theusername admin and no password (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the “Check for updates” button and updating your RouterOS software to the latestversion to ensure the best performance and stability. The device needs to have an active internetconnection.
- To manually update the device go to our webpage and download the latest software version packages.
- Open WinBox and upload them to the Files menu.
- Reboot the device.
- Set up your password to secure the device.

## Powering

The board accepts power from the direct-input power jack (5.5 mm outside and 2 mm inside, female, pin-positive plug) and accepts 10-57 V ⎓ DC. The Ethernet port 1 also accepts passive PoE power input. The power consumption of this device under maximum load is up to 11 W. It is possible to connect both power inputs at the same time and they will work in failover mode (input with higher voltage will work as the main source).

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

The device is set up as a switch, with 192.168.88.1 as the management IP of the bridge interface. RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case the IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device.
The device is equipped with an RJ45 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, and no parity. Standard RJ45 to COM cable can be used, pinout can be found in the documentation (see link above).
For recovery purposes, it is possible to boot the device for reinstallation, see the next section.

## Buttons and jumpers

The reset button has these functions:

- Hold this button during boot time until the user LED light starts flashing, and release the button to reset the RouterOS configuration.
- Keep holding the button for 5 more seconds or until the user LED turns off, then release it to make the RouterBOARD look for Netinstall servers. The first Ethernet port is used for the Netinstall process.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load the backup RouterBOOT without reset. This is useful for RouterBOOT debugging and recovery.

## LED indicators

- The power LED is lit when the router is powered by the DC jack or PoE.
- The user LED can be configured from RouterOS.
- The port LEDs indicate the individual Ethernet and SFP port activity.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please use a Phillips screwdriver to attach rackmount ears on both sides of the device if the designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
  *[Figure]*
- Place the device in the rackmount enclosure and align it with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.

The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
We recommend Cat6 cables for our devices.
The mounting and configuration of this device should be done by a qualified person.

## Specifications

Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).
For more information about this product, specifications, pictures, downloads, and test results please visit our web page: <https://mikrotik.com/product/CRS112-8G-4S-IN>

## Operating system support

The device supports RouterOS software with version number 6.45.6 at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

## Included parts

*[Figure]*

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs112-8g-4s-in.md](../regulatory/crs112-8g-4s-in.md).
