# Quick Guide G6

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/13500468/Quick+Guide+G6
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2026-03-27. The translations into other languages are omitted; the English guide is complete.

# Models: RB912UAG-5HPnD-OUT (BaseBox 5), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple), RB911G-5HPacD-NB (NetBox 5), RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP)

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.10.1 or the latest version to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed*

*This is Wireless Network Device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

**The most important technical specifications for this product can be found on the last page of this Quick Guide.**

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant <https://mikrotik.com/consultants>*

Depending on the antenna used, you must set its gain and set the installation setting to '*Outdoor*'. This is to ensure that EIRP meets the limit set by the local authorities. This is done in the Quickset menu.

**First steps:**

- Remove top cover;
- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through *WebFig* or the *WinBox* tool at [https://mt.lv/WinBox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility;**
- Access *WebFig* by opening [http://192.168.88.1](http://192.168.88.1/), and for *WinBox*, download the tool, navigate to the *Neighbors*tab, and click on the MAC address. The username is *"admin"*with no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit [mikrotik.com](http://mikrotik.com), select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the *WebFig*or*WinBox* *"Files"* menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the *"Quick Set"* menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 375 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## ***WLAN***

|  |  |
| --- | --- |
| Operating Frequency / Maximum output power  Betriebsfrequenz / maximale Ausgangsleistung  Fréquence de fonctionnement / puissance de sortie maximale  Frequenza operativa / massima potenza di uscita  Frecuencia de funcionamiento / potencia de salida máxima  Рабочая частота / максимальная выходная мощность | 5470-5725 MHz / 27 dBm |

> **Note**
>
> This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

|  |  |  |  |
| --- | --- | --- | --- |
| ***(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques*** ***/******(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:*** | | | |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification, (V/A) (DE) Ausgangsspezifikationen des Gleichstromadapters, (V/A) (FR) Spécifications de sortie de l'adaptateur de courant continu, (V/A) (IT) Specifiche di uscita dell'adattatore di corrente continua, (V/A) (ES) Especificaciones de salida del adaptador de corriente continua, (V/A) (RU) Выходные характеристики адаптера постоянного тока, (В/А) | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |
| PoE In Ethernet Port | 24 V / 1.2 | IP54 | -40°..+70°C |

> **Tip**
>
> Please, test your antenna with our device in accreditation laboratory to be in compliance with EU rules.

#83672

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-g6.md](../../regulatory/quick-guide-g6.md).
