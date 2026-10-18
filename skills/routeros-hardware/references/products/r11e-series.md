# R11e series

> Source: https://manual.mikrotik.com/hardware/r11e-series
>
> Category: LTE products

*[Figure]* *[Figure]*
R11e-LTE-US is a Cat-4 modem. It can be integrated into any MikroTik product that has a miniPCI-e slot.

> **This article covers**
>
> - **R11e-LTE-US**
> - **R11e-LTE**
> - **R11e-4G**
> - **R11e-LTE6**

## Specifications

- Interface – Mini-PCIe;
- Temperature Operating -30°C .. +70°C
- LTE Channel Bandwidth: 1.4/3/5/10/15/20 MHz
- LTE Category: 4 (150Mbps Downlink, 50Mbps Uplink)
- 3G Category: R7 (Cat14 - 21.1Mbps Downlink)
- LTE (FDD) bands: 2/4/5/12 (1900/1700/850/700)
- 3G bands: 2/5 (1900/850)

## Installing the module in your device

R11e-TE-US for professional use. Each of the cards comes in ESD protective packaging. When handling electrical equipment observe the following safety precautions:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- After unpacking place the card on the anti-static mat;
- When installing make sure there are no objects that can damage or touch the PCB plate;
- The card can be installed in your desired device using the factory provided screw holes in a PCB plate;
- Locate miniPCIe slot on your device;
- Unscrew two factory attached screws;
- Optionally you can use the thermal pad by placing it under the card, the thermal pad is not included in the package;
- Install the module to the miniPCIe slot and secure it with previously removed screws. Tightening torque 0,3 Nm;
- Attach antenna cables to the connectors on the module:
  *[Figure]*

When installing outdoors ensure that the device case is waterproof and is designed for outdoor use.
*Mounting and configuration of this device should be done by a qualified person.*

## Configuration

The device will be automatically recognized when used in a MikroTik RouterOS powered device. Configuration can be set in the “Wireless” menu. More information about the configuration of LTE can be found in our documentation: [LTE/5G manual](https://manual.mikrotik.com/docs/mobile-networking/lte-5g)

The device is tested with RouterOS v6 and above. It might be compatible with other operating systems, but drivers are not included with the card.

## Operating system support

The module supports RouterOS. Other operating systems have not been tested.

## Important Notice to OEM integrators

1. This module is limited to OEM installation ONLY.
2. This module is limited to installation in mobile or fixed applications, according to Part 2.1091(b).
3. The separate approval is required for all other operating configurations, including portable configurations with respect to Part 2.1093 and different antenna configurations

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/r11e-series.md](../regulatory/r11e-series.md).
