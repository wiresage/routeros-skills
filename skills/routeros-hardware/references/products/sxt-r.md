# SXT R

> Source: https://manual.mikrotik.com/hardware/sxt-r
>
> Category: LTE products

*[Figure]*

## [SXT R](https://mikrotik.com/product/sxt_r) (RBSXTR)

The SXT R comes without modem, it has built-in LTE antenna, two 10/100 Ethernet connectors which support MDI-X auto-detection. There are two micro SIM card slots available, to switch between cell providers. See the [SXT R product page](https://mikrotik.com/product/sxt_r) for full specifications and brochures.

## First use

- Open the bottom lid.
- Install the desired card into miniPCIe slot, refer to paragraph (link).
- Insert the micro-SIM cards into the micro-SIM slots (SIM A slot is a default).
- Connect the device to the power source (see "SXT kit-series#Powering").
- Once the device is powered on and PC connected to the device, open <https://192.168.88.1>

in your web browser or WinBox to start the configuration (or, for some models, check user and wireless passwords on the sticker).

- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen.
- You should select the "Check for updates" button on the right side and update your RouterOS software to the latest version to ensure the best performance and stability. Must have an internet connection and a valid SIM card.
- To manually update the device, go to our web page and download the latest (MIPSBE) software packages to your PC.
- Open Web browser or WinBox and upload packages to the Files menu and reboot the device.
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to login next time.
- Select the "Apply Configuration" to save changes.

## Extension slots and ports

- Two 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- MiniPCIe slot and two SIM slots (can't be used separately) to be used with a 3G/4G/LTE modems.
- The Mode button allows you to run any script when the button is pushed.

## Powering

The device accepts 18-57 V DC passive and 802.3af/at PoE power from the Ethernet port ETH1. The package contains a 24 V adapter and a passive PoE injector. Power consumption without attachments up to 6 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## MiniPCIe slot usage

This SXT version is without a factory modem installed. In order to install the module, you will need to remove the plastic top and withdraw the PCB plate from the bottom case. Installing a miniPCIe module should be done by a qualified person, follow safety precautions when handling electrical equipment:

*[Figure]*

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
- Removing the top cover, insert plastic tool in one of the six holes, turn slightly to the side and twitch carefully to slightly release the cover from holding into the place.
- Continue to work around until all of the clamps are released.
- Remove the top cover by lifting it up.
- You will access the upper side of PCB and antenna, remove two black soft pads to access PCB holders.
- Push both plastic holders to opposite sides to release the PCB board from its position.
- Remove the PCB board, carefully lift it up and place it on the anti-static mat.
- Locate the mini PCIe slot on the bottom of the PCB and remove two factory attached screws.
- Attach provided a thick thermal pad to the card.
- Install the card into a miniPCIe slot so that the thermal pad is between PCB and card.
- The secure card in place using previously removed two screws.
- Attach the grey uFL connector to the MAIN antenna connector of the modem, attach the black cable to the secondary (or AUX) connector. Use silicone type rubber to secure wiring in place.
- Attach a thinner thermal pad to the top of the card.
- Reassembly in backorder.
  After you have reinserted the device into the case, slide in the SIM cards from your mobile operator into the SIM slots, with the chips facing down.

## Mounting

SXT designed to be mounted on the pole, the package includes mounting bracket and steel clamp.

*[Figure]*

- With the clip pointed forward, slide the mounting bracket into the rail on the bottom of the case, until the clip clicks into place.
- Guide the clamp through the opening in the bracket.
- Attach the unit to a pole, with the Ethernet port pointing downward.
- Use a PH2 screwdriver to tighten the rings when alignment is complete.
- Fix the Ethernet cable to the pole using zip ties, less than one meter from the unit, to avoid the cable being pulled out of the port.
- Check mounting angle and positioning.
  When mounting outdoors, ensure that any cable openings are directed downwards. Use POE injector and proper grounding, this device has specially designed grounding connector under the port cover. Recommended using Cat5/6 cable. The IP rating scale for this device is IP54.
  The SXT device has a sliding door, behind which the Ethernet ports and the reset buttons are located. This door can be also secured shut with a screw in the provided screw hole.
  When using both Ethernet ports, make sure to cut a wider cable opening in the plastic door. You can use pliers to tear out the plastic piece that is protecting the cable opening. When closing the plastic door, make sure to apply pressure, until it "clicks" into place.
  *Mounting and configuration of this device should be done by a qualified person.*

## Grounding

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw behind the case door. Attach your grounding wire to the grounding screw, then attach the other end of the grounding wire to the grounded mast. This is to substantially reduce the risk of ESD and lightning damage.

## LED indicators

- The power LED indicates that the unit is receiving power in the ETH1 port.
- LTE LED indicates that the device is currently connected to a cellular tower.
- LTE Signal LEDs display the strength of the cellular signal.
- PoE LED indicates that the ETH2 port is currently powering another device with PoE.

## Reset button

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. The mode button can be configured in RouterOS menu /system routerboard mode-button.

## Accessories

Package includes the following accessories that come with the device:

*[Figure]*

## Specifications

For more information about this product, specification and pictures visit our web page: <https://mikrotik.com/product/sxt_r>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## SIM slot usage

*[Figure]*

SIM card slot is designed to use with Micro SIM cards.

Nano SIM cards have different thickness, usage with adapter are not recommended.

250

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/sxt-r.md](../regulatory/sxt-r.md).
