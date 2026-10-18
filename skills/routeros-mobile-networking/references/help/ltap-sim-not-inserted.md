# LtAP : SIM not inserted

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/8323152/LtAP+SIM+not+inserted
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2019-12-04.

## Problem

LtAP log messages indicate, that the SIM card is not inserted:

```
00:05:35 lte,async lte1: sent AT+CPIN?
00:05:35 lte,async lte1: rcvd +CME ERROR: SIM not inserted
```

## Solution

The modem does not see any SIM cards inserted:
+CME ERROR: SIM not inserted

Please check if you are using the correct SIM slot. For the modem inserted in the bottom mini-pcie slot (this is the slot where modem that comes pre-installed in an LtAP lte kit is located) you need to use either sim slot 2 or sim slot 3. And the used sim slot needs to be selected in RouterOS.

CLI command to select the sim slot:
/system routerboard modem set sim-slot=2

## Related articles

- [Downgrading RouterOS](https://help.mikrotik.com/docs/spaces/RKB/pages/328316/Downgrading+RouterOS)
- [Cannot upgrade SwOS](https://help.mikrotik.com/docs/spaces/RKB/pages/15303614/Cannot+upgrade+SwOS)
- [Default password](https://help.mikrotik.com/docs/spaces/RKB/pages/285147143/Default+password)
- [Try Before RMA](https://help.mikrotik.com/docs/spaces/RKB/pages/57475128/Try+Before+RMA)
- [Upgrade failing to detect a new version](https://help.mikrotik.com/docs/spaces/RKB/pages/33325062/Upgrade+failing+to+detect+a+new+version)
