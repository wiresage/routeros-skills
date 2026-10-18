# CRS320-8P-8B-4S+RM

> Source: https://manual.mikrotik.com/hardware/crs320-8p-8b-4s-plus-rm
>
> Category: Switches

*[Figure]*

The first MikroTik high-power PoE++ switch – for easy and cost-effective powering of industry standard 802.3af/at/bt devices. Forget about countless power cables – create a cleaner space with PoE++! See the [CRS320-8P-8B-4S+RM product page](https://mikrotik.com/product/crs320_8p_8b_4s_rm) for full specifications and brochures.

## Quickstart

- Connect with your PC to any Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Use WebFig in a web browser or the "WinBox" configuration tool <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Please attach rubber pegs on the bottom of the router if the desired placement is on the flat surface or use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.
  *[Figure]*
- Place the device in the rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
  The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
  We recommend Cat6 cables for our devices.
  Mounting and configuration of this device should be done by a qualified person.

## Powering

The unit is equipped with one Hot Swap IEC type AC power supply, 636W, which accepts 100-240 V ⏦ (~ 50/60 Hz 11 A max).
The second PSU slot is intended to be equipped with the same Hot Swap IEC type AC power supply, 636 W, which accepts 100-240 V ⏦ (~ 50/60 Hz 11 A max).
The maximum power consumption without attachments is 36 W, and under maximum load (using two power supplies), it can reach 1150W.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Configuration

Full RouterOS and SwOS documentation is located here: <https://mt.lv/help> This device is not preconfigured other than an IP address on the master Ethernet port. You can connect from any port, as all ports are switched together by default. Another configuration has to be applied according to the documentation manual linked above.
The Initial connection has to be done via the Ethernet cable, using the MikroTik WinBox utility. WinBox should be used to connect to the default IP address of 192.168.88.1 from any port, with the username admin and no password (or, for some models, check user and wireless passwords on the sticker).
For recovery purposes, it is possible to boot the device from the network, see Buttons, and Jumpers.
In case the IP connection is not available, the WinBox utility can also be used to connect to the MAC address of the device. Applies only when the device has booted RouterOS.
The device is equipped with an RJ45 serial port, set by default to 115200bit/s, 8 data bits, 1 stop bit, no parity. Standard RJ45 to COM cable can be used, pinout can be found in our manual: <https://mt.lv/help> Marvell Prestera switch chip features user manual.

## Power output

This device can supply PoE power to external devices through its Ethernet ports. All ports provide ~54V.

**Ethernet ports 1 to 8** can power 802.3 af/at devices. By default, the PoE mode is set to auto, ensuring it will not damage devices. It will auto-detect devices with PoE support and provide power. Once a PoE device is detected, it will be powered, and the PoE LEDs will turn on.
**Ethernet ports 9 to 16** can power 802.3 af/at/bt devices, supporting "Type 3" (Classes 5-6) and "Type 4" (Classes 7-8).
Each 802.3 af/at port can provide up to 30W with high voltage.
Each 802.3 bt port can provide up to 90W.

Supports only fully compliant 802.3 at/af/bt PD devices: mAP-lite, RB1100AHx4, CRS510-8XS-2XQ, CRS504-4XQ-OUT, CRS504-4XQ-IN

Non-isolated devices like NetMetal ax can cause ground loop issues, if ground path is produced by PSU or earthing cable.
If such device is required, RBGPOE-CON-HP should be used to provide galvanic isolation

## Use case schemes

### Description of Terminology Used in the recommended connection Schemes

Unlike our previous 802.3 af/at Power Sourcing Equipment, this is our first PoE switch with full implementation of the 802.3 af/at/bt standard. It supports only fully compliant 802.3 af/at/bt Powered Devices, such as CRS510-8XS-2XQ-IN, CRS504-4XQ-IN, CRS504-4XQ-OUT, FTC11XG, mAP lite, RB1100AHx4 and future models.

**PSE** - Power sourcing equipment.
**PD** - Powered Device.
**PSU** - Power Supply Unit.
**AF/AT** - IEEE 802.3af and 802.3at are standards for Power over Ethernet (PoE), which allows Ethernet cables to transmit power alongside data to power devices such as IP cameras, wireless access points, and VoIP phones.
**8P** - eight ports IEEE 802.3 af/at.
**8B** - eight ports IEEE 802.3 bt.

#### Use case 1

An **802.3 af/at/bt** device, such as the CRS504-4XQ-OUT, CRS510-8XS-2XQ-IN, or CRS504-4XQ-IN , can be connected to one of the **8B** ports, but it shouldn't be additionally connected with a grounded **PSU**.

*[Figure]*

#### Use case 2

To power a Passive PoE device, the RBGPOE-CON-HP should be used. Grounded or floating **PSU** can be used for redundancy.

*[Figure]*

#### Use case 3 - Special cases for 802.3 af/at Powered Device with non-isolated PoE

- Any ground connection should be avoided.
- If the ground connection is required, for a Powered Device with non-isolated PoE RBGPOE-CON-HP should be used.
- Grounded PSU can't be used for Powered Devices at the same time.
- An SFP cage, USB and RS232 ports should not have a connection to the ground.

*[Figure]*

## Buttons

**Reset button**:

- Hold this button during boot time until the USR LED light starts flashing, release the button to reset RouterOS configuration.
- Hold the Reset button and power on your device (wait until the "USR" led is blinking then stable "On", and when the "USR" led is "Off" - release the Reset button) - the device is booting in bootp mode to reinstall RouterOS using Netinstall. **The MGMT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load backup RouterBOOT without resetting. This is useful for RouterBOOT debugging and recovery.

## Extension slots and ports

- 16 gigabit Ethernet ports (With Auto MDI/X so you can use either straight or cross-over cables for connecting to other network devices).
- 4x 10G SFP ports.
- MGMT/BOOT labeled port.
- RJ45 serial port.

## LED indicators

- PWR LED is lit when the router is powered on.
- USER LED indicates the device's state while powering it up into different modes, such as resetting the configuration or booting device for the Netinstall utility.
- PoE FAULT LED indicates an exceeded overall max PoE output limit.
- FAN FAULT LED indicates a problem with any of the cooling fans.
- Triangle LEDs (top row) indicate PoE-Out status:**Red LED:** Indicates that the respective port uses PoE 802.3af/at.
- **Flashing single red LED:** Indicates a problem starting low voltage or high (802.3af/at) voltage device.
- **Purple LED:** Indicates that the respective port uses PoE 802.3bt.
- **Flashing single purple LED:** Indicates a problem starting a high (802.3bt) voltage device.
- The square orange and green Ethernet port LEDs indicate individual Ethernet port activity.
- The triangle SFP+ port green LEDs indicate individual SFP+ port activity.

## Accessories

Package includes the following accessories that come with the device:

*[Figure]*

See the [MikroTik wired interface compatibility](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/crs320-8p-8b-4s-plus-rm.md](../regulatory/crs320-8p-8b-4s-plus-rm.md).
