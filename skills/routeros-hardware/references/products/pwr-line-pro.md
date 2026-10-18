# PWR-LINE PRO

> Source: https://manual.mikrotik.com/hardware/pwr-line-pro
>
> Category: Data over Powerlines

*[Figure]*

The PWR-LINE PRO allows Ethernet-like connectivity between supported devices over regular electrical power lines. When plugged into the same electrical circuit, the device will establish Ethernet connectivity by using the HomePlug AV 2 standard. The device supports 802.1q. PWR-LINE PRO does not require any system software or configuration, it's ready to use.

## Connecting

- Plug one PWR-LINE PRO device into a power socket.
- Connect to one of the LAN ports of your MikroTik router to the PWR-LINE PRO Ethernet port.
- Plug another PWR-LINE PRO unit (or any other compatible device) somewhere in the same electrical circuit.
- Use the sync button to connect the devices and your local network will automatically be extended. Please see the section on how to pair additional PWR-LINE PRO devices.
- PWR-LINE PRO supports PoE out from Ethernet port to power another MikroTik device, this can be activated with a switch, please see section.

## Mounting

PWR-LINE PRO can be mounted on the wall using four provided screws:

- To access mounting points, remove a center screw, that is holding top cover, using PH2 screwdriver.

*[Figure]*

- Mark four points for screw holes in the desired place on the wall for PWR-LINE PRO.
- Drill using a 5 mm drill bit for dowel holes and insert them by slight tapping if necessary.
- Mount PWR-LINE PRO and close top cover, center screw tightening force 0.5 – 0.7 Nm, attach provided 3M sticker to cover center screw.

## Powering

The device accepts power from a wall socket where it is plugged into.
100-240 V AC ⏦, ~50/60 Hz.
The power consumption under maximum load can reach 5 W. Max power consumption with PoE-Out 14 W.

*In order to reach a speed of 600 Mbps, your electrical sockets needs to be grounded.*
*To connect with another PWR-LINE device, both need to be on the one electrical phase.*

## Extension slots and ports

- One Gigabit Ethernet port, supporting 24 V PoE output by default settings is set to OFF.

## Buttons and jumpers

### PWR connection button (sync)

*[Figure]*

- Hold 0.5 – 3 seconds. For 120 seconds will try to communicate with another PWR-LINE PRO device. A blinking amber LED light indicates that it is in search mode. You have to also do the same on the other PWR device, so they can synchronize. Press button again to cancel the search.
- Hold 5 – 8 seconds. A new security key is generated. This is needed to remove a PWR-LINE PRO device from an existing PWR network.
- Hold 10 – 15 seconds. Resets all PWR related settings.
- In case of trouble to pair device, hold the SYNC button for 5 - 8 seconds to generate new network key and then re-attempt to pair it in PWR-LINE PRO network again holding SYNC button for 0.5 – 3 seconds.

## LED lights and PoE switch

*[Figure]*

- Blue LED indicates device power ON state.
- Amber LED indicates that the device is paired, blinking amber indicated that the device is in search mode. It can be activated with a sync button. Please refer to the section.
- Green LED indicates Ethernet port connectivity.
- Red LED indicates that PoE is active.
- PoE switch default position is OFF. A standard ballpoint pen can be used to switch positions. The Red light will indicate that PoE is active.

## Accessories

Package includes the following accessories that come with the device:

- K-62 fastening set.
- EU/US power cord, D03+QT1 H03VV-F 0x0.75 mm2, 30 cm RoHS, White color.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/pl7510gi>

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/pwr-line-pro.md](../regulatory/pwr-line-pro.md).
