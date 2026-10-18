# GPeR

> Source: https://manual.mikrotik.com/hardware/gper
>
> Category: Accessories

*[Figure]*

Gigabit Passive Ethernet Repeater. See the [GPeR product page](https://mikrotik.com/product/gper) for full specifications and brochures.

## Connecting

- Connect your desired network cable with power to the PoE in Ethernet port, and extend it through PoE out.
- Connect the cable to the next GPeR unit or the other device.
- Check your final device on the line, for PoE compatibility and use jumpers to manually disable PoE out- if not needed, see section (link)

## Powering

The device requires power to the Ethernet port:

- Ethernet port accepts passive PoE or 802.3af/at DC 24 - 57 V**⎓**.
  The power consumption under maximum load can reach 2 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

### Jumper usage

If the destination device does not support PoE powering, the power passthrough can be disabled manually by removing both jumpers on the "PoE out" side. This will only work if "PoE in" is served by passive PoE source, as 802.3af/at switches will not be able to power the GPeR itself.

*[Figure]*

- When reattaching jumpers, please note horizontal placement as shown below:
  When all four jumpers are connected GPeR works in both directions.

## Mounting

The device is designed for use indoors, the IP rating scale for this device is IPX0. It is possible to attach the device to a wall, using the provided screw hole on the mounting bracket of the unit.

Please use waterproof case when using outdoors. <https://mikrotik.com/product/gper_ip67_case>

*[Figure]*

Recommended using Cat5/6 cable.
*Mounting and configuration of this device should be done by a qualified person.*

## Extension slots and ports

- Two Gigabit Ethernet ports.

## LED status

The device has two LEDs indicating the active status of each connected Ethernet port.

## Accessories

The package includes the following accessories that come with the device:

- Mounting bracket with screw and dowel.

## Specifications

Dimensions are in millimeters.

*[Figure]*

The IP68 case can be obtained separately, <https://mikrotik.com/product/gper_ip67_case>

*[Figure]*

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/gper>

## MikroTik mobile app

*[Figure]*

*[Figure]*

Use the MikroTik smartphone app to configure your routers in the field through GPeR, or to apply the most basic initial settings for your MikroTik home access points. Scan QR code and choose your preferred OS.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/gper.md](../regulatory/gper.md).
