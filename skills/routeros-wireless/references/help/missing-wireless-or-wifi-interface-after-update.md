# Missing wireless or wifi interface after update

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/280657934/Missing+wireless+or+wifi+interface+after+update
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2024-11-04.

# Problem

After [manual RouterOS upgrade](https://help.mikrotik.com/docs/spaces/ROS/pages/328142/Upgrading+and+installation#Upgradingandinstallation-Manualupgradeprocess), for my wireless device, wireless interface is missing.

# Solution

Starting from RouterOS version 7.13, significant changes have been made to the RouterOS wireless packages.

Drivers for older wireless and 60GHz interfaces, are now part of a separate *wireless* package instead of being a part of the bundle package. 802.11ax (AX) devices require an additional *wifi-qcom*package.

If you upgraded a device manually, you also have to upload also corresponding wireless package - for legacy wireless (and 60ghz) devices, it is a *wireless* package, for 802.11ax (AX) devices - a *wifi-qcom* package.

There to options of how to get required package.

##### Method 1 - MikroTik Software page

Go to [MikroTik Software page](https://mikrotik.com/download).

Select the appropriate RouterOS version for your device.

Select the appropriate Architecture of your device (device architecture can be found in System → Resource).

Download Extra packages. *Wireless* or *wifi-qcom* are located in Extra packages zip file.

Upload the corresponding package to your device and reboot it.

##### Method 2 - MikroTik Product page

List of packages that are preinstalled in factory can be found in the [MikroTik Products page](https://mikrotik.com/products).

Find your device in product list.

Open device *Support & Download* section.

From *RouterOS current release,* download all latest stable packages.

Upload packages to your device and reboot it.

> **Note**
>
> RouterOS and the corresponding wireless package must be the same version.
>
> It is not possible to install *wireless* package from 7.16.1 version if RouterOS 7.15.3 is installed.

[7.13 new wireless packages](https://help.mikrotik.com/docs/pages/viewpage.action?pageId=228655144)
