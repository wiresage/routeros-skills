# SEXTANT G

> Source: https://manual.mikrotik.com/hardware/sextant-g
>
> Category: Wireless systems

*[Figure]*

## [SEXTANT G](https://mikrotik.com/product/RBSEXTANTG-5HPnD) (RBSEXTANTG-5HPnD)

The RouterBOARD SEXTANT G comes as a complete set and includes a built-in 802.11n dual chain wireless device and a dual-polarization 18 dBi antenna. It has one Gigabit Ethernet connector which supports MDI-X auto-detection. The package includes the SEXTANT G device, a power adapter, a Gigabit PoE injector and two hose clamps. See the [SEXTANT G product page](https://mikrotik.com/product/RBSEXTANTG-5HPnD) for full specifications and brochures.

## First use

- Connect an Ethernet cable to the port behind the small plastic door
- The SEXTANT G accepts 24 V Passive PoE from a *Gigabit PoE injector*
- The default IP address from LAN is 192.168.88.1 for configuration
- Username is **admin** and there is no password (or, for some models, check user and wireless passwords on the sticker)
- Choose your country, to apply country regulation settings.

## Powering

The board accepts power from the Ethernet port (Passive PoE) 8-30 V DC. The package contains a 24V adapter. The maximum power consumption of the device is 13.8 W.

## Mounting

With the clip pointed forward, slide the mounting bracket into the rail on the bottom of the case, until the clip clicks into place. The device comes bundled with a hose clamp - guide the clamp through the opening in the bracket and around the pole where it will be mounted. Tighten the hose clamp screw when alignment is complete. Two screw holes are provided as additional security against accidental bracket movement.
The device has a sliding door, behind which the Ethernet port and the reset jumpers are located. This door can be also secured shut with a screw in the provided screw hole. Built-in antenna is connected as follows: chain0 = horizontal polarization, chain1 = vertical polarization. This equipment should be installed and operated with a minimum distance of 30 cm between the radiator and any part of your body.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations. RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case the IP connection is not available, the WinBox tool
(<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). For recovery purposes, it is possible to boot the device from the network, see a section .

## Reset button

The reset button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/sextant-g.md](../regulatory/sextant-g.md).
