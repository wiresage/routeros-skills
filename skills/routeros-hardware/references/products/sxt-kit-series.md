# SXT kit-series

> Source: https://manual.mikrotik.com/hardware/sxt-kit-series
>
> Category: LTE products

*[Figure]*

> **This article covers**
>
> - **SXT 4G kit**
> - **SXT LTE6 kit**
> - **SXT LTE kit-US**
> - **SXT LTE kit**
> - **SXT LTE6 kit** (2023)

The SXT kit comes as a complete set and includes a built-in modem, connected to a built-in antenna. It has two 10/100 Ethernet connectors that support MDI-X auto-detection. There are two micro SIM card slots available, to switch between cell providers.

## First use

- Open the bottom lid.
- The IMEI number can be found on the case and packaging labels.
- Insert the SIM cards into the micro-SIM slots (SIM A slot is a default).If using another slot, the configuration can be changed in RouterOS with the CLI command:/system routerboard modem set sim-slot=downAfter changing SIM slots, the LTE modem will be restarted. It can take some time (depending on the modem and board around 30 seconds) to fully initialize it, so make sure you test your modem. See [Dual SIM Application](https://manual.mikrotik.com/docs/mobile-networking/dual-sim-application) for configuration details.
- Connect the device to the power source (see "").
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at <https://mt.lv/winbox> Access **WebFig** by opening <https://192.168.188.1>, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and select the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- Select the "Check for updates" button and update RouterOS to the latest version. Must have a valid SIM card inserted and active Internet connection;
- For a manual update of the device, visit the products page at <https://mikrotik.com/products> to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.
  All pre 7.1.4 versions of ROS will have the default IP set to 192.168.88.1, after an upgrade to 7.1.4 the default IP is set to 192.168.188.1.

## Mounting

SXT is designed to be mounted on the pole, the package includes a mounting bracket and steel clamp.

- With the clip pointed forward, slide the mounting bracket into the rail on the bottom of the case, until the clip clicks into place.
- Guide the clamp through the opening in the bracket.
- Attach the unit to a pole, with the Ethernet port pointing downward.
  *[Figure]*
- Use a PH2 screwdriver to tighten the rings when alignment is complete.
- Fix the Ethernet cable to the pole using zip ties, less than one meter from the unit, to avoid the cable being pulled out of the port.
- Check mounting angle and positioning.
  When using both Ethernet ports, make sure to cut a wider cable opening in the plastic door. You can use pliers to tear out the plastic piece that is protecting the cable opening. When closing the plastic door, make sure to apply pressure, until it "clicks" into place.
  *The mounting and configuration of this device should be done by a qualified person.*

When mounting on the wall, ensure that the cable feed is pointing downwards.
The IPX rating scale of this device is IP54. You should use Cat6 shielded cables.
Warning! This equipment should be installed and operated with a minimum distance of 20 cm between the device and your body.

## Grounding

The installation infrastructure (towers and masts), as well as the router itself, must be properly grounded. The device includes a grounding wire attachment screw behind the case door. Attach your grounding wire to the grounding screw, then attach the other end of the grounding wire to the grounded mast. This is to substantially reduce the risk of ESD and lightning damage.

## Powering

The device accepts power from the Ethernet port:

- 12 - 57 V DC ⎓ passive and 802.3af/at PoE to the port ETH1.
  The power consumption under maximum load can reach 5 W, with attachments 22 W.

### Connecting to a PoE Adapter

- Use an ethernet cable to connect the device to the PoE out (PoE+DATA or Data+Power) port of the PoE adapter.
- Plug the PoE adapter RJ45 connector into your local router, switch, or computer ethernet port.
- Connect the PSU DC plug into the PoE adapter, then connect PSU to the AC power source.

## Configuration

Once logged in, you should select the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, make sure you have selected the country where the device will be used, to conform to local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: <https://mt.lv/help> In case IP connection is not available, the WinBox tool (<https://mt.lv/winbox> be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device for reinstallation, see a section .

The default configuration is CPE RouterMode:

*LTE interface connected to providers network (WAN port);

*WAN port is protected by a firewall and enabled DHCP client.

LAN Configuration:

IP Address 192.168.88.1/24 is set on the bridge (LAN port)

All pre 7.1.4 versions of ROS will have the default IP set to 192.168.88.1, after an upgrade to 7.1.4 the default IP is set to 192.168.188.1.

DHCP Server enabled;

DNS: enabled.

WAN (gateway) Configuration:

gateway: lte1;

ip4 firewall: enabled;

NAT: enabled.

## Extension slots and ports

- Two Ethernet ports that support automatic cross/straight cable correction (Auto MDI/X), so you can use either straight or cross-over cables for connecting to other network devices.
- The ETH2 port is capable of powering another RouterBOARD device with passive PoE (up to 57 V). The maximum output current is 600 mA when using less than 30 V to power this device and 400 mA when using more than 30 V.
- MiniPSIe slot.
- Two micro SIM slots.
- Integrated LTE module, supported bands depend on a region (check brochure).

## SIM slot usage

*[Figure]*

SIM card slot is designed to be used with Micro SIM cards.
Nano SIM cards have different thicknesses and usage with an adapter is not recommended.

## Reset button

The reset button has three functions:

- Hold this button during boot time until the LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds);
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total of 10 seconds);
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total of 15 seconds);
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Mode button

The action of the mode buttons can be configured from RouterOS software to execute any user-supplied RouterOS script. You can also disable this button. The mode button can be configured in RouterOS menu /system routerboard mode-button

## Accessories

The package includes the following accessories that come with the device:

- ADAPT1_EU/US Switching Power Supply 24 V, 0.8 A, 19.2 W, 85.3%, VI, cable:150 cm Hor CMC;
- CLAMP1_Hose Clapmp SUS304 (Philips type; clamping diameter range 35-70 mm);
- POE1_POE Injector with shielded connector;
- BRAC1_SXT5D mounting;

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

**To troubleshoot any issues, visit the page provided and navigate to the dedicated troubleshooting section for detailed guidance and solutions: Troubleshooting articles**

## Innovation, Science, and Economic Development Canada

| Model | Contains IC |
| --- | --- |
| RBSXTR&R11e-4G | 7442A-R11E4G |
| RBSXTR&R11e-LTE6 | 7442A-R11ELTE6 |
| RBSXTR&R11e-LTE-US | 7442A-R11ELTE |
| RBSXTR&R11e-LTE | - |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada's license-exempt RSS(s). Operation is subject to the following two conditions:

- This device may not cause interference;
- This device must accept any interference, including interference that may cause undesired operation of the device.
  L'émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d'Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes:
- L'appareil ne doit pas produire de brouillage;
- L'appareil doit accepter tout brouillage radioélectrique subi, mźme si le brouillage est.
  This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

**IMPORTANT: Exposure to Radio Frequency Radiation.**
This equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 45 cm between the radiator and any part of your body.
Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 45 cm entre le radiateur et toute partie de votre corps.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/sxt-kit-series.md](../regulatory/sxt-kit-series.md).
