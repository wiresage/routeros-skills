# RBM33G

> Source: https://manual.mikrotik.com/hardware/rbm33g
>
> Category: RouterBOARD

*[Figure]*

Powerful OEM board with three Gigabit LAN and two miniPCIe slots. See the [RBM33G product page](https://mikrotik.com/product/rbm33g) for full specifications and brochures.

## First use

- (Optional) Install the device in a case.
- Connect cables to wireless cards and Ethernet ports.
- Plug-in power cable (directly or through the PoE injector) to turn on the device, please see (link) paragraph.
- The Initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility. WinBox should be used to connect to the default IP address of 192.168.88.1 with the username admin and no password (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability,
- Choose your country, to apply country regulation settings (if applicable), and set up your password on the screen that loads.

## Assembly

M33G for professional use. Each of the devices comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
- After unpacking please place the router on the anti-static mat.
- When mounting unit make sure there are no objects that can damage or touch the PCB plate.
- Note that ETH, USB and other ports are extending over the perimeter of the PCB plate.
  The device can be mounted in your desired location using the factory provided four holes in a PCB plate, located on each side of the device.

## Mounting

Mounting and configuration of this device should be performed by a qualified person.

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded.

## Powering

The device accepts power with the following modes:

- Passive 11-28 V DC ⎓ PoE to J1 Ethernet port. The Higher voltage needed to compensate for power loss on long cables at least 18 V is suggested.
- Direct input to the power jack DC ⎓ 11-28 V.
  The maximum total power consumption with all interfaces loaded is 24 W. Maximum power to each extension card is 3 A.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the POE port of the POE adapter.
- Connect an Ethernet cable from your LAN to the LAN port of the POE adapter, please mind arrows for data and power flow.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Booting process

RouterOS is the operating system of all RouterBOARD routers. Please see documentation: <https://mt.lv/help> This device is not preconfigured other than an IP address on the Ethernet port. Other configurations have to be applied according to the documentation manual linked above.
In case you wish to boot the device from the network, for example, to use MikroTik Netinstall, hold the reset button of the device when starting it until the LED light turns off, and the device will start to look for Netinstall servers.
In case the IP connection is not available, the WinBox utility can also be used to connect to the MAC address of the device. More information in the documentation.

## Extension slots and ports

- Three Gigabit Ethernet ports (With Auto MDI/X so you can use either straight or cross-over cables for connecting to other network devices). The J1 (first from the left) Ethernet port accepts 11-30 V DC powering from a passive PoE injector.
- Two miniPCIe slots for either an 802.11 wireless card or a 3G/LTE modem. Mini-SIM 2FF slots available for miniPCIe 3G/LTE modems and have no functionality when a modem is not installed.
- One M.2 (M key) slot for PCI-e SSD disk. The mounting hole is for 2242 size cards, for other sizes, an extender is suggested. Any speed M.2 cards will operate at 1x PCIe speed.
- One microSD slot for a storage card.
- One DB9 RS232 serial port for serial console access. Configured as 115200 bit/s, 8 data bits, 1 stop bit, no parity.

## USB jumper

Located right next to the USB 3.0 port. When loaded, the jumper enables the USB 3.0 port. Remove the jumper to switch the USB 2.0 lines to the J10 (central) miniPCIe slot (USB 3.0 lines remain enabled to the USB port). This is required if you need to use two cellular modems in the device. Normally you can use the LTE modem in the J8 (left-hand side) slot and use an 802.11 wireless card in the J10 slot. In this case, you can leave the jumper on, as most wireless cards operate on a PCI express. Removing the jumper enables the use of a secondary cellular modem in the central J10 slot, but disables the USB 2.0 functionality of the USB port, while USB 3.0 can still be used on the USB port. Refer to the diagram below:

*[Figure]*

## Boot configuration jumpers

Default jumper configuration for MikroTik RouterOS boot:

*[Figure]*

## MiniPCIe, SIM slot usage

Installing a miniPCIe module should be done by a qualified person, please follow safety precautions when handling electrical equipment:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
- Place the PCB board on the anti-static mat.
- Locate the miniPCIe slot on the PCB and remove two factory attached screws.
- Install the card into miniPCIe slot.
- The secure card in place using previously removed two screws.
- Attach the grey uFL connector to the MAIN antenna connector of the modem, attach the black cable to the secondary (or AUX) connector.
  Slide in the SIM cards from your mobile operator into the SIM slots. The slot accepts miniSIM (2FF). Each MiniPCie slot corresponds to the SIM slot which is located under them. The SIM slots cannot be switched in RouterOS.

## GPIO pinout

M33 pinout is shown below:

*[Figure]*

All output pins are open drain.

Digital input voltage is 0 to 3.63 V max.

To receive a logical "0" on the pin, the voltage should be between 0 to 1.4 V.

To receive a logical "1" on the pin, the voltage should be between 1.41 to 3.63 V.

By default pins 12,13,15,16 are configured for the second "serial1" port usage:

```ros
/system/routerboard/settings/set gpio-function=serial1
```

They can be resigned for GPIO usage in /iot/gpio/digital menu with following commands:

```ros
/system/routerboard/settings/set gpio-function=""/system/reboot
```

## Buttons and jumpers

**RouterBOOT reset button.** This button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode (total 10 seconds).* Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- K-25 set.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/rbm33g>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rbm33g.md](../regulatory/rbm33g.md).
