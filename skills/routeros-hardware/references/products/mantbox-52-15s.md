# MANTBox 52 15s

> Source: https://manual.mikrotik.com/hardware/mantbox-52-15s
>
> Category: Wireless systems

*[Figure]*

## [mANTBox 52 15s](https://mikrotik.com/product/mantbox_52_15s) (RBD22UGS-5HPacD2HnD-15S)

mANTBox 52 15s. See the [MANTBox 52 15s product page](https://mikrotik.com/product/mantbox_52_15s) for full specifications and brochures.

## Quickstart

- Open the cover;
- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at <https://mt.lv/WinBox>; **multiple configuration methods are available to ensure accessibility;**
- Access **WebFig** by opening <https://192.168.88.1>, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and click on the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version. Must have a valid SIM card inserted and active Internet connection;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Powering

The device accepts power in the following ways:

- The Ethernet port accepts 802.3af/at PoE 12-57 V DC ⎓.
- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-57 V DC⎓.
  The power consumption under maximum load can reach 21 W.

## Mounting

The mANTbox comes with a QuickMount adapter that can be attached to a wall using the included screws, or attached to a pole, using the included metal mounting ring. The QuickMount allows the device to be adjusted horizontally and vertically.

- Attach the quick mount to the back of the device.
  *[Figure]*
- Attach the device to the pole and secure it with a provided steel clamp. Clamping diameter 35 – 70 mm.
  *[Figure]*
- Please avoid connecting a loose Ethernet cable to the Ethernet port, secure the cable to a wall or the pole, so that the cable weight is not pulling the port. It is recommended to secure the Ethernet cable less than 2m from the device. This is to ensure that the cable doesn't damage the port by its weight, or doesn't fall out.
  We recommend using Cat6 shielded cables.
  Warning! This equipment should be installed and operated with a minimum distance of 25 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.

## Configuration

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest visiting the RouterOS documentation page to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default).

First-time configuration <https://mt.lv/configuration>;

The device upgrade <https://mt.lv/upgrade>;

## Grounding

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw behind the case door. Attach your grounding wire to the grounding screw, then attach the other end of the grounding wire to the grounded mast. This is to substantially reduce the risk of ESD and lightning damage.

*[Figure]*

The device includes a grounding connection (marked ⏚).

## Opening cover

To open the cover, please turn the captive screw by hand anti-clockwise and lift it.

*[Figure]*

## Extension slots and ports

- Built-in wireless interface 5 GHz and 2.4 GHz.
- One SFP port for 1.25GBit modules, DDMI support.
- Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or crossover cable for connecting to other network devices.

## Buttons and jumpers

The reset button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- Switching Power Supply DC ⎓ 24 V;
- Hose Clamp, 35-70 mm;
- Fastening set K-41;
- Gigabit POE injector cable with shielded connector;
- Mounting bracket.
  Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/mantbox-52-15s.md](../regulatory/mantbox-52-15s.md).
