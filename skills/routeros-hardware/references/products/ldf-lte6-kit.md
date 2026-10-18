# LDF LTE6 kit

> Source: https://manual.mikrotik.com/hardware/ldf-lte6-kit
>
> Category: LTE products



## [LDF LTE6 kit](https://mikrotik.com/product/ldf_lte6_kit) (RBLDFR&R11e-LTE6)

*[Figure]*

The LDF (Lite dish feed) is an outdoor LTE system, meant to be installed on an offset dish. The device comes with a modem and is ready to use. See the [LDF LTE6 kit product page](https://mikrotik.com/product/ldf_lte6_kit) for full specifications and brochures.

## Quickstart

- Open the Ethernet port door;
- Insert the SIM card into the slot, with the chip facing UP;
- Connect the device to the included PoE injector with Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Open the <https://192.168.88.1> in your web browser;
- User name: **admin**, and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Use the check for update option to upgrade the device to the latest version. You must have an active SIM card with available data;
- The device will reboot;
- Connect again and in the **QuickSet** menu set your country, to apply country regulation settings;
- Secure your device and set a strong password.

## Powering

The device accepts PoE 802.3af/at 12-57 V DC ⎓. A PoE injector is included in the package.
Maximum power consumption 6 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Assembly and Mounting

The device is compatible with standard offset dishes. Assemble Ethernet cable with cover as shown in the illustration:

- The rubber seal has been cut on the side so you can attach it to the Ethernet cable. It needs to be inside the Housing nut when assembling the compression nut will compress it to the Ethernet cable.

*[Figure]*

*[Figure]*

- Attach the unit to your dish, LDF mounting diameter is 40 mm. Please, ensure placement with an arrow facing upwards.
  *[Figure]*
- Plugin Ethernet cable and tighten the cover by screwing it clockwise.
  The device is designed to be used outdoors and mounted on the dish, with an Ethernet cable connecting to the back of the unit.
  ensure to mount the LDF unit on the offset mount in the proper position - the unit facing upwards to the dish.
  The dish will act as a reflector, amplifying the signal. The final position of your assembly should be placed and installed on the pole. For pole mounting instructions refer to your dish mounting instructions.
  ensure that the cable feed is pointing downwards.
  The IPX rating scale of this device is IP54.

Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.

*The mounting and configuration of this device should be done by a qualified person.*

## Sim slot usage

*[Figure]*

The Sim slot is located under the cover, insert the micro-SIM card accordingly as shown in the picture. With the chip facing up!

## Extension slots and ports

- One Ethernet port, supports automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- MiniPCIe slot with an integrated modem.
- Mode button.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Included parts

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ldf-lte6-kit.md](../regulatory/ldf-lte6-kit.md).
