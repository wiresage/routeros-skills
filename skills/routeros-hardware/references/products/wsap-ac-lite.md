# wsAP ac lite

> Source: https://manual.mikrotik.com/hardware/wsap-ac-lite
>
> Category: Indoor wireless

*[Figure]*

The wsAP is a wall socket wireless access point. It is already configured, you can simply connect the Internet cable and start using wireless Internet. We recommend you to set up a password to secure your device. See the [wsAP ac lite product page](https://mikrotik.com/product/wsap_ac_lite) for full specifications and brochures.
As with any MikroTik wireless access point, you can also manage it using the CAPsMAN wireless access point management server. In this case, all configuration will be done in CAPsMAN. See Buttons and jumpers on how to set this device as a managed CAP.

## Mounting

The device should be mounted on standard electrical wall boxes, where ethernet cabling has already been installed. The included mounting plate fits most worldwide wall box standards. Orient the wall mounting plate on top of your wall box, and install the screws that fit your wall box screw holes the best. Once the plate is in place, plug the required cables into the wsAP unit, and mount the unit on the mounting plate by putting it on the mounting hooks and slightly pulling it downward, to secure in place.

## Powering

The device only accepts powering at the E1 port with PoE, so you must either a passive PoE injector (not included), or make sure your switch supports passive or 802.3af/at PoE output. The power consumption under maximum load can reach 8 W.

## Setup

- Connect your Internet cable to the E1 port.
- Set your computer IP configuration to automatic (DHCP).
- From your computer, connect to the wireless network name which starts with "MikroTik", or connect to the E2 ethernet port.
- The E3 port supports PoE output, so you can power an IP phone from this port. The E3 automatically detects if the connected device supports PoE input, so you can also safely connect devices that do not support PoE powering.
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration**,** since there is no password by default (or, for some models, check user and wireless passwords on the sticker)., you will be logged in automatically. Set up your password in the screen that loads.

## Configuration

By default, the device is configured as a wireless access point, with the first ethernet port (E1) configured as a DHCP client, and the E2 / E3 interfaces are bridged together with the wireless interface. A DHCP server is configured on the bridge interface. The RJ11 phone port is passive passthrough only, to connect your line to the back of the unit, and to connect the RJ11 compatible phone on the front of the unit for better cable management.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see section .

## Extension slots and ports

- Three RJ45 ethernet ports that support automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices. The E3 port is capable of powering another RouterBOARD device with passive and 802.3af/at PoE. The maximum output current is 500 mA when using less than 30 V to power this device and 420 mA when using more than 30 V.
- Two directly linked (passthrough) RJ11 ports.
- One USB type A connector with max 0.5 A output at 5 V.
- The integrated wireless module which supports AP/CPE/P2P/Repeater modes.

## Buttons and jumpers

### Reset button

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

The action of the mode button can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. By default, the button will run a script, which will disable all LED lights. Useful after you have connected all devices, before mounting the unit on the wall.

## LED indicators

There are eight LED lights on the unit, which can be controlled in RouterOS software, or disabled altogether.

- 5G and 2G indicate the wireless activity on the 5 GHz and 2 GHz wireless interfaces.
- E1, E2, and E3 indicate the port activity of the respective ethernet ports.
- The power LED is lit when the router is powered from the E1 port.
- The user LED can be configured from RouterOS.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

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

Safety warnings and regulatory statements are in [regulatory/wsap-ac-lite.md](../regulatory/wsap-ac-lite.md).
