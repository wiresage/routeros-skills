# CCR1036-8G-2S+-series

> Source: https://manual.mikrotik.com/hardware/ccr1036-8g-2s-plus-series
>
> Category: Ethernet routers

*[Figure]* *[Figure]*

> **This article covers**
>
> - **CCR1036-8G-2S+**
> - **CCR1036-8G-2S+EM**

## Quickstart

The Ethernet port 1 has a default IP address for connecting: 192.168.88.1. Username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker). The device doesn't have any other configuration applied by default, please set up WAN IP addresses, user password, and update the device.
Connecting the device to the internet:

- Connect your ISP Ethernet cable to the Ethernet port1;
- Connect with your PC to the Ethernet port3;
- Open WinBox on your computer and check Neighbors tab for CCR;
- Choose the device and connect;
- Choose Quick Set on the left side of the screen;
- Set address Acquisition to automatic, or enter your Network details manually;
- Set your local Network IP Address 192.168.88.1;
- Type a secure password in the Password field and confirm again;
- Click Apply;
- The device will receive an IP if your Network has DHCP server enabled, or if you have entered Network details correct and internet connection will be available.
- Click on the Check for updates and on newly opened window choose Download&Install if new version if available.
- You are ready to use your device.
  RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case the IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side

## Powering

The device has dual removable (hot-swap compatible) power supply units AC **⏦** 110-240V with standard IEC compatible sockets. Maximum power consumption of 73 W.

## Reset button

The reset button has two functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

*[Figure]*

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown on the picture to the right;
- Place the device in rackmount enclosure and align with the holes so that the device fits conveniently;
- Tighten screws to secure it in place.

The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment. We recommend Cat6 cables for our devices.

## LEDs

The device has four LED lights. PWR1/2 indicates which power supply is being used. FAULT indicates a problem with the cooling fans. USER can be configured in software.

## Operating system support

The device supports RouterOS software with the version number v6.46 at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

## PCIe usage

M.2 Slot PCIe 4x, to install SSD please follow instructions:

1. Turn off device (unplug power cords);2. Unscrew 6 screws which hold CCR upper lid;
2. Open lid;
3. Unscrew screw which will hold SSD;
4. Insert SSD in m.2 slot;
5. Attach power cords and check does SSD properly initializing;
6. Screw back 6 lid screws.
   Also please note, that by default you should use m.2 2280 form factor SSD.

The CCR1036 models have PCIe Gen 2.0 x4 connection to the M.2 slot.
Recommended are NVMe M.2 2280mm M key SSD disks with a capacity of up to 1TB.

*[Figure]*

Safety Notice
Electric shock hazard. This equipment is to be serviced by trained personnel only.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ccr1036-8g-2s-plus-series.md](../regulatory/ccr1036-8g-2s-plus-series.md).
