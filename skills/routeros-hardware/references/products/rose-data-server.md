# ROSE Data Server

> Source: https://manual.mikrotik.com/hardware/rose-data-server
>
> Category: Ethernet routers

### RDS2216-2XG-4S+4XS-2XQ

*[Figure]*

## Product specifications

- Product code: RDS2216-2XG-4S+4XS-2XQ.
- CPU architecture: ARM 64bit.
- CPU core count: 16.
- CPU: AL73400 2000 MHz.
- Size of RAM: 32 GB.
- RAM type: DDR4.
- Storage (FLASH): 32 MB.
- Storage (NAND): 128 MB.
- Number of 1G Ethernet ports: 1.
- Number of 1G/2.5G/5G/10G Ethernet ports: 2.
- Number of 10G SFP+ ports: 4.
- Number of 25G SFP28 ports: 4.
- Number of 100G QSFP28 ports: 2.
- Switch chip model: 98DX4310.
- Switch connection to CPU: 4x25 Gbps.
- Operating system: RouterOS v7 only, License level 6.
- Dimensions: 476 x 443 x 29 mm.
- Operating temperature: -20°C to +50°C.

## Extension slots and ports

- Number of M.2 SATA slots: 2
- Number of 2.5" Disk trays: 20 (U.2 format SSD disks with a maximum height of 7mm only)
- USB slot: 2 (USB 3.0 Type A and USB 2.0 Type A)
- Serial console port: RJ45
  RDS2216-2XG-4S+4XS-2XQ has SATA3 connections to the two M.2 slots.Recommended are SATA3 M.2 2280mm B+M key SSD disks with no capacity limitations.

## Powering

The unit is equipped with two Hot Swap IEC type AC power supply, 550W, which accepts 100-240 V ⏦ (~ 50/60 Hz 7 A max).

The maximum power consumption without attachments is 105 W, and under maximum load, it can reach 286W.

- 100G QSFP28 supported speeds: 1x 100G; 1x 40G; 4x 25G; 4x 10G; 4x 1G. Not supported: 2x 50G; 1x 50G; 2x 40G
- 25G SFP28 supported speeds: 1x 25G; 1x 10G; 1x 2.5G; 1x 1G. Not supported: 1x 5G

## First Use - RouterOS set up before connecting disks

- Connect your PC to the MGMT/BOOT labeled port or the first Ethernet port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Configuration should be made using WebFig in a web browser or the WinBox configuration tool <https://mt.lv/winbox> Open <https://192.168.88.1> in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user password on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

## Install Disks

To install disks:

1. Open the tray by pressing the button on the right side and pulling it out.

*[Figure]*

*[Figure]*

*[Figure]*

*[Figure]*

1. Mount the disk inside the bracket (optionally securing it with screws).

*[Figure]*

*[Figure]*

1. Insert the tray back into its slot, pushing forward until it locks.

*[Figure]*

*[Figure]*

*[Figure]*

*[Figure]*

1. Disk trays are numbered from the upper left (starting at 1) to the last tray at the bottom right.

*[Figure]*

(link)

**Always use `/disk eject-drive` before physically removing any drives from your RouterOS device.**

**Forced removal is not supported and may lead to data loss.**

## Mounting

The device is designed for indoor use and can be either mounted in a rack using the provided rack mount ears or placed on a desktop. The included rack mount ear set is recommended for racks up to 600 mm deep. For rackmount installation, follow these steps using a Phillips screwdriver:

1. Attach the Rackmount ears to the front sides of the device.

*[Figure]*

*[Figure]*

*[Figure]*

*[Figure]*

1. Attach the small rear Rackmount support ears to both sides of the device.

*[Figure]*

*[Figure]*

*[Figure]*

*[Figure]*

1. Attach the long rear Rackmount support ears to the rack’s rear side.

*[Figure]*

1. Install the device in the rack, ensuring that the case support ears are securely fixed to the long support ears.

*[Figure]*

*[Figure]*

*[Figure]*

*[Figure]*

*[Figure]*

*[Figure]*

## Buttons

**Reset button**:

- Hold this button during boot time until the USR LED light starts flashing, release the button to reset RouterOS configuration.
- Hold the Reset button and power on your device (wait until the "USR" led is blinking then stable "On", and when the "USR" led is "Off" - release the Reset button) - the device is booting in bootp mode to reinstall RouterOS using Netinstall. **The MANAGEMENT/BOOT Ethernet port is used for the Netinstall process.** See RouterOS documentation about using the Netinstall recovery utility.
  Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Release the button before LED begins to flash, to only load backup RouterBOOT without resetting. This is useful for RouterBOOT debugging and recovery.

## LED indicators

### Back panel

- The PWR1/2 LED lights up when the router is powered on and connected to an appropriate power unit.
- The USER LED indicates the device's state during different boot modes, such as resetting the configuration or booting the device for the Netinstall utility.
- The FAULT LED lights up if there is an issue with any of the cooling fans.
- The square orange and green Ethernet port LEDs indicate individual 10G Ethernet port activity.
- The triangle 25G SFP28 and SFP+ port green LEDs indicate individual 25G SFP28 and SFP+ port activity.
- The circled 100G QSFP28 port green LEDs indicate individual lane activity for the 100G QSFP28 ports.
  Front Panel:
- The USER LED indicates the device's state during different boot modes, such as resetting the configuration or booting the device for the Netinstall utility.
- The FAULT LED lights up if there is an issue with any of the cooling fans.
- The POWER LED turns on when the router is powered up.
- The 2.5" Disk Tray LEDs (green and blue) indicate whether a disk is installed in the corresponding tray.

## Accessories

- IEC power cord 2pcs.;
- Rackmount ear (ROSE);
- Small rear support ears (ROSE);
- Long rear Rackmount support ears (ROSE);
- K-90 Fastening set
  The included rack mount ear set is recommended for racks up to 600 mm deep.

## Operating system support

The device supports RouterOS v7 and above. The specific factory-installed version is listed in `/system resource`. Other operating systems have not been tested.

## Safety and regulatory information

Safety warnings and regulatory statements are in [regulatory/rose-data-server.md](../regulatory/rose-data-server.md).
