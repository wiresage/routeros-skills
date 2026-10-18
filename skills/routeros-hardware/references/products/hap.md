# hAP

> Source: https://manual.mikrotik.com/hardware/hap
>
> Category: Indoor wireless

hAP

*[Figure]*

The hAP is a simple home wireless access point. It is configured out of the box, you can simply plug in your internet cable and start using wireless internet. See the [hAP product page](https://mikrotik.com/product/RB951Ui-2nD) for full specifications and brochures.

## Connecting

- Connect your Internet cable to port 1, and local network PCs to ports 2-5.
- Set your computer IP configuration to *automatic* (DHCP).
- Wireless "access point" mode is enabled by default, you can connect to the wireless network name which starts with "MikroTik".
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button on the right side and updating your RouterOS software to the latest version to ensure the best performance and stability.
- To personalize your wireless network, SSID can be changed in the fields "Network Name".
- Choose your country on the left side of the screen in the field "Country", to apply country regulation settings.
- Set up your wireless network password in the field "WiFi Password" the password must be at least eight symbols.
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to login next time.
- Click on the "Apply Configuration" to save changes.

## Powering

The board accepts power from the power jack or the first Ethernet port (Passive PoE):

- Direct-input power jack (5.5mm outside and 2mm inside, female, pin positive plug) accepts 10-28 V ⎓ DC;
- The First Ethernet port accepts passive Power over Ethernet 10-28 V ⎓ DC.
  The power consumption under maximum load can reach 5 W.

## Connecting with a mobile app

*[Figure]*

Use your smartphone to access your router through WiFi.

- Insert the SIM card and power on the device.
- Scan QR code with your smartphone and choose your preferred OS.
- Connect to the wireless network. SSID starts with MikroTik and has the last digits of the device's MAC address.
- Open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Mounting

The device is designed to be used indoors, by placing it on the desktop.
We recommend using Cat5 shielded cable. When using and installing this device please pay attention to the Maximum Permissible Exposure (MPE) safety distance with a minimum of 20 cm between the radiator and your body.

## Extension slots and ports

- Five individual 10/100 Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- One Integrated Wireless 2.4 GHz 802.11b/g/n, 2x2 MIMO with two onboard PIF antennas, max gain 1.5 dBi
- One USB type-A slot
- The Ether5 port supports PoE output for powering other RouterBOARD devices. The port has an auto-detection feature, so you can connect Laptops and other non-PoE devices without damaging them. The PoE on Ether5 outputs approximately 2 V below input voltage and supports up to 0.58 A (So provided 24 V PSU will provide 22 V/0.58 A output to the Ether5 PoE port).

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

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

Please make sure the device has a lock package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hap.md](../regulatory/hap.md).
