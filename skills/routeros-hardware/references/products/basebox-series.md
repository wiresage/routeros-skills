# BaseBox-series

> Source: https://manual.mikrotik.com/hardware/basebox-series
>
> Category: Wireless systems

*[Figure]*

## [BaseBox 5](https://mikrotik.com/product/RB912UAG-5HPnD-OUT) (RB912UAG-5HPnD-OUT)

> **This article covers**
>
> - **[BaseBox 2](https://mikrotik.com/product/RB912UAG-2HPnD-OUT)** (RB912UAG-2HPnD-OUT)
> - **[BaseBox 5](https://mikrotik.com/product/RB912UAG-5HPnD-OUT)** (RB912UAG-5HPnD-OUT)
> - **[BaseBox 6](https://mikrotik.com/product/basebox_6)** (RB912UAG-6HPnD-OUT)

The Basebox is a solid and weatherproof outdoor device based on the RB912 wireless router model. It has high power wireless and one Gigabit Ethernet connector, which supports MDI-X auto-detection. The device has two RPSMA connectors for connecting external antennas. The device is packaged with a power adapter, a PoE injector, and two mounting loops. Extra places for more RP-SMA connectors are available on the unit in this case.

## First use

- Choose your powering solution, please see the Reset button.

## Extension slots and ports

BaseBox 2 model - 2.4 GHz, 802.11b/g/n.

- BaseBox 5 model - 5 GHz, 802.11a/n.
- BaseBox 6 model - 6 GHz, 802.11a/n.
- One 10/100/1000 Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or crossover cable for connecting to other network devices.
- USB type-A slot.
- One miniPCIe slot. *This device might be incompatible with the R11e-LTE international modem.*

## The miniPCI-e slot usage

- Remove top cover;
- Unscrew two screws on the back of the device;
  *[Figure]*
- Open Ethernet port cover and withdraw it from the base of the device;
  *[Figure]*
- Unscrew the antenna connector;
  *[Figure]*
- Withdraw the PCB plate from the base cover;
  *[Figure]*
- Install your modem and reassemble.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Included parts

*[Figure]*

*DIN mount includes four screws to attach it to the back of the device.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/basebox-series.md](../regulatory/basebox-series.md).
