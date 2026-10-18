# NetBox 5 ax

> Source: https://manual.mikrotik.com/hardware/netbox-5-ax
>
> Category: Wireless systems

*[Figure]*

## [NetBox 5 ax](https://mikrotik.com/product/netbox_5_ax) (L11UG-5HaxD-NB)

A Wi-Fi 6 upgrade of the popular NetBox 5. AP/CPE/Point-to-point – it can do it all! PoE-in, DC jack, Gigabit Ethernet, durable outdoor enclosure, modern dual-core ARM CPU, Wi-Fi-6 5GHz wireless. See the [NetBox 5 ax product page](https://mikrotik.com/product/netbox_5_ax) for full specifications and brochures.

## Quickstart

Please follow these quick steps to set up your device:

- Remove the upper cover (see [Removing upper cover](#removing-upper-cover));
- Please attach antennas to the SMA connector (see [Antenna usage](#antenna-usage)) before connecting to the power source;
- Open the bottom cover (see [Opening bottom cover](#opening-bottom-cover));
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

The device accepts power in the following ways:

- Ethernet port accepts Passive PoE 18-28 V DC ⎓.
  The device consumes a maximum of 6W without attachments. Under maximum load, its power consumption can reach up to 15W.

### Connecting to a PoE Adapter

- Connect the device to the included PoE injector using an Ethernet cable, attaching it to the data+power or PoE-out port;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector.

## Removing upper cover

*[Figure]*

- To remove the upper cover, press both side clips.
- Pull cover to the side while holding the body. When assembling please not mark on the top cover or reference.

## Opening bottom cover

- To open the bottom cover, unscrew the locking screw.
- Pull cover slightly from the device body.

*[Figure]*

*[Figure]*

- Lift it, but do not remove it completely.

## Extension slots and ports

- Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.
- USB type A port.
- 2 External SMA antenna connectors.
- Integrated Wireless module operating at 5 GHz, 802.11a/n/ac/ax protocol.

## Mounting

The NetBox 5 ax is designed to be used outdoors and mounted on a pole or DIN rail.When mounting, please ensure that the cable feed is pointing downwards.
The IP rating scale of this device is IP54. We recommend using Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 240 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.
*Mounting and configuration of this device should be done by a qualified person.*

### Mounting on the pole

The Mounting hose clamp is provided with the package.

- Guide hose clamp through the opening on the back of the device and attach it to the mast.
- Align and secure with hose clamp screw using PH2 screwdriver.
- The device should be always placed by TOP cover facing upwards.

*[Figure]*

- Connect your antenna.
  *[Figure]*
- The antenna is no provided with the device only for illustration purposes.

## Grounding

The installation infrastructure (towers and masts), must be properly grounded.
Please secure all loose Ethernet cables and antenna cables to the pole or mast approximately 30cm from the device, so that the cable weight is not pulling the ports and connectors.

### Mounting using DIN rail

*[Figure]*

When mounting on the DIN rail, please find a special bracket in the package and secure it with four screws to the back of the unit. With the attached mounting bracket you will be able to slide the device on the DIN rail.

## Front status LED behavior

The LEDs are located under the bottom cover.

*[Figure]*

RouterOS allows configuring each LED's activity the way that the user wishes. It is possible to configure the LEDs to display wireless strength, blink the LEDs on interface traffic activity and many other options. See the [LEDs](https://manual.mikrotik.com/docs/hardware/leds) page for further information.
Default factory configuration for this device:

*[Figure]*

- Solid Blue – The device is powered on.
- Solid Green – Indicates the device's state while powering it up into different modes, such as resetting the configuration or booting device for the Netinstall utility.
- Solid Green – Active Ethernet port.
- 4-8 Solid Green – The set of five green LEDs, shows the signal strength.

## Configuration

We recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. Please make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox> be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). Check additional help from your local trainers or become a trainer of yourself. <https://mikrotik.com/training/about>
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

The package includes the following accessories that come with the device:

- EU/US Switching Power Supply 24 V DC ⎓, 1.2 A, 28.8 W.
- Hose clamp 35/70 w4 A2 9 mm.
- Gigabit POE injector cable with shielded connector (RBGPOE).
- K-27 din-rail bracket mounting set.

## Antenna usage

*[Figure]*

To connect to the external antenna please use, the "Flex-guide" - can be obtained separately. A super low loss 50cm long RPSMA cable for superior connection quality, suited for indoor and outdoor use, this cable provides superior matching and loss values. <https://mikrotik.com/product/ACRPSMA>
SMA connectors located under the upper cover (see [Removing upper cover](#removing-upper-cover)) to access them.

Please connect and disconnect the antenna, when the device is turned off!

See [Wireless Interface](https://manual.mikrotik.com/docs/wireless/abgn/wireless-interface) for configuration information.

## Specifications

For more information about this product, specifications, pictures, downloads, and test results please visit our web page: <https://mikrotik.com/product/netbox_5_ax#fndtn-specifications>

<https://i.mt.lv/cdn/product_files/NetBox5ax_240425.pdf>

L11UG-5HaxD-NB-US (USA) is factory locked for 5170-5330MHz, 5490-5730MHz and 5735-5835MHz frequencies. This lock can not be removed.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/netbox-5-ax.md](../regulatory/netbox-5-ax.md).
