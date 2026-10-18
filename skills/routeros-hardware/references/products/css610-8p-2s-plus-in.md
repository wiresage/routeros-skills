# CSS610-8P-2S+IN

> Source: https://manual.mikrotik.com/hardware/css610-8p-2s-plus-in
>
> Category: Switches

*[Figure]*

Your compact, affordable PoE powerhouse with 8x Gigabit PoE-out ports and 2x 10 Gigabit SFP+ ports. See the [CSS610-8P-2S+IN product page](https://mikrotik.com/product/css610_8p_2s_in) for full specifications and brochures.

## Quickstart

- Download the latest SwitchOS software version from <https://mikrotik.com/download>;
- Connect your computer to any of the ethernet ports;
- Connect the device to the power source;
- Set the IP address of your computer to 192.168.88.3;
- Open your Web browser, the default management IP address is 192.168.88.1, with the username **admin** and no password (or, for some models, check user and wireless passwords on the sticker);
- Upload the file with the web browser to the Upgrade tab, the device will reboot after an upgrade;
- Set up your password to secure the device.

## Powering

The device accepts power from the power jack or from the AC source.

- Direct-input power jack (5.5mm outside and 2mm inside, female, pin positive plug) accepts 48-57V DC.
- AC input range 100-240 V.
- Max power consumption (without attachments) 12 W.
- Max power consumption 162 W.

## PoE-Out

- PoE-Out 802.3 af/at and passive PoE
- PoE-Out ports ether1-ether8:PoE-Out voltage: low voltage 28V;
- high voltage 54V (AC input) or 48-57V (DC Input)
- Maximum low voltage PoE-Out output current: 1000 mA (per port).
- Maximum high voltage PoE-Out output current: 625 mA (per port).
- Total output power 140 W.
  PoE-Out high voltage varies depending on the power supply: if an AC power supply is used PoE-Out high voltage will always be ~54V; if a DC Jack power supply is used PoE-Out high voltage will match the input voltage on the DC Jack. PoE-Out low voltage is constant at ~28V.
  **if AC and DC power supplies are used simultaneously PoE-Out high voltage will depend on the higher input voltage. It will change only if the DC Jack input exceeds 54 volts.*

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter.
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter.
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## LED

The power supply will be determined by a device and given the appropriate Voltage if it's low the LED will light Green if the requirement is the high LED will light red, and none when no power is required for the client device.

*[Figure]*

## Configuration

SwOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> For recovery purposes, it is possible to boot the device for reinstallation, see section Buttons and Jumpers.

First-time configuration: [CSS610 series SwOS manual](https://manual.mikrotik.com/docs/bridging-and-switching/swos/css610);

The device upgrade <https://mt.lv/upgrade>;

## Extension slots and ports

- Product code CSS610-8P-2S+IN.
- A number of 1G Ethernet ports 8.
- A number of 10G SFP+ ports 2.
- Switch chip model 88E6193X.
- Dimensions 272 x 216 x 50 mm.
- Operating temperature -40°C to +70°C.

## Specifications

Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Mounting

The device is designed to use indoors and it can be mounted in a rackmount enclosure using provided rack mounts, or it can be placed on the desktop. Use a Phillips screwdriver to attach rackmount ears on both sides of the device if designated use is for rackmount enclosure:

- Attach rack ears to both sides of the device and tighten four screws to secure them in place, as shown in the picture.

*[Figure]*

- Place the device in a rackmount enclosure and align with the holes so that the device fits conveniently.
- Tighten screws to secure it in place.
  The device has no protection from water contamination, please ensure the placement of the device in a dry and ventilated environment.
  *The mounting and configuration of this device should be done by a qualified person.* *We recommend using Cat6 cables for our devices.*

## Buttons and jumpers

Hold this button during boot time until the LED light starts to flash. Release the button to reset SwOS configuration and load backup software for reinstallation and upgrade.

## Operating system support

This device runs SwOS, which is the only supported OS for this device.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

### Federal Communication Commission Interference Statement

*[Figure]*

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
  FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

### Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes : 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

### UKCA marking

*[Figure]*

| **(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques/ (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:** |  |  |
| --- | --- | --- |
| (EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Варианты входной мощности продукта | (EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP | (EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура |
| AC input (100 - 240 V AC) DC Jack (48 - 57 V DC) | IP20 | ±0°..+60°C |

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/css610-8p-2s-plus-in.md](../regulatory/css610-8p-2s-plus-in.md).
