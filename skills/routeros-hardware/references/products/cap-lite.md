# cAP lite

> Source: https://manual.mikrotik.com/hardware/cap-lite
>
> Category: Indoor wireless

*[Figure]*

Included with the product are two different casings, which can easily be swapped out, or, if you really like to fit the design with the environment, we are providing 3D printer friendly design files. See the [cAP lite product page](https://mikrotik.com/product/RBcAPL-2nD-307) for full specifications and brochures.

## Connecting

- Connect POE to the Ethernet port, please see Reset button.

## Reset button

The reset button has three functions:Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).

- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Extension slots and ports

- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- One Integrated Wireless 2.4 GHz 802.11b/g/n.
- One USB type AB slot.

## Accessories

Package includes the following accessories that come with the device:

- DC ⎓ EU/US Switching Power Supply 24 V, 0.2 A, 4.8 W, Level VI, cable:1.5m).
- POE Injector with shielded ethernet cable/connector (RBPOE).
- K-49 fastening set.
- Map wall cover.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

*[Figure]*

*[Figure]*

*[Figure]*

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

## Mounting

*[Figure]*

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Datasheet for any device is available on the official manufacturer website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).

Please make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/cap-lite.md](../regulatory/cap-lite.md).
