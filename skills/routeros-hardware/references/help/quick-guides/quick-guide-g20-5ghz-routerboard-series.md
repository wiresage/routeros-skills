# Quick Guide G20 - 5GHz RouterBOARD series

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/15303579/Quick+Guide+G20+-+5GHz+RouterBOARD+series
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2026-07-21. The translations into other languages are omitted; the English guide is complete.

# **Models:** RB911G-5HPnD, RB912UAG-5HPnD, RB922UAGS-5HPacD, RB911G-5HPacD, RB911-5HnD (911 Lite5 dual), RB911-5HacD (911 Lite5 ac), RB911-5Hn (911 Lite5)

## *[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.10.2 or the latest stable version, to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be installed according to instructions.*

*This "5GHz RouterBOARD" series Quick Guide covers models: RB911G-5HPnD, RB912UAG-5HPnD, RB922UAGS-5HPacD, RB911G-5HPacD, RB911-5HnD (911 Lite5 dual), RB911-5HacD (911 Lite5 ac), RB911-5Hn (911 Lite5).*

*This is a wireless network device. You can find the product model name on the label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*The most important technical specifications for this product can be found on the last page of this Quick Guide.*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*If you need help with configuration, please seek a consultant <https://mikrotik.com/consultants>*

Depending on the antenna used, you need to set its gain and set "*Installation*" to "*Indoor*" or "Outdoor", depending on the type of use. This is to ensure that the EIRP complies with the limit set by the local authorities. This is done in the Quickset menu.

**First Use:**

- This product comes without enclosure and is designed to be installed into the users' end products or enclosures. Compatible MikroTik enclosure for this product can be found at <https://mikrotik.com/products/group/enclosures>
- The device comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:
  - Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
  - After unpacking please place the router on the anti-static mat;
  - When mounting the unit make sure there are no objects that can damage or touch the PCB plate;
  - The device can be mounted in your desired location using the factory-provided holes in a PCB plate, located on each side of the device;
- Before connecting the device to the power source, please attach the antennas to the connectors;
- Connect the device to the power source;
- Connect your PC to the Ethernet port;
- Configuration should be made using a web browser WebFig or the WinBox configuration tool [https://mt.lv/WinBox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility;**
- Open [http://192.168.88.1](http://192.168.88.1/) in a web browser to start setup. If the IP address is unavailable, use WinBox and connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit [mikrotik.com](http://mikrotik.com), select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "*QuickSet"* menu set up the *"PTP Bridge AP"* mode and choose your country, to apply country regulation settings;
- Set the antenna gain, depending on the antenna used;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- The product comes without enclosure and is meant to be installed into the enclosure by trained and qualified personnel. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes.
- Do not attempt to disassemble, repair, or modify the device. If service is needed, please contact MikroTik support.
- This product can be used both indoors and outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow correct procedures could result in hazardous situation to people and damage to the system. To install outdoors make sure to use at least IP54 rating enclosure.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.

**Exposure to Radio Frequency Radiation:**This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 330 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039

## ***[Figure]***

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-g20-5ghz-routerboard-series.md](../../regulatory/quick-guide-g20-5ghz-routerboard-series.md).
