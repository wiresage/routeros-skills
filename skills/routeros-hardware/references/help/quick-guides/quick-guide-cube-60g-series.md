# Quick Guide - Cube 60G series

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/21725255/Quick+Guide+-+Cube+60G+series
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2024-11-20. The translations into other languages are omitted; the English guide is complete.

# **Models:** CubeG-5ac60ad (Cube 60G ac), CubeG-5ac60adpair (Wireless Wire Cube)

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.2.3 or the latest version to ensure compliance with local authority regulations!*
>
> *It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.*

*This "Cube 60G" series Quick Guide covers models: CubeG-5ac60ad (Cube 60G ac), CubeG-5ac60adpair (Wireless Wire Cube).*

*[Figure]*

*This is Wireless Network Device. You can find the product model name on the case label (ID).*

*Please visit the user manual page on <https://mt.lv/um> for the full up to date user manual. Or scan the QR code with your mobile phone.*

**The most important technical specifications for this product can be found on the last page of this Quick Guide.**

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant <https://mikrotik.com/consultants>*

**First steps:**

- Connect the device to the included PoE injector with Ethernet cable;
- Connect the PoE injector into the PC or to the network switch;
- Connect the power adapter to the PoE injector;
- Download WinBox configuration tool <https://mt.lv/winbox>;
- Open WinBox and connect to the device;
- Default IP: 192.168.88.1, user name: *admin*, for the paired models IP: 192.168.88.2/192.168.88.3, please find the password on the sticker;
- Download the latest RouterOS software from <https://mikrotik.com/download>;
- Choose ARM packages, and save them to your PC;
- Open WinBox and upload downloaded packages, drag and drop into any windows;
- Restart the device;
- Connect again and select your Region in the Wireless menu, W60G tab, and in *QuickSet*menu set your Country, to apply country regulation settings.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole but can also be installed indoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures!

**Exposure to Radio Frequency Radiation:**This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 21 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## ***[Figure]***

##

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

> **Note**
>
> This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

| **(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:** | | | | |
| --- | --- | --- | --- | --- |
| **(EN) Product Power Input Options** **(DE) Produkt Stromquellen Optionen** **(FR) Options d'entrée d'alimentation du produit** **(IT) Opzioni di ingresso alimentazione del prodotto** **(ES) Opciones de entrada de energía del producto** **(RU) Варианты входной мощности продукта** | **(EN) DC Adapter Output Specification** **(DE) Ausgangsspezifikationen des Gleichstromadapters** **(FR) Spécifications de sortie de l'adaptateur de courant continu** **(IT) Specifiche di uscita dell'adattatore di corrente continua** **(ES) Especificaciones de salida del adaptador de corriente continua** **(RU) Выходные характеристики адаптера постоянного тока** | | **(EN) IP class of the enclosure** **(DE) IP-Klasse des Gehäuses** **(FR) Classe IP du boîtier** **(IT) Classe IP della custodia** **(ES) Clase de IP del recinto** **(RU) Класс защиты корпуса IP** | **(EN) Operating Temperature** **(DE)Betriebstemperatur** **(FR) température de fonctionnement** **(IT) temperatura di esercizio** **(ES) Temperatura de funcionamiento** **(RU) Рабочая Температура** |
| **Votage, V** | **Current, A** |
| PoE In Ethernet Port (21-57 V DC) | 24 | 0.8 | IP54 | -33°..+70°C |

#66566

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-cube-60g-series.md](../../regulatory/quick-guide-cube-60g-series.md).
