# cAP ax

> Source: https://manual.mikrotik.com/hardware/cap-ax
>
> Category: Indoor wireless

*[Figure]*

The best-selling ceiling access point is back – stronger than ever! A new generation of wireless greatness for your office, hotel, mall, or any other setups in crowded areas. Modern quad-core CPU, 1GB of RAM, 2x Gigabit Ethernet ports, PoE, Gen 6 802.11ax wireless, PSU – included! See the [cAP ax product page](https://mikrotik.com/product/cap_ax) for full specifications and brochures.

## Connecting

- Make sure your Internet service provider is allowing hardware change and will issue an automatic IP address;
- Connect the device to the power source;
- Open network connections on your computer and search for MikroTik wireless network - connect to it;
- The configuration can be done through the wireless network using a web browser or mobile app. Alternatively, you can use a WinBox configuration tool <https://mt.lv/winbox> Open <https://192.168.88.1> in your web browser to start configuration, user name: a*dmin* and there is no password by default **(or, for some models, check user and wireless passwords on the sticker);**
- Click the "Check for updates" button and update your RouterOS software to the latest version;
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Choose your country, to apply country regulation settings;
- Set up your wireless network password;
- Set up your router password.

## Powering

- PoE-in 802.3af/at
- PoE-Out Passive PoE up to 57V (<30v DC jack must be used, >30V PoE-In and
- DC jack can be used)
- PoE-Out ports
- Ether2, max out per port output (input < 30 V): 600 mA, max out per port output (input > 30 V): 400 mA. Over 300 mA current, please use a DC jack for powering the device.
- Number of DC inputs 2
- Supported input voltage 18-57 V (DC jack) 18-57 (PoE-In)
- Max power consumption (without attachments) 11 W
- Max power consumption 36 W

## Mounting

It is possible to attach the device to a wall or ceiling, using the provided mounting bracket on the back of the unit:

- Attach the mounting bracket to the wall or ceiling with provided screws;
- Use drill bit if necessary with provided dowels;
- Connect needed cables to the device;
- Attach the device to the mounting bracket by sliding.
  *[Figure]*

*Mounting and configuration of this device should be done by a qualified person.*
Warning! This equipment should be installed and operated with a minimum distance of 30 cm between the device and your body. Operation of this equipment in the residential environment could cause radio interference.

Operating humidity can be from 5% to 95% non-condensing.

## Configuration

By default, the device is configured as a wireless access point, with the first ethernet port (Eth1) configured as a DHCP client, and the second interface bridged together with the wireless interface. A DHCP server is configured on the bridge interface.
Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> If an IP connection is unavailable, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the device's MAC address from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see the section .

## Extension slots and ports

- Product code cAPGi-5HaxD2HaxD
- CPU Quad core IPQ-6010 1.8 GHz
- Size of RAM 1 GB
- RAM type DDR3L
- Storage 128 MB, NAND
- Number of 1G Ethernet ports 2
- Wireless interface model QCN-5022 (2.4 GHz), QCN-5052 (5 GHz)
- Wireless 2.4 GHz 802.11b/g/n/ax dual-chain, 5 GHz 802.11a/n/ac/ax dual-chain
- Antenna gain 5.5 dBi
- Operating system RouterOS v7, License level 4
- Switch chip model IPQ-6010
- Dimensions 228 x 48 mm
- Operating temperature -40°C to +70°C tested

## Buttons and jumpers

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, and release the button to reset the RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, the LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until the LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

*[Figure]*

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. By default, the buttons will enable "dark mode", which disables LED lights. The mode button can be configured in the RouterOS menu /system routerboard mode-button.

## Accessories

The package includes the following accessories that come with the device:

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## MikroTik mobile app

Use the MikroTik smartphone app to configure your router in the field, or to apply the most basic initial settings for your MikroTik home access point.

*[Figure]*

- Scan the QR code and choose your preferred OS.
- Install and open the application.
- Click Connect to establish a connection to your device through a wireless network (check the wireless passwords on the sticker).
- The username is "**admin**" and there is no password (or, for some models, check user and wireless passwords on the sticker).
- Choose Quick Setup and the application will guide you through all basic configuration settings in a couple of easy steps.
- An advanced menu is available to fully configure all necessary settings.

## Notice

- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- In case WLAN devices work with different ranges than the above regulations, then a customized firmware version from the manufacturer/supplier is required to be applied to the end-user equipment and also prevent the end-user from reconfiguration.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- The datasheet for any device is available on the official manufacturer's website.
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 2.400 – 2.4835 GHz, and the TX power is limited to 20dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.150 – 5.250 GHz, and the TX power is limited to 23dBm (EIRP).
- Products with the letters “EG” at the end of their serial number have their wireless frequency range limited to 5.250 – 5.350 GHz, and the TX power is limited to 20dBm (EIRP).

Please make sure the device has a locking package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with the country code “-EG”. This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end user's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

### Federal Communication Commission Interference Statement

| cAPGi-5HaxD2HaxD | TV7CPG52X |
| --- | --- |

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

*[Figure]*

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and the receiver.
- Connect the equipment to an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
  FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC and IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 30 centimeters from your body, occupational user, or the general public.

**FCC regulations restrict operation to indoor use only.**

### Innovation, Science and Economic Development Canada

| cAPGi-5HaxD2HaxD | 7442A-CAPAX |
| --- | --- |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC and IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 30 centimeters from your body, occupational user, or the general public.

### UKCA marking

*[Figure]*

### CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение cAPGi-5HaxD2HaxD е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: <https://mikrotik.com/products> |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení cAPGi-5HaxD2HaxD je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: <https://mikrotik.com/products> |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen cAPGi-5HaxD2HaxD er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: <https://mikrotik.com/products> |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp cAPGi-5HaxD2HaxD der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: <https://mikrotik.com/products> |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός cAPGi-5HaxD2HaxD πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: <https://mikrotik.com/products> |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type cAPGi-5HaxD2HaxD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: <https://mikrotik.com/products> |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico cAPGi-5HaxD2HaxD es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: <https://mikrotik.com/products> |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp cAPGi-5HaxD2HaxD vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: <https://mikrotik.com/products> |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi cAPGi-5HaxD2HaxD on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: <https://mikrotik.com/products> |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type cAPGi-5HaxD2HaxD est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: <https://mikrotik.com/products> |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa cAPGi-5HaxD2HaxD u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: <https://mikrotik.com/products> |
| HU | Mikrotīkls SIA igazolja, hogy a cAPGi-5HaxD2HaxD típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: <https://mikrotik.com/products> |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio cAPGi-5HaxD2HaxD è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: <https://mikrotik.com/products> |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að cAPGi-5HaxD2HaxD er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: <https://mikrotik.com/products> |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas cAPGi-5HaxD2HaxD atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: <https://mikrotik.com/products> |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta cAPGi-5HaxD2HaxD atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: <https://mikrotik.com/products> |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju cAPGi-5HaxD2HaxD huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: <https://mikrotik.com/products> |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur cAPGi-5HaxD2HaxD conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: <https://mikrotik.com/products> |
| NO | Mikrotīkls SIA erklærer herved at utstyret cAPGi-5HaxD2HaxD er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: <https://mikrotik.com/products> |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego cAPGi-5HaxD2HaxD jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: <https://mikrotik.com/products> |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio cAPGi-5HaxD2HaxD está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: <https://mikrotik.com/products> |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio cAPGi-5HaxD2HaxD este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: <https://mikrotik.com/products> |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu cAPGi-5HaxD2HaxD je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: <https://mikrotik.com/products> |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme cAPGi-5HaxD2HaxD skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: <https://mikrotik.com/products> |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning cAPGi-5HaxD2HaxD överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: <https://mikrotik.com/products> |

#### WLAN

| Operating Frequency / Maximum output power Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность | 2400-2483.5 MHz / 20 dBm |
| --- | --- |
| 5150-5250 MHz / 23 dBm |  |
| 5250-5350 MHz / 20 dBm |  |
| 5470-5725 MHz / 30 dBm |  |
| 5725-5850 MHz / 14 dBm |  |
| 5850-5895 MHz / 14 dBm |  |

This MikroTik device meets Maximum WLAN transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

*[Figure]*

Restrictions to 5 GHz only.

| **(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:** |  |  |  |  |
| --- | --- | --- | --- | --- |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification (DE) Ausgangsspezifikationen des Gleichstromadapters (FR) Spécifications de sortie de l'adaptateur de courant continu (IT) Specifiche di uscita dell'adattatore di corrente continua (ES) Especificaciones de salida del adaptador de corriente continua (RU) Выходные характеристики адаптера постоянного тока | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |  |
| **Voltage, V** | **Current, A** |  |  |  |
| DC Jack (18 - 57 V DC) PoE in Ethernet (18 - 57 V DC) | 24 | 1.5 | IP20 | ±0°..+40°C |

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/cap-ax.md](../regulatory/cap-ax.md).
