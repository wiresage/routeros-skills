# Quick Guide G5

> Source: https://help.mikrotik.com/docs/spaces/QG/pages/15302721/Quick+Guide+G5
>
> Only on help.mikrotik.com: the manual has no quick guides. The help site is frozen; this page was last edited 2026-03-26. The translations into other languages are omitted; the English guide is complete.

# **Models:** RBGroove52HPn (Groove 52), RBGrooveGA-52HPacn (GrooveA 52 ac), RBMetalG-52SHPacn (Metal 52 ac)

## *[Figure]*

## **EN - English -****Quick Guide**:

> **Note**
>
> *This device needs to be upgraded to RouterOS v7.9.2 or the latest version to ensure compliance with local authority regulations!*
>
> *It is the end user's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.*

*This Quick Guide covers the model: RBGroove52HPn (Groove 52), RBGrooveGA-52HPacn (GrooveA 52 ac), RBMetalG-52SHPacn (Metal 52 ac).*

*This is Wireless Network Device. You can find the product model name on the case label (ID). *[Figure]**

*Please visit the user manual page on <https://mt.lv/um> for the full up-to-date user manual. Or scan the QR code with your mobile phone.*

**The most important technical specifications for this product can be found on the last page of this Quick Guide.**

*Technical specifications, brochures, and more info about products at <https://mikrotik.com/products>*

*Configuration manual for software in your language with additional information can be found at <https://mt.lv/help>*

*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant <https://mikrotik.com/consultants>*

Depending on the antenna used, you must set its gain and set the installation set to '*Outdoor*'. This is to ensure that EIRP meets the limit set by the local authorities. This is done in the WebFig Quickset menu.

**First steps:**

- Open the upper cover and connect an external antenna (mandatory);
- Open the bottom cover and connect the device to the power source;
- Connect the device to the included PoE injector with an Ethernet cable to the *"data+power"* end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Navigate to the network connections section on your computer and locate the wireless network named "*MikroTik-...*". Proceed to connect to it (check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at [https://mt.lv/WinBox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility;**
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
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
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## **Innovation, Science, and Economic Development Canada**

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

**Antenna Installation WARNING:** It is the installer's responsibility to ensure that when using the authorized antennas in Canada (or where IC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

**Installation de l'antenne AVERTISSEMENT** : Il est de la responsabilité de l'installateur de s'assurer que lors de l'utilisation des antennes autorisées au Canada (ou là où les règles d'IC s'appliquent) ; seules les antennes certifiées avec le produit doivent être utilisées. L'installateur doit configurer le niveau de puissance de sortie des antennes, conformément aux réglementations nationales et par type d'antenne. Une installation professionnelle est requise pour les équipements avec connecteurs afin d'assurer la conformité aux questions de santé et de sécurité.

LIST OF APPROVED 2.4 GHz ANTENNAS:

- 15 dBi Omni Directional (Model: WLO-2450-15)
- 13 dBi Omni Directional HP (Model: ODH 24-13)
- 20 dBi Panel (Model: WLP-2450-20)
- 17 dBi Sector (Model: SA 24-90-17-WB)
- 24 dBi Dish (Model: DC 24-HD-PFIP)

LIST OF APPROVED 5 GHz ANTENNAS:

- 8.5 dBi Omni Directional (Model: MT-482016/N/A)
- 24 dBi Panel Antenna (Model: PA58-24-ANT)
- 32 dBi Dish Antenna (Model: HDDA5W-32-DP2)

The same type of antenna and lower antenna gain as those listed above may also be used in accordance with certification.

**Exposure to Radio Frequency Radiation:**This MikroTik equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

**Exposition aux rayonnements de radiofréquence :** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements IC définies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à moins de 20 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/quick-guide-g5.md](../../regulatory/quick-guide-g5.md).
