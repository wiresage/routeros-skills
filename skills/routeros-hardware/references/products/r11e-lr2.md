# R11e-LR2

> Source: https://manual.mikrotik.com/hardware/r11e-lr2
>
> Category: IoT products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/r11e-lr2-31679419e5e4a56e1f4d2b5566cb004f.pdf).

*[Figure]*

R11e-LR2 - LR mPCIe Gateway module. It can be integrated into a RouterBOARD product with mPCIe slot. Requires LR package installation to configure in RouterOS.

## Specifications

notePlease keep in mind that not all servers support 2.4 GHz LoRa communication. As of this moment, the 2.4 GHz LoRa is supported by the TTN and ChirpStack servers.

Low power-consuming with mini PCIe interface, for long-distance data, transmit:

- Product code R11e-LR2
- LoRa band 2.4 GHz
- Tx chain number 1
- Rx chain number 4
- TX/RX channels 2403 MHz, 2425 MHz, 2450 MHz, 2479 MHz
- RF Output power 10 dBm
- Operating temparature -40°C to +70°C

## Installing the module in your device

R11e-LR2 for professional use. Each of the cards comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- After unpacking please place the card on the anti-static mat;
- When installing make sure there are no objects that can damage or touch the PCB plate;
- The card can be installed in your desired device using the factory provided screw holes in a PCB plate;
  *Pictures added for illustration purposes, the device configuration, and the placement of the miniPCIe card may vary.*
- Locate miniPCIe slot on your device;
- Unscrew two factory attached screws;

*[Figure]*

*[Figure]*

- Install the module to the miniPCIe slot and secure it with previously removed screws. Tightening torque 0,3 Nm.

*[Figure]*

## Connecting to the antenna

When installing outdoors please ensure that the device case is waterproof and is designed for outdoor use. The IP rating scale for this device is IP0.
*The mounting and configuration of this device should be done by a qualified person.*

You can use UFL or MMCX connectors.

If your device does not have internal antennas, it is possible to connect to the external antennas by adding cable connectors, product code — [ACSMAUFL](https://mikrotik.com/product/acsmaufl). Please connect and disconnect the antenna, when the device is turned off!

We recommend using TOF-2400-8V-4 Omni antenna

When using UFL connector, attach the antenna cable to the connector shown below:

*[Figure]*

When using MMCX connector, attach the antenna cable to the connector shown below:

*[Figure]*

After you attach the antenna, you can turn the device on. Make sure that the right connector is used by the module in the software settings.

In order to do that, go to the device's GUI and check which connector is used under **LoRa* → *Devices* → "Double-click" on the gateway → Under the "**Antenna**" section:

*[Figure]*

## Configuration for RouterOS

To set the configuration for LR please connect to the device and log in with your web browser, WinBox, or mobile application. Two easy steps to follow:
**First step:**

- Once logged in, Quick Set will be selected, please switch to WebFig on the right side of the screen. If the configuration is done through a mobile application then click on the gear symbol on the right side of the screen to open up an advanced menu.
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

**To use the module in other devices packet forwarder from Semtech is required:** [packet_forwarder](https://github.com/Lora-net/gateway_2g4_hal/tree/master/packet_forwarder)

## Operating system support

The module supports RouterOS software version v6. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/r11e-lr2.md](../regulatory/r11e-lr2.md).
