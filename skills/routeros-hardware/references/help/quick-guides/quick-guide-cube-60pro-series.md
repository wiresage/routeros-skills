# Quick Guide - Cube 60Pro Series

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/33849356/Quick+Guide+-+Cube+60Pro+Series
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2026-04-27. The translations into other languages are omitted; the English guide is complete.

# **Models:** CubeG-5ac60ay (Cube 60Pro ac), CubeG-5ac60ay-SA (CubeSA 60Pro ac), CubeG-5ac60aypair (Wireless Wire Cube Pro)

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.13 or the latest version to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. *All MikroTik radio devices must be installed according to instructions.**

*This "Cube 60Pro" series Quick Guide covers models: CubeG-5ac60ay (Cube 60Pro ac), CubeG-5ac60ay-SA (CubeSA 60Pro ac), CubeG-5ac60aypair (Wireless Wire Cube Pro).*

*[Figure]*

*This is a wireless network device. You can find the product model name on the case label (ID).*

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*The most relevant technical specifications for this product can be found on the last page of this Quick Guide.*

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*If you need help with configuration, please seek a consultant <https://mikrotik.com/consultants>*

**First steps:**

- Connect the device to the included PoE injector with Ethernet cable;
- Connect the PoE injector into the PC or to the network switch;
- Connect the power adapter to the PoE injector;
- Configuration should be made using a web browser WebFig or the WinBox configuration tool [https://mt.lv/WinBox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility;**
- Default IP: 192.168.88.1, user name: *admin*, for the paired models IP: 192.168.88.2/192.168.88.3, please find the password on the sticker;
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit [mikrotik.com](http://mikrotik.com), select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the *WebFig**or* *WinBox* *"Files"* menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole but can also be installed indoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures!

**Exposure to Radio Frequency Radiation:**This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated more than 20 cm away from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## ***WiGig***

|  |  |
| --- | --- |
| Operational channels / Maximum output power  Betriebskanäle / maximale Ausgangsleistung  Canaux opérationnels / puissance de sortie maximale  Canali operativi / massima potenza di uscita  Canales operacionales / potencia de salida máxima  Операционные каналы / максимальная выходная мощность | 58.32 GHz / <40 dBm |
| 60.48 GHz / <40 dBm |
| 62.64 GHz / <40 dBm |

## ***WLAN***

|  |  |
| --- | --- |
| Operating Frequency / Maximum output power  Betriebsfrequenz / maximale Ausgangsleistung  Fréquence de fonctionnement / puissance de sortie maximale  Frequenza operativa / massima potenza di uscita  Frecuencia de funcionamiento / potencia de salida máxima  Рабочая частота / максимальная выходная мощность | 5470-5725 MHz / 27 dBm |

| ***(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:*** | | | | |
| --- | --- | --- | --- | --- |
| **(EN) Product Power Input Options** **(DE) Produkt Stromquellen Optionen** **(FR) Options d'entrée d'alimentation du produit** **(IT) Opzioni di ingresso alimentazione del prodotto** **(ES) Opciones de entrada de energía del producto** **(RU) Параметры входной мощности продукта** | **(EN) DC Adapter Output Specification** **(DE) Ausgangsspezifikationen des Gleichstromadapters** **(FR) Spécifications de sortie de l'adaptateur de courant continu** **(IT) Specifiche di uscita dell'adattatore di corrente continua** **(ES) Especificaciones de salida del adaptador de corriente continua** **(RU) Выходные характеристики адаптера постоянного тока** | | **(EN) IP class of the enclosure** **(DE) IP-Klasse des Gehäuses** **(FR) Classe IP du boîtier** **(IT) Classe IP della custodia** **(ES) Clase de IP del recinto** **(RU) Класс защиты корпуса IP** | **(EN) Operating Temperature** **(DE)Betriebstemperatur** **(FR) température de fonctionnement** **(IT) temperatura di esercizio** **(ES) Temperatura de funcionamiento** **(RU) Рабочая Температура** |
| **Voltage, V** | **Current, A** |
| PoE In Ethernet Port (18 - 48 V DC) | 24 | 0.8 | IP66 | -33°..+70°C |

## #75933

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-cube-60pro-series.md](../../regulatory/quick-guide-cube-60pro-series.md).
