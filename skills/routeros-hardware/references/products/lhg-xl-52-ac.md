# LHG XL 52 ac

> Source: https://manual.mikrotik.com/hardware/lhg-xl-52-ac
>
> Category: Wireless systems

*[Figure]*

## [LHG XL 52 ac](https://mikrotik.com/product/lhg_xl_52_ac) (RBLHGG-5HPacD2HPnD-XL)

Extremely powerful dual-band backbone / CPE for long-distance connection without downtime. See the [LHG XL 52 ac product page](https://mikrotik.com/product/lhg_xl_52_ac) for full specifications and brochures.

## Quickstart

Please follow these quick steps to set up your device:

- Assemble unit (see [Assembling](#assembling)).
- Open the Ethernet door.
- Connect the device to the PoE (see [Connecting to a PoE Adapter](#connecting-to-a-poe-adapter)).
- Mount unit (see [Mounting](#mounting)).
- Open network connections on your PC, mobile phone or other device and search for MikroTik wireless network and connect to it.
- The configuration can be done through the wireless network using a web browser or mobile app - (see [Configuration](#configuration)). Alternatively, you can use the **WinBox** configuration tool <https://mt.lv/winbox>.
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, user name: **admin** and there is no password by default (or, for some models, check user and wireless passwords on the sticker).
- When using a mobile application choose Quick setup and it will guide you through all necessary configuration in six easy steps.
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, to apply country regulation settings and set up your password on the screen that loads.

## Powering

The device accepts the power to the Ethernet port:

- PoE 802.3af/at 12-57 V DC ⎓.
  The power consumption under maximum load can reach 18 W. Without attachments 16 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Assembling

The device needs to be assembled from four parts, LHG dish, two legs and, the main body.

- Attach two legs to the main body, legs are different and marked with L and R.
- Attach the assembly to the dish.
- Secure with provided screws using PH2 screwdriver.

*[Figure]*

## Mounting

The LHG XL ac is designed to be used outdoors and mounted on pole or mast. The package includes an adjustable mounting assembly.

When mounting, please ensure that cable feed is pointing downwards.
The IP rating scale of this device is IP54. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference. Mounting and configuration of this device should be done by a qualified person.

The Mounting assembly is provided with the package.

*[Figure]*

- Attach the mounting assembly to the back of the dish using four screws.
- Attach the unit to the pole using U clamp placing washers and nuts in order as shown on the illustration.
- Align the unit accordingly to the signal and secure nuts.
- The device should be always placed by UP arrow facing upwards.
  *[Figure]*

## Grounding

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded.
The device includes a grounding wire attachment connector behind the Ethernet door. Attach your grounding wire to the grounding connector, then attach the other end of the grounding wire to the grounded mast.
Please secure all loose Ethernet cables and antenna cables to the pole or mast approximately 30cm from the device, so that the cable weight is not pulling the ports and connectors.

## Front status LED behavior

RouterOS allows configuring each LED's activity the way that the user wishes. It is possible to configure the LEDs to display wireless strength, blink the LEDs on interface traffic activity and many other options. For further information please visit the [LEDs](https://manual.mikrotik.com/docs/hardware/leds) manual page.
Default factory configuration for this device:

*[Figure]*

- Green LED the fourth level of signal strength.
- Green LED the third level of signal strength.
- Green LED the second level of signal strength.
- Green LED the first level of signal strength.
- Solid Green – Active SFP port.
- Solid Green – Active Ethernet port.
- Solid Green – User-defined LED.
- Solid Blue – The device is powered on.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Configuration

The device is configured as a wireless client, you will need to select AP to connect and set up a password.
We recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. Please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see a section [Reset button](#reset-button).

## Extension slots and ports

- Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- SFP port.
- Integrated Wireless module operating at 2.4 GHz, 802.11b/g/n protocol.
- Integrated Wireless module operating at 5 GHz, 802.11a/n/ac protocol.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RBLHGG-5HPacD2HPnD-XL look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU Switching Power Supply 24 V ⎓ 1.2 A 28.8 W 86.8 % VI 220 cm RA DC plug mod Hor shorter plug.
- Gigabit POE injector.
- LHG case
- LHG legs L, R.
- LHG XL 550mm Dish
- Montage assembly
- LHG 2 fastening set.
- LHG 60 fastening set.
  Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Specifications

For more information about this product, specifications, pictures, downloads and test results please visit our web page: <https://mikrotik.com/product/lhg_xl_52_ac>

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/lhg-xl-52-ac.md](../regulatory/lhg-xl-52-ac.md).
