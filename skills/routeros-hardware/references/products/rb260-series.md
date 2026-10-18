# RB260-series

> Source: https://manual.mikrotik.com/hardware/rb260-series
>
> Category: Switches

*[Figure]* *[Figure]*

> **This article covers**
>
> - **[RB260GS](https://mikrotik.com/product/RB260GS)**
> - **[RB260GSP](https://mikrotik.com/product/RB260GSP)**

The CSS106 is a network switch with five Ethernet ports and one SFP, it is powered by the SwOS operating system. It is already configured, with all ports switched together. We recommend you to set up a password to secure your device. CSS106-1G-4P-1S has PoE output capabilities on four of it's Ethernet ports.

Tested and recommended to use with MikroTik SFP modules: S-85DLC05D, S-31DLC20D and S-35/53LC20D (not included)

## Powering

The power consumption of this device under maximum load is up to 11 W. The device accepts powering in the following ways:

- Direct-input power jack (5.5mm outside and 2mm inside, female, pin positive plug) accepts 11-30 V DC.
- The combo ethernet port accepts passive Power over Ethernet 11-30 V DC, PoE injector is not included.

## First use

See [Connecting to the switch](https://manual.mikrotik.com/docs/bridging-and-switching/swos/css106#connecting-to-the-switch) in the SwOS manual.

- Power the device either from the power jack (11-30 V accepted, a power adapter is bundled with the device) or from the first port over Passive PoE (11-30 V).
- Download the latest version of SwitchOS software from <https://mikrotik.com/download>;
- Connect your computer to one of the Ethernet ports;
- Connect the device to the power supply;
- Set the IP address of your computer to 192.168.88.2;
- Open your web browser, the default IP management address is 192.168.88.1, with username: **admin** and no password (or, for some models, check user and wireless passwords on the sticker);
- Upload a file with the web browser in the Upgrade tab, the device will reboot after the upgrade;
- Set your password to secure your device.

## Configuration

The device is set up as a switch, with 192.168.88.1 as the management IP of the master interface.

SwOS is an operating system designed specifically for the administration of MikroTik switch products.

SwOS is configurable from your web browser. It gives you all the basic functionality for a managed switch, plus more: allows you to manage port-to-port forwarding, broadcast storm control, apply MAC filter, configure VLANs, mirror traffic, apply bandwidth limitation and even adjust some MAC and IP header fields.

See the [CSS106 (RB260) series SwOS manual](https://manual.mikrotik.com/docs/bridging-and-switching/swos/css106) for configuration details.

## Power Output

The CSS106-1G-4P-1S model can supply PoE powering to external devices from its Ethernet ports. This is convenient, as you don't need any additional PoE injectors to power other devices. The output voltage will be the same as the input Voltage. By default, it is set to "auto", so it is safe to plug any device into the powered ports. The maximum power output of each ethernet port in this mode is 1 A, total for all ports 2 A. Once Power Output is enabled in RouterOS, the Ethernet LED light turns from Green to Red. Red LED means the port is currently providing PoE power. For the best PoE output functionality, please use the power jack to power the CSS unit.

## Buttons and jumpers

Hold this button during boot time and release after LED light stops flashing to reset SwOS configuration and load primary backup firmware.
Access to primary firmware allows the reinstallation of the main firmware.

See [Reset](https://manual.mikrotik.com/docs/bridging-and-switching/swos/css106#reset) in the SwOS manual.

## Operating system support

The CSS runs SwOS, which is the only supported OS for this device. See the [SwOS manual](https://manual.mikrotik.com/docs/bridging-and-switching/swos) for more information.

*[Figure]*

### GSP Models

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb260-series.md](../regulatory/rb260-series.md).
