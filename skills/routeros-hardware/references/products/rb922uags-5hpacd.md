# RB922UAGS-5HPacD

> Source: https://manual.mikrotik.com/hardware/rb922uags-5hpacd
>
> Category: RouterBOARD

*[Figure]*

720Mhz CPU, 128MB RAM, 1xGigabit Ethernet, 1xSFP cage, 1xminiPCI-e, 1xSIM, onboard 802.11ac Two Chain 5Ghz wireless, RouterOS L4. See the [RB922UAGS-5HPacD product page](https://mikrotik.com/product/RB922UAGS-5HPacD) for full specifications and brochures.

## First use

- Insert the miniPCIe card and SIM card.
- Connect antenna cables to the miniPCIe card.
- (Optional) Install the device in a case.
- Connect Ethernet cable to the gigabit ethernet port.
- Plug-in power cable to turn on the device.
- Access by 192.168.88.1;
- User name admin, no password (or, for some models, check user and wireless passwords on the sticker).
- Choose your country, to apply country regulation settings.
- Set up a password.

## Powering

The device accepts power from the power jack or from the Ethernet port:

- Direct-input power jack (5.5mm outside and 2mm inside, female, pin positive plug) accepts 8-30 V DC.
- Ethernet port accepts passive Power over Ethernet 8-30 V DC.
  The power consumption under maximum load can reach 17 W.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- One gigabit ethernet port accepts 10-30 V DC powering from a passive PoE injector.
- One SFP cage.
- One miniPCIe slot for 3G/4G/LTE modem or another wireless card.
- USB port.
- 2x MMCX connectors for the built-in powerful 802.11ac 2x2 radio.
- SIM slot (requires 3g miniPCIe card).

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## MiniPCIe slot usage

The device is equipped with a miniPCIe supports 3G/4G/LTE modem or WiFi module. A SIM slot is provided for use together with a miniPCIe modem and cannot be used separately.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb922uags-5hpacd.md](../regulatory/rb922uags-5hpacd.md).
