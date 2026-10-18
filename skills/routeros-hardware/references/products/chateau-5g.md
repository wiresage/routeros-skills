# Chateau 5G

> Source: https://manual.mikrotik.com/hardware/chateau-5g
>
> Category: LTE products

*[Figure]*

## [Chateau 5G](https://mikrotik.com/product/chateau_5g) (D53G-5HacD2HnD-TC&RG502Q-EA)

## Quickstart

follow these quick steps to set up your device:

*[Figure]*

- Connect an external antennas to the SMA connector (The antennas are provided in the package, see "(link)");
- Insert micro SIM card into the slot located under the device;

*[Figure]*

- Connect your computer to one of the Ethernet ports;
- Connect the power adapter to the DC jack;
- Once the device is powered on and PC connected to the device, open <https://192.168.88.1> in your web browser to start the configuration (or, for some models, check user and wireless passwords on the sticker);
- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen;
- You should select the "Check for updates" button on the right side and update your RouterOS software to the latest version to ensure the best performance and stability, Must have a valid SIM card inserted;
- To manually update the device, go to <https://mikrotik.com/download>
- Choose ARM packages for this device and download them to your PC.
- Upload downloaded packages to the WebFig "Files" menu and reboot the device.
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates.
- To personalize your wireless network, SSID can be changed in the fields "Network Name";
- Choose your country on the left side of the screen in the field "Country", to apply country regulation settings;
- Set up your wireless network password in the field "WiFi Password" the password must be at least eight symbols;
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to log in next time;
- Select the "Apply Configuration" to save changes.

## Connecting with a mobile app

Use your smartphone to access your router through WiFi.

*[Figure]*

- Insert the SIM card and power on the device.
- Scan QR code with your smartphone and choose your preferred OS.
- Connect to the wireless network. SSID starts with MikroTik and has the last digits of the device's MAC address.
- Open application.
- By default, the IP address and user name will be already entered.
- Select Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Extension slots and ports

*[Figure]*

- (link).
- (link) DC jack 2.0 mm.
- Five Gigabit ports, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- USB type-A.
- (link) for Micro sim card.
- Mode button.
- Cover for external (link) is not provided for models with antennas.
- WPS (link)
- Integrated Wireless module operating at 2.4 GHz, 802.11b/g/n protocol. Antenna gain 3 (dBi).
- Integrated Wireless module operating at 5 GHz, 802.11a/n/ac protocol. Antenna gain 4 (dBi).

## Mounting

The device is designed to be used indoors, by placing it on the desktop.

You should use Cat5 shielded cable. When using and installing this device pay attention to the Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

## Powering

The device accepts power from an adapter:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) 12-28 V DC⎓.
  The power consumption under maximum load can reach 17 W, with attachments of 23 W.

## Configuration

You should check for updates frequently to receive the latest updates for your RouterOS software to ensure the best performance and stability.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section (link).

## Mode button

The mode button is located on the back of the unit, on the right side.
The Default configuration for the Mode button is dark mode - to turn off all LEDs. The button can be configured in RouterOS to run any user-specified scripts.

## Sync button

The sync button is located on the top of the unit. WPS Sync button, if configured on the wireless interface, can be used to connect new clients.

*[Figure]*

- Press and hold the WPS button for 1 – 5 seconds to enable WPS for wireless interfaces.

## Front LED status

*[Figure]*

- Wireless network activity.
- Ethernet port activity.
- System LED with alternate mode for cellular modem status indication.
- Signal strength.

### System LED alternate modem mode indications

When cellular modem interface is enabled, System LED have have alternate indications:

blinking red - SIM card not inserted

yellow - established connection in 3G mode

blue - established connection in LTE mode

green - established connection in 5G NSA mode

violet - established connection in 5G SA mode

blinking - connection establishment in progress, modem registered in cellular network, APN is not activated yet

## SIM slot usage

*[Figure]*

SIM card slot is designed to use with Micro SIM cards.
Nano SIM cards have different thicknesses, usage with an adapter is not recommended.

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

- ADAPT1_ EU/US Switching Power Supply 24V, 1.2A.
- CAB3_ CAT5E UTP Flat Cable, 8P8C, AWG32, 1.5m.
- ANT8-9_ external LTE antenna.

## Antenna usage

SMA connectors are for provided LTE antennas.

When connecting or disconnecting the external antennas device must be powered off, otherwise, the device may be damaged!

External antenna sockets are located on the back of the device.

- Screw both antennas to the SMA sockets (Follow the instructions in the illustrations).

*[Figure]*

## Removing back cover to access PCB

In case there is a need to access PCB, the back cover can be removed.

- Remove center screw;
  *[Figure]*
- Use a small screwdriver to pry open backplate in marked spots;
- Continue to pry it open by going up;
  *[Figure]*
- At the end lift off the whole backplate.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/chateau-5g.md](../regulatory/chateau-5g.md).
