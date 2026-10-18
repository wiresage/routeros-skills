# LHG R

> Source: https://manual.mikrotik.com/hardware/lhg-r
>
> Category: LTE products



## [LHG R](https://mikrotik.com/product/rblhgr) (RBLHGR)

*[Figure]*

LHG R without factory installed modem, you can choose your own solution.

## Quickstart

- While holding the unit by its central column, apply force to the tab, which holds the latch closed, until the latch pops open.
- Insert the SIM card into the slot, with chips facing UP.
- Install your desired modem.
- Assemble case by attaching legs to the base of the unit, see Case assembly paragraph.
- Mount unit in your desired place, see Mounting paragraph.
- Connect an Ethernet cable to the Ethernet port, connect the other end of the Ethernet cable to the included PoE injector.
- Plug the PoE injector into your PC.
- Plug the included power supply into the PoE injector to start up the device. See the powering paragraph.
- Set LAN computer IP configuration to *automatic* (DHCP).
- Open <https://192.168.88.1> in your web browser to start the configuration.
- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen (or, for some models, check user and wireless passwords on the sticker).
- Update the device by selecting the "Check for updates" button on the right side and updating your RouterOS software to the latest version to ensure the best performance and stability. Must have a valid SIM card inserted.
- To manually update the device, go <https://mikrotik.com/download>
- Choose MIPSBE packages for this device and download it to your PC.
- Upload downloaded packages to the WebFig "Files" menu and reboot the device. Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates.

## Extension slots and ports

- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices. The Ethernet port accepts 9-30 V DC powering from a passive PoE injector.
- MiniPCIe slot and SIM slot (can't be used separately) to be used with a 3G/4G/LTE modem.

## Powering

The device can be powered from 12-57 V 802.3af/at sources and also Passive PoE injectors (one power supply and PoE injector are included).
Maximum power consumption 6 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Opening the case cover

To access the miniPCIe slot, the opening of the unit's top cover is required. As an opening tool, you can use a large size flat head screwdriver or a small coin. Be extremely cautious when opening, because the incorrect opening of the clip can break it off!
*Mounting and configuration of this device should be done by a qualified person.*
Follow these steps:

*[Figure]*

Additional Caution when lifting up the cover, do not force it with sharp objects.

## miniPCIe slot usage

The device is equipped with a miniPCIe slot to be used with a 3G/4G/LTE modem. One SIM slot is provided for use together with a miniPCIe modem. The SIM slot is not used separately.
In this case, an internal antenna is not connected (located inside the enclosure). Installing a miniPCIe module should be done by a qualified person, follow safety precautions when handling electrical equipment:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
- Open the upper cover as shown on instruction previously.
- The antenna is located underneath PCB.
- Locate the miniPCIe slot on the PCB and remove two factory attached screws.
- Attach provided a thick thermal pad to the card, and install the card into miniPCIe slot so that the thermal pad is between PCB and card.
  *[Figure]*
- Insert your desired card.
- The secure card in place using previously removed two screws.
- Attach the black uFL connector to the MAIN antenna connector of the modem, attach the gray cable to the DIV connector.
- Attach a thinner thermal pad to the top of the card.
- Reassembly in backorder.
  After reassembly, slide in the SIM card from your mobile operator into the SIM slot, with the chips facing up as shown on the port label. The slot accepts MicroSIM (3FF).

## Assembly

- Attach the two legs to the LHG case by sliding them onto the respective sides, legs are different and cannot be exchanged (when looking at the product place it that cover for Ethernet port is in front of you, leg marked R is for the right side, leg marked L is for the left side).
- Snap the assembled LHG unit to the grid in the appropriate central location.
- Fix the two legs in place with included two self thread screws (Phillips screwdriver PH2).
  The package also contains a grounding cable connector and a 5-degree angle adapter, for easier up or downward tilt adjustment.

## Mounting

*[Figure]*

- Slide the included metallic mounting rings into the two slots on the back of the antenna dish.
- Attach the unit to a pole, with the Ethernet port pointing downward.
- Use a PH2 screwdriver to tighten the rings.
- Fix the Ethernet cable to the pole using zip ties, less than one meter from the unit, to avoid the cable being pulled out of the port.
- Check mounting angle and positioning.
- Optional: If required, before mounting the unit, you can insert the included 5-degree adjustment adapter into the top or bottom slot where the mounting ring is inserted. This will create an additional upward or downward angle when the unit is tightened to a vertical pole.
- Insert a 5-degree angle adapter to one of the slots and remount the unit.
  When mounting outdoors, ensure that any cable openings are directed downwards. Use POE injector and proper grounding, this device has specially designed grounding connector under the port cover. Recommended using shielded Cat5/6 cable. The IP rating scale for this device is IP54.

## Configuration

Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Reset button

The reset button has three functions:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.
  The device includes a grounding connection behind the Ethernet port door, which you should connect to the grounding installation of the tower or building where the device will be used. This is to substantially reduce the risk of ESD and lightning damage.

## Mode button

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. The mode button can be configured in RouterOS menu /system routerboard mode-button.

## Specifications

For more information about this product, specification and pictures visit our web page: <https://mikrotik.com/product/rblhgr>

## Accessories

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

*[Figure]*

*[Figure]*

*[Figure]*

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/lhg-r.md](../regulatory/lhg-r.md).
