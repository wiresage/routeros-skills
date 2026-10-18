# CRS-series

> Source: https://manual.mikrotik.com/hardware/crs-series
>
> Category: Switches

*[Figure]* *[Figure]*

> **This article covers**
>
> - **CRS109-8G-1S-2HnD-IN**
> - **CRS112-8G-4S-IN**
> - **CRS210-8G-2S+IN**
> - **CRS212-1G-10S-1S+IN**

The CRS is a highly configurable switch, powered by RouterOS.

## First use

- Mount unit or place on the flat surface, please see paragraph for instructions.
- Choose your powering solution, please see the section for possibilities.
- The Initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility.
- Use WinBox to connect to the default IP address of 192.168.88.1 from any port, with the username admin and no password, the device is set up as a switch (or, for some models, check user and wireless passwords on the sticker).
- Update the device by clicking the "Check for updates" button to v6.46 or the latest RouterOS software to ensure the best performance and stability. The device needs to have an active internet connection.
- To manually update the device, go to our download page <https://mikrotik.com/download>
- Choose your architecture (MIPSBE) and download the latest packages from any channel to your PC.
- Open WinBox and upload packages in the Files menu.
- Reboot the device.
- Updating software will ensure the latest security fixes and regulations set by local law.
- Choose your Country.
- Set up your password to secure the device.

## Powering

The devices accept power in the following ways:

- direct-input power jack: 8-56V (24V 0.8A PSU included),
- passive PoE input: 8-56V (injector included).
  Except for CRS212-1G-10S-1+IN, which only accepts 8-30V direct input, with no PoE input support

## Extension slots and ports

- Except for CRS212: Eight (8) 10/100/1000 (Gigabit) Ethernet ports (Auto MDI/X).
- For CRS109: One SFP cage, compatible with 1.25G SFP modules, Built-in 802.11b/g/n 2GHz wirelessaccess point.
- For CRS112: Four SFP cages, compatible with 1.25G SFP modules.
- For CRS210: Two SFP+ cages, SFP+1 compatible with 1.25G and 10G, SFP+2 compatible 10G SFPmodules only.
- For CRS212: Ten SFP cages, one SFP+ cage, one Gigabit Ethernet port.
  The device is equipped with an RJ45 serial port, set by default to 115200bit/s, 8 data bits, 1 stop bit, no
  parity. Standard RJ45 to COM cable can be used, pinout can be found in the [Serial Console manual](https://manual.mikrotik.com/docs/management-tools/serial-console#rj45-type-serial-port)

## Configuration

Once logged in, we recommend clicking the “Check for updates” button in the QuickSet menu, as updating your
RouterOS software to the latest version ensures the best performance and stability. For wireless models, please
make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest
starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available,
the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side
(all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section Reset button.

## Default configuration

- CRS109-8G-1S-2HnD-IN: ports 2-8 are switched, wireless interface and switch are bridged, and bridgecontains a DHCP server. Eth1 and SFP1 have DHCP client configured.
- All other models all the ports are switched.
  Both models can be accessed through the IP 192.168.88.1, the username is admin and there is no password.
  Please connect with your web browser to this IP address to configure it. See this page for connection and
  configuration guides: [RouterOS documentation](https://manual.mikrotik.com/docs/introduction)

## Reset button

The reset button has three functions:

• Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
• Release the button when the LED turns solid green to clear all configuration and defaults.
• Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers
(required for reinstalling RouterOS over the network).

Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed
before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS
menu /system resource. Other operating systems have not been tested.

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Datasheet for any device is available on the official manufacturer website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).

Please make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs-series.md](../regulatory/crs-series.md).
