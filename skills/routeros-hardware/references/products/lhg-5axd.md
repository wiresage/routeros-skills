# LHG-5axD

> Source: https://manual.mikrotik.com/hardware/lhg-5axd
>
> Category: Wireless systems

*[Figure]*

## [LHG 5 ax](https://mikrotik.com/product/lhg_5_ax) (LHG-5axD)

Long-range outdoor CPEs with modern Wi-Fi 6 performance, rugged design, and unbeatable pricing. See the [LHG-5axD product page](https://mikrotik.com/product/lhg_5_ax) for full specifications and brochures.

## Assembly and Mounting

- Attach the two legs to the LHG case.
  *[Figure]*
- Snap the assembled LHG unit to the grid in the appropriate locations.
- Fix the legs in place with two self-thread screws (Use Phillips screwdriver PH2).
  *[Figure]*

The device is designed to be mounted on the pole using zip ties or steel clamps as shown in the picture. The clamping diameter with provided steel clamps is 35 – 70 mm.

*[Figure]*

- Guide provided steel clamps through the unit.
- Attach the device to the pole.
- Align and tighten the clamps to secure the device.Optional: If required, before mounting the unit, you can insert the included 5-degree adjustment adapter into the top or bottom slot where the mounting ring is inserted. This will create an additional upward or downward angle when the unit is tightened to a vertical pole.

*[Figure]*

The device includes a grounding connection (marked ⏚) which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage.
Warning! This equipment should be installed and operated with a minimum distance of 40 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.

Connect the Ethernet cable to the Ethernet port located under the door and guide through the leg as shown in the picture:

*[Figure]*

Additional mounting brackets can be purchased separately:

LHG mount

*[Figure]*

solidMOUNT

*[Figure]*

## Quickstart

- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Access **WebFig** by opening <https://192.168.88.1>, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and click on the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the "Quick Set" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.
  The device is preconfigured as a wireless client and all you need to do is select the AP to connect to and set a device password. You can do this in the Quick Set tab that is opened by default. We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
  In case the IP connection is not available, WinBox can be used to connect to the MAC address of the device.
  In case you wish to boot the device from the network, for example, to use MikroTik Netinstall, hold the RESET button of the device when starting it, until the LED light turns off, then the device will start to look for Netinstall servers. More information about using RouterOS and connecting to this device in our documentation: <https://mt.lv/help##> Powering
  The device accepts powering only from Passive PoE injectors.
  PoE in input Voltage: 12-28 V.

## Extension slots and ports

- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One integrated wireless device with a built-in grid antenna.

## Buttons and jumpers

The reset button has three functions:

- Reset RouterOS configuration - Hold the button during boot until the USR LED light starts flashing, then release it to reset the configuration (about 5 seconds).
- Enable CAP mode. Keep holding for 5 more seconds (total 10 seconds) until the USR LED turns solid, then release to turn on CAP mode. The device will now search for a CAPsMAN server.
- Reinstall RouterOS using Netinstall (BOOTP mode). Two types of booters are available:Regular booter - Power on the device, wait 1-2 seconds, then press and hold the Reset button. Wait until the USR LED is blinking and then turns solid ON. When the USR LED turns OFF, release the Reset button - the device will enter BOOTP mode.
- Backup booter - Power off the device, press and hold the Reset button, then power it on. Wait until the USR LED is blinking and then turns solid ON. When the USR LED turns OFF, release the Reset button - the device will enter BOOTP mode using the backup booter.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/lhg-5axd.md](../regulatory/lhg-5axd.md).
