# RB1100-series

> Source: https://manual.mikrotik.com/hardware/rb1100-series
>
> Category: Ethernet routers

*[Figure]* *[Figure]*

> **This article covers**
>
> - **[RB1100AHx4](https://mikrotik.com/product/rb1100ahx4)**
> - **[RB1100AHx4 Dude Edition](https://mikrotik.com/product/RB1100Dx4)**

The RB1100 is a rack-mountable ethernet router with 13 Gigabit Ethernet ports. Two of the ports provide bypass functionality.

## Powering

The device accepts powering from the dual/failover IEC power connectors on the back of the case. You can use either of them separately or both connectors at the same time, for failover purposes. The device also accepts 12-57V passive or 802.3af/at PoE on Ethernet port 13. The device also has a terminal block for Telecom -48V DC supply or any other DC supply in the 24-57 V range.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default). For recovery purposes, it is possible to boot the device from the network, see section .

## Booting process

First, the RouterBOOT loader is started. It displays boot information on the onboard RS232C asynchronous serial port. The serial port is set by default to 115200bit/s, 8 data bits, 1 stop bit, no parity.
The RouterOS system will then load. It will be also indicated by two beeps.
You can connect to the device with SSH, WinBox GUI or the web interface, by plugging your computer into port Ether1, and connecting to 192.168.88.1 user admin and no password (or, for some models, check user and wireless passwords on the sticker). The device doesn't have a DHCP server enabled by default, your PC should be configured with an address from this network.
More information on connecting to the device: <https://mt.lv/help##> Extension slots and ports

- 13x Gigabit Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices. ETH13 port accepts PoE power, and can be used to boot the device from the network for reinstalling with the Netinstall utility (see documentation)
- DB9 RS232C asynchronous serial port
- microSD slot
- 2x M.2 slots, accepting SATA type M.2 SSD disks in 2280 form factor (only Dx4 model)
- 2x 2.5 inch SATA connectors, accepting standard 2.5" SATA HDD disks (only Dx4 model)
  Recommended are SATA3 M.2 2242mm/2260mm/2280mm B+M key SSD disks with no capacity limitations.

## Buttons and jumpers

The reset button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.
  The bypass switch allows binding ports 11 and 12 together in bypass mode, which means that if the device loses power, the ports will be connected together, allowing data pass from one port to the other, as if the device would not be there.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

*[Figure]*

Safety Notice
Electric shock hazard. This equipment is to be serviced by trained personnel only.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb1100-series.md](../regulatory/rb1100-series.md).
