# Quick Guide G16-a - LHGR kit series

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/27131954/Quick+Guide+G16-a+-+LHGR+kit+series
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2024-01-26. The translations into other languages are omitted; the English guide is complete.

# **Models:** RBLHGR&R11e-LTE6 (LHG LTE6 kit), RBLHGR&R11e-LTE-US (LHG LTE kit), RBLHGR&R11e-LTE (LHG LTE kit), RBLHGR&R11e-4G (LHG 4G kit)

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.2 or the latest stable version, to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.*

**This "LHGR kit" series Quick Guide covers models: RBLHGR&R11e-LTE6 (LHG LTE6 kit), RBLHGR&R11e-LTE-US (LHG LTE kit), RBLHGR&R11e-LTE (LHG LTE kit), RBLHGR&R11e-4G (LHG 4G kit).**

*This is a wireless network device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*Technical specifications, brochures, and more info about products are at <https://mikrotik.com/products>*

*The most important technical specifications for this product can be found on the last page of this Quick Guide.*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*If you need help with configuration, please seek a consultant <https://mikrotik.com/consultants>*

This device accepts input of 24 V DC, 0.38 A power adapter connected to PoE, which is provided in the original packaging of this device. When using a PoE injector and a different power source, the range is 12-57 V (direct current)***.***

**First steps:**

- Open the Ethernet port door;
- Insert the SIM card into the slot, with the chip facing UP;
- Connect the device to the included PoE injector with Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Open the [http://192.168.188.1](http://192.168.88.1) in your web browser;
- User name: *admin*, and there is no password**(or, for some models, check user and wireless passwords on the sticker)**;
- Use the check for update option to upgrade the device to the latest version. You must have an active SIM card with available data;
- The device will reboot;
- Connect again and in the *QuickSet* menu set your country, to apply country regulation settings;
- Secure your device and set a strong password.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 130 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas iela 2,  Riga, Latvia, LV1039.

## ***[Figure]***

## **GSM / WCDMA / LTE**

|  |  |  |
| --- | --- | --- |
| Operating Frequency / Maximum output power  Betriebsfrequenz / maximale Ausgangsleistung  Fréquence de fonctionnement / puissance de sortie maximale  Frequenza operativa / massima potenza di uscita  Frecuencia de funcionamiento / potencia de salida máxima  Рабочая частота / максимальная выходная мощность | E-GSM-900 | 900 MHz / 33 dBm |
| DCS-1800 | 1800 MHz / 30 dBm |
| WCDMA Band I | 1922.4 MHz / 24 dBm ± 2.7 dB |
| WCDMA Band VIII | 882.4 MHz / 24 dBm ± 2.7 dB |
| LTE Band 1 | 2100 MHz / 23dBm ± 2.7 dB |
| LTE Band 3 | 1800 MHz / 23dBm ± 2.7 dB |
| LTE Band 7 | 2600 MHz / 23dBm ± 2.7 dB |
| LTE Band 8 | 900 MHz / 23dBm ± 2.7 dB |
| LTE Band 20 | 800 MHz / 23dBm ± 2.7 dB |
| LTE Band 38 | 2600 MHz / 23dBm ± 2.7 dB |
| LTE Band 40 | 2300 MHz / 23dBm ± 2.7 dB |

> **Note**
>
> This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

|  |  |  |  |
| --- | --- | --- | --- |
| ***(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques*** ***/******(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:*** | | | |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification, (V/A) (DE) Ausgangsspezifikationen des Gleichstromadapters, (V/A) (FR) Spécifications de sortie de l'adaptateur de courant continu, (V/A) (IT) Specifiche di uscita dell'adattatore di corrente continua, (V/A) (ES) Especificaciones de salida del adaptador de corriente continua, (V/A) (RU) Выходные характеристики адаптера постоянного тока, (В/А) | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |
| PoE In Ethernet Port (12-57 V DC) | 24 V / 0.38 | IP54 | -30°..+60°C |

#66933

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-g16-a-lhgr-kit-series.md](../../regulatory/quick-guide-g16-a-lhgr-kit-series.md).
