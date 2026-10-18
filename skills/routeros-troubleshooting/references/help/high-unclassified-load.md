# High unclassified load

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/32702649/High+unclassified+load
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2020-07-10.

## Problem

When running Tools > Profile, the CPU states that there is a high usage and the process is "unclassified".

## Solution

The processes are added in each version, to ensure it is not already classified please upgrade your device to the latest ROS software version.

Please follow these steps before contacting support:

1. Upgrade the RouterOS software to the latest version <https://mt.lv/upgrade>;
2. Upgrade the firmware by running /system routerboard upgrade, in the CLI;
3. Reboot the device and ensure that the unclassified process is persistent;
4. Create supout.rif file and contact support, describing situation - when exactly the unclassified process shows, how long it takes after the reboot to show, etc.

## Related articles

- [High unclassified load](https://help.mikrotik.com/docs/spaces/RKB/pages/32702649/High+unclassified+load)
