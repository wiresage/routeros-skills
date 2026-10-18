# NetMetal-series

> Source: https://manual.mikrotik.com/hardware/netmetal-series
>
> Category: Wireless systems

*[Figure]*

## [NetMetal 5](https://mikrotik.com/product/RB922UAGS-5HPacD-NM) (RB922UAGS-5HPacD-NM)

> **This article covers**
>
> - **[NetMetal 5](https://mikrotik.com/product/RB922UAGS-5HPacD-NM)**
> - **[NetMetal 5SHP](https://mikrotik.com/product/RB921UAGS-5SHPacD-NM)**
> - **[NetMetal 5 triple](https://mikrotik.com/product/RB922UAGS-5HPacT-NM)**
> - **[NetMetal 5SHP triple](https://mikrotik.com/product/RB921UAGS-5SHPacT-NM)**

The NetMetal is a solid and waterproof outdoor device. It has a high power wireless interface, and one Gigabit Ethernet connector, which supports MDI-X auto-detection. The device has two or three RP-SMA connectors for connecting external antennas (depends on model). The device is packaged with a 24 V power adapter, a PoE injector, and two mounting loops. There are four models available – two Three-chain devices (with miniPCIe slot and without), and two Dual-chain models (with miniPCIe slot and without). Extra places for more RP-SMA connectors are available on the unit in this case.

## Quickstart

- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Access **WebFig** by opening <https://192.168.88.1>, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and click on the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- DHCP Client enabled on the bridge;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the "QuickSet, CPE" menu set up the following: Choose your country, to apply country regulation settings;
- Set the antenna gain, depending on the antenna used;
- Set up your router password in the bottom field.

## Mounting

The NetMetal is designed to be used outdoors and mounted on pole or DIN rail.

When mounting, please ensure that the cable feed is pointing downwards.
The IP rating scale of this device is IP66. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.Mounting and configuration of this device should be done by a qualified person.The mounting hose clamp is provided with the package.

*[Figure]*

- Guide hose clamp through the opening on the back of the device.
- Attach to the pole or mast.
- Align and secure by hose clamp screw using HEX3 screwdriver.
- The device should be always placed by TOP cover facing upwards.
  *[Figure]*
- When mounting on the DIN rail, please find a special bracket in the package and secure it with four screws to the back of the unit.

*[Figure]*

- With the attached mounting bracket you will be able to slide the device on the DIN rail.

## Powering

The ethernet port accepts passive Power over Ethernet 8-30 V DC. The package contains a 24 V adapter and a PoE injector. The maximum power consumption of the device is 21 W at 24 V.

## Configuration

The device is configured as a bridge, with all interfaces bridged and DHCP Client enabled.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).

## Extension slots and ports

- Built-in 5GHz 802.11ac/a/n wireless, AP/station/bridge modes supported (for CPE, AP, PtP modes)
- One 10/100/1000 Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or crossover cable for connecting to other network devices. The Ethernet port accepts 8-30 V DC powering from a passive PoE injector.
- One USB 2.0 or 3.0 port (depends on model) for extra storage or 3G/4G modem

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode for managing the unit from a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.
We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/netmetal-series.md](../regulatory/netmetal-series.md).
