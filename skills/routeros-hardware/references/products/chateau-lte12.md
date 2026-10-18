# Chateau LTE12

> Source: https://manual.mikrotik.com/hardware/chateau-lte12
>
> Category: LTE products

*[Figure]*

## [Chateau LTE12](https://mikrotik.com/product/chateau_lte12) (RBD53G-5HacD2HnD-TC&EG12-EA)

The Chateau is a home router to be used with a cellular network provider sim card.

## Quickstart

follow these quick steps to set up your device:

*[Figure]*

- Connect your computer to one of the Ethernet ports;
- Optional - Connect an external antenna to the SMA connector (The antennas are not provided in the package, see "(link) for Micro sim card.
- Mode button.
- Cover for external (link)
- WPS (link)
- Integrated Wireless module operating at 2.4 GHz, 802.11b/g/n protocol.
- Integrated Wireless module operating at 5 GHz, 802.11a/n/ac protocol.

## Mounting

The device is designed to be used indoors, by placing it on the desktop.

You should use CAT5 shielded cable. When using and installing this device pay attention to the Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

## Powering

The device accepts power from an adapter:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin-positive plug) 12-28 V DC⎓.
  The power consumption under maximum load can reach 17 W, with attachments 23 W.

## Configuration

Configuration can be done using a web browser via WebFig, the WinBox tool <https://mt.lv/winbox>, or a (link). Multiple methods are available to ensure accessibility.

- To access WebFig, open <https://192.168.88.1> in your browser.
- For WinBox, download the tool, go to the Neighbors tab, and select the MAC address. The default username is "admin", **find the password on the device sticker**.
  You should check for updates frequently to ensure your RouterOS software remains up to date for the best performance and stability. Select the "Check for updates" button in WinBox or WebFig to update to the latest version.

A valid SIM card must be inserted or an eSIM set up, along with an active Internet connection, for updates to work.

RouterOS provides a wide range of configuration options beyond what's described in this document. We suggest visiting <https://mt.lv/help> explore these features.

For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mode button

Mode button is located on the back of the unit, to the right side (see "")
The Default configuration for the Mode button is dark mode - to turn off all LEDs. The button can be configured in RouterOS to run any user-specified scripts.

## Sync button

The sync button is located on the top of the unit. The WPS Sync button, if configured on the wireless interface, can be used to connect new clients.

*[Figure]*

- Press and hold the WPS button for 1 – 5 seconds to enable WPS for wireless interfaces.

## Front LED status

*[Figure]*

- Wireless network activity.
- Ethernet port activity.
- System LED with alternate mode for cellular modem status indication.
- Modem signal strength indicators.

### System LED alternate modem mode indications

Blinking red: SIM card not inserted

Yellow: 3G

Blue: LTE

Blinking: connection establishment in progress, modem registered in cellular network, APN is not activated yet

When LTE is not connected to the network, the system LED will blink red to indicate that there is some issue with the LTE connection. If the LTE interface is intentionally disabled (not being used), the system LED will glow blue.

## SIM slot usage

*[Figure]*

SIM card slot is designed to be used with Micro SIM cards.
Nano SIM cards have different thickness, and usage with an adapter are not recommended.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the green LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total of 10 seconds).
- To reinstall RouterOS using the Netinstall utility, enter the device into BOOTP mode. There are two types of booters available: the regular booter and the backup booter.Regular booter - Power on the device, wait 1-2 seconds, then press and hold the Reset button. Wait until the System LED is blinking green, then turns solid "On". When the green LED turns "Off", release the Reset button - the device will enter BOOTP mode.
- Backup booter – Power off the device, press and hold the Reset button, then power it on. Wait until the System LED is blinking green, then solid "On". When the green LED turns "Off", release the Reset button - the device will enter BOOTP mode using the backup booter.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

NetinstallWhen performing Netinstall, make sure to use the latest v7 version of both ROS files and the Netinstall software.

## Accessories

The package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24 V ⎓, 1.2 A, 28.8 W, 86.8 %, VI, cable:150 cm.
- CAT5E UTP Flat Cable, 8P8C, AWG32, 1.5 m, white color.

## LTE Antenna usage

SMA connectors are for LTE antennas.

The device has two external antenna connectors on the back behind the doors.

- Open doors by pulling them upwards.
- Screw the LTE antenna to the SMA connector located on the left side. The maximum diameter for antenna connectors or any other adapters used is 13 mm.

*[Figure]*

When using one antenna, connect to the SMA connector on the left side (ANT1).
Only when using two antennas, you can connect to the right SMA connector (ANT4).

*[Figure]*

connect and disconnect the antenna, when the device is turned off!
SMA connectors on the device are female.

You should use our antenna <https://mikrotik.com/product/mant_lte_5o>

## Removing front cover to access PCB

In case there is a need to access PCB, the front cover can be removed.

- Remove center screw;
  *[Figure]*
- Use a small screwdriver to pry open cover in marked spots;
- Continue to pry it open by going up;
  *[Figure]*
- At the end lift off the whole cover.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/chateau-lte12.md](../regulatory/chateau-lte12.md).
