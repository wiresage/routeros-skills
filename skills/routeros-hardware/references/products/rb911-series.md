# RB911-series

> Source: https://manual.mikrotik.com/hardware/rb911-series
>
> Category: RouterBOARD

> **This article covers**
>
> - **911 Lite5**
> - **911 Lite5 Dual**
> - **911 Lite5 ac**
> - **RB911G-2HPnD**
> - **[RB911G-5HPnD](https://mikrotik.com/product/RB911G-5HPnD)**
> - **RB911G-5HPacD**

## First use

- (Optional) Install the device in a case.
- Connect and Ethernet cable to the Ethernet port.
- Plug-in power cable to turn on the device.
- Open network connections on your PC, mobile phone or other device and search for MikroTik wireless network and connect to it.
- The configuration has to be done through the wireless network using a web browser or mobile app - (see ""). Alternatively, you can use the WinBox configuration tool <https://mt.lv/winbox>.
- Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start configuration, user name: a*dmin* and there is no password by default (or, for some models, check user and wireless passwords on the sticker).
- We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability.
- Choose your country, to apply country regulation settings and set up your password on the screen that loads.

## Assembly

911 series router for professional use. Each of the devices comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- After unpacking please place the router on the anti-static mat;
- When mounting unit make sure there are no objects that can damage or touch the PCB plate.
  The device can be mounted in your desired location using the factory provided four holes in a PCB plate, located on each side of the device.

The IPX rating scale of this device is IPX0. When installing for outdoor applications please ensure the water protection for the device. We recommend using Cat6 shielded cables.
The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded.

## Powering

The device accepts power with the following modes:

- Passive 10-30 V DC ⎓ PoE to Ethernet port. The higher the voltage needed to compensate for power loss on long cables. At least 18 V is suggested.
- Direct input to the power jack 10-30 V. DC ⎓.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Booting process

RouterOS is the operating system of all RouterBOARD routers. Please see documentation here: <https://mt.lv/help> This device is not preconfigured other than an IP address on the Ethernet port. Another configuration has to be applied according to the documentation manual linked above.
The initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility. WinBox should be used to connect to the default IP address of 192.168.88.1 with the username admin and no password.
In case you wish to boot the device from the network, for example, to use MikroTik Netinstall, hold the reset button of the device when starting it until the LED light turns off, and the device will start to look for Netinstall servers.
In case the IP connection is not available, the WinBox utility can also be used to connect to the MAC address of the device. More information in the documentation.

## Extension slots and ports

- RB911-5HnD – 5 GHz, 802.11a/n, consumption 7 W.
- RB911-5Hn – 5 GHz, 802.11a/n, consumption 5 W.
- RB911G-5HPacD – 5 GHz, 802.11a/n/ac, consumption 12 W, Gigabit Ethernet.
- RB911G-2HPnD – 2.4 GHz,802.11b/g/n, consumption 10 W, Gigabit Ethernet.
- RB911-5HacD - 5 GHz, 802.11a/n/ac, consumption 7 W.
- RB911G-5HPnD – 5 GHz, 802.11a/n, consumption 11 W, Gigabit Ethernet.

## Buttons and jumpers

RouterBOOT reset button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode (total 10 seconds).* Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan QR code and choose your preferred OS.
- Install and open application.
- By default, the IP address and user name will be already entered.
- Click Connect to establish a connection to your device through a wireless network.
- Choose Quick setup and application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb911-series.md](../regulatory/rb911-series.md).
