# SXTsq-series

> Source: https://manual.mikrotik.com/hardware/sxtsq-series
>
> Category: Wireless systems

*[Figure: SXTsq Lite5]*

## [SXTsq 5 High Power](https://mikrotik.com/product/sxtsq_5_high_power) (RBSXTsq5HPnD)

The SXTsq is an outdoor wireless router with a built-in directional antenna. It can be used as a CPE or for point to point links (use RouterOS wireless mode "bridge" to work as a single-client AP for point to point scenarios). List of products in series:
**SXTsq Lite2**
**SXTsq Lite5**
**SXTsq 5 ac**
**SXTsq 5 High Power**

## Quickstart

- Open the Ethernet door.
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

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure: MikroTik mobile app]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Configuration

The device is preconfigured as a wireless client (CPE), and all you need to do is select the AP to connect to and set a device password. You can do this in the quickSET tab that is loaded by default. In case IP connection is not available, WinBox can be used to connect to the MAC address of the device.
In case you wish to boot the device from the network, for example, to use MikroTik Netinstall, hold the RESET button of the device when starting it, until the LED light turns off, then the device will start to look for Netinstall servers.
More information about using RouterOS and connecting to this device in our documentation: <https://mt.lv/help##> Mounting

The IP rating scale for this device is IP54. When mounting outdoors, please ensure that any cable openings are directed downwards. We recommend using POE injector and proper grounding. When using and installing this device please pay attention to Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

The device comes bundled with a metal mounting ring, which can be used on one of the three mounting slots on the backside of the device.

- Use a Phillips screwdriver to loosen the metal ring.
- Slide one end of it through the most convenient of the three mounting slots.
- Position the device on the pole where it will be mounted.
- Slide the loose end of the mounting ring back to its closing latch and use the screwdriver to tighten it.
- The included ring mount allows for mounting on 3-7 cm diameter poles.

It's recommended to secure Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.
As an additional option, you can use "quickMOUNT-X" – mounting bracket for easy adjustment that can be obtained separately. Product web page: <https://mikrotik.com/product/qm_x>

*[Figure: Mounting bracket]*

*[Figure: Mounting bracket adjustment]*

Specially designed for the SQ series enables vertical and horizontal adjustment on the pole.

## Powering

The SQ series only accepts DC ⎓ power from Passive PoE injectors (one power supply and PoE injector are included)
**SXTsq Lite2** accepts 10-30 V DC ⎓ consuming at maximum load 5 W.
**SXTsq Lite5** accepts 10-30 V DC ⎓ consuming at maximum load 6 W.
**SXTsq 5 ac** accepts 10-28 V DC ⎓ consuming at maximum load 7 W.
**SXTsq 5 High Power** accepts 10-28 V DC ⎓ consuming at maximum load 7 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Extension slots and ports

- One Ethernet 10/100 Mbit (**SXTsq 5 ac –** Gigabit Ethernet), supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated Wireless:
- **SXTsq Lite22.4 GHz, 802.11b/g/n, antenna gain 10 dBi.**
- **SXTsq Lite55 GHz, 802.11a/n, antenna gain 16 dBi.**
- **SXTsq 5 ac5 GHz, 802.11a/n/ac, antenna gain 16 dBi.**
- **SXTsq 5 High Power5 GHz, 802.11a/n, antenna gain 16 dBi.**

## Buttons and jumpers

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Grounding

The device includes a grounding connection (marked ⏚) which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage.

## Accessories

Package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24V DC ⎓, 0.38 A, 9 W, cable:1.5 m.
- Hose Clamp SUS304 (Phillips type; clamping diameter range 30-70 mm).
- POE Injector with shielded connector/Gigabit POE injector.

## Specifications

For more information about SQ series products, specifications, pictures, downloads, and test results please visit our web pages:
**SXTsq Lite2** <https://mikrotik.com/product/sxtsq_lite2>
**SXTsq Lite5** <https://mikrotik.com/product/RBSXTsq5nD>
**SXTsq 5 ac** <https://mikrotik.com/product/sxtsq_5_ac>
**SXTsq 5 High Power** <https://mikrotik.com/product/sxtsq_5_high_power>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/sxtsq-series.md](../regulatory/sxtsq-series.md).
