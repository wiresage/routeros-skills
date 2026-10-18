# Chateau PRO ax

> Source: https://manual.mikrotik.com/hardware/chateau-pro-ax
>
> Category: Indoor wireless

*[Figure]*

A Wi-Fi 6 home access point for the advanced users – it comes with an exceptionally powerful wireless system and a matching CPU. See the [Chateau PRO ax product page](https://mikrotik.com/product/chateau_pro_ax) for full specifications and brochures.

### Chateau PRO ax (H53UiG-5HaxQ2HaxQ)

## Quickstart

Please follow these quick steps to set up your device:

*[Figure]*

- Make sure your Internet service provider is allowing hardware change and will issue an automatic IP address;
- Connect your ISP cable to the first Ethernet port;
- Connect the device to the included power adapter;
- Connect your computer to the wireless network;
- The configuration can be done through the wireless network using a web browser or mobile app. Alternatively, you can use a WinBox configuration tool <https://mt.lv/winbox> Open <https://192.168.88.1> in your web browser to start configuration, user name: a*dmin* and there is no password by default (or, for some models, check user and wireless passwords on the sticker);
- Click the"Check for updates" button and update your RouterOS software to the latest version;
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- Choose your country, to apply country regulation settings;
- Set up your wireless network password;
- Set up your router password.

## Connecting with a mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan the QR code and choose your preferred OS.
- Install and open the application.
- Click Connect to establish a connection to your device through a wireless network (check the wireless passwords on the sticker).
- The username is "**admin**" and there is no password (or, for some models, check user and wireless passwords on the sticker).
- Choose Quick Setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Extension slots and ports

- (link) is not provided for models with antennas.
- WPS .
- Product code: H53UiG-5HaxQ2HaxQ
- CPU: Quad-Core IPQ-8072A 2208 MHz
- CPU architecture: ARM 64bit
- Size of RAM: 1 GB
- RAM type: DDR3
- Storage: 128 MB, NAND.
- Number of 1G Ethernet: ports 5
- Number of 1G Ethernet ports with Passive PoE output, up to 57V and a maximum of 0.6A ports: 1, Ether5
- Number of USB ports: 1, USB 3.0 type A
- Switch chip model: IPQ-8072
- Wireless interface model: QCN-5024 (2.4 GHz), QCN-5054 (5 GHz)
- Wireless: 2.4 GHz 802.11b/g/n/ax 4x4 MIMO, 5 GHz 802.11a/n/ac/ax 4x4 MIMO
- WiFi speed: AX3600
- Dimensions 240 x 156 x 44 mm
- Operating system RouterOS v7, License level 6
- Operating temperature -40°C to +70°C
- IP 20

## Mounting

The device is designed to be used indoors, by placing it on the desktop.

We recommend using CAT5 shielded cable. When using and installing this device please pay attention to the Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

## Powering

- A number of DC inputs 1.
- DC jack input Voltage 18-57 V.
- Power adapter nominal voltage 48 V.
- Power adapter nominal current 1.35 A.
- Max power consumption without attachments is 18 W.
- Max power consumption 55 W.
- Networked standby (HiNA) ≤ 8 W.

## Configuration

We recommend checking for updates frequently to receive the latest updates for your RouterOS software to ensure the best performance and stability.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox> be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

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
- System LED.
- Signal strength.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration.
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server.
- Or Keep holding the button for 5 more seconds until the LED turns off, then release it to make the RouterBOARD look for Netinstall servers.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- ADAPT1_ EU/US Switching Power Supply 48 V, 1.35 A.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/chateau-pro-ax.md](../regulatory/chateau-pro-ax.md).
