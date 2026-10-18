# DynaDish 6

> Source: https://manual.mikrotik.com/hardware/dynadish-6
>
> Category: Wireless systems

*[Figure]*

## [DynaDish 6](https://mikrotik.com/product/dynadish_6) (RBDynaDishG-6HnD)

The Dynadish 6 uses the same effective antenna design and enclosure as our successful 5 GHz model, but this new device operates in the licensed 6GHz frequency. This means less interference than the often saturated 5 GHz frequencies for higher speed and more reach. By operating above the most popular WiFi frequencies you are now able to build your wireless links from busy towers without suffering problems with noise.

It is a simple and completely integrated product with everything you need to quickly install a reliable point to point link.

This product is not suitable for unlicensed ISM bands. Device use is subject to country regulations. Availability might be limited depending on distributor stock and country regulations.

## Quickstart

Please follow these quick steps to set up your device:

- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at <https://mt.lv/WinBox>; multiple configuration methods are available to ensure accessibility;
- Access **WebFig** by opening <https://192.168.88.1>, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and click on the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the "Quick Set" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Powering

The device accepts 12-30 V DC from Passive PoE injectors. Power consumption is up to 10 W.

## Booting process

The device is preconfigured as a wireless client (CPE), and all you need to do is select the AP to connect to and set a device password. You can do this in the quickSET tab that is loaded by default. In case IP connection is not available, WinBox can be used to connect to the MAC address of the device.
In case you wish to boot the device from the network, for example, to use MikroTik Netinstall, hold the RESET button of the device when starting it, until the LED light turns off, then the device will start to look for Netinstall servers.More information about using RouterOS and connecting to this device in our documentation: +<https://mt.lv/help##> Extension slots and ports

- One 10/100/1000 Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated wireless 802.11a/n, 2x2 MIMO with a built-in parabolic dish antenna, max gain 25dBi

## Buttons and jumpers

RouterBOOT reset button (RESET, front panel) has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds)
- Or Keep holding the button until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds)

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/dynadish-6.md](../regulatory/dynadish-6.md).
