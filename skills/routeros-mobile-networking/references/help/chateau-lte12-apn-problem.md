# Chateau LTE12 APN problem

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/30146629/Chateau+LTE12+APN+problem
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2020-08-20.

## Problem

No internet connection, not desired APN is used or the LTE interface receives an incorrect IP address.

## Solution

By default MBIM modems use the networks provided APN ignoring the manually set one. With some SIM cards the modem can receive an unexpected APN from the network. To resolve this add use-network-apn=no to the APN profile.

CLI commands to accomplish this (replace "internet" with your APN):

```
/interface lte apn add apn=internet use-network-apn=no/interface lte set lte1 apn-profiles=internet
```

## Related articles

- [Downgrading RouterOS](https://help.mikrotik.com/docs/spaces/RKB/pages/328316/Downgrading+RouterOS)
- [Cannot upgrade SwOS](https://help.mikrotik.com/docs/spaces/RKB/pages/15303614/Cannot+upgrade+SwOS)
- [Default password](https://help.mikrotik.com/docs/spaces/RKB/pages/285147143/Default+password)
- [Try Before RMA](https://help.mikrotik.com/docs/spaces/RKB/pages/57475128/Try+Before+RMA)
- [Upgrade failing to detect a new version](https://help.mikrotik.com/docs/spaces/RKB/pages/33325062/Upgrade+failing+to+detect+a+new+version)
