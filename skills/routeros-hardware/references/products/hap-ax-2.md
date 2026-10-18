# hAP ax²

> Source: https://manual.mikrotik.com/hardware/hap-ax-2
>
> Category: Indoor wireless

*[Figure]*

A Generation 6 version of the legendary hAP ac². With PoE-in and PoE-out, much faster wireless, more RAM, and a modern CPU. The smallest fully-fledged AX router on the market! See the [hAP ax² product page](https://mikrotik.com/product/hap_ax2) for full specifications and brochures.

## Powering

- Number of DC inputs 2 (PoE-in, DC jack)
- PoE-in input Voltage 18-28 V
- DC jack input Voltage 12-28 V
- PoE-out Passive PoE Ether1, max out per port output (input < 30 V): 600mA
- Max total out 0.6 A
- Total output power 16.8 W
- Power adapter nominal voltage 24 V
- Power adapter nominal current 1.2 A
- Max power consumption (without attachments) 12 W
- Max power consumption 27 W

## Setup

- Make sure your Internet service provider is allowing hardware change and will issue an automatic IP address;
- Connect the device to the power source;
- Open network connections on your computer and search for "MikroTik-..." wireless network - connect to it;
- The configuration can be done through the wireless network using a web browser or mobile app. Alternatively, you can use a WinBox configuration tool <https://mt.lv/winbox> Open <https://192.168.88.1> in your web browser to start configuration, user name: **admin** and there is no password by default **(or, for some models, check user and wireless passwords on the sticker)**;
- Click the "Check for updates" button and update your RouterOS software to the latest version;
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the (**WebFig**) (**Files**) menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- Set up your wireless network password;
- Set up your router password.

## Configuration

We recommend clicking the "Check for updates" button and updating your RouterOS software to the latest version to ensure the best performance and stability. RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the internet port by default). For recovery purposes, it is possible to boot the device from the network, see section .

## Extension slots and ports

- Product code C52iG-5HaxD2HaxD-TC.
- CPU Quad-Core IPQ-6010 864 MHz.
- CPU architecture ARM 64bit.
- Size of RAM 1 GB.
- Storage 128 MB, NAND.
- A number of 1G Ethernet ports 5.
- A number of 1G Ethernet ports with PoE-out 1.
- Switch chip model IPQ-6010.
- Wireless interface model QCN-5052 (2.4 GHz), QCN-5052 (5 GHz).
- Wireless 2.4 GHz 802.11ax dual-chain, 5 GHz 802.11 802.11ax dual-chain.
- Wireless antenna max gain 2.4 GHz (4.5 dBi), 5 GHz (4 dBi).
- Dimensions 120 x 101 x 37 mm.
- Operating system RouterOS, License level 4.
- Operating temperature -40°C to +50°C.

## Buttons and jumpers

RouterBOOT reset button has the following functions:

- Hold the button before powering on the device, and at power-up, the button will force load the backup boot loader. Continue holding the button for the other two functions of this button.
- Release the button when the green LED starts flashing, to reset the RouterOS configuration. To not load the backup boot loader, you can start holding the button after power is already applied.
- Release the button after LED is no longer flashing (~20 seconds) to cause the device to look for Netinstall servers (required for reinstalling RouterOS over the network).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Notice

- Datasheet for any device is available on the official manufacturer website.
- For some models, check the user and wireless passwords on the sticker.
- The Frequency band 5.470-5.725 GHz isn’t allowed for commercial use.
- Please make sure the device has a locking package (firmware version from the manufacturer) which is required to be applied to the end-user equipment to prevent the end-user from reconfiguration. The product will be marked with country code “-EG” - C52iG-5HaxD2HaxD-TC-EG.
- For Outdoor Usage: End-user requires approval/license from the NTRA.
- Firmware for Egypt Regulatory have their wireless frequency range limited to 2.400 – 2.4835 GHz, the TX power is limited to 20dBm (EIRP).
- Firmware for Egypt Regulatory have their wireless frequency range limited to 5.150 – 5.250 GHz, the TX power is limited to 23dBm (EIRP).
- Firmware for Egypt Regulatory have their wireless frequency range limited to 5.250 – 5.350 GHz, the TX power is limited to 20dBm (EIRP).
  This device needs to be upgraded to the latest version to ensure compliance with local authority regulations! It is the end users responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements.
  All MikroTik radio devices must be professionally installed.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

### Federal Communication Commission Interference Statement

| Model | FCC ID |
| --- | --- |
| C52iG-5HaxD2HaxD-TC-US | TV7C52-5AXD2AXD |

*[Figure]*

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 38 centimeters from your body, occupational user, or the general public.

**FCC regulations restrict operation to indoor use only.**

### Innovation, Science and Economic Development Canada

| Model | IC |
| --- | --- |
| C52iG-5HaxD2HaxD-TC-US | 7442A-C52AX |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 38 centimeters from your body, occupational user, or the general public.

**Exposition aux rayonnements de radiofréquence :** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements IC définies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à moins de 38 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

### UKCA marking

*[Figure]*

### CE Declaration of Conformity

| BG | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение C52iG-5HaxD2HaxD-TC е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: <https://mikrotik.com/products> |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení C52iG-5HaxD2HaxD-TC je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: <https://mikrotik.com/products> |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen C52iG-5HaxD2HaxD-TC er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: <https://mikrotik.com/products> |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp C52iG-5HaxD2HaxD-TC der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: <https://mikrotik.com/products> |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός C52iG-5HaxD2HaxD-TC πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: <https://mikrotik.com/products> |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type C52iG-5HaxD2HaxD-TC is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: <https://mikrotik.com/products> |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico C52iG-5HaxD2HaxD-TC es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: <https://mikrotik.com/products> |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp C52iG-5HaxD2HaxD-TC vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: <https://mikrotik.com/products> |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi C52iG-5HaxD2HaxD-TC on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: <https://mikrotik.com/products> |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type C52iG-5HaxD2HaxD-TC est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: <https://mikrotik.com/products> |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa C52iG-5HaxD2HaxD-TC u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: <https://mikrotik.com/products> |
| HU | Mikrotīkls SIA igazolja, hogy a C52iG-5HaxD2HaxD-TC típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: <https://mikrotik.com/products> |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio C52iG-5HaxD2HaxD-TC è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: <https://mikrotik.com/products> |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að C52iG-5HaxD2HaxD-TC er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: <https://mikrotik.com/products> |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas C52iG-5HaxD2HaxD-TC atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: <https://mikrotik.com/products> |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta C52iG-5HaxD2HaxD-TC atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: <https://mikrotik.com/products> |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju C52iG-5HaxD2HaxD-TC huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: <https://mikrotik.com/products> |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur C52iG-5HaxD2HaxD-TC conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: <https://mikrotik.com/products> |
| NO | Mikrotīkls SIA erklærer herved at utstyret C52iG-5HaxD2HaxD-TC er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: <https://mikrotik.com/products> |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego C52iG-5HaxD2HaxD-TC jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: <https://mikrotik.com/products> |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio C52iG-5HaxD2HaxD-TC está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: <https://mikrotik.com/products> |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio C52iG-5HaxD2HaxD-TC este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: <https://mikrotik.com/products> |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu C52iG-5HaxD2HaxD-TC je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: <https://mikrotik.com/products> |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme C52iG-5HaxD2HaxD-TC skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: <https://mikrotik.com/products> |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning C52iG-5HaxD2HaxD-TC överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: <https://mikrotik.com/products> |

### WLAN

| Operating Frequency / Maximum output power Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность | WLAN | 2400-2483.5 MHz / 20dBm |
| --- | --- | --- |
| WLAN | 5150-5250 MHz / 23 dBm |  |
| WLAN | 5250-5350 MHz / 20 dBm |  |
| WLAN | 5470-5725 MHz / 27 dBm |  |
| WLAN | 5725-5850 MHz / 14 dBm |  |
| WLAN | 5850-5895 MHz / 14 dBm |  |

This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

*[Figure]*

Restrictions to 5GHz only

| **(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques /(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:** |  |  |  |  |
| --- | --- | --- | --- | --- |
| (EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта | (EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока | (EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP | (EN) Operating Temperature(DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |  |
| Voltage, V | Current, A |  |  |  |
| DC Jack (12 - 28 V DC) PoE in Ethernet (18 - 28 V DC) | 24 | 1.2 | IP20 | ±0°..+50°C |

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/hap-ax-2.md](../regulatory/hap-ax-2.md).
