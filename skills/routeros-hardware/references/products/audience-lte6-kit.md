# Audience LTE6 kit

> Source: https://manual.mikrotik.com/hardware/audience-lte6-kit
>
> Category: LTE products

*[Figure]*

## [Audience LTE6 kit](https://mikrotik.com/product/audience_lte6_kit) (RBD25GR-5HPacQD2HPnD&R11e-LTE6)

The Audience LTE6 kit is a home access point with a built-in LTE modem. You can extend the wireless coverage by adding more Audience devices to the network — they form a single network with the same SSID, so your devices can roam freely within its range.

## Connecting

- Insert Micro SIM card see (SIM slot usage).
- Plug the included power adapter to start up the device (see "").
- The device will boot up, the front led indicator will light in solid blue, and the Wireless network will be available for connecting.
- Open network connections on your PC, mobile phone, or other device and search for MikroTik wireless network and connect to it.
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker). For mobile phones use the application (see "").
- Select the "Check for updates" button and update your RouterOS software to the latest version, need to have a valid SIM card.
- Choose WebFig tab, on the left menu, choose CAPsMAN.
- Select the Security Cfg.
- Select to add new:Choose Authentication Type: WPA PSK, WPA2 PSK;Encryption: aes ccm;Passphrase: strongwirelesspassword;
  *[Figure]*
- Select OK.
- Select the Configurations tab.
- Choose one interface example: cfg-2ghz.
- Find the Security and choose the previously created profile: security1.
- Find the Country and set your Country.
- Select OK.
- Same for the cfg-5ghz-ac interface.
- On the left menu choose System>Password.
- Enter the password for the device and select Change.
  To add another Audience device to the network (see "").

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Select Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Powering

The device accepts power from the power jack or from the Ethernet port:

- Provided direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-57 V DC ⎓.
- Ethernet 1 port accepts Passive PoE 24-57 V DC ⎓.
  The power consumption under maximum load can reach 30 W.
  **Connecting to a POE Adapter.** POE adapter is not included in a package, if you consider using it, follow these steps:
- Connect the Ethernet cable from the Audience to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Mounting

The device is designed to be used indoors and placed on a flat surface with all needed cables connecting to the back of the unit. The IPX rating scale of IPX0. You should use Cat6 shielded cable for Audience devices.
*Warning! This equipment should be installed and operated with a minimum distance of 50 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.*

## Configuration

Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see section .

## Extension slots and ports

- Two Gigabit Ethernet ports.
- Integrated Wireless 2.4 GHz 802.11b/g/n, antenna gain 3.5 dBi.
- Integrated Wireless 5.0 GHz 802.11a/n/ac, antenna gain 4.5 dBi. 5180 – 5320 MHz.
- Integrated Wireless 5.0 GHz 802.11a/n/ac, antenna gain 4.5 dBi. 5500 – 5825 MHz.
- Audience LTE6 kit - MiniPCIe slot with factory-installed R11e-LTE6 card and SIM slot.

## Buttons and jumpers

The reset button functions as described below:

- Hold this button before applying power, release after three seconds since powering, to load backup Boot loader. This might be necessary if the device is not operating because of a failed RouterBOOT upgrade. When you have started the device with the backup loader, you can either set RouterOS to force backup loader in the RouterBOARD settings or have a chance to reinstall the failed RouterBOOT from an fwf file (total 3 seconds).
- If you keep holding this button for 2 more seconds until the green LED light starts flashing, release the button to reset RouterOS configuration to default (total 5 seconds).
- To connect this device to a wireless network managed by CAPsMAN, keep holding the button for 5 more seconds, LED turns solid green, release now to turn on CAPs mode (total 10 seconds).
- Or Keep holding the button for 5 more seconds until the green LED turns off, then release it to make the RouterBOARD look for Netinstall servers. You can also simply keep the button pressed until the device shows up in the Netinstall program on Windows (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

### WPS Sync button

Use the WPS Sync button to expand your wireless repeater network coverage by adding multiple Audience devices to it.

- On the chosen Audience AP, push the "WPS-Sync" button once, to turn on WPS mode for two minutes and make it wait for Audience repeater. The status LED will blink green.
- The Audience repeater needs to be booted with pressed "WPS-Sync" button for the device to configure itself according to the "WPS-Sync" mode and to connect to the Audience AP. Release the "WPS-Sync" button when the status LED is blinking amber.
- If the Audience repeater fails to connect to the Audience AP, then connecting can be repeated through RouterOS or by pressing "WPS-Sync" button and releasing after 5 seconds, the device will turn on "WPS-Sync" mode for two minutes and search for Audience AP. Status LED will blink amber.
- To add a third Audience repeater to your network, push the "WPS-Sync" button on the second Audience in your network, then boot the third unit with the "WPS-Sync" button pressed. Repeat with as many units as needed, adding more devices to your network.

## Front status LED behavior

- Solid blue – the device is powered on.
- Blinking green – the device is in Access Point mode and waits for another Audience device to be connected.
- Blinking amber (Red + Green) – the device searches and tries to connect to another Audience device.
- Solid green – the device has established a connection in an Audience network.
- Blinking Red – the device runs radar detection for Dynamic Frequency Selection (DFS).

## SIM slot usage

SIM card slot is designed to use with Micro SIM cards.

- Nano SIM cards have different thickness, usage with adapters are not recommended.
  *[Figure]*

## Accessories

*[Figure]*

## Specifications

For more information about this product, specifications, and pictures visit our web page: <https://mikrotik.com/product/audience_lte6_kit>

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

make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/audience-lte6-kit.md](../regulatory/audience-lte6-kit.md).
