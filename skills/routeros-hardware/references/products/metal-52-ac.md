# Metal 52 ac

> Source: https://manual.mikrotik.com/hardware/metal-52-ac
>
> Category: Wireless systems

*[Figure]*

## [Metal 52 ac](https://mikrotik.com/product/RBMetalG-52SHPacn) (RBMetalG-52SHPacn)

The RBMetalG-52SHPacn Metal comes preinstalled in an outdoor case, with a built-in wireless interface, an N-Male antenna connector, and one 10/100/1000 Ethernet connector which supports MDI-X auto-detection. The device is packaged with a 24 V power adapter, a PoE injector, and two mounting loops. Several models are available (dual-band, single band, AP and CPE variants).

## Quickstart

- Connect the antenna to the N-Male connector (see [Antenna usage](#antenna-usage));
- Open the cover of the Ethernet port (see [Opening Ethernet cover](#opening-ethernet-cover));
- Guide your cable through the cover and connect to the Ethernet port (see [Opening Ethernet cover](#opening-ethernet-cover));
- The device accepts 10-30 V Passive PoE from a PoE injector. The included injector should be connected with the "Data" end into a PC, the "Data + Power" port should be connected to the device, by using an Ethernet cable of the desired length (not included);
- Use the provided rubber insulator to put on the Ethernet cable, and push it into the case opening, so that the opening is tightly closed;
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

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open applications.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Powering

The device accepts powering from an Ethernet port (Passive PoE). Under maximum load, the power consumption of this device is 11 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).

## Mounting

The device is to be mounted vertically so that the Ethernet cable points downwards.

*Mounting and configuration of this device should be done by a qualified person.*

If you wish to tighten the device to a pole, you can do it with the provided mounting loops. The device comes bundled with two mounting loops – guide the loops around the device through the provided edge markings, and around the pole where it will be mounted.

An electric tape can be used to increase friction between materials use it between clamps and the mounting surface. It will help to hold the device in place. The mounting hose clamp is provided with the package.

*[Figure]*

- Guide hose clamp through the opening on the back of the device.
- Attach to the pole or mast.
- Align and secure by hose clamp screw using PH2 screwdriver.
  The device should be placed by the antenna facing upwards. You should avoid connecting a loose Ethernet cable to the Ethernet port, secure the cable to a wall or the pole, so that the cable weight is not pulling the port. It is recommended to secure the Ethernet cable less than 2m from the device. This is to ensure that the cable doesn't damage the port by its weight or doesn't fall out.

When mounting, please ensure that cable feed is pointing downwards.
The IP rating scale of this device is IP54. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Opening Ethernet cover

*[Figure]*

- To open the cover, release clips for both fasteners and cover will be free to open.
- Guide your Ethernet cable through the rubber seal in the cover opening.
- Crimp RJ-45 connector on the cable and connect with Ethernet port.

## Antenna usage

Attach antenna by screwing it to the connector located on the device.

*[Figure]*

Please connect and disconnect the antenna, when the device is turned off!

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RBMetalG-52SHPacn look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/RBMetalG-52SHPacn>
RBMetalG-52SHPacn-US (USA) is factory locked for 2412-2462MHz, 5170-5250MHz and 5725-5835MHz frequencies. This lock can not be removed.
RBMetalG-52SHPacn (International) supports 2412-2484MHz and 5150MHz-5875MHz range (Specific frequency range can be limited by country regulations).

## Accessories

Package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24 V ⎓ 0.8A, 19.2 W.
- 2.4Ghz/5Ghz Dual Band OMNI Antenna 6 dBi for N FEMALE, Grey color, PVC housing, 285 mm length.
- Gigabit POE injector.
- Plastic tie strap fastener 2 pcs.
- Hose clamp 50 / 70 2 pcs.
- N-Male to N-Female Right Angle Adapter.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/metal-52-ac.md](../regulatory/metal-52-ac.md).
