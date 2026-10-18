# CCR2004-1G-2XS-PCIe

> Source: https://manual.mikrotik.com/hardware/ccr2004-1g-2xs-pcie
>
> Category: Ethernet routers

*[Figure]*

A smart PCIe network interface card that adds full-fledged router capabilities to your servers. The smart and easy way to create 25 Gigabit networks if you want to save space in your server room! See the [CCR2004-1G-2XS-PCIe product page](https://mikrotik.com/product/ccr2004_1g_2xs_pcie) for full specifications and brochures.

## Quickstart

- Insert the device into the PCIe slot of the computer;
- Turn on the computer;
- Configuration should be made using the WinBox configuration tool <https://mt.lv/winbox> Open the **Neighbors** tab and connect to the device using the MAC address;
- The user name: **admin**, by default there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Powering

The device uses power from PCIe with Maximum power consumption of 29W.

## Configuration

By default, the PCIe interface will show up as four virtual Ethernet interfaces. Two interfaces in passthrough mode to the 25G SFP28 cages. The remaining two virtual Ethernet-PCIe interfaces are bridged with the Gigabit Ethernet port for management access.

## Specifications

- Product code CCR2004-1G-2XS-PCIe
- CPU AL32400 2 GHz
- CPU architecture ARM 64bit
- CPU core count 4
- Size of RAM 4 GB
- RAM type DDR4
- Storage 128 MB, NAND
- Number of 1G Ethernet ports 1
- Number of 25G SFP28 ports 2
- Operating system RouterOS (License level 6)
- Dimensions 170 x 69 x 18 mm
- Operating temperature -20°C to +60°C
- Max power consumption 25 W

## Reset

*[Figure]*

To reset this device to factory settings you must turn off your PC.

- Place a metal object into the reset hole so that it makes contact with both metalized sides.
- Turn on the PC and hold the screwdriver until both 25G SFP28 LEDs starts flashing RED and then release it, it will reset the RouterOS configuration.
- If you Keep holding for more than 5 seconds up to 20 seconds until the red LEDs turns off, it to make the RouterBOARD look for Netinstall servers.

## Included Parts

*[Figure]*

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

**The device is supported in Linux (minimum kernel 5.15.25) and RouterOS (minimum version 7.x), but it will not be recognized in Windows.**

<https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=bf8e59fd315f>

*[Figure]*

Safety Notice
Electric shock hazard. This equipment is to be serviced by trained personnel only.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

### Federal Communication Commission Interference Statement

*[Figure]*

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

### Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes : 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

### UKCA marking

*[Figure]*

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/ccr2004-1g-2xs-pcie.md](../regulatory/ccr2004-1g-2xs-pcie.md).
