# SXT 2

> Source: https://manual.mikrotik.com/hardware/sxt-2
>
> Category: Wireless systems

*[Figure]*

## [SXT 2](https://mikrotik.com/product/RBSXTG-2HnDr2-168) (RBSXTG-2HnD)

SXT is an outdoor wireless router that can be used as a CPE in a PtM setup, or for point-to-point links. Please ensure the device is correctly mounted, with the cable pointing straight down.

## Assembly and mounting

With the clip pointed forward, slide the mounting bracket into the rail on the bottom of the case, until the clip clicks into place. The SXT comes bundled with a hose clamp, guide the clamp through the opening in the bracket and around the pole where it will be mounted. Tighten the hose clamp screw when alignment is complete. Two screw holes are provided as additional security against accidental bracket movement.
The SXT device has a sliding door, behind which the Ethernet port and the reset jumpers are located. This door can be also secured shut with a screw in the provided screw hole.

## Quickstart

- Open the ethernet door to connect an ethernet cable to the ethernet port, connect the other end of the ethernet cable to the included PoE injector.
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

## Powering

The device only accepts 8-32 V power from Passive PoE injectors (one power supply and PoE injector are included).

## Extension slots and ports

- One Ethernet (10/100 Mbit or Gigabit, depends on model), supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated Wireless with a built-in directional antenna, max gain 16 dBi.

## Mounting

SXT designed to be mounted on the pole, the package includes a mounting bracket and steel clamp.

- With the clip pointed forward, slide the mounting bracket into the rail on the bottom of the case, until the clip clicks into place.
- Guide the clamp through the opening in the bracket.
- Attach the unit to a pole, with the Ethernet port pointing downward.
- Use a PH2 screwdriver to tighten the rings when the alignment is complete.
- Fix the Ethernet cable to the pole using zip ties, less than one meter from the unit, to avoid the cable being pulled out of the port.
- Check mounting angle and positioning.
  When using both Ethernet ports, make sure to cut a wider cable opening in the plastic door. You can use pliers to tear out the plastic piece that is protecting the cable opening. When closing the plastic door, make sure to apply pressure, until it "clicks" into place.
  *Mounting and configuration of this device should be done by a qualified person.*

When mounting on the wall, please ensure that the cable feed is pointing downwards.
The IPX rating scale of this device is IP54. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body.

## Grounding

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw behind the case door. Attach your grounding wire to the grounding screw, then attach the other end of the grounding wire to the grounded mast. This is to substantially reduce the risk of ESD and lightning damage.

## Buttons and jumpers

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.
  The device includes a grounding connection behind the ethernet port door (a screw or a metal loop, depending on the model), which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage.

## Included parts

Steel clamp - 25 - 70mm.

Gigabit PoE injector.

Adapter 24 V 0.38A.

## Operating system support

The device only supports RouterOS software with version number 6.46 at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/sxt-2.md](../regulatory/sxt-2.md).
