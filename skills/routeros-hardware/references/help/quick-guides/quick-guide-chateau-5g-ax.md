# Quick Guide - Chateau 5G ax

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/111346010/Quick+Guide+-+Chateau+5G+ax
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2024-12-20. The translations into other languages are omitted; the English guide is complete.

*[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.11.2 or the latest stable version, to ensure compliance with local authority regulations!*
>
> *It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.*

*This Quick Guide covers the model: S53UG+M-5HaxD2HaxD-TC&RG502Q-EA.*

*This is a wireless network device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

*The most relevant technical specifications for this product can be found on the last page of this Quick Guide.*

*Technical specifications, brochures, and more info about products are at <https://mikrotik.com/products>*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*If you need help with configuration, please seek a consultant <https://mikrotik.com/consultants>*

**First steps:**

- Insert the micro SIM card into the slot located under the device;
- Connect the device to the power source;
- Connect to the device through either one of the Ethernet ports or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use Webfig in a web browser or the "WinBox" configuration tool at <https://mt.lv/winbox>;
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use Winbox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin," and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version. Must have a valid SIM card inserted and active Internet connection;
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the WebFig or Winbox "Files" menu and reboot the device;
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
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## ***[Figure]***

## **WLAN/WCDMA/LTE**

|  |  |  |
| --- | --- | --- |
| Operating Frequency / Maximum output power      Betriebsfrequenz / maximale Ausgangsleistung      Fréquence de fonctionnement / puissance de sortie maximale      Frequenza operativa / massima potenza di uscita      Frecuencia de funcionamiento / potencia de salida máxima      Рабочая частота / максимальная выходная мощность | WCDMA I | 1922.4 MHz / 23dBm ± 2.7 dB |
| WCDMA III | 1712.4 MHz / 23dBm ± 2.7 dB |
| WCDMA V | 826.4 MHz / 23dBm ± 2.7 dB |
| WCDMA VIII | 882.4 MHz / 23dBm ± 2.7 dB |
| WLAN | 2400-2483.5 MHz / 20dBm |
| WLAN | 5150-5250 MHz / 23 dBm |
| WLAN | 5250-5350 MHz / 23 dBm |
| WLAN | 5470-5725 MHz / 30 dBm |
| WLAN | 5725-5825 MHz / 14 dBm |
| WLAN | 5850-5895 MHz / 14 dBm |
| LTE Band 1 | 2100 MHz / 23dBm ± 2.7 dB |
| LTE Band 3 | 1800 MHz / 23dBm ± 2.7 dB |
| LTE Band 5 | 850 MHz / 23dBm ± 2.7 dB |
| LTE Band 7 | 2600 MHz / 23dBm ± 2.7 dB |
| LTE Band 8 | 900 MHz / 23dBm ± 2.7 dB |
| LTE Band 20 | 800 MHz / 23dBm ± 2.7 dB |
| LTE Band 28 | 700 MHz / 23dBm ± 2.7 dB |
| LTE Band 32 | 1500 MHz / 23dBm ± 2.7 dB |
| LTE Band 34 | 2000 MHz / 23dBm ± 2.7 dB |
| LTE Band 38 | 2600 MHz / 23dBm ± 2.7 dB |
| LTE Band 40 | 2300 MHz / 23dBm ± 2.7 dB |
| LTE Band 42 | 3500 MHz / 23, 26dBm ± 3 dB |
| LTE Band 43 | 3700 MHz / 23dBm ± 3 dB |
| 5G NR Band n1 | 2100 MHz / 23dBm ± 2 dB |
| 5G NR Band n3 | 1800 MHz / 23dBm ± 2 dB |
| 5G NR Band n7 | 2600 MHz / 23dBm ± 2 dB |
| 5G NR Band n8 | 900 MHz / 23dBm ± 2 dB |
| 5G NR Band n20 | 800 MHz / 23dBm ± 2 dB |
| 5G NR Band n28 | 700 MHz / 23dBm ± 2 dB |
| 5G NR Band n38 | 2600 MHz / 23dBm ± 2 dB |
| 5G NR Band n40 | 2300 MHz / 23dBm ± 2 dB |
| 5G NR Band n41 | 2500 MHz / 26dBm ± 2 dB |
| 5G NR Band n77 | 3700 MHz / 26dBm ± 2 dB |
| 5G NR Band n78 | 3500 MHz / 26dBm ± 2 dB |

> **Note**
>
> This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.
>
> The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

*[Figure]*

| ***(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques /******(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:*** | | | | |
| --- | --- | --- | --- | --- |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification (DE) Ausgangsspezifikationen des Gleichstromadapters (FR) Spécifications de sortie de l'adaptateur de courant continu (IT) Specifiche di uscita dell'adattatore di corrente continua (ES) Especificaciones de salida del adaptador de corriente continua (RU) Выходные характеристики адаптера постоянного тока | | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |
| Voltage, V | Current, A |
| DC Jack (12 - 28 V DC) | 24 | 1.5 | IP20 | ±0°..+70°C |

#76354

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-chateau-5g-ax.md](../../regulatory/quick-guide-chateau-5g-ax.md).
