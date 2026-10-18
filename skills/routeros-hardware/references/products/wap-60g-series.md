# wAP 60G series

> Source: https://manual.mikrotik.com/hardware/wap-60g-series
>
> Category: 60 GHz products

This guide can be downloaded as a [PDF file](https://manual.mikrotik.com/assets/files/wap-60g-series-9b51ea18dc11beafdef583ebaff01300.pdf).

> **This article covers**
>
> - **[Wireless Wire](https://mikrotik.com/product/wireless_wire)** (RBwAPG-60adkit)
> - **[wAP 60G](https://mikrotik.com/product/wap_60g)** (RBwAPG-60ad)
> - **[wAP 60G AP](https://mikrotik.com/product/wap_60g_ap)** (RBwAPG-60ad-A)
> - **wAP 60Gx3 AP** (RBwAPG-60ad-SA)

wAP60G devices work in the 60GHz wireless spectrum, the operating temperature of these devices is from -40°C up to +70°C. The devices have a one-gigabit ethernet port and can be powered from a power jack or from ethernet. Devices can be securely mounted on a wall, ceiling, or on a pole/mast.

## Quickstart

- Connect the device to the included PoE injector with Ethernet cable to the data+power end;
- Connect the data end of the PoE injector into the computer;
- Connect the power adapter to the PoE injector;
- Download WinBox configuration tool <https://mt.lv/winbox> Default IP: `192.168.88.1`, user name: **admin** and there is no password, please find the password on the sticker;
- Set an IP address of your computer to `192.168.88.2`;
- In case the IP connection is not available, please use the Neighbors tab and connect through MAC address;
- Once connected configure the device, so it has an active Internet connection <https://mt.lv/configuration>;
- Upgrade the RouterOS software to the latest version <https://mt.lv/upgrade>;
- Choose your country, to apply country regulation settings;
- Set the *Installation* to indoors or outdoors, depending on the usage type;
- Secure your device and set a strong password;
- For more configuration information, please visit the [W60G interface manual](https://manual.mikrotik.com/docs/wireless/w60g/);
- wAP60G AP units come pre-configured with WISP Bridge default configuration;
- Wireless Wire and wAP60G units come pre-configured with PTP Bridge default configuration;
- Wireless Wire devices have already, randomly generated, matching SSID, and Wireless passwords.

## Powering

The devices accept powering both from a power adapter, and through the ethernet port:

- Direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) accepts 12-57 V DC.
- Ethernet port accepts PoE input 12-57 V DC (passive and 802.3af/at).
  A power adapter and a passive PoE injector are included in the box. If using the PoE injector, make sure to use the "Power + Data" connector to connect to the wAP60G device and the "Data" connector to your router or switch.

## Configuration and connecting

Full RouterOS documentation is located here: <https://mt.lv/help> Specific wAP 60G configuration can be found in the [W60G interface manual](https://manual.mikrotik.com/docs/wireless/w60g/).
Access the device by connecting to the Ethernet port and then use the MikroTik WinBox utility for connection.
For recovery purposes, it is possible to boot the device from the network, see section .
In case the IP connection is not available, the WinBox utility can also be used to connect to the MAC address of the device.

## Mounting

**Mounting on the mast or pole:**

*[Figure]*

** It's recommended to use electrical tape to increase friction between materials.*

- Mount plastic tie straps to steel brackets guiding them through holes.
- Mount bracket to the device.
- Secure them with a screw.
- Mount and align the device on the pole or mast.
- Guide Ethernet cable through the opening and connect to the Ethernet port.
- Close bottom latch and secure with a screw.
  It's recommended to secure an Ethernet cable to the pole using zip ties. With the distance from the device approximately 30 cm.

*[Figure]*

**Mounting unit on the wall:**

- Use included a template to mark spots for drilling holes. And if needed for Ethernet cable. Align accordingly, it will depend on how the device will be mounted finally.
- Insert dowels if needed, depends on wall structure and material.
- Place included a steel bracket on the wall.
- Use screws to secure it in place.
- Extend your Ethernet cable through the opening and connect to the Ethernet port.
- Mount the device on the steel bracket
- Secure it in place with the screw.
- Close bottom latch.

Avoid mounting the device on the low ground spot, as you won't be able to attach and close the bottom latch. **Mounting on the ceiling:**

*[Figure]*

A Special bracket is included in the package to mount on the drop ceiling. As it consists of two parts, to be attached on both sides of the ceiling tile.

- Use the template to mark spots for holes.
- Place both mounting brackets on the spot.
- Secure them together using screws.
  Continue assembling in the same manner if mounting on the wall.
- Extend your Ethernet cable through the opening and connect to the Ethernet port.
- Mount the device on the steel bracket.
- Secure it in place with the screw.
- Close bottom latch.

## Bottom Lid

- The bottom lid is secured in place with the captive screw.
- Use the Philips PH2 screwdriver to unscrew it, but do not remove the screw completely.

*[Figure]*

- Pull the cover in the opposite direction from the device to remove it.

*[Figure]*

- Reassemble.

## Buttons and jumpers

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when the green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Included items

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Notes

This device meets the Maximum TX power limit per ETSI regulations. The operational mode in the 60 GHz band: 58.32 GHz, 60.48 GHz, 62.64 GHz. This device is certified for outdoor use in Point to Multipoint applications. In the following countries this device cannot be used in Fixed Point-to-Point applications:

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/wap-60g-series.md](../regulatory/wap-60g-series.md).
