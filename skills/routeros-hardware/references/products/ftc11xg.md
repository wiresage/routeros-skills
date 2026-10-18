# FTC11XG

> Source: https://manual.mikrotik.com/hardware/ftc11xg
>
> Category: Accessories

*[Figure]*

The FTC11XG is a weatherproof IP55 Fiber-to-Copper converter to transform your 10 Gigabit SFP+ fiber connections into RJ45 10 Gigabit Ethernet. It runs a full version of SwOS Lite and has its own switch-chip!. See the [FTC11XG product page](https://mikrotik.com/product/ftc11xg) for full specifications and brochures.

## First steps:

- Use a screwdriver to unscrew the central screw and remove the plastic cover;
- Underneath the cover, there are Ethernet and SFP output ports;
- Set your IP for PC to 192.168.88.2/24;
- Connect your devices;
- Choose your powering solution (see "");
- Open <https://192.168.88.1> in your web browser to start configuration, user name: admin and there is no password by default;
- Download the latest version of SwitchOS Lite software from <https://mikrotik.com/download>;
- Upload a file with the web browser in the Upgrade tab, the device will reboot after the upgrade;
- Set up your password to secure the device.
- If needed, the device can be mounted on the wall;
- The screws with dowels are included in the package.

## Mounting

The device can be mounted in several ways: on a wall, pole, or mast using a specially designed MikroTik holder that comes with the package. The unit can be attached to the pole using zip ties or a steel clamp (not included).
To prevent the bottom lid from opening, use the included M4x14 PH2 security screw.
The IP rating for this device is IP55.
When mounting outdoors, please ensure that any cable openings are directed downwards. Recommended using Cat5/6 cable. Use the proper case grounding.

### Mounting on the mast or pole:

*[Figure]*

*[Figure]*

- Mount the included bracket to the pole or mast using steel hose clamp (not included), guiding it through the hole.
- Mount and align the device on the previously installed bracket on the pole or mast.
- Unscrew the bottom lid screw and open the lid.
- Guide the cables through the opening and connect them to the appropriate ports.
- Close the bottom lid and secure it with a screw.
  It's recommended to secure Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.

### Mounting unit on the wall:

*[Figure]*

*[Figure]*

- Place the bracket at the location where you plan to install the device and mark spots for drilling holes and, if needed, for cables. Align accordingly, depending on the final mounting position of the device.
- Drill the holes.
- Insert included dowels if needed, depending on the wall structure and material.
- Screw the included bracket onto the wall or ceiling.
- Mount and align the device on the previously installed bracket.
- Unscrew the bottom lid screw and open the lid.
- Guide the cables through the opening and connect them to the appropriate ports.
- Close the bottom lid and secure it with a screw.
  Avoid mounting the device on the low ground spot, as you won't be able to attach and close the bottom latch.

## Bottom Lid

- The bottom lid is secured in place with the screw.
- Use the Philips PH2 screwdriver to unscrew it.

*[Figure]*

- Pull the lid in the opposite direction from the device to remove it.

*[Figure]*

- Reassemble.

*[Figure]*

## Powering

The device accepts power from the power jack or from the Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 18-57 V ⎓ DC;
- Ethernet1 port accepts 802.3 bt PoE.
  The maximum power consumption without attachments is 9W, and under maximum load, it can reach 10W.

### Connecting to a PoE Adapter:

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.
  The product should be properly grounded.

## Extension slots and ports

- One 10/100/1000 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- One 1G/2.5G/5G/10G Ethernet port.
- One 10G SFP+ port.

## Configuration and operating system support

This FTC11XG has built-in backup SwOS firmware which can be loaded in case standard firmware breaks or an upgrade fails:

- Holding the reset button for a few seconds while the device is powered and booting will reset the configuration and load the backup firmware. The reset button is located under the bottom lid.
- After loading backup firmware, it is possible to connect to 192.168.88.1 (or leased address from a DHCP server) using a web browser and install new SwOS firmware.

## LED indicators

This device features LED indicators, including PWR LED (Power), ETH activity, and SFP activity LEDs.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ftc11xg.md](../regulatory/ftc11xg.md).
