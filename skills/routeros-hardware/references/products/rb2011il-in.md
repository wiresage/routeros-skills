# RB2011iL-IN

> Source: https://manual.mikrotik.com/hardware/rb2011il-in
>
> Category: Ethernet routers

*[Figure]*

## First use

- Choose your powering solution, please see the (link) on how to connect.
- The device will boot up and after the short beep, the network will be available for connecting.
- Set your computer IP configuration to automatic (DHCP).
- Once connected to the network, open <https://192.168.88.1> in your web browser to start configuration, since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Set up your password on the screen that loads.

## Powering

The device accepts powering from either the power jack or from the LAN1 Ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside diameter, female, pin positive plug) accepts 8-30 V DC (overvoltage protection starts at 30 V).
- Eth1 port accepts 8-30 V DC input (at the board; higher voltage needed to compensate for power loss on long cables) from non-standard (passive) Power over Ethernet injectors. The board does not work with IEEE802.3af compliant 48 V power injectors.
  Maximum power consumption 6 W, with attachments 18 W.

### Connecting to a POE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Power output

The PoE on Ether10 outputs approximately 2 V below input voltage and supports up to 0.58 A (So provided 24 V PSU will provide 22 V at 0.58 A output to the Ether5 PoE port).

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the front of the unit.
Alternatively, the unit can be mounted on the wall, the kit can be obtained separately, please visit our product page for detailed info: <https://mikrotik.com/product/RBWMK>
Grounding screw is located on the backside of the device case, please connect it accordingly to efficient ground.

*[Figure]*

When mounting on the wall, please ensure that cable feed is pointing downwards.
The IPX rating scale of this device is IPX0. We recommend using Cat6 shielded cables.

## Extension slots and ports

- Five 10/100/1000 (Gigabit) Ethernet ports (Auto MDI/X)
- Five 10/100 (Fast) Ethernet ports (Auto MDI/X)
- Ether10 supports 500 mA output power, ~2 V below the input voltage. Power out support auto-detect to protect non-PoE devices.

## Buttons and jumpers

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and bridge all interfaces.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/RB2011iL-IN>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

*[Figure]*

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb2011il-in.md](../regulatory/rb2011il-in.md).
