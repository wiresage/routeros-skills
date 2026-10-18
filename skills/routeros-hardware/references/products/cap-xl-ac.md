# cAP XL ac

> Source: https://manual.mikrotik.com/hardware/cap-xl-ac
>
> Category: Indoor wireless

The ceiling AP on steroids! Our bestseller cAP is back – juiced up and stronger than ever. Compared to the previous cAP models, the improved high-gain antenna increases the covered area by up to 100%! See the [cAP XL ac product page](https://mikrotik.com/product/cap_xl_ac) for full specifications and brochures.

### cAP XL ac (RBcAPGi-5acD2nD-XL)

*[Figure]*

## Connecting

- Connect POE to Ethernet port 1, please see the (link).

## Extension slots and ports

Product code RBcAPGi-5acD2nD-XL

- CPU Quad-core IPQ-4018 710 MHz
- Size of RAM 128 MB
- RAM type DDR3L
- Storage 16 MB, Flash
- Number of 1G Ethernet ports 2
- Wireless 2.4 GHz 5 GHz
- Supported protocol 802.11b/g/n 802.11a/n/ac
- Antenna gain 6 dBi 5,5 dBi
- Number of chains 2
- Operating system RouterOS (License level 4)
- Switch chip model IPQ-4018
- Dimensions 191 x 42 mm
- Operating temperature -40°C to +70°C

## Buttons and jumpers

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

There are two mode buttons on this unit, but they both are performing the same action. The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. By default, the buttons will enable "dark mode", which disables beeps and LED lights. The mode button can be configured in the RouterOS menu /system routerboard mode-button.

## LED indicators

*[Figure]*

There are seven LED lights on the unit, which can be disabled altogether if necessary.

- User – user-configurable led for any desired script.
- 5G – 5GHz interface activity.
- 2G – 2.4 GHz interface activity.
- E2 – Ethernet 2 connected.
- E1 – Ethernet 1 connected.
- PoE LED indicates that the ETH2 port is currently powering another device with PoE.
- The power LED indicates that the unit is receiving power in the ETH1 port.

## Accessories

The package includes the following accessories that come with the device:

- ADAPT1_ EU/US Switching Power Supply 24V, 1.2A.
- POE1_ Gigabit POE injector.
- BRAC1_ CAPGB-Mounting Bracket.
- Screw set 2 screws and dowels for mounting.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Notice

- Datasheet for any device is available on the official manufacturer website.
- For some models, check the user and wireless passwords on the sticker.
- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- Please make sure the device has a locking package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG” - RBcAPGi-5acD2nD-XL-EG.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Firmware for Egypt Regulatory have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Firmware for Egypt Regulatory have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Firmware for Egypt Regulatory have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).
  This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements.
  All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/cap-xl-ac.md](../regulatory/cap-xl-ac.md).
