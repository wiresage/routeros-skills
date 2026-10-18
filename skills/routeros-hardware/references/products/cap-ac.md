# cAP ac

> Source: https://manual.mikrotik.com/hardware/cap-ac
>
> Category: Indoor wireless

*[Figure]*

The cAP (RBcAPGi-5acD2nD) ac is a ceiling mountable wireless access point. It is already configured, you can simply plug in your ISP cable and start using wireless Internet.

## Connecting

- Remove metal ring see ;
- Connect POE to the Ethernet port 1, please see the section for instructions on how to connect POE.
- Set your computer IP configuration to *automatic* (DHCP).
- The device wireless access point mode is enabled by default.
- The device will boot up and Wireless network will be available for connecting.
- Open network connections on your computer and search for MikroTik wireless network - connect to it;
- The configuration can be done through the wireless network using a web browser or mobile app. Alternatively, you can use a WinBox configuration tool <https://mt.lv/winbox> Open <https://192.168.88.1> in your web browser to start configuration, user name: a*dmin* and there is no password by default (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the *"Support&Downloads"* menu;
- Upload downloaded packages to the **WebFig** or **WinBox** **Files** menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the *"QuickSet"* menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Removing mounting ring

The Mounting ring comes installed on the device, in order to access Ethernet ports please remove it by turning it counterclockwise and the ring will be released.

*[Figure]*

## Powering

The device accepts power from the Ethernet port, so you must either use the included passive PoE injector or make sure your switch supports passive or 802.3af/at PoE output.

- Ethernet port accepts 12-57 V DC **⎓** (802.3af/at or passive PoE).
  The power consumption under maximum load can reach 13 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Mounting

It is possible to attach the device to a wall or ceiling, using the provided mounting bracket on the back of the unit:

- Attach the mounting bracket to the wall or ceiling with provided three screws;
- Use 5 mm drill bit if necessary with provided dowels;
  *[Figure]*
- Connect needed cables to the device;
- If needed second mounting bracket can be used for additional support when working on thin ceilings or walls, provided screw length is 20 mm;
- Attach the second mount to the other side of the ceiling and secure with screws through the first mount;
- Attach the device to the mounting bracket and turn clockwise until the device secures in place;
  *Mounting and configuration of this device should be done by a qualified person.*
  Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

Operating humidity can be from 5% to 95% non-condensing.

## Configuration

By default, the device is configured as a wireless access point, with the first ethernet port (Eth1) configured as a DHCP client, and the second interface bridged together with the wireless interface. A DHCP server is configured on the bridge interface.
Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- Two 10/100/1000 Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices. The Eth2 port is capable of powering another RouterBOARD device with passive PoE (up to 57 V). The maximum output current is 500mA when using less than 30V to power this device and 400mA when using more than 30V.
- Integrated Wireless 2.4 GHz 802.11b/g/n, supports AP/CPE/P2P/repeater modes.
- Integrated Wireless 5 GHz 802.11a/n/ac.

## Buttons and jumpers

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

There are two mode buttons on this unit, but they both are performing the same action. The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. By default, the buttons will enable "dark mode", which disables beeps and LED lights. The mode button can be configured in the RouterOS menu /system routerboard mode-button.

## LED indicators

There are seven LED lights on the unit, which can be disabled altogether if necessary.

- User – user-configurable led for any desired script.
- 5G – 5GHz interface activity.
- 2G – 2.4 GHz interface activity.
- E2 – Ethernet 2 connected.
- E1 – Ethernet 1 connected.
- PoE LED indicates that the ETH2 port is currently powering another device with PoE.
- The power LED indicates that the unit is receiving power in the ETH1 port.

## Accessories

Package includes the following accessories that come with the device:

- K-46 mounting set.
- DC ⎓ EU/US Switching Power Supply 24 V, 1.2 A, 28.8 W, Level VI, cable:1.5 m.
- POE Injector with shielded ethernet cable/connector (RBPOE).
- cAP mount ceiling attachment.
- Case cover.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/cap_ac>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Datasheet for any device is available on the official manufacturer website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).

Please make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/cap-ac.md](../regulatory/cap-ac.md).
