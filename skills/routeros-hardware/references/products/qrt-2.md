# QRT 2

> Source: https://manual.mikrotik.com/hardware/qrt-2
>
> Category: Wireless systems

The QRT is an outdoor CPE unit with the following hardware specifications:

*[Figure]*

## [QRT 2](https://mikrotik.com/product/RBQRTG-2SHPnDr2) (RBQRTG-2SHPnD)

## Quickstart

Please follow these quick steps to set up your device:

- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Access **WebFig** by opening <https://192.168.88.1>, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and click on the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the "Quick Set" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.
- Mount the unit in your desired place, please see (link)

## Extension slots and ports

Gigabit Ethernet port, passive PoE on Ethernet port.

- 2.4 GHz wireless, supported protocol 802.11b/g/n, antenna gain 17 (dBi).

## Opening latch

To access the Ethernet port and reset button, please open latch:

*[Figure]*

- Pull the latch out downwards from the device.
- Lift the latch, but do not remove them completely.

*[Figure]*

## Front status LED behavior

RouterOS allows configuring each LED's activity the way that the user wishes. It is possible to configure the LEDs to display wireless strength, blink the LEDs on interface traffic activity, and many other options. For further information please visit the [LEDs](https://manual.mikrotik.com/docs/hardware/leds) manual page.
Default factory configuration for this device:

*[Figure]*

- Solid Blue – The device is powered on.
- Solid Green – Connected Ethernet port.
- Solid Green – User-defined LED.
- Solid Green – The set of five green LEDs, shows the signal strength.

## Mounting

The device is designed to be used outdoors and mounted on the mast with all needed cables connecting through the latch of the unit.

*Mounting and configuration of this device should be done by a qualified person.*

When mounting on the mast, please ensure that the cable feed is pointing downwards.
The IP rating scale of this device is IP54. We recommend using Cat5/6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 30 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference. The QRT box contains several parts that need to be assembled. Please follow this process:

- Attach the two brackets (A) to the swivel adjuster (B), by using the four provided screws (use a PH1 screwdriver).

*[Figure]*

- Place the two U-bolts (C) around the mast or pole, and guide them through the holes on the swivel adjuster (D). Then, tighten the U-bolts, each with one regular washer, one spring washer, and one nut, as shown in the image to the right. All nuts need to be tightened using a size 10 (3/8 in) wrench. Maximum diameter of the pole can be up to 70 mm.

*[Figure]*

- Use the mounting bracket (E), and put it on to the back of the antenna. Install with one rubber ring, one washer, and one nut for each of the built-in bolts (in that order).

*[Figure]*

- Attach the swivel adjuster to the mounting bracket. Use the long bolt in the position (F). Put one regular washer, and one spring washer onto the shorter screws, then put them in positions (G). Do not tighten too much, as you need to adjust the antenna now.

*[Figure]*

- Once antenna level and angle are adjusted according to the wireless signal in software, tighten all nuts. Note the degrees of angle for future reference.
  Wind load16 kg @ 40m/s, 9kg @ 30 m/s;

## Grounding

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw on the backside of the unit. Attach your grounding wire to the grounding screw, then attach the other end of the grounding wire to the grounded mast, please see the picture:

*[Figure]*

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes accessories that come with the device:

- Montage elements: QRT U Bolt, Steel - Zinc plated, DIA 6 mm, U mast clamp, antenna mount.
- EU Switching Power Supply 24 V, 0.8 A, 19.2 W, DC ⎓, 85.3 %, VI, cable:150 cm Hor CMC.
- K-QRT_Fastening set for QRT.
- ZCPOEC006-R2_Gigabit POE injector cable with shielded connector.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Specifications

For more information about this product, specifications, pictures, downloads, and test results please visit our web page: <https://mikrotik.com/product/RBQRTG-2SHPnDr2>

## MikroTik mobile app

*[Figure]*

*[Figure]*

*[Figure]*

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/qrt-2.md](../regulatory/qrt-2.md).
