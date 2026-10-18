# MQS

> Source: https://manual.mikrotik.com/hardware/mqs
>
> Category: Accessories

The MQS – Mobile Quick Setup is a tiny wireless device made to simplify MikroTik device configuration in the field.

## Quickstart

- Power the device with USB, for example, from your laptop or a power bank.
- From your laptop or smartphone, connect to the MQS wireless network which starts with "RBMQS".
- The MQS by default has a DHCP server enabled on the wireless interface.
- The Management interface has an IP address 192.168.88.3. To avoid conflicts with other MikroTik devices.
- Open <https://192.168.88.3> in your web browser to start configuration, there is no password and user name: admin (or, for some models, check user and wireless passwords on the sticker).
- The MQS does not have RouterOS software, its configuration possibilities are limited.

## LED indicators

*[Figure]*

- The LED displays active POE.
- Displays an active connection of the Ethernet port.
- Displays the access point mode.
- Displays the station mode.
- User LED indicates that the device is currently in factory firmware, after the update it will no longer be active, to bring the device in factory firmware, hold reset button when booting and LED will light up again.
- The power LED indicates that the unit is receiving power.

## Mounting

If desired, the device can be mounted to with a zip tie through the opening on it's back, or with provided strap or with wall mounting bracket. The IP rating scale for this device is IPX0. To comply with health regulations, install and use this device at least 20cm away from your body.

## Powering

- MicroUSB port accepts 5 V powering.
- Ethernet port accepts passive Power over Ethernet 12-28 V DC (compensate for the loss on cable, so more than 12 V recommended).
  The power consumption under maximum load can reach up to 7 W, without attachments 1 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE+DATA port of the POE adapter.
- Connect an Ethernet cable from your local network (LAN) to the POE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Configuration

We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> WinBox and MikroTik mobile app can be used to configure other devices through MQS. MQS itself can be configured only in the web interface.

## Extension slots and ports

- Built-in 2 GHz wireless access point module, AP/station/bridge/p2p modes are supported. Onboard PIF antennas built-in.
- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices. The Ethernet port accepts 12-28 V DC powering and is also capable of POE output.
- One micro-USB 2.0 port for powering only.

## Buttons and jumpers

### Reset button

Hold this button during boot time, to reset software and firmware to factory settings.

### Mode button

By default, MQS will boot as an AP if you hold this button during boot time the MQS will boot into station mode. These modes can be adjusted through the quick-set menu.

## Accessories

Package includes the following accessories that come with the device:

- USB A Male Straight to Micro USB male flat cable L=100 mm w/o data pins.
- Velcro strap 16x300 mm, (with rubber back).
- Plastic tie strap 4.8 mm (W), 157 mm (L), nylon, BLACK.
- K-33 fastening set.
- MQS mounting bracket.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/mqs>

## Upgrading

To keep your device up to date, please visit our MQS product Support & Download section and check for the latest software version:

- Visit <https://mikrotik.com/product/mqs#fndtn-downloads>
- Download firmware "MQS current release";
- Connect to the MQS using a web browser;
- Choose the Upgrade tab;
- Click on the "Choose File" button and browse to downloaded file;
- Hit the Upgrade button and wait for the setup to finish.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/mqs.md](../regulatory/mqs.md).
