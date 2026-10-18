# hAP ac3 LTE6 kit

> Source: https://manual.mikrotik.com/hardware/hap-ac3-lte6-kit
>
> Category: LTE products

*[Figure]*

## [hAP ac3 LTE6 kit](https://mikrotik.com/product/hap_ac3_lte6_kit) (RBD53GR-5HacD2HnD&R11e-LTE6)

The hAP ac3 LTE6 kit is a simple home wireless access point. It is configured out of the box, you can simply insert your SIM card and start using wireless internet. See the [hAP ac3 LTE6 kit product page](https://mikrotik.com/product/hap_ac3_lte6_kit) for full specifications and brochures.

## Quickstart

follow these quick steps to set up your device:

- Insert micro SIM card into the slot;
- After inserting the SIM card close to the SIM port lid, do not remove the card while the device is powered on.
  *[Figure]*
- Connect the device to the power source (see "");
- Open network connections on your PC, mobile phone, or other device and search for MikroTik wireless network and connect to it;
- The configuration has to be done through the wireless network using a web browser or mobile app - (see ""). Alternatively, you can use a WinBox configuration tool <https://mt.lv/winbox> Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, user name: a*dmin* and there is no password by default (or, for some models, check user and wireless passwords on the sticker);
- When using a mobile application choose Quick setup and it will guide you through all necessary configuration in six easy steps;
- Select the "Check for updates" button on the right side and update your RouterOS software to the latest version, must have a valid SIM card inserted;
- To personalize your wireless network, SSID can be changed in the fields "Network Name";
- Choose your country on the left side of the screen in the field "Country", to apply country regulation settings;
- Set up your wireless network password in the field "WiFi Password" the password must be at least eight symbols;
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to login next time;
- Select the "Apply Configuration" to save changes.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Select Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Powering

The device accepts powering from the adapter:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) 12-28 V DC⎓.
  The power consumption under maximum load can reach 16 W, with attachments 22 W.

## Base plate mounting instruction

- The base plate comes with the package, in order to assemble follow these instructions.
- Place the small tip of the base plate into the case on the bottom of the device and fold it down.
  *[Figure]*
- While holding with both hands, use fingers to slightly press it and push down till it locks, follow the sequence on the illustration.
  *[Figure]*

## Configuration

Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the back of the unit.

The mounting base can be attached to the wall with the provided screws:

- Attach the base to the wall, using provided screws;
  *[Figure]*
- Attach the unit to the mounting base by following previously instructions in the base plate section.*For optimal performance, ensure good airflow and place the device on the stand in an open space.*
  Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

## Extension slots and ports

- Five Gigabit Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- Integrated Wireless 5GHz, 802.11a/n/ac and 2.4 GHz b/g/n.
- SIM slot.

## Buttons and jumpers

The **reset button** has the following default functions, or can be modified to run scripts:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

The **Mode Button** enables the execution of custom scripts, that can be added by the user.

The **front blue LED button**, enables WPS mode.

## Status LEDs

The front LED bar displays cellular modem received signal strength.

System LED have alternate modem mode indications, when cellular modem interface is enabled, System LED have have alternate indications:

blinking - connection establishment in progress, modem registered in cellular network, APN is not activated yet

red - established connection in 2G mode

yellow - established connection in 3G mode

blue - established connection in LTE mode

blinking red - SIM card not inserted

## Accessories

The package includes the following accessories that come with the device:

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Datasheet for any device is available on the official manufacturer website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).

make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hap-ac3-lte6-kit.md](../regulatory/hap-ac3-lte6-kit.md).
