# GPeRx4

> Source: https://manual.mikrotik.com/hardware/gperx4
>
> Category: Accessories

*[Figure]*

Effortlessly split a single high-power PoE port into multiple standard PoE connections with the compact and durable GPeR14i. Expand, extend, and power your network with ease!

## Connecting

- Unlock the enclosure by simultaneously pressing the buttons located on both sides of the lower case, and then proceed to remove the cover from the device;
- Thread the cables through the rubber seal located on the underside of the case;
- Connect your desired network cable with power to the PoE in the Ethernet port, and extend it through the PoE out ports;
- Connect the cable to the next device or another GPER14i unit;

## Powering

This device offers two distinct power supply options:

- The First Ethernet port is a PoE-in that supports 802.3bt and accepts DC voltage in the range of 48 to 57V⎓.
- The two-pin connector is compatible with DC voltage in the range of 24 to 57V⎓.
- You can power up an additional GPER14i unit using the two-pin connector. To achieve this, connect the device to the two-pin connectors of another GPER14i unit, and ensure that the SwOS Lite System's "Power I/O" option is configured as "Output." To enable this operation, the device itself must be powered via PoE-in.
  Outgoing power WarningPlease ensure that the device's power consumption does not exceed the incoming power capacity of the power-feeding device, taking into account its current load.

Max power consumption: 115W. It is important to note that all other ports are limited to 30W power consumption

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.
  Connecting the two-pin connector:
- Attach the positive wire to the + slot.
- Attach the negative wire to the - slot.

## Grounding

The grounding wire should be connected to the RouterBOARD grounding wire attachment point. This wire should then be connected to the base of the installation location, ensuring the connection meets grounding standards. The grounding screws M4 are not included.

## Mounting

The device is designed for use outdoors, the IP rating scale for this device is IP68. It is possible to attach the device on the pole, using the provided screw hole on the mounting bracket of the unit.

Recommended using Cat5/6 cable.
*Mounting and configuration of this device should be done by a qualified person.*

## Extension slots and ports

- 1 PoE-in 802.3bt Gigabit Ethernet port.
- 3 PoE-out 802.3af/at Gigabit Ethernet ports.
- 1 two-pin connector DC power voltage slot in the range of 24 to 57V⎓.

## LED status

The device's LED indication can only be seen with an open case.

- DC-in status LED.
- DC-out status LED.
- The Ethernet port active status LED.
- The PoE-out status LED

## The Reset button

The reset button is located on the plate, and can be used with an opened case. Hold this button until DC-in LED light starts flashing, release the button to reset configuration to default.

## Accessories

The package includes the following accessories that come with the device:

- Mounting bracket with screw and dowel.

## Specifications

Dimensions: H x W x D, mm: 280 x 75 x 70 mm

*[Figure]*

*[Figure]*

*[Figure]*

For more information about this product, specification, and pictures, please visit our web page: <https://mikrotik.com/product/gper>

## Configuration

This device operates on the SwOS Lite operating system.

- Set your IP for PC to 192.168.88.2/24;
- Connect your PC to any unused Ethernet port;
- Open your web browser, the default IP management address is 192.168.88.1, with username: **admin** and no password (or, for some models, check user and wireless passwords on the sticker);
- Download the latest version of SwitchOS Lite software from <https://mikrotik.com/download>;
- Upload a file with the web browser in the Upgrade tab, the device will reboot after the upgrade;
- Set up your password to secure the device.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/gperx4.md](../regulatory/gperx4.md).
