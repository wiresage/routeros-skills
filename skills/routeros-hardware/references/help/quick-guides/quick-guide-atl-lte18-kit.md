# Quick Guide - ATL LTE18 kit

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/48660486/Quick+Guide+-+ATL+LTE18+kit
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2026-03-04. The translations into other languages are omitted; the English guide is complete.

# **Models:** ATLGM&EG18-EA (ATL LTE18 kit)

*[Figure]*

# **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.7 or the latest stable version, to ensure compliance with local authority regulations!*
>
> *It is the end user's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.*

*This Quick Guide covers the model: ATLGM&EG18-EA (ATL LTE18 kit)*

*This is a wireless network device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*The most important technical specifications for this product can be found on the last page of this Quick Guide.*

*Technical specifications, brochures, and more info about products are at <https://mikrotik.com/products>*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*If you need help with configuration, please seek a consultant <https://mikrotik.com/consultants>*

**First steps:**

- Open the Ethernet port door;
- Insert the Micro SIM card into the slot, with the chip facing UP;
- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through *WebFig* or the *WinBox* tool at [https://mt.lv/WinBox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility.**
- Access *WebFig* by opening [http://192.168.188.1](http://192.168.88.1/), and for *WinBox*, download the tool, navigate to the *Neighbors*tab, and click on the MAC address. The username is *"admin"*with no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version. Must have a valid SIM card inserted and active Internet connection;
- For a manual update of the device, visit [mikrotik.com](http://mikrotik.com), select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## **UK Conformity Assessed**

***[Figure]***

## **WCDMA/LTE**

|  |  |  |
| --- | --- | --- |
| Operating Frequency / Maximum output power  Betriebsfrequenz / maximale Ausgangsleistung  Fréquence de fonctionnement / puissance de sortie maximale  Frequenza operativa / massima potenza di uscita  Frecuencia de funcionamiento / potencia de salida máxima  Рабочая частота / максимальная выходная мощность | WCDMA Band I | 2100 MHz / 25dBm |
| WCDMA Band III | 1800 MHz / 25dBm |
| WCDMA Band VIII | 900 MHz / 24.5dBm |
| LTE Band 1 | 2100 MHz / 24.5dBm |
| LTE Band 3 | 1700 MHz / 24.5dBm |
| LTE Band 7 | 2600 MHz / 24.5dBm |
| LTE Band 8 | 900 MHz / 24.5dBm |
| LTE Band 20 | 800 MHz / 24.5dBm |
| LTE Band 28 | 700 MHz / 24.5dBm |
| LTE Band 38 | 2600 MHz / 24.5dBm |
| LTE Band 40 | 2300 MHz / 24.5dBm |

> **Note**
>
> This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

| ***(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques /******(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:*** | | | | |
| --- | --- | --- | --- | --- |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification (DE) Ausgangsspezifikationen des Gleichstromadapters (FR) Spécifications de sortie de l'adaptateur de courant continu (IT) Specifiche di uscita dell'adattatore di corrente continua (ES) Especificaciones de salida del adaptador de corriente continua (RU) Выходные характеристики адаптера постоянного тока | | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |
| Voltage, V | Current, A |
| PoE In Ethernet Port (12 - 57 V DC) | 24 | 0.8 | IP54 | -40°..+70°C |

#72755

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-atl-lte18-kit.md](../../regulatory/quick-guide-atl-lte18-kit.md).
