# Quick Guide - nRAY series

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/28606572/Quick+Guide+-+nRAY+series
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2024-11-20. The translations into other languages are omitted; the English guide is complete.

# **Models:** nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY)

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.10 or the latest stable version, to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.*

*This "nRAY" series Quick Guide covers models: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).*

*[Figure]*

*This is a wireless network device. You can find the product model name on the case label (ID).*

**The most important technical specifications for this product can be found on the last page of this Quick Guide.**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*If you need help with configuration, please seek a consultant <https://mikrotik.com/consultants>*

**First steps:**

- Take the Ethernet port cover from the package;
- Guide Ethernet cable through the opening;
- Plug into the Ethernet port and screw clockwise tightly, to ensure water protection;
- Connect the PoE injector into the computer;
- Connect the power adapter to the PoE injector;
- Download WinBox configuration tool <https://mt.lv/winbox>;
- Default IP: 192.168.88.1, user name: *admin* and there is no password, for the paired models IP: 192.168.88.2/192.168.88.3, please find the password on the sticker;
- Once connected, configure the device, so it has an active Internet connection <https://mt.lv/configuration>;
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the Winbox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Connect again and select your Region in the Wireless menu, W60G tab, to apply country regulation settings;
- For *nRAY 60G*models, set up your router password in the QuickSet menu, to the right and repeat it, it will be used to log in next time.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole but can also be installed indoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures!

**Exposure to Radio Frequency Radiation:**This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 53 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## ***[Figure]***

## ***WiGig***

|  |  |
| --- | --- |
| Operational channels / Maximum output power  Betriebskanäle / maximale Ausgangsleistung  Canaux opérationnels / puissance de sortie maximale  Canali operativi / massima potenza di uscita  Canales operacionales / potencia de salida máxima  Операционные каналы / максимальная выходная мощность | 58.32 GHz / <40 dBm |
| 60.48 GHz / <40 dBm |
| 62.64 GHz / <40 dBm |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques*** ***/*** ***(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:*** | | | | |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification (DE) Ausgangsspezifikationen des Gleichstromadapters (FR) Spécifications de sortie de l'adaptateur de courant continu (IT) Specifiche di uscita dell'adattatore di corrente continua (ES) Especificaciones de salida del adaptador de corriente continua (RU) Выходные характеристики адаптера постоянного тока | | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |
| Voltage, V | Current, A |
| PoE In Ethernet port (12 - 57 V DC) | 24 | 0.38 | IP55 | -30°..+70°C |

#72835

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-nray-series.md](../../regulatory/quick-guide-nray-series.md).
