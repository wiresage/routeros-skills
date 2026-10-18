# netFiber 9

> Source: https://manual.mikrotik.com/hardware/netfiber-9
>
> Category: Switches

*[Figure]*

A remarkable outdoor switch for setting up an optical 10G network that can even perform some light routing. The spiritual successor to the beloved FiberBox. Gigabit Ethernet, SFP/SFP+, PoE. See the [netFiber 9 product page](https://mikrotik.com/product/netfiber_9) for full specifications and brochures.

### netFiber 9 (CRS310-1G-5S-4S+OUT)

## Quickstart

- Connect with your PC to any Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Use WebFig in a web browser or the "WinBox" configuration tool <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Extension slots and ports

*[Figure]*

- DC power connector 18 – 57 V.
- LED indicating a power state of the device.
- A number of 1G SFP ports - 5.
- A number of 10G SFP+ ports - 4.
- Reset button.

## Configuration

Full documentation for both RouterOS and SwOS is available at: <https://mt.lv/help> You can configure the device using WebFig in a web browser or the "WinBox" configuration tool <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility.**
**To start setup, open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker).
The device is equipped with an RS-232 serial port, set by default to 115200 bit/s, 8 data bits, 1 stop bit, no parity. For recovery purposes, it is possible to reinstall the device from the network, see the Reset button.

Marvell Prestera switch chip features user manual

The device supports booting either RouterOS (for full routing and switching functionality) or SwOS (for switch-only operation). By default, the device boots into RouterOS, but you can switch to the other operating system as follows:

- From SwOS: Go to the System menu and click the Boot RouterOS button at the bottom of the page.
- From RouterOS: Open System → RouterBOARD → Settings and select Boot OS.
  It is also possible to choose the operating system and configure other boot options using the serial console menu.

## Powering

The device accepts power in the two ways following ways:

- Direct-input power jack 1, (5.5 mm outside and 2.1 mm inside, female, pin positive plug) accepts 18-57 V DC⎓.
- PoE in 802.3af/at 18 - 57 V DC⎓.
  The power consumption under maximum load can reach 10 W, with attachments 16.3 W.

## Bottom Lid

- The bottom lid is secured in place with the captive screw, it can be unscrewed by hand, but do not remove the screw completely.
- Pull the cover towards.
  *[Figure]*
- Lift to access Ethernet ports.

## Mounting

The device can be mounted in several ways: pole, wall, or ceiling. The package also includes a drill hole template with detailed mounting instructions, to help you with the drill hole marking. The device has eight mounting points for versatility use zip ties or steel clamps for mounting on the pole.

The IP rating scale for this device is IP54. When mounting outdoors, please ensure that any cable openings are directed downwards.

*[Figure]*

*[Figure]*

**Mounting points:**

- There are eight mounting points on the back of this device. Choose the most relevant ones.
- Middle points are designed for mounting on the mast, there are curves on the case for slim fitment.
  It's recommended to secure an Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.

The device must be mounted by an UP arrow facing upwards.

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw on the backside.

- Attach your grounding wire to the grounding screw.
- Attach the other end of the grounding wire to the grounded mast.
  The mounting and configuration of this device should be performed by a qualified person. **Mounting on the mast or pole:**

*[Figure]*

- Insert provided steel clamps into mounting spots.
- Attach the unit to the mast.
- Align the device and secure it by tightening steel clamps with a PH2 screwdriver.
- Guide Ethernet cables through the opening, connect to the Ethernet ports.
- Close bottom latch and secure with a screw.
  **A – Always make sure to place the unit in an upwards position.** ***B - It's recommended to use electrical tape to increase friction between materials.*** **Mounting unit on the wall:**
- Use included a template to mark spots for drilling holes. Align accordingly, it will depend on how the device will be mounted finally.
  *[Figure]*
- Insert dowels if needed, depending on wall structure and material.
- Insert screws and screw them by leaving approximately 1 cm out.
- Attach the unit to the position.
- Use screw holes under the bottom cover and tighten them to secure them in place. Extend your Ethernet cables through the openings and connect to Ethernet ports.
- Close bottom latch.
  Carefully check the wall for electric cables before drilling mounting holes.

## Buttons and jumpers

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configurations and bridge all interfaces.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- EU Switching Power Supply 48V, 0.95A;
- Gigabit POE injector;
- Hose Clamp SUS304;
- OED-drill-template, paper brochure;
- K-66 fastening set.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/netfiber-9.md](../regulatory/netfiber-9.md).
