# hAP ac²

> Source: https://manual.mikrotik.com/hardware/hap-ac-2
>
> Category: Indoor wireless

*[Figure]*

The hAP is a simple home wireless access point. It is already configured, you can simply plug in your ISP cable and start using wireless internet. We recommend you to set up a password to secure your device. See the [hAP ac² product page](https://mikrotik.com/product/hap_ac2) for full specifications and brochures.

## Powering

The device accepts power from the power jack or from the first Ethernet port (Passive PoE):

- direct-input power jack (5.5mm outside and 2mm inside, female, pin positive plug) accepts 12-30 V DC
- first Ethernet port accepts passive Power over Ethernet accepts 18-28 V DC (compensate for the loss on cable, so more than 12V recommended)
  The power consumption under maximum load can reach 15 W.

## Setup

- Connect your internet cable to the first port, and, if you have wired devices, connect them to the other ports
- Set your computer IP configuration to automatic (DHCP).
- From your PC or smartphone, connect to the wireless network name which starts with "MikroTik".
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration**,** since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker).
- . Set up your password in the screen that loads. Please also specify your country, to make sure local regulations are observed.

## Configuration

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest to start here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device from the network, see section .

## Extension slots and ports

- The Ethernet ports are connected through a switch chip, can be configured individually and support automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- The integrated wireless module which supports AP/CPE/P2P/Repeater modes.

## Buttons and jumpers

RouterBOOT reset button has the following functions:

- Hold the button before powering on the device, and at power-up, the button will force load the backup boot loader. Continue holding the button for other functions of this button.
- Release the button when green LED starts flashing, to reset RouterOS configuration.
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server. It is also possible to enable CAPs mode via the command line, to do so run the command "/system reset-configuration caps-mode=yes".
- Press the Reset button and power on your device (wait until the USR led is blinking then stable "On", and when the USR led is "Off" - release the Reset button) - the device is booting in bootp mode to reinstall RouterOS using Netinstall over the network using Ether1.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hap-ac-2.md](../regulatory/hap-ac-2.md).
