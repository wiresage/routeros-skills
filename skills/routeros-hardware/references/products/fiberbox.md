# FiberBox

> Source: https://manual.mikrotik.com/hardware/fiberbox
>
> Category: Switches

### FiberBox (CRS105-5S-FB)

*[Figure]*

The Fiberbox is an outdoor switch with five SFP ports, ideal for locations where distance is restricting the use of regular ethernet cables. The device is weatherproof and comes with a hose clamp and zip ties, ready to be installed on high masts and towers. See the [FiberBox product page](https://mikrotik.com/product/fiberbox) for full specifications and brochures.

## Quickstart

*[Figure]*

The default configuration utilizes switch chip features to configure the dumb switch. All ethernet ports are added to the switch group and the default IP address 192.168.88.1/24.

- The Initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility.
- Use WinBox to connect to the default IP address of 192.168.88.1 from any port, with the username admin and no password, the device is set up as a switch (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your system software to the latest version to ensure the best performance and stability.
- Set up your password to secure the device.

## Mounting

We recommend using Cat6 shielded cable for our devices.

Use a steel clamp to guide through the back of the device.

*[Figure]*

Attach to the pole and secure by tightening firmly.

*[Figure]*

## Powering

The device accepts powering:

- Direct input power (5.5 mm outside and 2 mm inside, female, pin positive) accept DC ⎓ 9-30 V DC;
  The power consumption of this device under maximum load up to 11 W.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: CRS3xx and CSS3xx series Manual.The Initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility. WinBox should be used to connect to the default IP address of 192.168.88.1 from any port, with the username admin and no password.
For recovery purposes, it is possible to reinstall the device from the network, see the MikroTik wired interface compatibilityWhen using devices that come with separated SFP+ cages, it is still not recommended to deploy the S+RJ10 transceivers beside each other. Use S+RJ10 in every second interface to avoid transceivers overheating which may cause unpredictable behavior.
Operating system support

The device supports RouterOS v6. The specific factory-installed version number is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/fiberbox.md](../regulatory/fiberbox.md).
