# LHG Lite60

> Source: https://manual.mikrotik.com/hardware/lhg-lite60
>
> Category: 60 GHz products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/lhg-lite60-78d98dce5497554c58a20e9c0f69791e.pdf).

The LHG Lite 60 is an outdoor wireless router with a built-in directional antenna that works in the 60GHz spectrum. It can be used as a CPE to connect to MikroTik devices that work in 60GHz access point mode.

## Assembly

Attach the two legs to the LHG case, then snap the assembled LHG unit to the grid in the appropriate locations. Fix the legs in place with two self thread screws (Included, use Phillips screwdriver PH2). The package also contains a grounding cable connector and a precision alignment mount. Alignment instructions available on the product page on <https://mikrotik.com/products/>.

## Connecting

- Open the ethernet door to connect an ethernet cable to the ethernet port, connect the other end of the ethernet cable to the included PoE injector (LHG Lite60), or an 802.3af/at the power source (supported only by the LHG 60G model).
- Plug the PoE injector into your network switch or ISP internet outlet.
- Plug the included power supply into the PoE injector to start up the device.
- For configuration purposes, set your computer IP configuration to static in the range of 192.168.88.0-254 (/24 or 255.255.255.0)
- The default IP address of the unit is 192.168.88.1/24, open this address in your web browser to start the configuration. The username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker).
  The device is preconfigured as a w60g station, and all you need to do is select the AP to connect to and set a device password. You can do this in the quickSET tab that is loaded by default. In case the IP connection is not available, WinBox can be used to connect to the MAC address of the device. We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
  More information about using RouterOS and connecting to this device in our documentation: +<https://mt.lv/help##> Powering
  The LHG Lite60 only accepts 12-30 V power from Passive PoE injectors (one power supply and PoE injector are included). The LHG 60G accepts 12-57 V 802.3af/at powering and also Passive PoE. Both models can consume up to 5 W at maximum load.

## Extension slots and ports

- One ethernet (10/100 Mbit or Gigabit, depends on model), supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated w60g interface with a built-in antenna.

## Buttons and jumpers

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery. The device includes a grounding connection (marked ⏚) which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/lhg-lite60.md](../regulatory/lhg-lite60.md).
