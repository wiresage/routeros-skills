# R11e-LR8

> Source: https://manual.mikrotik.com/hardware/r11e-lr8
>
> Category: IoT products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/r11e-lr8-d0ac4256b0bb1ec57c362648c9c7ec3a.pdf).

R11e-LR8 - LR mPCIe Gateway module. It can be integrated into a RouterBOARD product with mPCIe slot. Requires LR package installation to configure in RouterOS.

## Specifications

Low power-consuming with mini PCIe interface, for long-distance data, transmit:

- Interface – Mini-PCIe;
- Temperature Operating -40 / +70;
- Supports Class A and C;
- Frequency - 863-870MHz (EU);
- RF Output power - 862-870MHz (EU) @ 14dBm;
- *Receive max sensitivity - 137 dB @ SF12, Depends on the antenna used;*
- *Maximum power consumption 2 W.*

## Installing the module in your device

R11e-LR8 for professional use. Each of the cards comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- After unpacking please place the card on the anti-static mat;
- When installing make sure there are no objects that can damage or touch the PCB plate;
- The card can be installed in your desired device using the factory provided screw holes in a PCB plate;
  *Pictures added for illustration purposes, the device configuration, and the placement of the miniPCIe card may vary.*
- Locate miniPCIe slot on your device;
- Unscrew two factory attached screws;

*[Figure]*

*[Figure]*

- Optionally you can use the thermal pad by placing it under the card, the thermal pad is not included in the package;
- Install the module to the miniPCIe slot and secure it with previously removed screws. Tightening torque 0,3 Nm.

*[Figure]*

## Connecting to the antenna

If your device does not have internal antennas, it is possible to connect to the external antennas by adding cable connectors, product code — [ACSMAUFL](https://mikrotik.com/product/acsmaufl). Please connect and disconnect the antenna, when the device is turned off!

- Attach antenna cable to the connector on the module:

*[Figure]*

When installing outdoors please ensure that the device case is waterproof and is designed for outdoor use. The IP rating scale for this device is IP0.
*Mounting and configuration of this device should be done by a qualified person.*

## Configuration for RouterOS

To set the configuration for LR please connect to the device and log in with your web browser, WinBox, or mobile application. Two easy steps to follow:
**First step:**

- Once logged in, Quick Set will be selected, please switch to WebFig on the right side of the screen. If the configuration is done through mobile application then click on the gear symbol on the right side of the screen to open up an advanced menu.
- On the left side menu please find and select the section "Lora".
- On the newly opened window select the Servers tab.
- Click + to add a new server configuration.
- A new window will appear and you will have to enter:
  Name: (Server name)
  Address: (Server address)
  Up port: (Usually it's 1700)
  Down port: (Usually it's 1700)
- Click OK to save.
  **Second step:**
- Select the Device tab on the previous window.
- Double-click or tap on the line to configure.
- Choose the previously entered network on the drop-down menu.
- Click on the button Enable to enable the gateway.
- Click OK to save.
- The configuration is done.

## Specifications

The module can be installed on the miniPCIe to USB adapter and used in any of our devices with a USB slot and installed Lora package.

**To use the module in other devices packet forwarder from Semtech is required:** [packet_forwarder](https://github.com/Lora-net/packet_forwarder)

## Pinout

| Pin # | Value |
| --- | --- |
| 2 | 3V3 |
| 4 | GND |
| 9 | GND |
| 15 | GND |
| 18 | GND |
| 21 | GND |
| 22 | PERST# (not used in RouterOS) |
| 24 | 3V3 |
| 26 | GND |
| 27 | GND |
| 29 | GND |
| 34 | GND |
| 35 | GND |
| 36 | USB_D- |
| 37 | GND |
| 38 | USB_D+ |
| 39 | 3V3 |
| 40 | GND |
| 41 | 3V3 |
| 43 | GND |
| 50 | GND |
| 51 | Reserved |
| 52 | 3V3 |

## Operating system support

The module supports RouterOS software version v6 and v7. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/r11e-lr8.md](../regulatory/r11e-lr8.md).
