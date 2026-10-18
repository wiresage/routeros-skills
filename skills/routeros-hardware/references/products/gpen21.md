# GPEN21

> Source: https://manual.mikrotik.com/hardware/gpen21
>
> Category: Accessories

*[Figure]*

GPEN21 allows powering a PoE capable device over the Ethernet, using the same voltage, as provided with the DC input jack. See the [GPEN21 product page](https://mikrotik.com/product/gpen21) for full specifications and brochures.

## Powering

The device accepts power from a direct-input power jack (5.5 mm outside and 2 mm inside, female, pin positive plug) 12-57 V DC⎓.
Max power consumption 50 W.

## Power output

The device supports PoE out from the Ethernet port located under the cover. You can power MikroTik devices that support passive powering through Ethernet.

GPEN21 has an Ethernet and SFP port for fiber connectivity. Customers can choose to use GPEN21 to power the optical module for uplink to provider, **or to provide PoE** to power Ethernet uplink to the provider (that uses our GPeR and/or netPower products), which cannot be used together.

## Mode button

Reserved for future use.

## Mounting

**Step 1:**

- Remove the cover screw using a PH2 screwdriver;
- Remove the cover to access mounting points.
  **Step 2:**
- Drill holes using drill bit;
- Insert dowels if needed;
- Attach the unit to the wall and secure it with screws.
  Step 1.Step 2.

*[Figure]*

**Step 3:**

- Plug in the Ethernet cable going to the unit that will be powered;
- Plug in the power source for the GPEN.
- Outgoing Ethernet cable can be guided through position A or B for cable leading into the wall.Step 4:
- Re-attach cover;
- Secure cover using the screw;
- Use the sticker to cover the screw location.

*[Figure]*

Step 3.Step 4.
When mounting on the wall, please ensure that the cable feed is pointing downwards.

## Reset and Reinstall

The GPEN21 has built-in backup SwOS firmware which can be loaded in case standard firmware breaks or an upgrade fails:

Holding the Reset button for a few seconds while the device is booting will reset the configuration and load backup firmware. The reset button is located behind the front cover.
After loading backup firmware, it is possible to connect to 192.168.88.1 (or leased address from a DHCP server) using a web browser and install new SwOS firmware.

## Accessories

The package includes the following accessories that come with the device:

- K-62 screw kit includes four screws and dowels for mounting on the wall.
  Please see the [MikroTik SFP module compatibility table](https://manual.mikrotik.com/docs/wired-connections/mikrotik-wired-interface-compatibility).

## Specifications

<https://i.mt.lv/cdn/product_files/GPEN_concept_200204.pdf>

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/gpen21.md](../regulatory/gpen21.md).
