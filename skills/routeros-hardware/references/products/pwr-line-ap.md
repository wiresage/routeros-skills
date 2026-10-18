# PWR-LINE AP

> Source: https://manual.mikrotik.com/hardware/pwr-line-ap
>
> Category: Data over Powerlines

*[Figure]*

The PWR-LINE series devices allow Ethernet-like connectivity between supported devices over regular electrical power lines. When plugged into the same electrical circuit, the PWR devices will establish Ethernet connectivity by using the HomePlug AV standard.
The PWR-LINE AP is a wireless access point with a single Ethernet port, a built-in 802.11b/g/n WiFi Access Point and integrated PWR-LINE support.
Simply plug this device directly into one of the LAN ports of your MikroTik router, and add another one somewhere further in your premises, allowing to extend wireless network coverage without needing to install any LAN cables. You can install more PWR-LINE devices to further build your network, up to eight devices are supported.

## Connecting

- Plug one PWR-LINE AP device into a power socket.
- The main device should be plugged into one of the LAN ports of a router.
- Other PWR-LINE AP devices can be placed anywhere in any sockets in the same power circuit.
- Use the WinBox "Neighbors" tab to discover the addresses of the PWR LINE units.
- Since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker). Set up your wifi password and your country, to make sure local regulations are observed.
- To add more devices that will connect over the electrical lines, add compatible devices somewhere in the same electrical circuit. See section Buttons and Jumpers on how to pair individual PWR-LINE devices.
  Important note! The device is configured as a bridge, for extending your LAN network. By default, it does not have a password or firewall, and should not be connected directly to the internet, without configuring it accordingly.
  RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device from the network, see section (link).

## Powering

The device accepts powering directly from 100-240 V ~50/60Hz wall socket it is plugged into. The power consumption under maximum load can reach 7 W.

## Extension slots and ports

- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- Integrated Wireless 2.4 GHz 802.11b/g/n with onboard PIF antennas, max gain 1.5 dBi.

## Buttons and jumpers

The PWR-LINE AP has the following buttons:

### Reset button

- Hold the button before powering on the device, and at power-up, the button will force load the backup boot loader. Continue holding the button for the other two functions of this button.
- Release the button when the green LED starts flashing, to reset RouterOS configuration. To not load the backup boot loader, you can start holding the button after power is already applied.
- Release the button after LED is no longer flashing (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

### Sync button

- Hold 0.5 – 3 seconds. For 120 seconds will try to communicate with another PWR-LINE device. A blinking orange LED light indicates that it is in search mode. You have to also do the same on the other PWR device, so they can synchronize. Press button again to cancel the search. You can also manually set the security keys in RouterOS settings.
- Hold 5 – 8 seconds. A new security key is generated. This is needed to remove a PWR-LINE device from an existing PWR network.
- Hold 10 – 15 seconds. Resets all PWR related settings.

### Mode button

This button can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button.

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Datasheet for any device is available on the official manufacturer website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).

Please make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/pwr-line-ap.md](../regulatory/pwr-line-ap.md).
