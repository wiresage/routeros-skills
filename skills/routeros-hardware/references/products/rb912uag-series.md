# RB912UAG-series

> Source: https://manual.mikrotik.com/hardware/rb912uag-series
>
> Category: RouterBOARD

> **This article covers**
>
> - **[RB912UAG-5HPnD](https://mikrotik.com/product/RB912UAG-5HPnD)**
> - **[RB912UAG-2HPnD](https://mikrotik.com/product/RB912UAG-2HPnD)**

## Mounting

912UAG series router for professional use. Each of the devices comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:

- use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage,
- after unpacking please place the router on the anti-static mat,
- when mounting unit make sure there are no objects that can damage or touch the PCB plate,
- note that ETH, USB port and DC jack are extending over the perimeter of the PCB plate.
  The device can be mounted in your desired location using the factory provided four holes in a PCB plate, located on each side of the device.
  *Warning! This equipment should be installed and operated with a minimum distance of 380 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.*

## Connecting

1. Choose your powering solution, please see Powering section for possibilities.
2. If needed, connect accessories to the miniPCIe slot, antenna cables to the miniPCIe card and insert SIM
   card.
3. Connect your ethernet cable to the gigabit ethernet port.
4. Connect your direct input power jack if not using POE, to start up the device.
5. The device will boot up and after short beep Wireless network will be available for connecting.
6. Open network connections on your pc, mobile phone or other device and search for MikroTik wireless
   network and connect to it.
7. Once connected to the wireless network, open <https://192.168.88.1> in your web browser to start
   configuration, since there is no password by default, you will be logged in automatically (or, for some models, check user and wireless passwords on the sticker).
8. We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest
   version to ensure the best performance and stability.
9. Choose your country, to apply country regulation settings and set up your password in the screen that
   loads.

## Powering

The device accepts power with the following modes:

- Passive 10-30 V PoE to the ethernet port. The higher the voltage needed to compensate for power loss on long cables. At least 18 V is suggested.
- Direct input to the power jack 10-30 V.
  Maximum power consumption 14 W.

## Configuration

RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- One gigabit ethernet port (With Auto MDI/X so you can use either straight or cross-over cables for connecting to other network devices). The ethernet port accepts 10-30 V DC powering from a passive PoE injector.
- One miniPCIe slot. *This device might be incompatible with the R11e-LTE international modem.*
- USB slot type A.
- SIM card slot.
- 5 GHz, 802.11a/n for RB912UAG-5HPnD.
- 2.4 GHz, 802.11b/g/n for RB912UAG-2HPnD.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rb912uag-series.md](../regulatory/rb912uag-series.md).
