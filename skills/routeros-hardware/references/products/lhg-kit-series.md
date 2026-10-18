# LHG kit-series

> Source: https://manual.mikrotik.com/hardware/lhg-kit-series
>
> Category: LTE products

*[Figure]*

> **This article covers**
>
> - **LHG LTE6 kit** (RBLHGR&R11e-LTE6)
> - **LHG LTE kit** (RBLHGR&R11e-LTE)
> - **LHG LTE kit-US** (RBLHGR&R11e-LTE-US)

## Quickstart

The default configuration CPE RouterMode:

- *WAN port is protected by a firewall and enabled DHCP client.
- LAN Configuration:
- IP address 192.168.188.1/24 is set on ether1 (LAN port);
- DHCP Server enabled;
- DNS Enabled;
- WAN (gateway) Configuration:
- Gateway: lte1;
- ip4 firewall: enabled;
- NAT: enabled.
- While holding the unit by its central column, apply force to the tab, which holds the latch closed, until the latch pops open.
- Insert the SIM card into the slot, with chips facing UP.
- Assemble the case by attaching legs to the base of the unit, see the (link) paragraph.
- Mount the unit in your desired place, see the (link) paragraph.
- Set LAN computer IP configuration to *automatic* (DHCP).
- Open <https://192.168.188.1> in your web browser to start the configuration.
- User name: a*dmin* and there is no password by default you will be logged in automatically to the Quick Set screen (or, for some models, check user and wireless passwords on the sticker).
- Update the device by selecting the "Check for updates" button on the right side and updating your RouterOS software to the latest version to ensure the best performance and stability. Must have a valid SIM card inserted.
- To manually update the device, go to <https://mikrotik.com/download>
- Choose MIPSBE packages for this device and download them to your PC.
- Upload downloaded packages to the WebFig "Files" menu and reboot the device.
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates.
- Set up your router password in the bottom field "Password" to the right and repeat it in the field "Confirm Password", it will be used to log in next time.
- Select the "Apply Configuration" to save changes.
  All pre 7.1.4 versions of ROS will have the default IP set to 192.168.88.1, after an upgrade to 7.1.4 the default IP is set to 192.168.188.1.

## Case assembly

- Attach the two legs to the LHG case by sliding them onto the respective sides, the legs are different and cannot be exchanged (when looking at the product place it that the cover for the Ethernet port is in front of you, leg marked R is for the right side, leg marked L is for the left side).
- Snap the assembled LHG unit to the grid in the appropriate central location.
- Fix the two legs in place with included two self-thread screws (Phillips screwdriver PH2).
  The package also contains a grounding cable connector and a 5-degree angle adapter, for easier up or downward tilt adjustment. See paragraph.

## Opening the case cover

Optional - to access the miniPCIe slot, the opening of the unit top cover is required. As an opening tool, you can use a large-size flat head screwdriver or a small coin. Be extremely cautious when opening, because the incorrect opening of the clip can break it off!
*The mounting and configuration of this device should be done by a qualified person.*
Follow these steps:

*[Figure]*

Additional Caution when lifting up the cover, do not force it with sharp objects.

## miniPCIe slot usage

The device is equipped with a miniPCIe slot and has already installed a modem depending on what model you have. One SIM slot is provided for use together with a miniPCIe modem. The SIM slot is not used separately.
Replacing a miniPCIe module should be done by a qualified person, follow safety precautions when handling electrical equipment:

- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- Open the upper cover as shown in instruction previously;
- The antenna is located underneath PCB;
- Locate the miniPCIe slot on the PCB and remove two factory attached screws;
  *[Figure]*
- Attach provided a thick thermal pad to the card, and install the card into miniPCIe slot so that the thermal pad is between PCB and card;
- Insert your desired card;
- The secure card is in place using previously removed two screws;
- Attach the grey uFL connector to the MAIN antenna connector of the modem, attach the black cable to the secondary (or AUX) connector;
- Attach a thinner thermal pad to the top of the card;
- Reassemble.
  After reassembly, slide in the SIM card from your mobile operator into the SIM slot, with the chips facing up as shown on the port label. The slot accepts MicroSIM (3FF).

## Powering

The device can be powered from 12-57 V 802.3af/at sources and also Passive PoE injectors (one power supply and PoE injector are included).
Maximum power consumption 6 W.

### Connecting to a PoE Adapter

- Connect the Ethernet cable from the device to the PoE+DATA port of the PoE adapter;
- Connect an Ethernet cable from your local network (LAN) to the PoE adapter;
- Connect the power cord to the adapter, and then plug the power cord into a power outlet.

## Mounting

*[Figure]*

- Slide the included metallic mounting rings into the two slots on the back of the antenna dish.
- Attach the unit to a pole, with the Ethernet port pointing downward.
- Use a PH2 screwdriver to tighten the rings.
- Fix the Ethernet cable to the pole using zip ties, less than one meter from the unit, to avoid the cable being pulled out of the port.
- Check mounting angle and positioning.
- Optional: If required, before mounting the unit, you can insert the included 5-degree adjustment adapter into the top or bottom slot where the mounting ring is inserted. This will create an additional upward or downward angle when the unit is tightened to a vertical pole.
- Insert a 5-degree angle adapter to one of the slots and remount the unit.
  When mounting outdoors, ensure that any cable openings are directed downwards. Use POE injector and proper grounding, this device has a specially designed grounding connector under the port cover. Recommended using shielded Cat5/6 cable. The IP rating scale for this device is IP54.
  *Warning! This equipment should be installed and operated with a minimum distance of 120 cm between the device and your body. The operation of this equipment in the residential environment could cause radio interference.*

## Configuration

Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case an IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see a section .

## Accessories

The package includes the following accessories that come with the device:

*[Figure]*

## Extension slots and ports

- One 10/100 Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices. The Ethernet port accepts 9-30 V DC power from a passive PoE injector.
- MiniPCIe slot and SIM slot (can't be used separately) to be used with a 3G/4G/LTE modem.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds);
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds);
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds);
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. The mode button can be configured in the RouterOS menu /system routerboard mode-button.

## Specifications

For more information about this product, specifications, pictures, downloads, and test results visit our web page: <https://mikrotik.com/product/lhg_lte6_kit>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, separate the device from household waste and dispose of it in a safe manner, such as at designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Innovation, Science, and Economic Development Canada

| Model | Contains FCCID |
| --- | --- |
| RBLHGR&R11e-LTE6 | 7442A-R11ELTE6 |
| RBLHGR&R11e-LTE-US | 7442A-R11ELTE |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada's license-exempt RSS(s). Operation is subject to the following two conditions:

- This device may not cause interference;
- This device must accept any interference, including interference that may cause undesired operation of the device.
  L'émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d'Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes:
- L'appareil ne doit pas produire de brouillage;
- L'appareil doit accepter tout brouillage radioélectrique subi, mźme si le brouillage est.
  This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

**IMPORTANT: Exposure to Radio Frequency Radiation.**
This equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 130 cm between the radiator and any part of your body.
Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 130 cm entre le radiateur et toute partie de votre corps.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/lhg-kit-series.md](../regulatory/lhg-kit-series.md).
