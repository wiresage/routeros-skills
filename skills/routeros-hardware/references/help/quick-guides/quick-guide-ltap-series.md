# Quick Guide - LtAP series

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/27132115/Quick+Guide+-+LtAP+series
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2023-05-24. The translations into other languages are omitted; the English guide is complete.

# **Models:** RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit)

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v6.49.7 or the latest stable version, to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.*

**This Quick Guide covers models: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).**

*This is a wireless network device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*The most important technical specifications for this product can be found on the last page of this Quick Guide.*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*If you need help with configuration, please seek a consultant <https://mikrotik.com/consultants>*

This Device accepts input of 24V DC, 1.2 A power adapter, which is provided in the original packaging of this device. Alternatively, it's possible to use a PoE injector together with the power source in the range of 12-30 V (direct current) or an Automotive DC port together with a power source of 12-30 V (direct current).

**First steps:**

- Unscrew two screws and remove the cover;
- Connect your Internet cable to the Ethernet port (this is optional if using LTE as the primary connection);
- Insert the SIM card into the SIM 2 slot (middle);
- Connect GPS antenna (optional);
- Connect to the power source;
- Set your computer IP configuration to automatic (DHCP);
- From your computer connect to the wireless network;
- Open the <https://192.168.88.1> in your web browser, for *LtAP model* Download the WinBox configuration tool <https://mt.lv/winbox>, there is no default IP address set, use the Neighbors tab and connect through the MAC address;
- User name: *admin*, and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Use the check for update option to upgrade the device to the latest version. You must have an active SIM card with available data;
- The device will reboot;
- Connect again and in the *QuickSet* menu set your country, to apply country regulation settings;
- Secure your device and set a strong password;
- The *LtAP* device comes without a modem, install it before inserting a SIM card.
- The following RouterOS "npk" packages are required for the core functionality of the product: gps, system.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

**Exposure to Radio Frequency Radiation:**This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

## ***[Figure]***

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-ltap-series.md](../../regulatory/quick-guide-ltap-series.md).
