# x86 on USB

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/130220233/x86+on+USB
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2025-11-12.

## Step-by-step guide

- Download the x86 CD image file, from <https://mikrotik.com/download>

**On Windows systems:**

- Download Rufus, <https://github.com/pbatard/rufus/releases/download/v3.18/rufus-3.18.exe>
- Connect your USB drive and open Rufus
- Select the downloaded ISO image and click START

**On Linux, FreeBSD, or MacOS systems:**

- **Warning! Double check the correct device address, dd can destroy data irreversibly!**
- Connect the USB drive and find its device address

  - MacOS use

    ```bash
    diskutil list
    ```
  - Linux/ FreeBSD

    ```bash
    fdisk -l
    ```
- **Ensure that USB drive is formatted and all old data erased, before using dd command.**
- Write the image to disk using dd:

  ```bash
  dd if=<your_downloaded_routeros_ISO> of=<disk_address> bs=1M status=progress oflag=sync
  ```
- After finishing, connect your USB to your x86 system and boot the USB.
- Proceed with the installation process by choosing "i" on your keyboard.
- After reboot, you will have x86 installed.

> **Info**
>
> Boot priorities should be changed in your BIOS settings. If RouterOS will be installed on the NVMe drive - USB has to be booted in UEFI mode.

> **Info**
>
> Make sure that CSM (Compatibility Support Module)support is disabled in the BIOS boot tab.

## Related articles

- [x86 on USB](https://help.mikrotik.com/docs/spaces/RKB/pages/130220233/x86+on+USB)
