# PowerBox Pro

> Source: https://manual.mikrotik.com/hardware/powerbox-pro
>
> Category: Ethernet routers

*[Figure]*

### PowerBox Pro (RB960PGS-PB)

The PowerBox is an outdoor device with five Gigabit Ethernet ports that supporting PoE power output to ports 2-5 (1 A maximum per port, 2 A total maximum). See the [PowerBox Pro product page](https://mikrotik.com/product/RB960PGS-PB) for full specifications and brochures.

## First use

- Connect your WAN cable to port 1, and the other devices to ports 2-5.
- Set client device IP configuration to automatic (DHCP).
- The default IP address from ports 2-5 (LAN) is 192.168.88.1.
- The username is admin, there is no password (or, for some models, check user and wireless passwords on the sticker).
- Use the WinBox configuration tool if the IP address is not available and connect through MAC Address.

## Powering

The power consumption of this device without attachments is 6 W, Max power consumption is 54 W. The device accepts power from the power jack or from the first Ethernet port (Passive PoE):

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-57 V DC.
- The ether1 port accepts Passive PoE input 12-57 V DC.

## Mounting

It is possible to attach the device to a DIN rail, using provided DIN rail bracket and screws. Since the device has a weatherproof outdoor case, you can mount it on a pole, with provided two zip ties or a steel clamp. The ground cable needs to be attached to a specially designed screw on the backside of the unit.

*[Figure]*

Please make sure to mount the device with the Ethernet ports facing down.

## Booting process

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device from the network, see section Buttons and jumpers.

## Extension slots and ports

CPU nominal frequency 800 MHz
Size of RAM 128 MB
Memory size 16 MB
10/100/1000 Ethernet ports 5
SFP 1
Switch chip model QCA8337
Dimensions 125 x 52 x 225 mm
Operating temperature -40°C .. +70°C tested

## Power output

The device supports passive or standard 802.3at/af PoE input/output. Ethernet ports 2-5 can power other PoE-capable devices with the same voltage as applied to the unit. Fewer power adapters and cables to worry about! It can power af/at mode B (4,5+)(7,8-) compatible devices if 48-57 V input voltage is used. The maximum power output per port is 1 A, and 2 A total using input voltage 12-30 V. Using input voltage 31-57 V power limit per port is 450 mA. Once Power Output is enabled in RouterOS, the Ethernet LED adds red color to it (green means Ethernet link is made, red means power but no link, red and green both means there is link and power).

## Buttons and jumpers

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

*[Figure]*

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/powerbox-pro.md](../regulatory/powerbox-pro.md).
