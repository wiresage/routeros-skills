# netPower Lite 7R

> Source: https://manual.mikrotik.com/hardware/netpower-lite-7r
>
> Category: Switches

*[Figure]*

An outdoor reverse PoE switch with Gigabit Ethernet and 10G SFP+ ports. See the [netPower Lite 7R product page](https://mikrotik.com/product/netpower_lite_7r) for full specifications and brochures.

### netPower Lite 7R (CSS610-1Gi-7R-2S+OUT)

## Quickstart

- Download the latest version of SwitchOS software from <https://mikrotik.com/download>;
- Connect your computer to one of the Ethernet ports;
- Connect the device to the power supply;
- Set the IP address of your computer to 192.168.88.2;
- Open your web browser, the default IP management address is 192.168.88.1, with username: **admin** and no password (or, for some models, check user and wireless passwords on the sticker);
- Upload a file with the web browser in the Upgrade tab, the device will reboot after the upgrade;
- Set your password to secure your device.

## Extension slots and ports

- Gigabit Ethernet, one port PoE-out.
- Gigabit Ethernet, eight ports.
- Gigabit Ethernet, seven ports, Reverse PoE (PoE in).
- Two - 10G SFP+ ports.

## Configuration

The device can be discovered using WinBox utility, by clicking on the Neighbors list. The default management address is 192.168.88.1.
SwOS is a simple software designed for the switch. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Powering

The device accepts power in the two ways following ways:

- Direct-input power jack, (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-57 V DC⎓.
- Direct-input block terminal, 12-57 V DC ⎓.
- PoE in, 12-57 V DC ⎓.
  The power consumption under maximum load can reach 7 W, with attachments 29 W.

## Power output

The device supports passive PoE from Ethernet port eight. You can power MikroTik devices which supports powering through Ethernet. The power delivered through the PoE port will depend on the incoming to the device.

### Connecting to a PoE Adapter, only to deliver power to other devices

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Bottom Lid

- The bottom lid is secured in place with the captive screw, it can be unscrewed by hand, but do not remove the screw completely.
- Pull the cover towards.
  *[Figure]*
- Lift to access Ethernet ports.

## Mounting

The device can be mounted in several ways: pole, wall, or ceiling. The package also includes a drill hole template with detailed mounting instructions, to help you with the drill hole marking. The device has eight mounting points for versatility use zip ties or steel clamps for mounting on the pole.
The IP rating scale for this device is IP54. When mounting outdoors, please ensure that any cable openings are directed downwards. We recommend using the POE injector and proper grounding with Cat6 shielded cable.
**Mounting points:**

- There are eight mounting points on the back of this device. Choose the most relevant ones.
- Middle points are designed for mounting on the mast, there are curves on the case for slim fitment.
  It's recommended to secure Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.

The device must be mounted by UP arrow facing upwards.

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw on the backside.

- Attach your grounding wire to the grounding screw.
- Attach the other end of the grounding wire to the grounded mast.
  Mounting and configuration of this device should be performed by a qualified person. **Mounting on the mast or pole:**

*[Figure]*

- Insert provided steel clamps into mounting spots.
- Attach the unit to the mast.
- Align the device and secure it by tightening steel clamps with a PH2 screwdriver.
- Guide Ethernet cables through the opening and connect to the Ethernet ports.
- Close bottom latch and secure with a screw.
  **A – Always make sure to place the unit in an upwards position.** ***B - It's recommended to use electrical tape to increase friction between materials.*** **Mounting unit on the wall:**
- Use included a template to mark spots for drilling holes. Align accordingly, it will depend on how the device will be mounted finally.
  *[Figure]*

*[Figure]*

- Insert dowels if needed, depends on wall structure and material.
- Insert screws and screw them by leaving approximately 1 cm out.
- Attach the unit to the position.
- Use screw holes under the bottom cover and tighten to secure in place. Extend your Ethernet cables through the openings and connect to Ethernet ports.
- Close bottom latch.

Carefully check the wall for electric cables before drilling mounting holes.

## Buttons and jumpers

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset the SwOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and bridge all interfaces.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- Hose Clamp SUS304.
- K-66 fastening set.
- OED-drill-template, paper brochure.

## Operating system support

The device supports SwOS software. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/netpower-lite-7r.md](../regulatory/netpower-lite-7r.md).
