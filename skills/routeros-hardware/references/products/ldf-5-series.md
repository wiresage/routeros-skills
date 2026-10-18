# LDF 5-series

> Source: https://manual.mikrotik.com/hardware/ldf-5-series
>
> Category: Wireless systems

*[Figure]*

## [LDF 5 ac](https://mikrotik.com/product/ldf_5_ac) (RBLDFG-5acD)

The LDF (Lite dish feed) is an outdoor wireless system with a built-in antenna, meant to be installed on satellite offset dish antennas.

## Assembly

The device is compatible with standard offset dishes, commonly used for satellite television. The offset mount is universal at 40 mm diameter, and the LDF can easily be placed inside it. To attach the Ethernet cable to the LDF unit, follow these steps:

- Assemble all components as shown in the illustration. If using pre-made cables, cut the rubber seal on one side, to put it onto the cable. Self crimped cables should be crimped after the seal is on the cable;
- Connect Ethernet cable to Ethernet connector on LDF;
- Attach Housing nut to LDF body by rotating clockwise;
- Slide rubber seal into housing nut, then seal the waterproof gland by turning compression nut clockwise.

*[Figure]*

## Assembling on dish

Please ensure to mount the LDF unit on the offset mount in the proper position as shown in the picture to the right. Unit facing upwards to the dish.

*[Figure]*

*[Figure]*

The dish will act as a reflector, amplifying the signal. The final position of your assembly should be placed and installed on the pole or wall as shown on the picture to the left.

## Mounting

The IP rating scale for this device is IP54.
The Device designed to use outdoors, please ensure that any cable openings are directed downwards. Use POE injector with Cat6 cable. Installation infrastructure (towers and masts), as well as the router itself, to be properly grounded.

*Mounting and configuration of this device should be done by a qualified person.*
*Warning! This equipment should be installed and operated with a minimum distance of 28 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.*

## Powering

The device accepts 10-28 V ⎓ DC input from passive Power over Ethernet injectors. The device does not work with IEEE802.3af compliant 48 V power injectors. A PoE injector is included in the package.
Maximum power consumption:

- LDF 5, 6 W;
- LDF 5 ac, 8 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

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

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Extension slots and ports

- Integrated wireless:
  LDF 5, 5 GHz, 802.11a/n;
  LDF 5 ac, 5 GHz, 802.11a/n/ac.
- One Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds);
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds);
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds);
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Specifications

For more information about this product, specifications, pictures, downloads and test results please visit our web page:

- LDF 5 - <https://mikrotik.com/product/rbldf_5nd>
- LDF 5 ac - <https://mikrotik.com/product/ldf_5_ac>

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point:

*[Figure]*

- Scan the QR code and choose your preferred OS.
- Install and open the application.
- Click Connect to establish a connection to your device through a wireless network (check the wireless passwords on the sticker).
- The username is "**admin**" and there is no password (or, for some models, check user and wireless passwords on the sticker).
- Choose Quick Setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## OEM statement

This module is intended for OEM installations only. As such the OEM integrator is responsible for ensuring that the end-user has no manual instructions to remove install or modify the module. This module is limited to installations in mobile or fixed applications. OEM integrators may utilize antennas of like an equal or lesser gain as appearing in the list in this document (reference 47 CFR, paragraph 15.204(c)(4) for further information on this topic. The MikroTik OEM RF Module complies with Part 15 of the FCC rules and regulations.
OEM Modules have been certified by the FCC for use with other products without any further certification (as per FCC section 2.1091). Separate approval is required for other operating configurations including portable configurations concerning to 47CFR paragraphs 2.1093 and different antenna configurations. The OEM is required to comply with all 47CFR labeling instructions and requirements for the finished products.
Changes or modifications not expressly approved by MikroTik could void the OEM authority to install or operate the equipment. OEMs must test their final product to comply with unintentional radiators (FCC section 15.107 and 15.109) before declaring compliance with their final product to Part 15 of the FCC Rules.
**WARNING**: the OEM must ensure that the FCC labeling requirements are met. This includes a visible labels on the outside of the OEM enclosure specifying the appropriate MikroTik OEM RF Module FCC identifier for this product as well as any other required FCC notices as presented above.
This enclosed device complies with 47CFR paragraph 15 C of the FCC rules and regulations. Operation is subject to the following two conditions: (1) this device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.
Labeling and text information should be of a size of type large enough to be readily legible, consistent with the dimensions of the equipment and the label.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ldf-5-series.md](../regulatory/ldf-5-series.md).
