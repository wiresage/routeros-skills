# RBM11G

> Source: https://manual.mikrotik.com/hardware/rbm11g
>
> Category: RouterBOARD



## First use

- Insert the miniPCIe card (not included), please see paragraph .
- (Optional) Install the device in a case.
- Connect antenna cables to the miniPCIe card and an Ethernet cable to the gigabit Ethernet port.
- Plug-in power cable to turn on the device.
- We recommend connecting to the device using WinBox with a default IP address of 192.168.88.1 with the username admin and no password (or, for some models, check user and wireless passwords on the sticker).

## Mounting

M11G router for professional use. Each of the devices comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
- After unpacking please place the router on the anti-static mat.
- When mounting unit make sure there are no objects that can damage or touch the PCB plate.
- Note that ETH and DC jack is extending over the perimeter of the PCB plate.
  The device can be mounted in your desired location using the factory provided four holes in a PCB plate, located on each side of the device.

## MiniPCIe slot

Installing a miniPCIe module should be done by a qualified person, please follow safety precautions when handling electrical equipment:

- Place the device on the anti-static mat.
- Locate the miniPCIe slot and remove two factory attached screws.
- Attach provided a thick thermal pad to the card, and install the card into miniPCIe slot so that the thermal pad is between PCB and card.
- The secure card in place using previously removed two screws.
- Attach the grey uFL connector to the MAIN antenna connector of the modem, attach the black cable to the secondary (or AUX) connector.
- Attach a thinner thermal pad to the top of the card.
- Mount unit in your desired location.
  After you mounted the device, slide in the SIM card from your mobile operator into the SIM slot, with the chip facing down. The slot accepts miniSIM (2FF).

## Powering

The device accepts power with the following modes:

- Passive 10-30 V PoE to Ethernet port. The Higher voltage needed to compensate for power loss on long cables. At least 18 V is suggested.
- Direct input to the power jack 10-30 V.
  Maximum power consumption 11 W.

## Booting process

RouterOS is the operating system of all RouterBOARD routers. Please see documentation here: <https://mt.lv/help> This device is not preconfigured other than an IP address on the Ethernet port. Another configuration has to be applied according to the documentation manual linked above.
The Initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility. WinBox should be used to connect to the default IP address of 192.168.88.1 with the username admin and no password.
In case you wish to boot the device from the network, for example, to use MikroTik Netinstall, hold the reset button of the device when starting it until the LED light turns off, and the device will start to look for Netinstall servers.
In case the IP connection is not available, the WinBox utility can also be used to connect to the MAC address of the device. More information in the documentation.

## Extension slots and ports

- One gigabit Ethernet port (With Auto MDI/X so you can use either straight or cross-over cables for connecting to other network devices). The Ethernet port accepts 10-30V DC powering from a passive PoE injector.
- miniPCIe slot for either an 802.11 wireless card or a 3G/LTE modem. SIM slot is available for miniPCIe 3G/LTE modems and has no functionality when a modem is not installed.

## Buttons and jumpers

RouterBOOT reset button has the following functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode (total 10 seconds).* Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Specifications

For more information about this product, specification and pictures please visit our web page: <https://mikrotik.com/product/m11g>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

*[Figure]*

*[Figure]*

*[Figure]*

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rbm11g.md](../regulatory/rbm11g.md).
