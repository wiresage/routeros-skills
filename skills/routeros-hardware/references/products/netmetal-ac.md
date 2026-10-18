# NetMetal ac²

> Source: https://manual.mikrotik.com/hardware/netmetal-ac
>
> Category: Wireless systems

*[Figure]*

## [NetMetal ac²](https://mikrotik.com/product/netmetal_ac2) (RBD23UGS-5HPacD2HnD-NM)

## Quickstart

The configuration is the same as PTP Bridge in AP mode, except that wireless mode is set to ap_bridge for PTMP setups. The router can be accessed directly using the address. If the device is connected to the network with enabled DHCP server, configured DHCP client on the bridge interface will get the IP address, that can be used to access the router.

Please follow these quick steps to set up your device:

- Open the upper cover;
- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through **WebFig** or the **WinBox** tool at <https://mt.lv/winbox>. **Multiple configuration methods are available to ensure accessibility;**
- Access **WebFig** by opening <https://192.168.88.1>, and for **WinBox**, download the tool, navigate to the **Neighbors** tab, and click on the MAC address. The username is "**admin**" with no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the **WebFig** or **WinBox** "**Files**" menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the "Quick Set" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

## Extension slots and ports

Gigabit Ethernet port, supporting automatic cross/straight cable correction (Auto MDI/X). Either straight or crossover cable can be used for connecting to other network devices.

- SFP port.
- External SMA antenna connectors.
- MiniPCIe slot.
- Integrated Wireless module operating at 2.4 GHz, 802.11b/g/n protocol.
- Integrated Wireless module operating at 5 GHz, 802.11a/n/ac protocol.
- USB type-A.

## Reset button

The reset button has three functions:

- Hold this button during boot time until LED light starts flashing, release the button to reset RouterOS configuration (total 5 seconds).
- Keep holding for 5 more seconds, LED turns solid, release now to turn on CAP mode. The device will now look for a CAPsMAN server (total 10 seconds).
- Or Keep holding the button for 5 more seconds until LED turns off, then release it to make the RouterBOARD look for Netinstall servers (total 15 seconds).
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Accessories

Package includes the following accessories that come with the device:

- EU Switching Power Supply 48 V ⎓ 0.95 A 45.6 W.
- Gigabit POE injector.
- K-27 DIN rail bracket mounting set.
- Hose clamp 40/60 w2 A2 9 mm.
  See the [MikroTik wired interface compatibility](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility) table for supported SFP modules.

## MiniPCIe slot usage

This NetMetal version is without modem installed. To install the module you will need to remove the upper cover and open the bottom cover. Installing a miniPCIe module should be done by a qualified person, please follow safety precautions when handling electrical equipment:

1. Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage.
2. Remove four screws using the HEX3 screwdriver.

*[Figure]*

1. Remove the top cover by lifting it.
2. Locate the miniPCIe slot on the PCB and remove two factory attached screws.

*[Figure]*

1. Attach provided a thick thermal pad to the card, and install the card into miniPCIe slot so that the thermal pad is between PCB and card.
2. Secure the card in place using previously removed two screws.
3. Attach the grey uFL connector to the MAIN antenna connector of the modem, attach the black cable to the secondary (or AUX) connector.
4. Attach a thinner thermal pad to the top of the card.

*[Figure]*

1. Drill holes for SMA connectors.
2. Guide through the card cables.
3. Reassemble.

When assembling make sure the rubber sealing is placed firmly around the case for equal spread to prevent water contamination. Case screw torque 2,5 Nm.
When mounting the antenna for the installed card, please make sure to keep them separate at a good distance from Wireless antennas.

## Antenna usage

Antenna Installation. WARNING: It is the installer's responsibility to ensure that when using the authorized antennas in the United States (or where FCC rules apply); only those antennas certified with the product are used. The use of any antenna other than those certified with the product is expressly forbidden in accordance with FCC rules CFR47 part 15.204. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.
LIST OF APPROVED 2GHz ANTENNAS:

- 5 dBi Dipole ACOMNIRPSMA
  LIST OF APPROVED 5GHz ANTENNAS:
- 30 dBi Parabolic dish MTAD-5G-30D3
- 19 dBi Sector MTAS-5G-19D120
  Antennas of the same type and lower gain than those listed above may be used in compliance with certification.
  More information on the wireless interface: [Wireless Interface](https://manual.mikrotik.com/docs/wireless/abgn/wireless-interface)

## Specifications

For more information about this product, specifications, pictures, downloads and test results please visit our web page: <https://mikrotik.com/product/netmetal_ax>

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

To avoid pollution of the environment, please separate the device from household waste and dispose of it in a safe manner, such as in designated waste disposal sites. Familiarize yourself with the procedures for the proper transportation of the equipment to the designated disposal sites in your area.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/netmetal-ac.md](../regulatory/netmetal-ac.md).
