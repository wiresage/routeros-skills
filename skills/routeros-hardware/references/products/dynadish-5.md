# DynaDish 5

> Source: https://manual.mikrotik.com/hardware/dynadish-5
>
> Category: Wireless systems

### DynaDish 5 (RBDynaDishG-5HacDr3)

*[Figure]*

## [DynaDish 5](https://mikrotik.com/product/RBDynaDishG-5HacDr3) (RBDynaDishG-5HacD)

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

The device accepts power to the Ethernet port - PoE 802.3af/at 24-57 V DC ⎓. Maximum power consumption 9 W.

## Configuration

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest visiting the RouterOS documentation page to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).

## Extension slots and ports

- One 10/100/1000 Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated Wireless 5 GHz 802.11a/n/ac, 2x2 MIMO with built-in parabolic dish antenna, max gain 24 dBi.

## Mounting

The device is designed to be used outdoors and mounted on a pole.

When mounting, please ensure that the cable feed is pointing downwards.
The IP rating scale of this device is IP54. We recommend using Cat6 shielded cables.The mounting and configuration of this device should be done by a qualified person.

- Attach provided mounting bracket with four screws to the device;
  *[Figure]*
- Attach to the pole or mast;
- Secure position with two screws;
- Align as needed and secure screws in step 3.
  *[Figure]*
- Note, the position of the ethernet cable must face down.Please secure all loose Ethernet cables and antenna cables to the pole or mast approximately 30cm from the device, so that the cable weight is not pulling the ports and connectors.

## Buttons and jumpers

The reset button has the following functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset the RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Included parts

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/dynadish-5.md](../regulatory/dynadish-5.md).
