# Groove-series

> Source: https://manual.mikrotik.com/hardware/groove-series
>
> Category: Wireless systems

> **This article covers**
>
> - **[Groove 52](https://mikrotik.com/product/RBGroove52HPnr2)**
> - **[GrooveA 52](https://mikrotik.com/product/RBGrooveA-52HPnr2)** (RBGrooveA-52HPn)
> - **[GrooveA 52 ac](https://mikrotik.com/product/RBGrooveGA-52HPacn)** (RBGrooveGA-52HPacn)

*[Figure]*

The RouterBOARD Groove comes preinstalled in an outdoor case, with a built-in wireless interface, an
N-Male antenna connector, and one 10/100 Ethernet connector which supports MDI-X auto-detection.
The device is packaged with a 24 V power adapter, a PoE injector, and two mounting loops. Several
models are available (dual-band, single-band, AP, and CPE variants).

## Quickstart

The Groove accepts 8-30 V Passive PoE from a PoE injector. The included injector should be connected with the "Data" end into a switch or other router, the "Data + Power" port should be connected to the Groove, by using an Ethernet cable of the desired length (not included).

Please follow these quick steps to set up your device:

- Attach provided antennas to the device, before connecting to the power source;
- Connect the ISP cable to the Ethernet1 port;
- Connect the device to the power source;
- Connect to the device through any of the ports, excluding Ethernet1, or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker); multiple configuration methods are available to ensure accessibility;
- Establish a connection using a mobile application. Alternatively, use **WebFig** in a web browser or the "**WinBox**" configuration tool at <https://mt.lv/WinBox>;
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use **WinBox** and choose the "**Neighbors**" tab to find the device;
- Proceed to connect using the MAC address. The username is "**admin**", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Powering

The device accepts powering from an Ethernet port (Passive PoE). Under maximum load, the power consumption of this device is 4 W.

## Mounting

The device is to be mounted vertically so that the Ethernet cable points downwards.
If you wish to tighten the Groove to a pole, you can do it with the provided mounting loops. The Groove
comes bundled with two mounting loops – guide the loops around the Groove through the provided edge
markings, and around the pole where it will be mounted. You should avoid connecting a loose Ethernet
cable to the Ethernet port, and secure the cable to a wall or the pole, so that the cable weight is not pulling
the port. It is recommended to secure the Ethernet cable less than 2m from the Groove device. This is to
ensure that the cable doesn't damage the port by its weight or doesn't fall out.

## Configuration

The AP model Groove (A) is configured as a wireless access point, with the ethernet port configured as a
DHCP client, for connecting to your ISP router or switch. A DHCP server is configured on the wireless
interface. The CPE model Groove is configured as a client, with the Ethernet port configured as a DHCP
server.
RouterOS includes many configuration options in addition to what is described in this document. We
suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case the IP connection is not available, the WinBox tool (<https://mt.lv/winbox>) can be used to connect to the
MAC address of the device from the LAN side (all access is blocked from the internet port by default).

## Reset button

The reset button has three functions:
• Hold this button during boot time until LED light starts flashing, release the button to reset
RouterOS configuration (total 5 seconds).
• Keep holding for 5 more seconds, LED turns solid, release now to turn on CAPs mode for
managing the unit from a CAPsMAN server (total 10 seconds).
• Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the
RouterBOARD looks for Netinstall servers (total 15 seconds).

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Innovation, Science, and Economic Development Canada

| Model | IC |
| --- | --- |
| Groove 52 | 7442A-GRVA52HPN |
| GrooveA 52 | 7442A-GRVA52HPN |
| GrooveA 52 ac | 7442A-GRVA52HPC |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes : 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

Antenna Installation WARNING: It is the installer's responsibility to ensure that when using the authorized antennas in Canada (or where IC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

**LIST OF APPROVED 2.4 GHz ANTENNAS:**

- 15 dBi Omni Directional (Model: WLO-2450-15)
- 13 dBi Omni Directional HP (Model: ODH 24-13)
- 20 dBi Panel (Model: WLP-2450-20)
- 17 dBi Sector (Model: SA 24-90-17-WB)
- 24 dBi Dish (Model: DC 24-HD-PFIP)
  **LIST OF APPROVED 5 GHz ANTENNAS:**
- 8.5 dBi Omni Directional (Model: MT-482016/N/A)
- 24 dBi Panel Antenna (Model: PA58-24-ANT)
- 32 dBi Dish Antenna (Model: HDDA5W-32-DP2)
  The same type of antenna and lower antenna gain as those listed above may also be used in accordance with certification.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/groove-series.md](../regulatory/groove-series.md).
