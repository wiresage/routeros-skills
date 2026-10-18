# hEX S

> Source: https://manual.mikrotik.com/hardware/hex-s
>
> Category: Ethernet routers

*[Figure]*

### hEX S (RB760iGS)

hEX S is a six-port wired Gigabit router with SFP port and PoE output.

## First use

- Connect your Internet cable to one of the two ports labeled "Internet", depending on whether you will use an SFP module or Ethernet.
- Choose your powering solution, please see the section for possibilities.
- Connect your direct input power jack if not using POE, to start up the device.
- Connect your local network computers to ports 2-5 set your computer IP configuration to automatic (DHCP).
- The IP address from the local network is 192.168.88.1, use it in your browser to access the device user admin and no password (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Set up your password on the screen that loads.

## Mounting

This device is designed for use indoors by placing it on the flat surface or mounting on the wall, mounting points are located on the bottom side of the device, screws are not included in the package. Screws with size 4x25 mm fit nicely, depending on your wall structure you can use dowels 6x30 mm and 6 mm drill bit if needed.
When mounting on the wall, please ensure that cable feed is pointing downwards. We recommend using Cat6 shielded cable for our devices. The IP rating scale for this device is IPX0.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device from the network, see section Buttons

## Powering

The device accepts power from the power jack or from the first Ethernet port:

- Direct input power jack (5.5mm outside and 2mm inside, female, pin positive) accepts DC ⎓ 12-57 V.
- The first Ethernet port accepts passive or 802.3af/at Power over Ethernet in the range of DC ⎓ 12-57 V.
  The power consumption of this device under maximum load without attachments is up to 6 W.
  When using 802.3af/at to power this device, we recommend not using grounding for best compatibility.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Extension slots and ports

- Five individual 10/100/1000 Gigabit Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One SFP module cage supports 1.25G modules.
- MicroSD slot for expanding built-in storage.
- USB type-A.

## Buttons

### Reset button

The RouterBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green SFP LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the SFP LED turns solid green to clear all configuration and bridge all interfaces.
- Release the button after SFP LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

### Mode button

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. The mode button can be configured in RouterOS menu /system routerboard mode-button.

## Accessories

Package includes the following accessories that come with the device:

*[Figure]*

Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/hex_s>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hex-s.md](../regulatory/hex-s.md).
