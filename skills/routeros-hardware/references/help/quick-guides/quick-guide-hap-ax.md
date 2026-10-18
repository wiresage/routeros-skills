# Quick Guide - hAP ax²

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/111346044/Quick+Guide+-+hAP+ax%C2%B2
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2026-03-03. The translations into other languages are omitted; the English guide is complete.

# Model: C52iG-5HaxD2HaxD-TC

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.11.2 or the latest stable version, to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.*

*This Quick Guide covers the model: C52iG-5HaxD2HaxD-TC.*

*This is a wireless network device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*The most relevant technical specifications for this product can be found on the last page of this Quick Guide.*

*Technical specifications, brochures, and more info about products are at <https://mikrotik.com/products>*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*If you need help with configuration, please seek a consultant <https://mikrotik.com/consultants>*

**First steps:**

- Ensure your Internet Service Provider (ISP) allows hardware changes and automatically assigns an IP address;
- Connect the ISP cable to the Ethernet1 port;
- Connect the device to the power source;
- Connect to the device through any of the ports, excluding Ethernet1, or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at [https://mt.lv/WinBox](https://mt.lv/winbox); ***multiple configuration methods are available to ensure accessibility;***
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin" and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit [mikrotik.com](http://mikrotik.com), select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 38 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## ***[Figure]***

## **WLAN**

|  |  |  |
| --- | --- | --- |
| Operating Frequency / Maximum output power  Betriebsfrequenz / maximale Ausgangsleistung  Fréquence de fonctionnement / puissance de sortie maximale  Frequenza operativa / massima potenza di uscita  Frecuencia de funcionamiento / potencia de salida máxima  Рабочая частота / максимальная выходная мощность | WLAN | 2400-2483.5 MHz / 20dBm |
| WLAN | 5150-5250 MHz / 23 dBm |
| WLAN | 5250-5350 MHz / 23 dBm |
| WLAN | 5470-5725 MHz / 30 dBm |
| WLAN | 5725-5850 MHz / 14 dBm |
| WLAN | 5850-5895 MHz / 14 dBm |

> **Note**
>
> This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.
>
> The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.
>
> *[Figure]*
>
> Restrictions to 5GHz only

| ***(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques /******(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:*** | | | | |
| --- | --- | --- | --- | --- |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification (DE) Ausgangsspezifikationen des Gleichstromadapters (FR) Spécifications de sortie de l'adaptateur de courant continu (IT) Specifiche di uscita dell'adattatore di corrente continua (ES) Especificaciones de salida del adaptador de corriente continua (RU) Выходные характеристики адаптера постоянного тока | | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |
| Voltage, V | Current, A |
| DC Jack (12 - 28 V DC)  PoE in Ethernet (18 - 28 V DC) | 24 | 1.2 | IP20 | ±0°..+50°C |

#74819, 74823

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-hap-ax.md](../../regulatory/quick-guide-hap-ax.md).
