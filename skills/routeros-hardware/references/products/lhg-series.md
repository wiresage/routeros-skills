# LHG-series

> Source: https://manual.mikrotik.com/hardware/lhg-series
>
> Category: Wireless systems

> **This article covers**
>
> - **[LHG 2](https://mikrotik.com/product/lhg_2)** (RBLHG-2nD)
> - **[LHG 5](https://mikrotik.com/product/RBLHG-5nD)** (RBLHG-5nD)
> - **[LHG HP5](https://mikrotik.com/product/RBLHG-5HPnD)** (RBLHG-5HPnD)
> - **[LHG 5 ac](https://mikrotik.com/product/lhg_5_ac)** (RBLHGG-5acD)

## Quickstart

- Open the Ethernet door to connect an Ethernet cable to the Ethernet port, connect the other end of the Ethernet cable to the included PoE injector.
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

## Assembly and Mounting

- Attach the two legs to the LHG case.

*[Figure]*

## [LHG 5](https://mikrotik.com/product/RBLHG-5nD) (RBLHG-5nD)

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

## Powering

The device accepts powering only from Passive PoE injectors.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated 2x2 MIMO wireless device with a built-in grid antenna.
  LHG 2 Dual chain 18 dBi, 2.4GHz, 802.11b/g/n. Maximum power consumption 5 W.
  LHG 5 Dual chain 24.5 dBi, 5GHz, 802.11 a/n. Maximum power consumption 6 W.
  LHG HP5 Dual chain 24dBi, 5GHz, 802.11 a/n. Maximum power consumption 7 W.
  LHG 5 ac Dual chain 24.5dBi, 5GHz, 802.11 a/n/ac. Maximum power consumption 8 W.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset the RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode (total 10 seconds).
- Or keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- Mounting set for LHG-5.
- POE Injector/Gigabit POE injector(For LHGG-5acD).
- LHG-5G-390 mm Dish 3,0x2.5x0,5 mm.
- DC ⎓ EU/US Switching Power Supply 24 V, 0.38 A, 9 W, Level VI, cable:1.5 m).
- Hose Clamp SUS304 (philips type ; clamping diameter range 35-70 mm).

## Specifications

For more information about LHG products, specifications and pictures please visit our web page: <https://mikrotik.com/product/lhg_2>
<https://mikrotik.com/product/RBLHG-5nD>
<https://mikrotik.com/product/RBLHG-5HPnD>
<https://mikrotik.com/product/lhg_5_ac>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

*[Figure]*

*[Figure]*

*[Figure]*

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/lhg-series.md](../regulatory/lhg-series.md).
