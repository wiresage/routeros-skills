# PowerBox

> Source: https://manual.mikrotik.com/hardware/powerbox
>
> Category: Ethernet routers

*[Figure]*

### PowerBox (RB750P-PBr2)

The PowerBOX is an outdoor device with five Ethernet ports. Package includes IEC cord, steel clamp, PoE injector, 24 V power adapter, and DIN mount. See the [PowerBox product page](https://mikrotik.com/product/RB750P-PBr2) for full specifications and brochures.

## First use

- Connect your WAN cable to port 1, and the other devices to ports 2-5.
- Set client device IP configuration to automatic (DHCP).
- The default IP address from ports 2-5 (LAN) is 192.168.88.1.
- Username is admin, there is no password (or, for some models, check user and wireless passwords on the sticker).

## Mounting

It is possible to attach the device to a DIN rail, using provided DIN rail bracket and screws. Since the device has a weatherproof outdoor case, you can mount it on a pole, with a provided steel clamp.

*[Figure]*

Please make sure to mount the device with the Ethernet ports facing down.

## Powering

The board accepts power from the power jack or from the first Ethernet port (Passive PoE):

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug)accepts 8-30 V DC,
- The first Ethernet port accepts passive Power over Ethernet accepts 8-30 V DC.
  The power consumption of this device is 2 W.

## Power output

This device can supply PoE powering to external devices from its Ethernet ports. This is convenient as you don't need any additional PoE injectors to power other devices. This feature is indicated by the letter "P" in the device model name. The output Voltage will be the same as input Voltage, and this feature will have to be enabled on the specific ports in RouterOS software. By default it is disabled. The maximum power output of each Ethernet port in this mode is 1 A (2 A total for all ports). Once Power Output is enabled in RouterOS, the Ethernet LED light shines also in red. Red LED means the port is currently providing PoE power, green means Ethernet has a link, both at the same time means Ethernet is linked and power is being outputted.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- Five individual Ethernet ports, supporting automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration.
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

*[Figure]*

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/powerbox.md](../regulatory/powerbox.md).
